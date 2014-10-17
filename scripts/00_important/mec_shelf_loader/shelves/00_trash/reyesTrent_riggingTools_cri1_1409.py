'''
Trent Reyes
reyesTrent_riggingTools_cri1_1409.py

Description:
	A group of rigging related tools.

How to Run:

import reyesTrent_riggingTools_cri1_1409
reload(reyesTrent_riggingTools_cri1_1409)

'''

print 'Rigging Tools Active'

import pymel.core as pm

def tool():
	print 'Tool Active.'

def snapping_tool():
	'''
	This tool moves the first selected object to the second.
		-Translates and Rotates the target object.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.snapping_tool()

	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	temp = pm.parentConstraint(target_joint, control_icon)
	pm.delete(temp)

	print 'The first selected object was moved to the second.'


def point_snapping_tool():
	'''
	This tool moves the first selected object to the second.
		-Translates the target object.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.point_snapping_tool()

	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	temp = pm.pointConstraint(target_joint, control_icon)
	pm.delete(temp)

	print 'The first selected object was moved to the second.'


def world_icon():
	'''
	This tool creates an icon in world orientation
	and snaps it to a target joint.
		- Select joint then execute function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.world_icon()

	'''


	# Get selected.
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	first_joint = selected[0]

	# Create a control icon.
	control_icon_1 = pm.circle(normal=[0, 1, 0], radius=2)[0]

	# Move the control to the target joint.
	# Delete the constraint.
	temp = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(temp)

	print 'Icons created.'

def joint_renamer():
	'''
	This tool renames an entire joint chain.
	Select root joint then execute function.
		- Will be prompted for two inputs:
			First- joint orientation
			Second- joint name

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.joint_renamer()

	'''

	# Select the root joint and I will get its children.
	joint_chain = pm.ls(selection=True, dag=True)

	# Do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
	    new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	    # Rename command
	    # variable.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)

def padding_tool():
	'''
	This tool creates pads for joint systems.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.padding_tool()
	'''

	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create empty group.
	pad = pm.group(empty=True)

	# Move group to joint.
	# 	Delete contraint.
	temp = pm.pointConstraint(root_joint, pad)
	pm.delete(temp)

	# Freeze tranforms.
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group.
	pm.parent(root_joint, pad)

	# Rename.
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	# Looping.



