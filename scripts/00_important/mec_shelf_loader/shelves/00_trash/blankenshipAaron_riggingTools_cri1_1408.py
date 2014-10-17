'''
Blankenship Aaron
blankenshipAaron_riggingTools_cri1_1408.py

Description
	This script contains a series of rigging tools.

'''

print 'Rigging Tools Active'

import pymel.core as pm

def delete_constraint():
	'''
	Deletes the contraint on the selected object.

	How to Run

	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.delete_constraint():
	'''
	import pymel.core as pm
	pm.delete( cn=True )

def hierarchy():
	'''

	Create a hierarchy based upon a given system.

	Select root joint chain and execute function

	How to Run

	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.hierarchy()


	'''

	'''
	Input
	What are we working on?
	The root joint
	'''
	import pymel.core as pm
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:',joint_system 

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)


	# Freeze Transforms on group
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
	# Normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group
	# Group control during the process
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 Created', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driver: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control.
	# Normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group
	# Group control during the process
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 2 Created', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driver: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_2, joint_2)


	'''
	Control 3
	'''
	# Create a control.
	# Normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group
	# Group control during the process
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 Created', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driver: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together.
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)
	print 'Hierarhcy Created.'

def delete_history():
	'''
	How to Run:


	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.delete_history()
	'''
	import pymel.core as pm
	pm.delete(ch=True)

def lock_and_hide():
	'''
	How to Run:


	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.lock_and_hide()
	'''

	import pymel.core as pm
	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected Control', control_icon


	print 'Channels locked and hidden.'

def lock_and_hide_trans():
	'''
	How to Run:


	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.lock_and_hide_trans()
	'''
	import pymel.core as pm
	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected Control', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden.'

def lock_and_hide_rotate():
	'''
	How to Run:


	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.lock_and_hide_rotate()
	'''
	import pymel.core as pm
	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected Control', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden.'

def unlock_and_show():
	'''
	How to Run:


	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.unlock_and_show()
	'''
	import pymel.core as pm
	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected Control', control_icon
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

def prime_tool():
	'''
	How to Run:

	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.priming_tools()
	'''
	import pymel.core as pm
	# Get Selected.
	selected =pm.ls(selection=True)
	# Print 'Joints Selected:', selected
	# target_joint = selected[0]

	for current_joint in selected:

		icon_name = current_joint.replace('_bind','_icon')
		local_pad_name = current_joint.replace('_bind','_local')

		# Create control
		# Normal set to x and radius is 1.8
		control_icon = pm.circle(name=icon_name,normal=[1, 0, 0], radius=1.8)[0]
	

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(current_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Contraint joint to control.
		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():
	'''
	Rename a selected joint chain.
		Naming convetion:
			lt_arm_01_bind
			lt_arm_03_waste

	The user will select the root joint and then execute the tool.
	'''
	'''
	How to Run:

	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.joint_renamer()
	'''


	# Input area!!!
	# Get selected root joint.
	joint_system = pm.ls(selection=True, dag=True)

	# Orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	# Loop through join chain.
	for current_joint  in joint_system:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		print 'Renaming: ', current_joint, 'New Name:', new_name
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Renaming: ', current_joint, 'New Name:', new_name
	current_joint.rename(new_name)

	print 'Selected joints has been renamed.'

def seperator_attribute():
	'''
	How to Run:


	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.seperator_attribute()
	'''

	import pymel.core as pm

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Create a float attribute
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', en="--------------:", keyable=True)
	attribute = first_selected.attr(attribute_name)
	attribute.set(lock=True)

def padding_tool():
	'''
	How to Run:


	import blankenshipAaron_riggingTools_cri1_1408
	reload(blankenshipAaron_riggingTools_cri1_1408)
	rigging_tools.padding_tool()
	'''
	import pymel.core as pm
	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create a empty group
	#
	pad = pm.group(empty=True)

	# Move group to joint.
	#	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)



	print 'Padding group created.'







