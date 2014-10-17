'''
Ariel Ermey
ermeyAriel_riggingTools_cri1_1408.py


How to Run:

import ermeyAriel_riggingTools_cri1_1408
reload(ermeyAriel_riggingTools_cri1_1408)

'''


print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy():
	'''
	Create a hierarchy based upon a given system.

	Select root joint chain and excuete function.

	import ermeyAriel_riggingTools_cri1_1408
	reload(ermeyAriel_riggingTools_cri1_1408)
	ermeyAriel_riggingTools_cri1_1408.hierarchy()
	'''

	'''
	Input
	What are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True, name='lt_middle_00_pad')

	# Move group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad) 
	pm.delete(temp_constraint)

	# Freeze Transforms on group
	pm.makeIdentity(root_pad, apply =True, t=1, r=1, s=1, n=0)

	# Paent root joint to the group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal = [1, 0, 0], radius=2
	control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1, 0, 0], radius=2)[0]

	# Greate a group.
	# Grouping control during the process.
	local_pad_1 = pm.group(control_icon_1, name='lt_middle_01_local')

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)
	

	'''
	Control 2
	'''
	# Create a control.
	# normal = [1, 0, 0], radius=2
	control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1, 0, 0], radius=2)[0]

	# Greate a group.
	# Grouping control during the process.
	local_pad_2 = pm.group(control_icon_2, name='lt_middle_02_local')

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control.
	# normal = [1, 0, 0], radius=2
	control_icon_3 = pm.circle(name='lt_middle_03_icon', normal=[1, 0, 0], radius=2)[0]

	# Greate a group.
	# Grouping control during the process.
	local_pad_3 = pm.group(control_icon_3, name='lt_middle_03_local')

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)
	
	'''
	Parent control together.
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)


	print 'Hierarchy Created'


def padding_tool():
	'''

	import ermeyAriel_riggingTools_cri1_1408
	reload(ermeyAriel_riggingTools_cri1_1408)
	ermeyAriel_riggingTools_cri1_1408.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group.
	# empty=True will create a empty group
	#
	pad = pm.group(empty=True)

	# Move group to joint.
	#	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	# lt_middle_01_bind
	# lt_middle_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created.'


def priming_tool():
	'''
	

	import ermeyAriel_riggingTools_cri1_1408
	reload(ermeyAriel_riggingTools_cri1_1408)
	ermeyAriel_riggingTools_cri1_1408.priming_tool()
	'''

	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# 
	target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# normal set to x and radius is 2
		control_icon = pm.circle(normal=[1, 0, 0], radius=2,
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


def joint_renamer():
	'''

	import ermeyAriel_riggingTools_cri1_1408
	reload(ermeyAriel_riggingTools_cri1_1408)
	ermeyAriel_riggingTools_cri1_1408.joint_renamer()
	'''

	'''
	Get Selected.

	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items:', joint_chain
	'''
	Figure out naming convention.
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
		print 'New Name:', new_name
		
		# Rename joint
		current_joint.rename(new_name)
		
	
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)


def delete_history():
	'''

	import ermeyAriel_riggingTools_cri1_1408
	reload(ermeyAriel_riggingTools_cri1_1408)
	ermeyAriel_riggingTools_cri1_1408.delete_history()
	'''

	# Delete Command deletes objects in 3D space.
	#	The ch flag is for deleting construction history.
	pm.delete(ch=True)

	print 'History has been deleted on all selected objects.'



def unlock_and_show():
	'''
	Unlock and make keyable all channels of the first selected object.

	import ermeyAriel_riggingTools_cri1_1408
	reload(ermeyAriel_riggingTools_cri1_1408)
	ermeyAriel_riggingTools_cri1_1408.unlock_and_show()
	'''

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)

	print 'First selected object has all channels shown.'


def lock_and_hide():
	'''
	Locks and unkeyable for all channels of the first selected object.

	import ermeyAriel_riggingTools_cri1_1408
	reload(ermeyAriel_riggingTools_cri1_1408)
	ermeyAriel_riggingTools_cri1_1408.lock_and_hide()
	'''

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	first_selected.tx.set(lock=True, keyable=False)
	first_selected.ty.set(lock=True, keyable=False)
	first_selected.tz.set(lock=True, keyable=False)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)
	first_selected.v.set(lock=True, keyable=False)

	print 'First selected object has all channels hidden.'	
	print 'Only rotate is shown.'

