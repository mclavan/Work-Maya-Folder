'''
Kevin Brown
BrownKevin_riggingTools_cri1_1408.py 

Description:
	This script is a series of rigging tools.

How to Run:

import BrownKevin_riggingTools_cri1_1408
reload (BrownKevin_riggingTools_cri1_1408)

'''


print 'Rigging Tools Active'

import pymel.core as pm 

def leg_ik():
	'''
	import BrownKevin_riggingTools_cri1_1408
	reload (BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.leg_ik()
	'''
	
	'''
	This control creates the IK systems needed for rigging 
	a leg system.
	'''

	# Get selected
	selected_joints = pm.ls(selection=True)
	print 'Selected Joints:', selected_joints

	# Get the root joint.
	root_joint = selected_joints[0]

	# Get the hierarchy
	leg_system = pm.ls(root_joint, dag=True)
	print 'Leg System:', leg_system

	ankle_joint = leg_system[2]
	ball_joint = leg_system[3]
	toe_joint = leg_system[4]
	# Research creating IKs.
	# RPIK ikHandle -sol ikRPsolver;
	# cmds.ikHandle( startJoint='joint1', endEffector='joint5', p=2, w=.5 )
	leg_ik = pm.ikHandle(startJoint=root_joint, endEffector=ankle_joint, sol='ikRPsolver')[0]
	print 'Leg IK', leg_ik
	# SCIK ikHandle;
	pm.ikHandle(startJoint=ankle_joint, endEffector=ball_joint)
	pm.ikHandle(startJoint=ball_joint, endEffector=toe_joint)

def priming_tool():
	'''
	import BrownKevin_riggingTools_cri1_1408
	reload (BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.priming_tool()
	'''

	'''
	This tool creates a locally oriented control for selected joint and children.

	Selected a group of them and then run the tool.

	'''

	# Get selected joints.
	selected_joints = pm.ls(selection=True, dag=True)

	for current_joint in selected_joints:
		print 'Current Control:', current_joint
		# Icon and pad names
		icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control icon
		control_icon = pm.circle(name=icon_name, normal=[1, 0, 0], radius=1.8)[0]

		# Creating a group (parenting the control under the group)
		local_pad = pm.group(control_icon, name=local_pad_name)

		# Move the group to the tatget joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():
	'''
	rename a selected joint chain
		naming convention:
			lt_arm_01_bind
			lt_arm_03_waste

	The use will select the root joint and then execute the tool.

	How to Run:
	import BrownKevin_riggingTools_cri1_1408
	BrownKevin_riggingTools_cri1_1408.joint_renamer()
	'''

	# Input Area
	# Get selected
	joint_system = pm.ls(selection=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	# Loop through chain
	for current_joint in joint_system:
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		print 'Renaming.', current_joint, 'New Name: ', new_name
		count = count + 1

	count = count - 1

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, 'waste')
	print 'Renaming.', current_joint, 'New Name: ', new_name
	current_joint.rename(new_name)



	print 'Selected joints have been renamed.'

