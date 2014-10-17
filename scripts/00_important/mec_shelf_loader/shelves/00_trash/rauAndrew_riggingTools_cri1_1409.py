"""
Andrew Rau
rigging_tools.py

This script gives the user useful rigging tools, such as:
	- snapping objects to others
	- creating locally-oriented controls
	- creating pads on joints
	- renaming joint chains
	- setting up hierarchy groups

How to Run:
	import rigging_tools
	reload(rigging_tools)
"""

import pymel.core as pm

def create_hierarchy():
	"""
	This tool will create a hierarchy and control system out of the selected joint chain.
	The system requires the user to input what body system they want to have ordered into hierarchy.
		(ex.) if lt_middle_01_bind is to be rigged, user must input 'middle' (without quotes)

	How to Run:
		import rigging_tools
		rigging_tools.create_hierarchy()
	"""

	# Ask user for a system name
	if pm.ls(selection=True) != []:
		user_input = pm.promptDialog(
								title='System Name',
								message='Enter system name:\n(ex. \"spine\")',
								button=['OK', 'Cancel'],
								defaultButton='OK',
								cancelButton='Cancel',
								dismissString='Cancel')
		if user_input == 'OK':
			system_name = pm.promptDialog(query=True, text=True)

			# Checks if system name is found in the scene
			if pm.ls('*'+system_name+'*') != []:
				padding_tool()
				priming_tool()

				# grab both joint pad and local pad
				joint_pad = pm.ls('*'+system_name+'_00_pad')
				local_pad = pm.ls('*'+system_name+'_01_local')

				pm.select(joint_pad[0], replace=True)
				pm.select(local_pad[0], add=True)
				pm.group(name='finger_world')

				print 'Joint and control icon hierarchy has been organized.'
			else:
				print 'System name called "'+system_name+'" isn\'t found in this scene.'
		else:
			print 'Hierarchy setup cancelled.'
	else:
		print 'Please select joint chain and execute command again.'

def snapping_tool():
	"""
	This moves first selected object to the second selected object.
		- translates AND rotates object

	Requires two objects to be selected.

	How to Run:
		import rigging_tools
		rigging_tools.snap_to_object()
	"""

	try:
		selected = pm.ls(selection=True)
		print 'Selected: {0}'.format(selected)

		target_obj = selected[0]
		parent_obj = selected[1]

		temp_constraint = pm.parentConstraint(target_obj, parent_obj)
		pm.delete(tem)

		print target_obj, 'was snapped to', parent_obj
	except:
		print 'Please select two objects and execute command again.'

def point_snapping_tool():
	'''
	This tool moves the first selected object to the second.
		- only translates object

	Requires two objects to be selected.

	How to Run:
		import rigging_tools
		rigging_tools.snapping_tool()
	'''

	try:
		selected = pm.ls(selection=True)
		print 'Selected: {0}'.format(selected)

		target_joint = selected[0]
		control_icon = selected[1]

		temp_constraint = pm.pointConstraint(target_joint, control_icon)
		pm.delete(temp_constraint)

		print target_obj, 'was point-snapped to', parent_obj
	except:
		print 'Please select two objects and execute command again.'

def joint_renamer():
	"""
	This tool renames all the joints in a chain.
	User selects the root joint of a joint chain, and tool renames each joint.
	Script will prompt user to input the joint's orientation and part of system to complete renaming.
		ex. 'ct' & 'spine'

	How to run:
		import rigging_tools
		rigging_tools.joint_renamer()
	"""
	try:
		# Select hierarchy from root joint chain
		pm.select(hierarchy=True)
		joint_chain = pm.ls(selection=True)
		print 'Selected items:', joint_chain

		# Setup naming system
		ori = raw_input()
		system_name = raw_input()
		count = 1
		suffix = 'bind'

		for current_joint in joint_chain:
			if current_joint != joint_chain[-1]:
				new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
				print 'New Name:', new_name

				# Rename joint
				current_joint.rename(new_name)

				count += 1
			else:
				suffix = 'waste'
				new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
				print 'New Name:', new_name

				# Rename joint
				current_joint.rename(new_name)

				count += 1

		print 'Selected joint chain has been renamed.'
	except:
		print 'Please select joint chain and execute command again.'

def padding_tool():
	"""
	This tool creates a pad for the selected item.
	It also moves the pad to the selected objects's location and freezes its transforms.

	To run:
		import rigging_tools
		rigging_tools.create_pad()
	"""
	try:
		# Grabs first object out of selection
		selected = pm.ls(selection=True)
		first_selected = selected[0]

		# Creates a pad and renames it
		pad_name = first_selected.replace('_01_bind', '_00_pad')
		pad = pm.group(name=pad_name, empty=True)
		
		# Snaps pad to object & freezes transforms
		temp_constraint = pm.pointConstraint(first_selected, pad)
		pm.delete(temp_constraint)
		pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

		# Make pad the parent of your selection
		pm.parent(selected, pad)

		print 'Joint pad named "'+pad_name+'" has been created.'
	except:
		print 'Please select joint chain and excecute command again.'

def priming_tool():
	"""
	This tool will create locally-oriented pads for each control, parent them in
	the correct order, snap the local pads to their respective joints, and orient
	constrain the joints to their respective icons.

	How to Run:
		import rigging_tools
		rigging_tools.priming_tool()
	"""
	try:
		# Gets joints out of selection for renaming the control icons
		pm.select(hierarchy=True)
		selected = pm.ls(selection=True)

		# Create icons and local pads lists
		icons = []
		local_pads = []

		# create counter to stop loop before the "_waste" joint
		count = 1
		for current_joint in selected:
			if count <= (len(selected) - 1):
				# Create icons
				icon_name = current_joint.replace('_bind', '_icon')
				icon = pm.circle(name=icon_name, normal=[1,0,0], radius=1, sections=16)
				
				# Create local pads
				local_name = current_joint.replace('_bind', '_local')
				local_pad = pm.group(name=local_name)

				# Snap local pads to joints
				temp_constraint = pm.parentConstraint(current_joint, local_pad)
				pm.delete(temp_constraint)

				# Create orient constraints on joints
				pm.orientConstraint(icon, current_joint)

				# Store icons and local pads in respective lists
				icons.append(icon_name)
				local_pads.append(local_name)
				count += 1

		# Create hierarchy for local pads and icons
		for x in range((len(local_pads) - 1)):
			pm.parent(local_pads[x+1], icons[x])

		print 'Local pads named "{0}", "{1}", and "{2}" created.'.format(local_pads[0], local_pads[1], local_pads[2])
	except:
		print 'Please select joint chain and execute command again.'
