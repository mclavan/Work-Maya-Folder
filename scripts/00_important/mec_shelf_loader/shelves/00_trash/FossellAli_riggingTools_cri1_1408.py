'''
Rigging Tools 
Ali Fossell

Description:
	All the rigging tools together
	

How to Run:

import FossellAli_riggingTools_cri1_1408
reload (FossellAli_riggingTools_cri1_1408)
'''
import pymel.core as pm 

print "Ali Fossell's Rigging Tools Active."

def joint_renaming_tool():
	'''
	Renamings a joint chain based upon a naming convention.

	Select the root joint and execute this function.

	How to Run:

	import FossellAli_riggingTools_cri1_1408
	reload (FossellAli_riggingTools_cri1_1408)
	FossellAli_riggingTools_cri1_1408.joint_renaming_tool()
	'''

	#Get Selected.
	#pm.ls(selection=True)


	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items:', joint_chain

	#Figure out naming convention
	#'lt_middle_01_bind' -> 'lt_middle_04_waste'
	#'ct_tail_01_bind', -> 'ct_tail_04_waste'

	ori = raw_input() 
	system_name = raw_input()
	count = 01
	suffix = 'bind'

	

	#Loop through joint chain.

	for current_joint in joint_chain:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix) 
		print 'New_Name', new_name

		# Rename joint
		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_name)

	print 'Name Change:', new_name
	joint_chain[-1].rename(new_name)

	print 'Joints Successfully Renamed'

def priming_tool():
	'''
	Created a local oriented control and padon the selected joint system.

	Select joints and excute this command.

	import FossellAli_riggingTools_cri1_1408
	reload (FossellAli_riggingTools_cri1_1408)
	FossellAli_riggingTools_cri1_1408.priming_tool()

	'''
	# Selected joints
	selected_joints = pm.ls(selection=True)

	# Loop through the selected 
	for current_joint in selected_joints:

		# Renaming control
		icon_name = current_joint.replace('_bind', '_icon'), 
		pad_name = current_joint.replace('_bind', '_pad')

		# Control Icon
		control_icon = pm.circle(name=icon_name, normal=[1, 0, 0,])[0]
		
		print 'Control Created:', control_icon
		# Grouping the icon
		local_pad = pm.group(name=pad_name)

		# Parent constraint group to joint
		temp = pm.parentConstraint(current_joint, local_pad)
		# Delete temp constraint
		pm.delete(temp)

		# Connecting the control to the finger
		pm.orientConstraint(control_icon, current_joint)

def padding_tool():
	'''
	Creates a world pad on the selected joint system.

	Select the root joint and excute this commmand.

	How to Run: 

	import FossellAli_riggingTools_cri1_1408
	reload (FossellAli_riggingTools_cri1_1408)
	FossellAli_riggingTools_cri1_1408.padding_tool()

	'''
	# Get selected root joint.
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Creates empty group.
	pad = pm.group(empty=True)

	# Snap group to root joint.
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transformations on pad.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to pad.
	pm.parent (root_joint, pad)

	print 'Joint System was Padded.'

	# Named properly
	pad_name = root_joint.replace('01_bind', '00_pad')

	print 'Pad Name:', pad_name
	pad.rename(pad_name)

def hierarchy_organizer():
	'''
	Creates a hierarchy for a given system.

	Select the root joint of the system and excute this function.

	How to Run:

	import FossellAli_riggingTools_cri1_1408
	reload (FossellAli_riggingTools_cri1_1408)
	FossellAli_riggingTools_cri1_1408.hierarchy_organizer()

	'''
	'''
	Imput (Joint System)
	'''
	#Get selected joint system
	selected = pm.ls(selection=True, dag=True)
	# Selected:[nt.Joint (u'lt_middle_01_bind)'),
	#	nt.Joint(u'lt_middle_02_bind'),
	#	nt.Joint(u'lt_middle_03_bind'),
	#	nt.Joint(u'lt_middle_04_waste')]

	print 'Selected:', selected
	joint_1 = selected [0]
	joint_2 = selected [1]
	joint_3 = selected [2]

	'''
	Joint Padding

	'''

	# Created an empty group
	root_pad = pm.group(empty=True)

	# Move empty group to the root joint.
	temp_constraint = pm.pointConstraint(joint_1, root_pad)
	pm.delete(temp_constraint)

	# Parent the root joint ot the pad.
	pm.parent(joint_1, root_pad)

	# Rename pad based on joint name.
	root_pad_name = joint_1.replace ('01_bind', '00_pad')
	root_pad.rename(root_pad_name)

	''' 
	Local Controls
	'''
	'''
	Control 1
	'''
	# Create control icon.
	control_1 = pm.circle(normal=[1, 0, 0])[0]

	print 'Control 1 Created:', control_1
	# Create group, group the icon with this group.
	pad_1 = pm.group()

	# parentConstrain the group to the joint.
	temp = pm.parentConstraint(joint_1, pad_1)
	# Delete the constraint.
	pm.delete(temp)

	# Connect the control with the finger.
	pm.orientConstraint(control_1, joint_1)

	# Lock and Hide transforms 
	# control_1.tx.set (lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)
	control_1.tx.set(lock=True, keyable=False)

	# Rename control and pad based on joint system
	new_control_name = joint_1.replace('_bind', '_icon')
	new_pad_name = joint_1.replace('_bind', '_local')
	control_1.rename(new_control_name)
	pad_1.rename(new_pad_name)

	''' 
	Control 2
	'''
	# Create control icon.
	control_2 = pm.circle(normal=[1, 0, 0])[0]

	print 'Control 2 Created:', control_2
	# Create group, group the icon with this group.
	pad_2 = pm.group()

	# parentConstrain the group to the joint.
	temp = pm.parentConstraint(joint_2, pad_2)
	# Delete the constraint.
	pm.delete(temp)

	# Connect the control with the finger.
	pm.orientConstraint(control_2, joint_2)

	# Lock and Hide transforms 
	# control_1.tx.set (lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)

	# Rename control and pad based on joint system
	new_control_name = joint_2.replace('_bind', '_icon')
	new_pad_name = joint_2.replace('_bind', '_local')
	control_2.rename(new_control_name)
	pad_2.rename(new_pad_name)

	'''
	Control 3
	'''
	# Create control icon.
	control_3 = pm.circle(normal=[1, 0, 0])[0]

	print 'Control 3 Created:', control_3
	# Create group, group the icon with this group.
	pad_3 = pm.group()

	# parentConstrain the group to the joint.
	temp = pm.parentConstraint(joint_3, pad_3)
	# Delete the constraint.
	pm.delete(temp)

	# Connect the control with the finger.
	pm.orientConstraint(control_3, joint_3)

	# Lock and Hide transforms 
	# control_1.tx.set (lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)

	# Rename control and pad based on joint system
	new_control_name = joint_3.replace('_bind', '_icon')
	new_pad_name = joint_3.replace('_bind', '_local')
	control_3.rename(new_control_name)
	pad_3.rename(new_pad_name)

	'''
	Parenting
	'''
	# Parent pad 3 to control 2
	pm.parent(pad_3, control_2)
	# Parent pad 2 to control 1
	pm.parent (pad_2, control_1)

	print 'Hierarchy Successfully Organized.'