def padding_tool():
	'''
	Creates a pad for the selected root joint.

	import BrownKevin_riggingTools_cri1_1408
	reload(BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected: ', selected
	root_joint = selected[0]

	# Create empty group 
	# (empty=True) this created empty group.
	pad = pm.group(empty=True)

	# Move group to joint.
	#	and delete constraint.
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	# Freeze transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group.
	pm.parent(root_joint, pad)

	# Renaming
	# lt_middle_01_bind
	# lt_middle_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created.'

# def lock_and_hide():

# 	# Get selected.
# 	selected_controls = pm.ls(selection=True)
# 	control_icon = selected_controls[0]
# 	print 'Selected Control', control_icon



# 	print 'Channels locked and hidden.'

def lock_and_hide_trans():
	'''
	locks and hides Transofrorms on selected.

	How to Run:
	import BrownKevin_riggingTools_cri1_1408
	reload (BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.lock_and_hide_trans()
	'''

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)



	print 'Channels locked and hidden.'

def lock_and_hide_rotate():
	'''
	Locks and hide rotates on selected.

	How to Run:
	import BrownKevin_riggingTools_cri1_1408
	reload (BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.lock_and_hide_rotate()
	'''

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)



	print 'Channels locked and hidden.'

def lock_and_hide_scale():
	'''
	Locks and hides scale for selected objects.

	How to Run:
	import BrownKevin_riggingTools_cri1_1408
	reload (BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.lock_and_hide_scale()
	'''

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)



	print 'Channels locked and hidden.'

def unlock_and_show():
	'''
	Unlocks and makes keyable all attributes on selected object.

	How to Run:
	import BrownKevin_riggingTools_cri1_1408
	reload (BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.unlock_and_show()
	'''

	# Get selected.
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


	print 'First selected object has all channels shown.'

def hierarchy():
	'''
	Create a hierarchy based upon a given system.

	Select root joint chain and execute function.

	How to Run:
	import BrownKevin_riggingTools_cri1_1408
	reload (BrownKevin_riggingTools_cri1_1408)
	BrownKevin_riggingTools_cri1_1408.hierarchy()
	'''

	'''
	input
	what are we working on?
	the root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	second_joint = joint_system[1]
	third_joint = joint_system[2]

	'''
	Padding the Root Joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True, name='lt_middle_00_pad')

	# Move group over to the target joint.
	kenny = pm.pointConstraint(root_joint, root_pad)
	pm.delete(kenny)

	# Freeze Transofrorms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.
	pm.parent(root_joint, root_pad)

	'''
	Control Icon 1
	'''

	# Create a control.
	# Change settings: normal x axis, radius is 2
	control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1, 0, 0], radius=2)[0]

	# Group control.
	local_pad_1 = pm.group(control_icon_1, name='lt_middle_01_pad')

	print 'Control', control_icon_1, 'Local Pad', local_pad_1

	# Delete history on control icon.

	# Move control to target joint.
	# Use parent constraint and delete the constraint.
	kenny = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon and driven is the target icon.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control Icon 2
	'''
	# Create a control.
	# Change settings: normal x axis, radius is 2
	control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1, 0, 0], radius=2)[0]

	# Group control.
	local_pad_2 = pm.group(control_icon_2, name='lt_middle_02_pad')

	print 'Control', control_icon_2, 'Local Pad', local_pad_2

	# Delete history on control icon.

	# Move control to target joint.
	# Use parent constraint and delete the constraint.
	kenny = pm.parentConstraint(second_joint, local_pad_2)
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon and driven is the target icon.
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	Control Icon 3
	'''
	# Create a control.
	# Change settings: normal x axis, radius is 2
	control_icon_3 = pm.circle(name='lt_middle_03_icon', normal=[1, 0, 0], radius=2)[0]

	# Group control.
	local_pad_3 = pm.group(control_icon_3, name='lt_middle_03_pad')

	print 'Control', control_icon_3, 'Local Pad', local_pad_3

	# Delete history on control icon.

	# Move control to target joint.
	# Use parent constraint and delete the constraint.
	kenny = pm.parentConstraint(third_joint, local_pad_3)
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon and driven is the target icon.
	pm.orientConstraint(control_icon_3, third_joint)
	'''
	Parenting
	'''
	# Parent local pad 2 to the control icon 1.
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)



	print 'Hierarchy Created'

# Creating control icons.
def control_icon():
	'''
	Control Icon 1
	'''
	# Get selected 

	selected = pm.ls(selection=True)
	print 'Selected', selected
	root_joint = selected[0]
	second_joint = selected[1]
	third_joint = selected[2]

	# Create a control.
	# Change settings: normal x axis, radius is 2
	control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1, 0, 0], radius=2)[0]

	# Group control.
	local_pad_1 = pm.group(control_icon_1, name='lt_middle_01_pad')

	print 'Control', control_icon_1, 'Local Pad', local_pad_1

	# Delete history on control icon.

	# Move control to target joint.
	# Use parent constraint and delete the constraint.
	kenny = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon and driven is the target icon.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control Icon 2
	'''
	# Create a control.
	# Change settings: normal x axis, radius is 2
	control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1, 0, 0], radius=2)[0]

	# Group control.
	local_pad_2 = pm.group(control_icon_2, name='lt_middle_02_pad')

	print 'Control', control_icon_2, 'Local Pad', local_pad_2

	# Delete history on control icon.

	# Move control to target joint.
	# Use parent constraint and delete the constraint.
	kenny = pm.parentConstraint(second_joint, local_pad_2)
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon and driven is the target icon.
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	Control Icon 3
	'''
	# Create a control.
	# Change settings: normal x axis, radius is 2
	control_icon_3 = pm.circle(name='lt_middle_03_icon', normal=[1, 0, 0], radius=2)[0]

	# Group control.
	local_pad_3 = pm.group(control_icon_3, name='lt_middle_03_pad')

	print 'Control', control_icon_3, 'Local Pad', local_pad_3

	# Delete history on control icon.

	# Move control to target joint.
	# Use parent constraint and delete the constraint.
	kenny = pm.parentConstraint(third_joint, local_pad_3)
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon and driven is the target icon.
	pm.orientConstraint(control_icon_3, third_joint)
	'''
	Parenting
	'''
	# Parent local pad 2 to the control icon 1.
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

def color_blue():
	'''
	Setting an objects color.

	sets selected objects color to blue.

	How to Run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.color_blue()
	'''
	# Getting the selected object
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)

def color_red():
	'''
	Setting an objects color.

	sets selected objects color to blue.

	How to Run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.color_red()
	'''
	# Getting the selected object
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	first_selected.overrideEnabled.set(1)
	red = 4
	first_selected.overrideColor.set(red)

def color_yellow():
	'''
	Setting an objects color.

	sets selected objects color to blue.

	How to Run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.color_yellow()
	'''
	# Getting the selected object
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(yellow)

def circle_control():
	'''
	Creates a circle to use for a control icon.

	How to Run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.circle_control()
	'''
	pm.circle(radius=1.8, normal=[0, 1, 0])

def circle_control16():
	'''
	creates a circle to use for a control icon with 16 points.

	How to Run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.circle_control16()
	'''
	pm.circle(radius=1.8, normal=[0, 1, 0], sections=16)

def square_control():
	'''
	creates a square to use as a control.

	How to Run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.sqaure_control()
	'''
	pm.circle(radius=1.8, normal=[0, 1, 0], degree=1, sections=4)

def arrow_control():
	'''
	Create an arrow that is used to controls.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.arrow_control()

	'''
	mel_line = 'curve -d 1 -p 0 0 -0.625 -p 0.625 0 0 -p 0.296799 0 0 -p 0.296799 0 1.253716 -p -0.323347 0 1.253716 -p -0.323347 0 0.0134231 -p -0.625 0 0 -p 0 0 -0.625 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	pm.mel.eval(mel_line)

def cube_control():
	'''
	creates a cube to use as a contorl.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.cube_control()
	'''
	mel_line = 'curve -d 1 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
	pm.mel.eval(mel_line)

def nuke():
	'''
	freezes transforms, deletes history, and centers pivots on selected

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.nuke()
	'''
	pm.delete(ch=True)
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

def parent_con():
	'''
	creates a parent constraint between two selected objects. snaps to location of parent.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.parent_con()
	'''
	pm.parentConstraint()

def parent_con_offset():
	'''
	creates a parent constraint between two selected objects. maintains offset.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.parent_con_offset()
	'''
	pm.parentConstraint(mo=True)

def orient_con():
	'''
	orient constrains two selected objects and snaps.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.orient_con()
	'''
	pm.orientConstraint()

def orient_con_offset():
	'''
	orient constrains two selected objects and maintains offset.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.orient_con_offset()
	'''
	pm.orientConstraint(mo=True)

def point_con():
	'''
	Creates point constrain between two selected objects and snaps

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.point_con()
	'''
	pm.pointConstraint()

def point_con_offset():
	'''
	Creates point constrain between two selected objects and maintains offset.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.point_con_offset()
	'''
	pm.pointConstraint(mo=True)

def float_att():
	'''
	creates float attribute.
	type in name of float attribute

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.float_att()
	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, keyable=True)

def sep_att():
	'''
	creates a serperation attribute on selected objects
	type in name of serperation attribute.

	how to run:
		import BrownKevin_riggingTools_cri1_1408
		reload (BrownKevin_riggingTools_cri1_1408)
		BrownKevin_riggingTools_cri1_1408.sep_att()
	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', en='---------------:', keyable=True)
	attribute = first_selected.attr(attribute_name)
	attribute.set(lock=True)