def hierarchy():
	'''
	Create a hierarchy based upon a given system.

	Select root joint chain and execute function.

	Joint chain should be named in order to work properly.
		Execute joint_renamer function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.hierarchy()

	'''

	joint_system = pm.ls(selection=True, dag=True)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	print 'Hierarchy Created.'

	'''
	Padding Root Joint

	'''
	# Create empty group.
	root_pad = pm.group(empty=True)

	# Move group over to the target.
	temp = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp)

	# Freeze Transforms on group.
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	
	# Parent root joint to the group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''

	'''
	Control 1 - root_joint
	'''
	# Create a control. (normal=[1, 0, 0], radius=2)
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 Created: ', control_icon_1
	print 'Local Pad 1 Created: ', local_pad_1

	# Move group over to the target joint.
	# Delete constraint after snapping.
	temp = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp)

	# Orient Constrain the joint to control.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2 - joint_2
	'''
	# Create a control. (normal=[1, 0, 0], radius=2)
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 2 Created: ', control_icon_2
	print 'Local Pad 2 Created: ', local_pad_2

	# Move group over to the target joint.
	# Delete constraint after snapping.
	temp = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp)

	# Orient Constrain the joint to control.
	pm.orientConstraint(control_icon_2, joint_2)
	'''
	Control 3 - joint_3
	'''
	# Create a control. (normal=[1, 0, 0], radius=2)
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 Created: ', control_icon_3
	print 'Local Pad 3 Created: ', local_pad_3

	# Move group over to the target joint.
	# Delete constraint after snapping.
	temp = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp)

	# Orient Constrain the joint to control.
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent controls to each other.
	'''
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	'''
	Rename controls.
	'''
	# STRING METHOD:

	# selected = pm.ls(selection=True)
	# first_selected = selected[0]
	# second_selected = selected[1]

	# new_icon_name = first_selected.replace('_bind', '_icon')

	# second_selected.rename(new_icon_name)
	# print 'New Icon Name: ', second_selected

	new_icon_name = root_joint.replace('_bind', '_icon')

	control_icon_1.rename(new_icon_name)
	print 'New Icon Name: ', control_icon_1

	new_icon_name = joint_2.replace('_bind', '_icon')

	control_icon_2.rename(new_icon_name)
	print 'New Icon Name: ', control_icon_2

	new_icon_name = joint_3.replace('_bind', '_icon')

	control_icon_3.rename(new_icon_name)
	print 'New Icon Name: ', control_icon_3

	'''
	Rename local pads.
	'''

	new_pad_name = control_icon_1.replace('_icon', '_local')

	local_pad_1.rename(new_pad_name)
	print 'New Local Pad Name: ', local_pad_1

	new_pad_name = control_icon_2.replace('_icon', '_local')

	local_pad_2.rename(new_pad_name)
	print 'New Local Pad Name: ', local_pad_2

	new_pad_name = control_icon_3.replace('_icon', '_local')

	local_pad_3.rename(new_pad_name)
	print 'New Local Pad Name: ', local_pad_3

	'''
	Rename root pad
	'''

	new_pad_name = root_joint.replace('_bind', '_pad')

	root_pad.rename(new_pad_name)
	print 'New Pad Name: ', root_pad

	'''
	Lock and hide attributes
	'''
	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=True, keyable=False)
	control_icon_1.tz.set(lock=True, keyable=False)
	control_icon_1.sx.set(lock=True, keyable=False)
	control_icon_1.sy.set(lock=True, keyable=False)
	control_icon_1.sz.set(lock=True, keyable=False)
	control_icon_1.v.set(lock=True, keyable=False)

	control_icon_2.tx.set(lock=True, keyable=False)
	control_icon_2.ty.set(lock=True, keyable=False)
	control_icon_2.tz.set(lock=True, keyable=False)
	control_icon_2.sx.set(lock=True, keyable=False)
	control_icon_2.sy.set(lock=True, keyable=False)
	control_icon_2.sz.set(lock=True, keyable=False)
	control_icon_2.v.set(lock=True, keyable=False)

	control_icon_3.tx.set(lock=True, keyable=False)
	control_icon_3.ty.set(lock=True, keyable=False)
	control_icon_3.tz.set(lock=True, keyable=False)
	control_icon_3.sx.set(lock=True, keyable=False)
	control_icon_3.sy.set(lock=True, keyable=False)
	control_icon_3.sz.set(lock=True, keyable=False)
	control_icon_3.v.set(lock=True, keyable=False)

def priming_tool():
	'''
	This tool creates local oriented controls with pads
	and constrains joints to them.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.priming_tool()
	'''

	# Get selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected: ', selected
	# target_joint = selected[0]

	for target_joint in selected:
		# Rename
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control. (norms to x, radius to 2)
		control_icon = pm.circle(normal=[1, 0, 0], radius=2, name=control_icon_name)[0]

		# Group control. (NOT empty group)
		local_pad = pm.group(name=local_pad_name)
		print 'Control Icon: ', control_icon
		print 'Pad Created: ', local_pad

		# Move group to target joint.
		#	Delete constraint.
		temp = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created.'


def unlock_and_show():
	'''
	This tool unlocks and shows main attributes of a selected object

	Select curve and run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.unlock_and_show()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	# Lock and Hide
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

def color_icon_blue():
	'''
	This tool colors selected icon blue.

	Select curve and run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.color_icon_blue()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)

def color_icon_yellow():
	'''
	This tool colors selected icon yellow.

	Select curve and run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.color_icon_yellow()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(yellow)

def color_icon_red():
	'''
	This tool colors selected icon red.

	Select curve and run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.color_icon_red()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	red = 13
	first_selected.overrideColor.set(red)

def add_attribute():
	'''
	This tool adds an attribute to target.

	Select curve and run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.add_attribute()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	# addAttr
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, keyable=True)

def add_separator_attribute():
	'''
	This tool adds a separator attribute for target.

	Select curve and run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.add_separator_attribute()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	# addAttr
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', en='---------------:', keyable=True)

