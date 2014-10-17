'''
tanatKriengkomol_riggingTools_cri1_1408.py

(By Tanat KP Kriengkomol)

Description:
	Practical use of loops.
	Renaming joint based upon a naming convention.

How to Run:
import tanatKriengkomol_riggingTools_cri1_1408
reload(tanatKriengkomol_riggingTools_cri1_1408)



'''

print 'AWAKENING RIGGING TOOLS...'

import pymel.core as pm

 
def hierarchy():
 	'''
 	Create a hierarchy based upon a given system.

 	Select root joint chain and execute function.
 	import tanatKriengkomol_riggingTools_cri1_1408
 	tanatKriengkomol_riggingTools_cri1_1408.hierarchy()
 	'''

	print 'CREATING HIERARCHY SYSTEM (do not disturb)'

 	'''
 	Working on root joint
 	'''
 	joint_system = pm.ls(selection=True, dag=True)

 	root_joint = joint_system[0]
 	joint_2 = joint_system[1]
 	joint_3 = joint_system[2]

 	'''
 	Padding Root Joint
 	'''

 	# Create empty group
 	root_pad = pm.group(empty=True)

 	# Move the group over to the target joint.
 	temp_constraint = pm.pointConstraint(root_joint, root_pad)
 	pm.delete(temp_constraint)

 	# Freeze Transformations on group
 	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

 	# Parent root joint to the group.
 	pm.parent(root_joint, root_pad)

 	'''
 	Local Controls
 	'''
 	'''
 	Control 1 - root_joint
 	'''

 	# Create a control.
 	# normal=[1, 0, 0], radius=2
 	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

 	# Create a group.
 	# Grouping crontol during the process.
 	local_pad_1 = pm.group()

 	# Output control and pad.
 	print 'Control 1 Created:' , control_icon_1
 	print 'Local Pad 1 Created:', local_pad_1

 	# Move group over to the target joint.
 	# Delete constraint after snapping.
 	# DRIVER --> DRIVEN, Joint --> Group
 	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
 	pm.delete(temp_constraint)

 	# Orient Constrain the joint to the control.
 	# Driver -> Driven.
 	pm.orientConstraint(control_icon_1, root_joint)

 	'''
 	Control 2
 	'''
 	# Create a control.
 	# normal=[1, 0, 0], radius=2
 	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

 	# Create a group.
 	# Grouping crontol during the process.
 	local_pad_2 = pm.group()

 	# Output control and pad.
 	print 'Control 2 Created:' , control_icon_2
 	print 'Local Pad 2 Created:', local_pad_2

 	# Move group over to the target joint.
 	# Delete constraint after sanpping.
 	# Driver: joint
 	# Driven: group
 	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
 	pm.delete(temp_constraint)

 	# Orient Constrain the joint to the control.
 	# Driver -> Driven.
 	# Control -> Joint.
 	pm.orientConstraint(control_icon_2, joint_2)

 	'''
 	Control 3
 	'''
 	# Creating control...
 	# normal=[1, 0, 0], radius=2
 	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

 	# Create a group.
 	# Grouping crontol during the process.
 	local_pad_3 = pm.group()

 	# Output control and pad.
 	print 'Control 3 Created:' , control_icon_3
 	print 'Local Pad 3  Created:', local_pad_3

 	# Move group over to the target joint.
 	# Delete constraint after sanpping.
 	# Driver: joint
 	# Driven: group
 	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
 	pm.delete(temp_constraint)

 	# Orient Constrain the joint to the control.
 	# Driver -> Driven.
 	#Control -> Joint.
 	pm.orientConstraint(control_icon_3, joint_3)

 	'''
 	Parent control together.
 	'''
 	# Pad 3 (Last) -> control 2
 	pm.parent(local_pad_3, control_icon_2)
 	pm.parent(local_pad_2, control_icon_1)

 	print 'HIERARCHY CREATION COMPLETED!'

def padding_tool():
	
	'''
	import tanatKriengkomol_riggingTools_cri1_1408
	reload(tanatKriengkomol_riggingTools_cri1_1408)
	tanatKriengkomol_riggingTools_cri1_1408.padding_tool
	'''

	print 'PREPARING PADDING TOOLS (give it some time)'

	selected = pm.ls(selection=True)
	
	root_joint = selected[0]

	# Create empty group
	# empty=True will create an empty group
	pad = pm.group(empty=True)

	# Move group to joint.
	# Delete constraint.
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)



	print 'PADDING CREATED!'

