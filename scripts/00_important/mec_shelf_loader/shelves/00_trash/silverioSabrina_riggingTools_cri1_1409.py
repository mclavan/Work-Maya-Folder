'''
Sabrina Silverio
rigging_tools.py

Description:
    A group of rigging tools.

How To Run:

import silverioSabrina_riggingTools_cri1_1409
reload(silverioSabrina_riggingTools_cri1_1409)

'''

import pymel.core as pm

print 'Rigging Tools Active.'

def heirarchy():
	'''
	Creates a heirarchy based upon a given system.

	Select the root joint and execute this function.

	import silverioSabrina_riggingTools_cri1_1409
	reload(silverioSabrina_riggingTools_cri1_1409)
	silverioSabrina_riggingTools_cri1_1409.heirarchy()
	'''
	'''
	Input (Joint System)
	'''

	# Get Selected Joint System
	selected = pm.ls(selection=True, dag=True)
	# Selected: [nt.Joint(u'ct_back_01_bind),
	#		nt.Joint(u'ct_back_02_bind)
	#		nt.Joint(u'ct_back_03_bind)
	#		nt.Joint(u'ct_back_04_bind)
	#		nt.Joint(u'ct_back_05_bind)
	#		nt.Joint(u'ct_back_06_waste)]

	print 'Selected:', selected
	joint_1 = selected[0]
	joint_2 = selected[1]
	joint_3 = selected[2]

	'''
	Joint padding_tool'''

	# Create an Empty Group
	root_pad = pm.group(empty=True)

	# Move the Empty Group to the Root Joint
	temp_constraint = pm.pointConstraint(joint_1, root_pad)
	pm.delete(temp_constraint)
# joint_1 not joint1
	# Parent the Root Joint to the pad
	pm.parent(joint_1, root_pad)

	# Rename the pad based on the Joint name
	root_pad_name = joint_1.replace('01_bind', '00_pad')
	root_pad.rename(root_pad_name)

	'''
	Local Controls
	'''
	'''
	Control 1
	'''

	# Create a control icon
	control_1 = pm.circle(normal=[1, 0, 0]) [0]

	print 'Control 1 Created:', control_1
	# Create a group, grouping the icon with it.
	pad_1 = pm.group()

	# Parent the group to the joint
	temp = pm.parentConstraint(joint_1, pad_1)
	# Delete constraint.
	pm.delete(temp)

	# Connect the control to the finger
	pm.orientConstraint(control_1, joint_1)

	# Lock and Hide all transforms
	# control_1.tx.set(lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)
	control_1.ty.set(lock=True, keyable=False)
	control_1.tz.set(lock=True, keyable=False)
	control_1.sx.set(lock=True, keyable=False)
	control_1.sy.set(lock=True, keyable=False)
	control_1.sz.set(lock=True, keyable=False)
	control_1.v.set(lock=True, keyable=False)

	# Rename the control and pad based on the Joint System
	new_control_name = joint_1.replace('_bind', '_icon')
	new_pad_name = joint_1.replace('_bind', '_local')
	control_1.rename(new_control_name)
	pad_1.rename(new_pad_name)
# Same joint_1 issue.  She fixed it later on in her code.
	'''
	Control 2
	'''

	#Create a control icon
	control_2 = pm.circle(normal=[1, 0, 0])[0]

	print 'Control 2 Created:', control_2
	# Create a group, grouping the icon with it.
	pad_2 = pm.group()

	# Parent the group to the joint
	temp = pm.parentConstraint(joint_2, pad_2)
	# Delete constraint.
	pm.delete(temp)

	# Connect the control to the finger
	pm.orientConstraint(control_2, joint_2)

	# Lock and Hide all transforms
	# control_2.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.ty.set(lock=True, keyable=False)
	control_2.tz.set(lock=True, keyable=False)
	control_2.sx.set(lock=True, keyable=False)
	control_2.sy.set(lock=True, keyable=False)
	control_2.sz.set(lock=True, keyable=False)
	control_2.v.set(lock=True, keyable=False)

	# Rename the control and pad based on the Joint System
	new_control_name = joint_2.replace('_bind', '_icon')
	new_pad_name = joint_2.replace('_bind', '_local')
	control_2.rename(new_control_name)
	pad_2.rename(new_pad_name)

	'''
	Control 3
	'''

	# Create a control icon
	control_3 = pm.circle(normal=[1, 0, 0]) [0]

	print 'Control 3 Created:', control_1
	# Create a group, grouping the icon with it.
	pad_3 = pm.group()

	# Parent the group to the joint
	temp = pm.parentConstraint(joint_3, pad_3)
	# Delete constraint.
	pm.delete(temp)

	# Connect the control to the finger
	pm.orientConstraint(control_3, joint_3)

	# Lock and Hide all transforms
	# control_3.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.ty.set(lock=True, keyable=False)
	control_3.tz.set(lock=True, keyable=False)
	control_3.sx.set(lock=True, keyable=False)
	control_3.sy.set(lock=True, keyable=False)
	control_3.sz.set(lock=True, keyable=False)
	control_3.v.set(lock=True, keyable=False)

	# Rename the control and pad based on the Joint System
	new_control_name = joint_3.replace('_bind', '_icon')
	new_pad_name = joint_3.replace('_bind', '_local')
	control_3.rename(new_control_name)
	pad_3.rename(new_pad_name)

	'''
	Parenting
	'''

	# Pad 3 to Control 2
	pm.parent(pad_3, control_2)
	# Pad 2 to Control 1
	pm.parent(pad_2, control_1)

	print 'Heirarchy Created!'