def three_finger_hand_attributes():
	'''
	This tool automatically adds attributes for a three finger had.

	Selected curve then run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.three_finger_hand_attributes()

	'''

	# Creating Attributes

	import pymel.core as pm

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	# addAttr()
	first_selected.addAttr('IKFK', keyable=True, min=0, max=10)

	first_selected.addAttr('CURLS', at='enum', en='---------------:', keyable=True)

	first_selected.addAttr('Index_Curl', keyable=True, min=-10, max=10)
	first_selected.addAttr('Middle_Curl', keyable=True, min=-10, max=10)
	first_selected.addAttr('Pinky_Curl', keyable=True, min=-10, max=10)

	first_selected.addAttr('SPREADS', at='enum', en='---------------:', keyable=True)

	first_selected.addAttr('Index_Spread', keyable=True, min=-10, max=10)
	first_selected.addAttr('Middle_Spread', keyable=True, min=-10, max=10)
	first_selected.addAttr('Pinky_Spread', keyable=True, min=-10, max=10)

	first_selected.addAttr('THUMB', at='enum', en='---------------:', keyable=True)

	first_selected.addAttr('Thumb_Curl', keyable=True, min=-10, max=10)
	first_selected.addAttr('Thumb_Drop', keyable=True, min=-10, max=10)

def ikfk_builder():
	'''
	This tool builds the basic ikfk system for an arm chain with three joints.

	Select arm root and run function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.ikfk_builder()

	'''

	# get selected
	selected = pm.ls(selection=True)

	bind_joint_chain = pm.ls(selected, dag=True)

	# duplicate joint chain
	ik_root_joint = pm.duplicate(selected, rc=True)[0]
	fk_root_joint = pm.duplicate(selected, rc=True)[0]

	ik_joint_chain = pm.ls(ik_root_joint, dag=True)

	for each in ik_joint_chain:
		new_name = each.replace("bind", 'ik')
		each.rename(new_name)

	fk_joint_chain = pm.ls(fk_root_joint, dag=True)

	for each in fk_joint_chain:
		new_name = each.replace("bind", 'fk')
		each.rename(new_name)

	# rename joint chains
	# joint_renamer(ik_joint_chain, 'lt', 'armIK')
	# joint_renamer(fk_joint_chain, 'lt', 'armFK')

	# make IK
	shoulder_joint_ik = ik_joint_chain[0]
	wrist_joint_ik = ik_joint_chain[2]

	arm_ik = pm.ikHandle(sol='ikRPsolver', sj=shoulder_joint_ik, ee=wrist_joint_ik, name='rt_arm_ik')[0]

	# Make icons
	mel_line = 'curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
	ik_icon = pm.mel.eval(mel_line)
	temp = pm.pointConstraint(wrist_joint_ik, ik_icon)
	pm.delete(temp)
	pm.makeIdentity(ik_icon, apply=True, translate=1, rotate=1, scale=1, normal=0)

	fk_shoulder_icon = pm.circle(normal=[1, 0, 0])[0]
	fk_shoulder_local = pm.group()
	temp = pm.parentConstraint(fk_joint_chain[0], fk_shoulder_local)
	pm.delete(temp)

	fk_elbow_icon = pm.circle(normal=[1, 0, 0])[0]
	fk_elbow_local = pm.group()
	temp = pm.parentConstraint(fk_joint_chain[1], fk_elbow_icon)
	pm.delete(temp)

	# Parent fk controls
	pm.parent(fk_elbow_local, fk_shoulder_icon)

	# Constrain ikfk systems to bind joints
	pm.parentConstraint(ik_joint_chain[0], fk_joint_chain[0], bind_joint_chain[0])
	pm.parentConstraint(ik_joint_chain[1], fk_joint_chain[1], bind_joint_chain[1])
	
	# Constrain icons to systems
	# fk
	pm.orientConstraint(fk_shoulder_icon, fk_joint_chain[0])
	pm.orientConstraint(fk_elbow_icon, fk_joint_chain[1])

	# ik
	pm.pointConstraint(ik_icon, arm_ik)


