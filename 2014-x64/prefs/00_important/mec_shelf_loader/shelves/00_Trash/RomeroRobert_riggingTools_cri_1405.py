'''
Romero_Robert_riggingTools_cri1_1405
Romero_Robert_riggingTools_cri1_1405hierarchy.py

Description:

How to Run:
import Romero_Robert_riggingTools_cri1_1405
reload(Romero_Robert_riggingTools_cri1_1405)
'''

import pymel.core as pm


print "Hierarchy Generated..."

def hierarchy():


	# The user will select the root joint and the tool
	#	will appy the systems

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'


	'''
	# Pad the root joint.
	'''

	# Create an empty group.
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	# Move group to target joint.
	# Point constrain group to root jont.
	#	offset off (Snapping)
	temp = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(temp)

	# Freeze transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group.

	pm.parent(root_joint, pad)



	# Create a local oriented control for each joint.
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind


	# Create control (circle)
	control_icon_1 = pm.circle(name = 'lt_middle_01_icon',radius = 1.2, normal = [1,0,0])[0]


	# Create group (NOT EMPTY)
	#	This will automaticaly parent the control under the group

	icon1 = pm.group(name = 'lt_middle_01_pad')

	# Move group to the target joint.
	temp = pm.pointConstraint(root_joint, icon1)
	pm.delete(temp)

	# Use a parent constraint driver is the joint.
	temp = pm.parentConstraint(root_joint, icon1)

	# 	Where driven is the group.
	#	Offset is off (Snapping)

	# Destroy the constraint
	pm.delete(temp)


	# Delete History on control
	pm. delete(icon1, ch=True)


	# Orient Constraint driver: control driven:joint.
	pm.orientConstraint(control_icon_1, root_joint)

	control_icon_2 = pm.circle(name = 'lt_middle_02_icon',radius = 1.2, normal = [1,0,0])[0]
	icon2 = pm.group(name = 'lt_middle_02_pad')
	temp = pm.pointConstraint(second_joint, icon2)
	pm.delete(temp)
	temp = pm.parentConstraint(second_joint, icon2)
	pm.delete(temp)
	pm. delete(icon2, ch=True)
	pm.orientConstraint(control_icon_2, second_joint)

	pm.parent(icon2, control_icon_1)

	control_icon_3 = pm.circle(name = 'lt_middle_03_icon',radius = 1.2, normal = [1,0,0])[0]
	icon3 = pm.group(name = 'lt_middle_03_pad')
	temp = pm.pointConstraint(third_joint, icon3)
	pm.delete(temp)
	temp = pm.parentConstraint(third_joint, icon3)
	pm.delete(temp)
	pm. delete(icon3, ch=True)
	pm.orientConstraint(control_icon_3, third_joint)

	pm.parent(icon3, control_icon_2)

def padding_tool():
	'''
	When you select a joint system this tool will create a world pad.

	Select the root joint to execute the command.

	import Romero_Robert_riggingTools_cri1_1405
	reload (Romero_Robert_riggingTools_cri1_1405)
	Romero_Robert_riggingTools_cri1_1405.padding_tool()

	'''

	# Get selected root oint.
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create an empty group.
	pad = pm.group(empty=True)

	# Snap group to root joint.
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms on pad.
	pm.parent(root_joint, pad)

	print 'Joint system has been padded.'

	# lt_arm_01_bind
	# lt_arm-00_pad
	# String method
	pad_name = root_joint.replace('01_bind', '00_pad')

	print "Pad Name:", pad_name
	pad.rename(pad_name)

def priming_tool():
	'''
	This tool will create a locally oriented control and pad on the joint system selected.

	Select the joints and execute the command.

	import Romero_Robert_riggingTools_cri1_1405
	reload(Romero_Robert_riggingTools_cri1_1405)
	Romero_Robert_riggingTools_cri1_1405.priming_tool()

	'''
	# Get selected Joints
	selected_joints=pm.ls(selection=True)

	# Loop through current selected.
	for current_joint in selected_joints:
		# Create control icon
		control_icon = pm.circle(normal=[1, 0, 0])[0]

		print 'Control Created:', control_icon
		# Create group, grouping icon along with it.
		local_pad = pm.group()

		# parentConstrain group to joint
		temp = pm.parentConstraint(current_joint, local_pad)
		# Delete constraint.
		pm.delete(temp)

		# Connect control to finger
		pm.orientConstraint(control_icon, current_joint)

		# Rename control and pad to match joint.
		new_control_name = current_joint.replace('_bind', '_icon')
		new_pad_name = current_joint.replace('_bind', '_local')
		control_icon.rename(new_control_name)
		local_pad.rename(new_pad_name)

