'''
Jacob Ford
Ford_Jacob_riggingtools_cri1_1405.py

Description:
	Grouping of rigging tools.

How to Run:

import Ford_Jacob_riggingtools_cri1_1405
reload(Ford_Jacob_riggingtools_cri1_1405)

'''

import pymel.core as pm

print 'Rigging Tools Active'

def hierarchy():
	'''

	import Ford_Jacob_riggingtools_cri1_1405
	reload(Ford_Jacob_riggingtools_cri1_1405)
	Ford_Jacob_riggingtools_cri1_1405.heirarchy()
	'''

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	#Pad the root joint.
	'''

	# Create an EMPTY group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad 

	# Move group to root joint.
	# Point constrain group to root joint.
	#	offset off(Snapping)
	temp = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(temp)

	# Freeze transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint, pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control in pad.
	print 'Control 1 Created:', control_icon_1
	print ' Local Pad 1 Created:', local_pad_1


	# Move group over to the target joint.
	# Delete contrain after snapping.
	# Driver: joint
	# Driven: group
	temp_contraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_contraint)
	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint 
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control in pad.
	print 'Control 2 Created:', control_icon_2
	print ' Local Pad 2 Created:', local_pad_2


	# Move group over to the target joint.
	# Delete contrain after snapping.
	# Driver: joint
	# Driven: group
	temp_contraint = pm.parentConstraint(second_joint, local_pad_2)
	pm.delete(temp_contraint)
	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint 
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	Control 3
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control in pad.
	print 'Control 3 Created:', control_icon_3
	print ' Local Pad 3 Created:', local_pad_3


	# Move group over to the target joint.
	# Delete contrain after snapping.
	# Driver: joint
	# Driven: group
	temp_contraint = pm.parentConstraint(third_joint, local_pad_3)
	pm.delete(temp_contraint)
	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint 
	pm.orientConstraint(control_icon_3, third_joint)

	'''
	Parent control together.
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent (local_pad_2, control_icon_1)



	# Create a local oriented control for each joint.
	#lt_middle_01_bind,lt_middle_02_bind, and lt_middle_03_end 


	#Create control (circle)

	#Create group (NOT EMPTY)
	# This will automatically parent the control under 
	#	the group.


	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off (Snapping)


	# Destroy the constraint


	# Delete the History on control

	#Orient Constraint driver: control driven : join

def joint_renamer():
	
	'''

	import Ford_Jacob_riggingtools_cri1_1405
	reload(Ford_Jacob_riggingtools_cri1_1405)
	Ford_Jacob_riggingtools_cri1_1405.joint_renamer()
	'''

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
	Loop through joint chain.
	'''

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name', new_name

		#Rename joint.
		current_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_name)

def padding_tool():
	'''

	import Ford_Jacob_riggingtools_cri1_1405
	reload(Ford_Jacob_riggingtools_cri1_1405)
	Ford_Jacob_riggingtools_cri1_1405.padding_tool()
	'''

	selected = pm.ls(selection=True)
	#print 'Current Selected', selected
	root_joint = selected[0]

	# Create empty group
	#empty=True will create an empty group
	#
	pad = pm.group(empty=True)

	#Move group to joint.
	#	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	#Freeze Transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#Parent joint to group
	pm.parent(root_joint, pad)

	#renaming
	#lt_middle_01_bind
	#lt_middle_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created'

def priming_tool():
	'''
	import Ford_Jacob_riggingtools_cri1_1405
	reload (Ford_Jacob_riggingtools_cri1_1405)
	Ford_Jacob_riggingtools_cri1_1405.priming_tool()
	'''

	# Get selected.
	selected = pm.ls(selection=True)
	# print 'Joint Selected', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		#Create control
		#normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		#Group control (NOT and empty group)
		local_pad = pm.group(name=local_pad_name)

		print'Control Icon:', control_icon
		print'Pad Created:', local_pad

		#Move group to target joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control
		pm.orientConstraint(control_icon, target_joint)



	print 'Local Oriented Controls Created'

def lock_hide_tsv():
	'''
	import Ford_Jacob_riggingtools_cri1_1405
	reload (Ford_Jacob_riggingtools_cri1_1405)
	Ford_Jacob_riggingtools_cri1_1405.lock_hide_tsv()
	'''

	#This tool will lock the Translates and the Scale

	selected = pm.ls(selection=True)
	print 'selected', selected

	for icon in selected:

		icon.tx.set(lock=True,keyable=False)
		icon.ty.set(lock=True,keyable=False)
		icon.tz.set(lock=True,keyable=False)
		icon.sy.set(lock=True,keyable=False)
		icon.sx.set(lock=True,keyable=False)
		icon.sz.set(lock=True,keyable=False)
		icon.v.set(lock=True,keyable=False)
		print 'Icon T,S,V locked and hidden', icon

def lock_hide_rsv():
	'''
	import Ford_Jacob_riggingtools_cri1_1405
	reload (Ford_Jacob_riggingtools_cri1_1405)
	Ford_Jacob_riggingtools_cri1_1405.lock_hide_rsv()
	'''

	#This tool will lock the Rotates and the Scales

	selected = pm.ls(selection=True)
	print 'selected',selected

	for icon in selected:

		icon.rx.set(lock=True,keyable=False)
		icon.ry.set(lock=True,keyable=False)
		icon.rz.set(lock=True,keyable=False)
		icon.sy.set(lock=True,keyable=False)
		icon.sx.set(lock=True,keyable=False)
		icon.sz.set(lock=True,keyable=False)
		icon.v.set(lock=True,keyable=False)
		print 'Icon R,S,V locked and hidden', icon

def unlock_show_trsv():
	'''
	import Ford_Jacob_riggingtools_cri1_1405
	reload (Ford_Jacob_riggingtools_cri1_1405)
	Ford_Jacob_riggingtools_cri1_1405.unlock_show_trsv()
	'''

	#This tool will unlock the Translates, Rotates and the Scales

	selected = pm.ls(selection=True)
	print 'selected',selected

	for icon in selected:

		icon.tx.set(lock=False,keyable=True)
		icon.ty.set(lock=False,keyable=True)
		icon.tz.set(lock=False,keyable=True)
		icon.rx.set(lock=False,keyable=True)
		icon.ry.set(lock=False,keyable=True)
		icon.rz.set(lock=False,keyable=True)
		icon.sy.set(lock=False,keyable=True)
		icon.sx.set(lock=False,keyable=True)
		icon.sz.set(lock=False,keyable=True)
		icon.v.set(lock=False,keyable=True)
		print 'Icon T,R,S,V unlocked and showing', icon