def leg_rfl_builder():
	'''
	This tool builds the basic rfl leg system.

	Select leg root and rfl root then execute function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.leg_rfl_builder()

	'''

	selected = pm.ls(selection=True)

	leg_root_joint = selected[0]
	rfl_root_joint = selected[1]

	leg_system = pm.ls(leg_root_joint, dag=True)
	rfl_system = pm.ls(rfl_root_joint, dag=True)

	root_joint = leg_system[0]
	ankle_joint = leg_system[2]
	ball_joint = leg_system[3]
	toe_joint = leg_system[4]

	ankle_ik = pm.ikHandle(sol='ikRPsolver', sj=root_joint, ee=ankle_joint, name='lt_ankle_ik')[0]
	ball_ik = pm.ikHandle(sol='ikSCsolver', sj=ankle_joint, ee=ball_joint, name='lt_foot_ik')[0]
	toe_ik = pm.ikHandle(sol='ikSCsolver', sj=ball_joint, ee=toe_joint, name='lt_toe_ik')[0]

	# Create controls

	# rfl
	# heel
	heel_icon = pm.circle(normal=[1, 0, 0])[0]
	temp = pm.pointConstraint(rfl_system[0], heel_icon)
	pm.delete(temp)
	pm.makeIdentity(heel_icon, apply=True, translate=1, rotate=1, scale=1, normal=0)

	# toe
	toe_icon = pm.circle(normal=[1, 0, 0])[0]
	temp = pm.pointConstraint(rfl_system[1], toe_icon)
	pm.delete(temp)
	pm.makeIdentity(toe_icon, apply=True, translate=1, rotate=1, scale=1, normal=0)

	# ball
	ball_icon = pm.circle(normal=[1, 0, 0])[0]
	temp = pm.pointConstraint(rfl_system[2], ball_icon)
	pm.delete(temp)
	pm.makeIdentity(ball_icon, apply=True, translate=1, rotate=1, scale=1, normal=0)

	# foot
	foot_icon = pm.circle(normal=[0, 1, 0])[0]
	temp = pm.pointConstraint(ankle_joint, foot_icon)
	pm.delete(temp)
	pm.makeIdentity(foot_icon, apply=True, translate=1, rotate=1, scale=1, normal=0)
	
	# parent controls
	# toe -> heel
	# ball -> toe
	pm.parent(heel_icon, foot_icon)
	pm.parent(toe_icon, heel_icon)
	pm.parent(ball_icon, toe_icon)

	# freeze transforms on controls

	# parent iks to controls
	pm.parent(ankle_ik, rfl_system[-1])
	pm.parent(ball_ik, rfl_system[-2])
	pm.parent(toe_ik, rfl_system[-3])

	heel_joint = rfl_system[0]
	toe_joint = rfl_system[1]
	ball_joint = rfl_system[2]

	pm.parentConstraint(heel_icon, heel_joint, mo=True)
	pm.orientConstraint(toe_icon, toe_joint, mo=True)
	pm.orientConstraint(ball_icon, ball_joint, mo=True)


