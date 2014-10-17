'''
Project 4 Rigging
alcozerEthan_riggingTools_cri1_1409.py

Description:
	Prectical use of loops.
	Renaming joint based upon a naming convention.
	Project 4 file with tools along with description of how to run and use the tools with.
How to Run:

import alcozerEthan_riggingTools_cri1_1409
reload(alcozerEthan_riggingTools_cri1_1409)


'''

print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy():
	'''
	Create a hierarchy based upon a given system.

	Select root joint chain and execute function.

	import alcozerEthan_riggingTools_cri1_1409
	alcozerEthan_riggingTools_cri1_1409.hierarchy
	'''

	'''
	Input
	What are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''
	
	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group over to the trarget joint.
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
	# normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	#Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move Group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)
	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	#Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move Group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)
	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)
	'''
	Control 3
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	#Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move Group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)
	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent Control together.
	'''
	# Pad 3(Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Hierarchy Created'

def padding_tool():
	'''
	Select chosen joint
	run function below

	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create a empty group.
	# 
	pad = pm.group(empty=True)

	# Move group to joint
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

def priming_tool():
	'''
	How to run:
	Select joints in joint series
	to apply multiple priming at once shift select other joints within the same system

	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.priming_tool()
	'''

	# Get Selected
	selected = pm.ls(selection=True)
	# print 'Joints Selected', selected 
	target_joint = selected[0]

	for target_joint in selected: 
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create Control
		#normal set to X and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT an emptry group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created', local_pad
		# Move group to target joint. 
		# 	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint
		pm.orientConstraint(control_icon, target_joint)

	print 'Local Oreiented Controls Created'

def joint_renamer():
	'''
	How to Run:
	select a joint system 
	run the function below

	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.joint_renamer()
	'''


	# Creating Attributes


	#Select the root Joints and I will get its children.
	joint_chain = pm.ls(selection=True, dag=True)

	# Do not worry about the waste suffix
	# ori_name_count_suffix
	# lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
	    new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	   # Rename Command
	   # variable.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)

# Color joint Maker -------------
def icon_yellow():
	'''
	How to Run:
	click on a object in maya and chose one of the three functions within Color Joint Maker to decide on color
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.icon_yellow()
	'''



	# Color Controls

	import pymel.core as pm

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	# first_selected.tx
	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(17)

	#Colors numbers Blue= 6 Red=13 Yellow=17
# Yellow

def icon_blue():
	'''
	How to run:
	click on a object in maya and chose one of the three functions within Color Joint Maker to decide on color
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.icon_blue()
	'''
	# Color Controls

	import pymel.core as pm

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	# first_selected.tx
	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(6)

	#Colors numbers Blue= 6 Red=13 Yellow=17
# Blue

def icon_red():
	'''
	How to run:
	click on a object in maya and chose one of the three functions within Color Joint Maker to decide on color
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.icon_red()
	'''
	# Color Controls

	import pymel.core as pm

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	# first_selected.tx
	first_selected.overrideEnabled.set(1)
	Red = 13
	first_selected.overrideColor.set(13)

	#Colors numbers Blue= 6 Red=13 Yellow=17
# Red
# --------------------------------

# Shape Icon Makers --------------


def cube_maker():
	'''
	How to run
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
 	alcozerEthan_riggingTools_cri1_1409.cube_maker()
 	'''

 	# Cube Maker

	mel_line = 'curve -d 1 -p 0.5 2.551033 1.614373 -p -0.5 2.551033 1.614373 -p -0.5 2.551033 2.614373 -p 0.5 2.551033 2.614373 -p 0.5 2.551033 1.614373 -p 0.5 1.551033 1.614373 -p -0.5 1.551033 1.614373 -p -0.5 2.551033 1.614373 -p -0.5 2.551033 2.614373 -p -0.5 1.551033 2.614373 -p -0.5 1.551033 1.614373 -p -0.5 1.551033 2.614373 -p 0.5 1.551033 2.614373 -p 0.5 2.551033 2.614373 -p 0.5 2.551033 1.614373 -p 0.5 1.551033 1.614373 -p 0.5 1.551033 2.614373 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 '

	pm.mel.eval(mel_line)


def square_maker():
	'''
	How to Run
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.square_maker()
	'''

	# Square Maker

	mel_line = 'nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 '

	pm.mel.eval(mel_line)

def arrow_maker():
	'''
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.arrow_maker()
	'''
	mel_line = 'curve -d 1 -p 0.0416312 0 0.974427 -p 0.0529483 0 -0.0341563 -p 1.014417 0 -0.0341563 -p 0.00366092 0 -1.040687 -p -0.989826 0 0.00666184 -p -0.257849 0 0.00666184 -p -0.257849 0 0.997186 -p 0.0416312 0 0.997186 -p 0.0281396 0 0.985753 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 '

	pm.mel.eval(mel_line)


# Other -------------


def unlock_and_show():
	'''
	To Run:
	For anything that has it's attributes hidden select the object and run the command below 
	the attributes will then be unhidden and keyable
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.unlock_and_show()
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
	# the above is different translations 
	# to unlock a object the command is (lock=False)
	# to make the selected keyable again change (keyable=True)
	# Will not crash if ran twice.


def IKFK_maker():
	'''
	How to run.
	Create five joint chain.
	Select the root joint of the chain
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.IKFK_maker()
	'''
	import pymel.core as pm
	#Giben to us by the user
	joint_chain = pm.ls(selection=True, dag=True)
	print joint_chain

	#    Isolate important joints.
	root_joint = joint_chain[0]
	ankle_joint = joint_chain[2]
	ball_joint = joint_chain[3]
	toe_joint = joint_chain[4]

	# Apply IK Handles
	# pm.ikHandle()
	# sj(startJoint) ee(endEffector)
	# name names the ik handle
	# What type of ik is created by default? SC
	# How do I create a RP?

	ankle_ik = pm.ikHandle(sol='ikRPsolver', ee=ankle_joint, name='lt_ankle_ik')
	ball_ik = pm.ikHandle(sol='ikSCsolver' ,ee=ball_joint, name='lt_ball_ik')
	toe_ik = pm.ikHandle(sol='ikSCsolver', ee=toe_joint, name='lt_toe_ik')


def cluster_maker():
	'''
	How to Run:
	make a curve of the IKFK system from the IKFK Maker
	select the curve
	import alcozerEthan_riggingTools_cri1_1409
	reload(alcozerEthan_riggingTools_cri1_1409)
	alcozerEthan_riggingTools_cri1_1409.cluster_maker()
	'''
	import pymel.core as pm
	#Given to us by the user
	selected = pm.ls(selection=True)

	selected_curve = selected[0]

	for current_cv in selected_curve.cv:
	    print current_cv
	    pm.cluster(current_cv)


def point_snapping_tool():
	'''
	This tool moves the first selected object to the second.
		-Translates and Rotates the target object.

	import alcozerEthan_riggingTools_cri1_1409
	alcozerEthan_riggingTools_cri1_1409.point_snapping_tool()
	'''
	
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	#By default commands work on selected.
	kenny = pm.pointConstraint(selected[0], selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second.'