def joint_renamer():
	'''

	import tanatKriengkomol_riggingTools_cri1_1408
	reload(tanatKriengkomol_riggingTools_cri1_1408)
	tanatKriengkomol_riggingTools_cri1_1408.joint_renamer
	'''

	print 'RENAMING JOINTS (almost done, please relax)'

	joint_chain = pm.ls(selection=True, dag=True)
	print 'Selected items:', joint_chain

	'''
	Use following naming convention.
	'lt_arm_01_bind' -> 'lt_arm_03_waste
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'

	'''
	Loop through joint chain
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		#Rename Joint
		current_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

	print 'JOINT RENAMING COMPLETE'

def priming_tool():
	'''
	import tanatKriengkomol_riggingTools_cri1_1408
	reload(tanatKriengkomol_riggingTools_cri1_1408)
	tanatKriengkomol_riggingTools_cri1_1408.priming_tool()
	'''

	print 'SUMMONING PRIMING TOOL'

	# Get Selected

	selected = pm.ls(selection=True)

	# print 'Joints Selected:', selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_icon')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT a empty group)
		local_pad = pm.group()

		print 'Control Icon:', control_icon
		print 'Pad Created', local_pad

		# Move group to target joint.
		# 	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


	print 'DING! LOCAL ORIENT CONTROLS CREATED!'

def colour_controls():
	# Changes the colour.

	selected =  pm.ls(selection=True)

	for current_item in selected:
		current_item.overrideEnable.set(1)
		red = 12
		current_item.overrideColor.set(red)

def reset_pose():
	'''
	import tanatKriengkomol_riggingTools_cri1_1408
	reload(tanatKriengkomol_riggingTools_cri1_1408)
	tanatKriengkomol_riggingTools_cri1_1408.reset_pose()
	'''

	# This resets the pose of the rig.

	selected = pm.ls(selection=True)
	print ' Current selected:', selected

	for current_item in selected:
		current_item.t.set[0, 0, 0]
		current_item.r.set[0, 0, 0]

def lock_hide_translate():
	'''
	import tanatKriengkomol_riggingTools_cri1_1408
	reload(tanatKriengkomol_riggingTools_cri1_1408)
	tanatKriengkomol_riggingTools_cri1_1408.lock_hide_translate()
	'''
	print 'LOCKING AND HIDING STUFF'
	print '(so the animators dont mess my rig up)'

	import pymel.core as pm

	selected = pm.ls(selected=True)
	print 'Current Selected:', selected

	current_item = selected[0]

	current_item.tx.set(lock=True, keyable=False)
	current_item.ty.set(lock=True, keyable=False)
	current_item.tz.set(lock=True, keyable=False)
	current_item.sx.set(lock=True, keyable=False)
	current_item.sy.set(lock=True, keyable=False)
	current_item.sz.set(lock=True, keyable=False)
	current_item.v.set(lock=True, keyable=False)

	print 'TRANSLATIONS HIDDEN FROM EVIL ANIMATORS'

def lock_hide_rotate():
	'''
	import tanatKriengkomol_riggingTools_cri1_1408
	reload(tanatKriengkomol_riggingTools_cri1_1408)
	tanatKriengkomol_riggingTools_cri1_1408.lock_hide_rotate()
	'''

	import pymel.core as pm

	selected = pm.ls(selected=True)
	print 'Current Selected:', selected

	current_item = selected[0]

	current_item.rx.set(lock=True, keyable=False)
	current_item.ry.set(lock=True, keyable=False)
	current_item.rz.set(lock=True, keyable=False)
	current_item.sx.set(lock=True, keyable=False)
	current_item.sy.set(lock=True, keyable=False)
	current_item.sz.set(lock=True, keyable=False)
	current_item.v.set(lock=True, keyable=False)

	print 'ROTATIONS HID FROM EVIL ANIMATORS'

def unlock():
	'''
	import tanatKriengkomol_riggingTools_cri1_1408
	reload(tanatKriengkomol_riggingTools_cri1_1408)
	tanatKriengkomol_riggingTools_cri1_1408.unlock()
	'''

	import pymel.core as pm

	selected = pm.ls(selected=True)
	print 'Current Selected:', selected

	current_item = selected[0]

	current_item.tx.set(lock=False, keyable=True)
	current_item.ty.set(lock=False, keyable=True)
	current_item.tz.set(lock=False, keyable=True)
	current_item.rx.set(lock=False, keyable=True)
	current_item.ry.set(lock=False, keyable=True)
	current_item.rz.set(lock=False, keyable=True)
	current_item.sx.set(lock=False, keyable=True)
	current_item.sy.set(lock=False, keyable=True)
	current_item.sz.set(lock=False, keyable=True)
	current_item.v.set(lock=False, keyable=True)

	print 'UNLOCKED HIDDEN'