def stretchy_back_builder():
	'''
	This tool creates a basic stretchy back system on selected joint chain.

	Select back root and execute function.

	import reyesTrent_riggingTools_cri1_1409
	reyesTrent_riggingTools_cri1_1409.stretchy_back_builder()

	'''

	# Create curve
	joint_chain = pm.ls(selection=True, dag=True)
 
	jointPositions = []  

	# Get Joint Positions 
	for joints in joint_chain:  
	    pos = pm.xform(joints, q=True, ws=True, t=True)  
	    jointPositions.append(tuple(pos))  

	# Curve snap to joint positions       
	pm.curve(p=jointPositions)

	# Create clusters
	selected = pm.ls(selection=True)

	selected_curve = selected[0]


	for current_cv in selected_curve.cv:
		print current_cv
		pm.cluster(current_cv)

	pm.group()

	# Create Controls
	# FK
	fk_icon_1 = pm.circle(normal=[0, 1, 0], radius=2)[0]
	temp = pm.pointConstraint(joint_chain[0], fk_icon_1)
	pm.delete(temp)
	pm.makeIdentity(fk_icon_1, apply=True, translate=1, rotate=1, scale=1, normal=0)

	fk_icon_2 = pm.circle(normal=[0, 1, 0], radius=2)[0]
	temp = pm.pointConstraint(joint_chain[1], fk_icon_2)
	pm.delete(temp)
	pm.makeIdentity(fk_icon_2, apply=True, translate=1, rotate=1, scale=1, normal=0)

	fk_icon_3 = pm.circle(normal=[0, 1, 0], radius=2)[0]
	temp = pm.pointConstraint(joint_chain[2], fk_icon_3)
	pm.delete(temp)
	pm.makeIdentity(fk_icon_3, apply=True, translate=1, rotate=1, scale=1, normal=0)

	fk_icon_4 = pm.circle(normal=[0, 1, 0], radius=2)[0]
	temp = pm.pointConstraint(joint_chain[3], fk_icon_4)
	pm.delete(temp)
	pm.makeIdentity(fk_icon_4, apply=True, translate=1, rotate=1, scale=1, normal=0)

	fk_icon_5 = pm.circle(normal=[0, 1, 0], radius=2)[0]
	temp = pm.pointConstraint(joint_chain[4], fk_icon_5)
	pm.delete(temp)
	pm.makeIdentity(fk_icon_5, apply=True, translate=1, rotate=1, scale=1, normal=0)

	fk_icon_6 = pm.circle(normal=[0, 1, 0], radius=2)[0]
	temp = pm.pointConstraint(joint_chain[5], fk_icon_6)
	pm.delete(temp)
	pm.makeIdentity(fk_icon_6, apply=True, translate=1, rotate=1, scale=1, normal=0)

	# fk_icon_7 = pm.circle(radius=2)[0]
	# temp = pm.pointConstraint(joint_chain[0], fk_icon_7)
	# pm.delete(temp)

	# Indy
	indy_icon_1 = pm.circle(normal=[0, 1, 0], radius=1.5)[0]
	temp = pm.pointConstraint(joint_chain[0], indy_icon_1)
	pm.delete(temp)
	pm.makeIdentity(indy_icon_1, apply=True, translate=1, rotate=1, scale=1, normal=0)

	indy_icon_2 = pm.circle(normal=[0, 1, 0], radius=1.5)[0]
	temp = pm.pointConstraint(joint_chain[1], indy_icon_2)
	pm.delete(temp)
	pm.makeIdentity(indy_icon_2, apply=True, translate=1, rotate=1, scale=1, normal=0)

	indy_icon_3 = pm.circle(normal=[0, 1, 0], radius=1.5)[0]
	temp = pm.pointConstraint(joint_chain[2], indy_icon_3)
	pm.delete(temp)
	pm.makeIdentity(indy_icon_3, apply=True, translate=1, rotate=1, scale=1, normal=0)

	indy_icon_4 = pm.circle(normal=[0, 1, 0], radius=1.5)[0]
	temp = pm.pointConstraint(joint_chain[3], indy_icon_4)
	pm.delete(temp)
	pm.makeIdentity(indy_icon_4, apply=True, translate=1, rotate=1, scale=1, normal=0)

	indy_icon_5 = pm.circle(normal=[0, 1, 0], radius=1.5)[0]
	temp = pm.pointConstraint(joint_chain[4], indy_icon_5)
	pm.delete(temp)
	pm.makeIdentity(indy_icon_5, apply=True, translate=1, rotate=1, scale=1, normal=0)

	indy_icon_6 = pm.circle(normal=[0, 1, 0], radius=1.5)[0]
	temp = pm.pointConstraint(joint_chain[5], indy_icon_6)
	pm.delete(temp)
	pm.makeIdentity(indy_icon_6, apply=True, translate=1, rotate=1, scale=1, normal=0)

	# Parent systems
	pm.parent(fk_icon_6, fk_icon_5)
	pm.parent(fk_icon_5, fk_icon_4)
	pm.parent(fk_icon_4, fk_icon_3)
	pm.parent(fk_icon_3, fk_icon_2)
	pm.parent(fk_icon_2, fk_icon_1)



# SQUARE
# mel_line = 'curve -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
# icon = pm.mel.eval(mel_line)

# print 'Control Icon Created: ', icon

# ARROW
# mel_line = 'curve -d 1 -p 2 0 1 -p 0 0 3 -p -2 0 1 -p -1 0 1 -p -1 0 -2 -p 1 0 -2 -p 1 0 1 -p 2 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
# icon = pm.mel.eval(mel_line)

# print 'Control Icon Created: ', icon

# CUBE
# mel_line = 'curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
# icon = pm.mel.eval(mel_line)

# print 'Control Icon Created: ', icon


# PYRAMID
# mel_line = 'curve -d 1 -p 0.707107 -0.353553 0 -p 0 0.353553 0 -p 9.27258e-08 -0.353553 -0.707107 -p 0.707107 -0.353553 0 -p -3.09086e-08 -0.353553 0.707107 -p 0 0.353553 0 -p -0.707107 -0.353553 -6.18172e-08 -p -3.09086e-08 -0.353553 0.707107 -p -0.707107 -0.353553 -6.18172e-08 -p 9.27258e-08 -0.353553 -0.707107 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;'
# icon = pm.mel.eval(mel_line)

# print 'Control Icon Created: ', icon





