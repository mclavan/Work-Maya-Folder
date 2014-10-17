'''
Tyler Peck
peckTyler_riggingTools_cri1_1408.py

Description:
	This script contains a series of rigging tools.

	Included in this script are:

	- unlock_and_show
		To unlock and show channels in channel box.

	- priming_tool
		To create control icons and name them.

	- joint_renamer
		To rename a joint chain.

	- hierarchy
		To create a hierarchy from the selected joint chain.

	- ikFK_switch
		To create a switch between an ik and fk system.

	- pivotPoint
		To grab the pivots of one thing and add them to another.

How to Run:

import peckTyler_riggingTools_cri1_1408
reload(peckTyler_riggingTools_cri1_1408)


'''


print ''
print 'Rigging Tools Active:'
print ''

import pymel.core as pm


def unlock_and_show():
	'''
	-*- Unlock and Show -*-

	Description:
		This function allows you to unlock and show all of the first selected object's channels.

	How to Run:

	import peckTyler_riggingTools_cri1_1408
	reload(peckTyler_riggingTools_cri1_1408)
	peckTyler_riggingTools_cri1_1408.unlock_and_show()
	'''

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print ' Selected Control: ', control_icon

	# Unlock and Show Translations, Rotates, Scale, and Visability.
	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)


	print ' Channels in the first selected object have been unlocked and are visable'

