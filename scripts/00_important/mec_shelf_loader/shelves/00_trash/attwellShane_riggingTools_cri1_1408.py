'''
Shane Attwell
attwellShane_riggingTools_cri1_1408.py

Discription:
	This script contains a series of rigging tools.

	Tools Included:
	- Hierarchy 
	- Padding
	- Printing Tool
	- Renaming Tool



'''

print 'Rigging Tools Active'

import pymel.core as pm

def lock_and_hide():

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon



	print 'Channels locked and hidden.'

def lock_and_hide_trans():

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	

	print 'Channels locked and hidden.'

def lock_and_hide_rotate():

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	

	print 'Channels locked and hidden.'

def unlock_and_show():

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)
	

	print 'Channels locked and hidden.'

def priming_tool():
	'''
	This tool will the second (driven) to the first (driver)
	'''
	# Get selected joints.
	selected_joints = pm.ls(selection=True, dag=True)

	for current_joint in selected_joints:
		print 'Current Control', current_joint
		
		# Icon and pad name
		icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control icon.

		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8)[0]

		# Create a group(parenting the control under the group)
		local_pad = pm.group(control_icon, name=local_pad_name)

		# Move the group to the target joint.
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group.
		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():
	'''

	Rename a selected joint chain.
		Naming Convention:
			lt_arm_01_bind
			lt_arm_03_waste

	The user will select the root joint and execute the tool.		

	How to Run:

	import attwellShane
	attwellShane.joint_renamer()

	'''

	# Input Area
	# Get selected root joint.
	joint_system = pm.ls(selection=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind
	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'bind'

	# Loop through joint chain.
	for current_joint in joint_system:
		# Assembling new name
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		print 'Renaming: ', current_joint, 'New Name: ', new_name
		
		# Pushing the count forward.
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Renaming: ', current_joint, 'New Name: ', new_name
	current_joint.rename(new_name)

	print 'Selected Joints has been renamed.'

def padding():
	'''

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# What is the correct flag?
	# empty=True will create a empty group

	pad = pm.group(empty=True)

	# move group to joint
		# and delete constraint

	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group

	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group

	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad

	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group Created'



def hierarchy():
	'''

	Create a hierarchy based upon a given system.

	Select root joint chain and execute function.

	import rigging_tools
	rigging_tools.hierarchy()
	'''
	
	'''
	Input
	What are you working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System', joint_system
	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''
	root_pad = pm.group(empty=True)

	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	pm.parent(root_joint, root_pad)
	
	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 Created', control_icon_1
	print 'Local Pad 1 Created', local_pad_1
	
	# Move group over to the target joint.
	# Delete Constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)
		
	'''
	Control 2

	'''
	# Create a control.
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 2 Created', control_icon_2
	print 'Local Pad 2 Created', local_pad_2
	
	# Move group over to the target joint.
	# Delete Constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3

	'''
	# Create a control.
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 Created', control_icon_3
	print 'Local Pad 3 Created', local_pad_3
	
	# Move group over to the target joint.
	# Delete Constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)


	'''
	Parent control together.
	'''
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Hierarchy Created.'	