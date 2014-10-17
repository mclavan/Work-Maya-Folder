'''
Rebecca Rivera
Rivera_Rebecca_riggingTools_Cri1_1408.py

Description:
	This script contains a series of rigging tools.


How to Run:

import Rivera_Rebecca_riggingTools_Cri1_1408
reload(Rivera_Rebecca_riggingTools_Cri1_1408)


'''

print 'Rigging Tools Active'

import pymel.core as pm 

def lock_and_hide():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls: ', control_icon
       
	
	print 'Channels locked and hide'

def lock_and_hide_trans():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls: ', control_icon

	control_icon.tx.set(lock=True, keyable=False) 
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hide'

def lock_and_hide_rotate():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls: ', control_icon
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
	print 'Channels locked and hide'

def unlock_and_show():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls: ', control_icon
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
	print 'Channels locked and hide'

def priming_tool():

	# Get selected.
	selected_controls = pm.ls(selection=True)

	for current_control in selected_controls:
		print 'Current Joint:', current_control
		# Icon and pad name
		new_icon_name = current_joint.replace('-bind', '_icon')
		local_pad_name = current_joint.replace('-bind', '_local')
		# Create a control icon
		control_icon = pm.circle(normal=[1, 0, 0], radius= 1.8)[0]

		# Create a group (parenting the control under the group)
		local_pad = pm.group(control_icon)
	
		# Move the group to the target joint 
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)


def joint_renamer():
	'''
	Rename a selected joint chain.
		naming convention:
			lt_arm_01_bind
			lt_arm_03_bind

	The user will select the root joint and then execute the tool.
	How to Run:	

	import Rivera_Rebecca_riggingTools_Cri1_1408
	Rivera_Rebecca_riggingTools_Cri1_1408.joint_renamer()

	'''

	# imput Area!!!
	# Get selected root joint.
	joint_system = pm.ls(selected=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'bind'

	# Loop through joint chain.
	for current_joint in joint_system: 
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)


		print 'Renaing: ', current_control, 'New Name: ', new_name

		# Pushing the count forward.
		count = count + 1

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')
		print 'Renaing: ', current_joint, 'New Name: ', new_name
		current_joint.rename(new_name)




	print'Selected joints have been renamed.'




def padding_tool():
	'''

	import Rivera_Rebecca_rigging_tools
	reload(Rivera_Rebecca_rigging_tools)
	Rivera_Rebecca_rigging_tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:',selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create a empty group
	# 
	pad = pm.group(empty=True)

	# Move group to joint
	#   and delete constraint
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

	print 'Padding group created'


def hierarchy():

	'''
	import Rivera_Rebecca_rigging_tools
	reload(Rivera_Rebecca_rigging_tools)
	Rivera_Rebecca_rigging_tools.hierarchy()
	'''

	import pymel.core as pm

	print 'Starter Script'

	root_joint = 'lt_middle_01_bind'
	joint_2 = 'lt_middle_02_bind'
	joint_3 = 'lt_middle_03_bind'

	# Create a group and name it 'lt_middle_00_pad'.
	pad = pm.group(empty=True, name='lt_middle_00_pad')

	print 'Root Joint', root_joint, 'and pad', pad

	# Move the group to the root joint.
	# A pointContsraint only translates.
	# What is our driver: ?? and driven: ??.
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	# Freeze Transforms (We have not done this yet)
	pm.makeIdentity(apply=True, t=1, r=1, s=1, normal=0)

	# Parent the root joint to the group.
	# We are parenting the root joint to the pad
	# Parent command works children first then father last
	pm.parent(root_joint, pad)

	print 'Pad Created:', pad, 'and moved to', root_joint

	# What is next?
	# Create a local oriented control for each finger joint

	# Create a circle icon
	# Rotation and size need to maych the joint
	# Donot forget to use the zero index [0]
	control_icon_1=pm.circle(radius=1.9, normal=[1,0,0],
		name='lt_middle_01_icon')[0]

	# Create a group for the control (Not empty)
	local_pad_1 = pm.group(name='lt_middle_01_local')

	# Use parent constraint to move local pad to joint.
	dixy = pm.parentConstraint(root_joint, local_pad_1)

	# Delete constraint
	pm.delete(dixy)

	# Orient constraint the "control" to the finger.
	pm.orientConstraint(control_icon_1, root_joint)


	# Create a circle icon
	# Rotation and size need to maych the joint
	# Donot forget to use the zero index [0]
	control_icon_2=pm.circle(radius=1.9, normal=[1,0,0],
		name='lt_middle_02_icon')[0]

	# Create a group for the control (Not empty)
	local_pad_2 = pm.group(name='lt_middle_02_local')

	# Use parent constraint to move local pad to joint.
	dixy = pm.parentConstraint(joint_2, local_pad_2)

	# Delete constraint
	pm.delete(dixy)

	# Orient constraint the "control" to the finger.
	pm.orientConstraint(control_icon_2, joint_2)

	# Create a circle icon
	# Rotation and size need to maych the joint
	# Donot forget to use the zero index [0]
	control_icon_3=pm.circle(radius=1.9, normal=[1,0,0],
		name='lt_middle_03_icon')[0]

	# Create a group for the control (Not empty)
	local_pad_3 = pm.group(name='lt_middle_03_local')

	# Use parent constraint to move local pad to joint.
	dixy = pm.parentConstraint(joint_3, local_pad_3)

	# Delete constraint
	pm.delete(dixy)

	# Orient constraint the "control" to the finger.
	pm.orientConstraint(control_icon_3, joint_3)


	'''
	parenting
	Childrean then parent

	'''
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2,control_icon_1)