def joint_renamer():
	'''
	# Select the root joint and loop through all joints in the joint chain
	# 'ori_name_count_suffix'
	# 'ct_back_01_bind'

	

	'''

	# What am I working on?
	# Get all joints in a selected joint chain.
	joint_chain = pm.ls(selection = True, dag = True)
	print 'Items Selected:', joint_chain

	# Build our new name.
	# 'lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'
	
	for current_joint in joint_chain:


		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		print 'Joint Name:', new_name
		current_joint.rename(new_name)
		
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)
		

		
	print 'Joint Chain Renamed'

def Color_Icon_Blue():
	'''
	# Select an icon and loop through all icons in chain.

	# Change color of icon to blue

	import Romero_Robert_riggingTools_cri1_1405
	reload(Romero_Robert_riggingTools_cri1_1405)
	Romero_Robert_riggingTools_cri1_1405.Color_Icon_Blue()
	'''

	# Select icon you would like to change color to.
	import pymel.core as pm
	
	selected_icon=pm.ls(selection=True)

	# Loop through current selected.
	for current_icon in selected_icon:
	# Get selected icon.
		first_selected = selected_icon[0]


		print 'First Selected Object:', first_selected
		first_selected.overrideEnabled.set(1)
		first_selected.overrideColor.set(6)

def Color_Icon_Red():
	'''
	# Select an icon and loop through all icons in chain.

	# Change color of icon to Red

	import Romero_Robert_riggingTools_cri1_1405
	reload(Romero_Robert_riggingTools_cri1_1405)
	Romero_Robert_riggingTools_cri1_1405.Color_Icon_Red()
	'''

	# Select icon you would like to change color to.
	import pymel.core as pm

	selected_icon=pm.ls(selection=True)

	# Loop through current selected.
	for current_icon in selected_icon:
		# Get selected icon.
		first_selected = selected_icon[0]


		print 'First Selected Object:', first_selected
		first_selected.overrideEnabled.set(1)
		first_selected.overrideColor.set(13)

def Color_Icon_Yellow():
	'''
	# Select an icon and loop through all icons in chain.

	# Change color of icon to yellow

	import Romero_Robert_riggingTools_cri1_1405
	reload(Romero_Robert_riggingTools_cri1_1405)
	Romero_Robert_riggingTools_cri1_1405.Color_Icon_Yellow()
	'''

	# Select icon you would like to change color to.
	import pymel.core as pm

	selected_icon=pm.ls(selection=True)

	# Loop through current selected.
	for current_icon in selected_icon:
		# Get selected icon.
		first_selected = selected_icon[0]


		print 'First Selected Object:', first_selected
		first_selected.overrideEnabled.set(1)
		first_selected.overrideColor.set(17)

def lock_hide_FK():
	'''
	# Select and object you would like to lock and hide fk.


	import Romero_Robert_riggingTools_cri1_1405
	reload(Romero_Robert_riggingTools_cri1_1405)
	Romero_Robert_riggingTools_cri1_1405.Color_Icon_Yellow()


	selected = pm.ls(selection=True)
	print 'Current Selected:', selected

	for current_item in selected:
	    current_item.tx.set(Lock=True, keyable=False)
	    current_item.ty.set(Lock=True, keyable=False)
	    current_item.tz.set(Lock=True, keyable=False)
	    
	    current_item.sx.set(Lock=True, keyable=False)
	    current_item.sy.set(Lock=True, keyable=False)
	    current_item.sz.set(Lock=True, keyable=False)
	    current_item.v.set(Lock=True, keyable=False)
	'''
	pass


		
	