def padding_tool():
	'''
	This tool creates a world pad on the selected joint system.

	Select the root joint and execute the command.

	import silverioSabrina_riggingTools_cri1_1409
	reload(silverioSabrina_riggingTools_cri1_1409)
	silverioSabrina_riggingTools_cri1_1409.padding_tool()
	'''

	# Get selected root joint.
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create an Empty Group
	pad = pm.group(empty=True)

	# Snap the group tot eh root joint.
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transformations on the pad
	pm.makeIdentity(pad, apply=True, t=0, r=0, s=1, n=0)

	# Parent the root joint to the pad.
	pm.parent(root_joint, pad)

	print 'The joint system has been padded.'

	# ct_back_01_bind
	# ct_back_00_pad
	# String method
	pad_name = root_joint.replace('01_bind', '00_pad')

	print 'Pad Name:', pad_name
	pad.rename(pad_name)

def priming_tool():
	'''
	This tool creates a local oriented control and pad on the selected joint system.

	Select the joints and execute command.

	import silverioSabrina_riggingTools_cri1_1409
	reload(silverioSabrina_riggingTools_cri1_1409)
	silverioSabrina_riggingTools_cri1_1409.priming_tool()
	'''

	# Get the selected joints
	selected_joints = pm.ls(selection=True)

	# Loop through the current selected.
	for current_joint in selected_joints:
		# Create a control icon
		control_icon = pm.circle(normal=[1, 0, 0])[0]

		print 'Control Created:', control_icon
		# Create group, grouping icon along with it.
		local_pad = pm.group()

		# Parent group to the joint
		temp = pm.parentConstraint(current_joint, local_pad)
		# Delete the contstraint
		pm.delete(temp)

		# Connect the control to the finger
		pm.orientConstraint(control_icon, current_joint)

		# Rename the control and pad to match the joint.
		new_control_name = current_joint.replace('_bind', '_icon')
		new_pad_name = current_joint.replace('_bind', '_local')
		control_icon.rename(new_control_name)
		local_pad.rename(new_pad_name)

def joint_renamer():
	'''
	This tool renames all the joints within a joint chain.
	It is based on the naming convention:
		ct_back_01_bind -> ct_back_07_waste

	Select the root joint and execute the command.

	import silverioSabrina_riggingTools_cri1_1409
	reload(silverioSabrina_riggingTools_cri1_1409)
	silverioSabrina_riggingTools_cri1_1409.joint_renamer
	'''

	# Get the selection joint.
	# Ge the selected root joint.
	joint_system = pm.ls(selection=True, dag=True)

	print 'Joint system:', joint_system

	# Naming convention
	# 'lt_arm_01_bind' -> 'lt_arm_03_waste'
	# 'ct_back)01_bind', -> 'ct_back_06_waste'

	ori = raw_input()
	system_name = raw_input()
	count = 1
	suffix = 'bind'

	# Loop through the joint chain.
	for current_joint in joint_system:
		new_joint_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name)
		print 'New Name:', new_joint_name

		# Rename the joint
		current_joint.rename(new_joint_name)
		count = count + 1

	new_joint_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_joint_name)

# This was very difficult, but the podcasts were super helpful! :)
