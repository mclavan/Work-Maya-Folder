'''
David Hobson
rigging_tools.py

Description:
	Group of rigging_tools

How to Run:

import rigging_tools
reload(rigging_tools)

'''

import pymel.core as pm
print 'Rigging Tools Active'

def hierarchy():
	pass

def joint_renamer():
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Selected Items:', joint_chain



	'''
	Figure out naming convention
	'lt_middle_01_bind' -> 'lt_middle_04_waste'
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'




	'''
	Loop throught joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name
		
		# Rename joint.
		current_joint.rename(new_name)
		

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	print 'New Name:', new_name
	current_joint.rename(new_name)

def padding_tool():

	'''
	import rigging_tools
	reload (rigging_tools)
	rigging_tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# Print 'Current Selected', selected
	
	root_joint = selected[0]


	# Create empty group
	# empty=True will create a empty group
	#
	pad = pm.group(empty=True)

	# Move group to joint.
	#	and delete constraint.
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	
	# Parent joint to group.
	pm.parent(root_joint, pad)

	# renaming
	# lt_middle_01_bind
	# lt_middle_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding Group Created.'

def priming_tool():
	'''
	import rigging_tools
	reload (rigging_tools)
	rigging_tools.priming_tool()
	'''

	# Get selected.
	selected = pm.ls(selection=True)
	# print 'Joint Selected', selected
	# target_joint = selected[0]

	
	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')


		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]
		
		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)


		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created.'