def priming_tool():
	'''
	-*- Priming Tool -*-

	Description:
		
		This function allows you to create icons that will be named properly as long as you have your joints named correctly.

		- I would recomend running the joint_renamer function if your joints aren't named in the naming format.
		- Naming Convention: 
			orientation_systemName_count_suffix
			lt_leg_01_bind

		You must select the individual joints that you want to create controls for.

	How to Run:

	import peckTyler_riggingTools_cri1_1408
	peckTyler_riggingTools_cri1_1408.priming_tool()
	'''

	# Get selected joints.
	selected_joints = pm.ls(selection=True)

	for current_joint in selected_joints:
		print 'Current Joint: ', current_joint
		# Icon and pad names
		icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control icon
		control_icon = pm.circle(name=icon_name, normal=[1, 0, 0], radius=1.8)[0]

		# Create a group (Parent the control under the group)
		local_pad = pm.group(control_icon, name=local_pad_name)

		# Move the group to the target joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# connect control to group
		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():
	'''
	-*- Joint Renamer -*-

	Rename a selected joint chain
		Naming convention:
			lt_arm_01_bind
			lt_arm_02_bind
			lt_arm_03_waste

	The User will select the root joint and then execute the tool.

	The first input box that pops up is for the orientation. (lt, rt, ct)
	The second input box that pops up is for the name of the joint itself. (back, arm, leg, foot, neck, head, etc.)

	How to Run:

	import peckTyler_riggingTools_cri1_1408
	peckTyler_riggingTools_cri1_1408.joint_renamer()
	'''

	# Input Area!!!
	# Get selected root joint
	joint_system = pm.ls(selection=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	# Loop through joint chain
	for current_joint in joint_system:
		# Assemling new name
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		print ' Renameded: ', current_joint, ' to New Name: ', new_name

		# Pushing the count forward.
		# count = count + 1
		count += 1

	# Naming the waste joint
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')

	# Rename joint
	current_joint.rename(new_name)

	print ' Renamed: ', current_joint, ' to New Name: ', new_name

	print ' Selected joints have been renamed'

def hierarchy():
	'''
	-*- Hierarchy -*-

	Description:
		Creates a hierarchy based on the current selected joint chain system.

		/* Note */ This version of the function has predefined names for what it creates.

		This fuction runs by selecting the root joint chain of your system then executing.

	How to Run:

	import peckTyler_riggingTools_cri1_1408
	peckTyler_riggingTools_cri1_1408.hierarchy()

	'''

	'''
	Input
	What are we working on?
	The root joint.
	'''
	# Get slected. 
	# r stands for root in the name below. (Making sure not to mix rJoint_system with joint_system from joint_renamer)
	rJoint_system = pm.ls(selection=True, dag=True)
	print ' Joint System, ', rJoint_system

	# Names for selections 0 (The root joint), 1 (the second joint down the line), and 2 (the third joint down the line.)
	root_joint = rJoint_system[0]
	joint_2 = rJoint_system[1]
	joint_3	= rJoint_system[2]

	'''
	Padding the root joint.
	'''

	# Create a new group.
	root_pad = pm.group(empty=True, name='lt_middle_00_pad')

	# Move group to joint.
	kenny = pm.pointConstraint(root_joint, root_pad)

	# Delect constraint.
	pm.delete(kenny)

	# Freeze Transforms.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent the joint to the group.
	pm.parent(root_joint, root_joint)

	'''
	Local Controls.
	'''

	'''
	Control Icon 1 - Root Joint
	'''

	# Create a control
	# Change settings, Normals to X-axis, radious = 2
	control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1,0,0], radius=2)[0]

	# Delete history of control icon
	pm.delete(ch=True)

	# Group the control
	local_pad_1 = pm.group(control_icon_1, name='lt_middle_01_local')

	# Print out the information being created.
	print ''
	print ' Control Icon Created: ', control_icon_1
	print ' Local Pad: ', local_pad_1

	# select the joint, then the group
	# Parent constraint the group to the joint
		# Driver = Joint
		# Driven = Local Pad
	kenny = pm.parentConstraint(root_joint, local_pad_1)

	# Delete the parent constraint
	pm.delete(kenny)

	# Orient constraint the ctrl to the joint
		# Driver = Control Icon
		# Driven = Joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control Icon 2 - Second Joint
	'''

	# Create a control
	# Change settings, Normals to X-axis, radious = 2
	control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1,0,0], radius=2)[0]

	# Delete history of control icon
	pm.delete(ch=True)

	# Group the control
	local_pad_2 = pm.group(control_icon_2, name='lt_middle_02_local')

	# Print out the information being created.
	print ''
	print ' Control Icon Created: ', control_icon_2
	print ' Local Pad: ', local_pad_2

	# select the joint, then the group
	# Parent constraint the group to the joint
		# Driver = Joint
		# Driven = Local Pad
	kenny = pm.parentConstraint(joint_2, local_pad_2)

	# Delete the parent constraint
	pm.delete(kenny)

	# Orient constraint the ctrl to the joint
		# Driver = Control Icon
		# Driven = Joint
	pm.orientConstraint(control_icon_2, joint_2)


	'''
	Control Icon 3 - Third Joint
	'''
	# Create a control
	# Change settings, Normals to X-axis, radious = 2
	control_icon_3 = pm.circle(name='lt_middle_03_icon', normal=[1,0,0], radius=2)[0]

	# Delete history of control icon
	pm.delete(ch=True)

	# Group the control
	local_pad_3 = pm.group(control_icon_3, name='lt_middle_03_local')

	# Print out the information being created.
	print ''
	print ' Control Icon Created: ', control_icon_3
	print ' Local Pad: ', local_pad_3

	# select the joint, then the group
	# Parent constraint the group to the joint
		# Driver = Joint
		# Driven = Local Pad
	kenny = pm.parentConstraint(joint_3, local_pad_3)

	# Delete the parent constraint
	pm.delete(kenny)

	# Orient constraint the ctrl to the joint
		# Driver = Control Icon
		# Driven = Joint
	pm.orientConstraint(control_icon_3, joint_3)

	print ''
	print ' Hierarchy has been created.'

	'''
	Parent Controls Together.
	'''

	# Parent local pad 3 to the control icon 2
	pm.parent(local_pad_3, control_icon_2)

	# Parent local pad 2 to the control icon 1
	pm.parent(local_pad_2, control_icon_1)

def ikFK_switch():

	'''
	-*- IK/FK Switch -*-

	/* Note */ This function is still being defeloped.

	Description:
		As it stands right now. This function duplicates the selected joint chain for an IK and FK switch.

		What it planned:
		- Naming the joints that are created in the duplication.

		/* Note: */ you can run the joint_renamer function to rename the new joint chains created.

		You select the root joint of the binding joint chain (or what ever joint chain that you are going to duplicate).
	How to Run:

	import peckTyler_riggingTools_cri1_1408
	peckTyler_riggingTools_cri1_1408.ikFK_switch()
	'''
	#starting a IK/FK switch
	selected = pm.ls(selection=True)
	binding_joints = pm.ls(selected[0], dag=True)

	# Duplicates the selected joint chain.
	root_ik_chain = pm.duplicate(binding_joints[0], rc=True)
	ik_chain = pm.ls(root_ik_chain, dag=True)

	root_fk_chain = pm.duplicate(binding_joints[0], rc=True)
	ik_chain = pm.ls(root_fk_chain, dag=True)

def pivotPoint():

	'''
	-*- Pivot Point -*-

	Description:
		This function copies the pivot points of what ever you selected first.
		Then placed those pivot points into what you selected second.

		/* Note: */ You need two things selected for this ro work properly
			This function will not freeze transforms. You'll have to do that yourself.
			Make sure the pivot points are correct.


	How to Run:

	import peckTyler_riggingTools_cri1_1408
	peckTyler_riggingTools_cri1_1408.pivotPoint()
	'''
	
	selected = pm.ls(selection=True)
	# Select to the joint then the control.
	driver = selected[0]
	driven = selected[1]	

	print 'Driver: {0} Driven: {1}'.format(driver, driven)
	driver_pivots = driver.getPivots(worldSpace=True)
	print 'Driver Pivots: {0}'.format(driver_pivots)
	driven.setPivots(driver_pivots, worldSpace=True)

