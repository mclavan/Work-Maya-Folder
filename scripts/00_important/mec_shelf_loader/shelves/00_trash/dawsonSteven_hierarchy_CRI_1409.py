"""
Steven Dawson
dawsonSteven_hierarchy_CRI_1409.py

Description
	A group of rigging tools.

How to Run:

import dawsonSteven_hierarchy_CRI_1409
reload(dawsonSteven_hierarchy_CRI_1409)
dawsonSteven_hierarchy_CRI_1409.tool()

"""

print 'Rigging Tools Active'

import pymel.core as pm 

# def tool():
# 	print 'Rigging Tools Active'

'''
Big Four (required)
'''
def hierarchy():
	'''
	Create a hiererchy based on a given system

	Select root joint chain and execute function.

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.hierarhcy()
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

	# Create empty group.
	root_pad = pm.group(empty=True)

	# Move group over to target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
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
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_01_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group(name='lt_middle_01_local')

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target location.
	# Delete constraint after snapping
	# Driver: joint
	# Driven: group
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
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_02_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group(name='lt_middle_02_local')

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to the target location.z
	# Delete constraint after snapping
	# Driver: joint
	# Driven: group
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
	# normal=[1,0,0], radius=2w
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_03_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group(name='lt_middle_03_local')

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to the target location.
	# Delete constraint after snapping
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	control_list = control_icon_1, control_icon_2, control_icon_3

	for indiv_cont in control_list:
		# Lock Translates
		indiv_cont.tx.set(lock=True, keyable=False)
		indiv_cont.ty.set(lock=True, keyable=False)
		indiv_cont.tz.set(lock=True, keyable=False)
		# Lock Rotates
		indiv_cont.sx.set(lock=True, keyable=False)
		indiv_cont.sy.set(lock=True, keyable=False)
		indiv_cont.sz.set(lock=True, keyable=False)
		# Lock Visibility
		indiv_cont.v.set(lock=True, keyable=False)

	print 'Hierarchy Created.'

def padding_tool():
	'''
	This tool will create a pad, parent the pad to the root joint, and name the pad.

	select root joint and execute command.

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.padding_tool()

	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected 


	root_joint = selected[0]

	# Create an empty group
	# empty=True will cerate a group with no object in it.
	pad = pm.group(empty=True)


	# Move group to joint.
	# 	Delete Constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Delete transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent
	pm.parent(root_joint, pad)

	# Renaming
	# ct_tail_01_bind
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def priming_tool():
	'''
	This tool will create a pad and a control
	It parents the pad over the control the deletes the temp constraint

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.priming_tool()
	'''
	
	# Get selected
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create a control
		# Normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, name = control_icon_name)[0]



		# Group control (NOT an empty group)
		local_pad = pm.group(name = local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group (NOT control) to target joint
		# delete Constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Costraint joint to Control
		pm.orientConstraint(control_icon, target_joint)

	print 'Local Orineted Controls Created'

def joint_renamer():
	'''
	This tool renames a selected joint chain

	Select a root joint and run the function
	- the script will prompt you first for the orientation ('lt', 'rt') and
	the name of the system ('arm', 'back')

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.joint_renamer()
	'''
	# Renaming Tool using For/In Looping Actions


	# Select the root joints and the children will be selected.
	joint_chain = pm.ls(selection=True, dag=True)

	# Do not worry about the waste suffix
	# ori_name_count_suffix
	# lt_arm_01_bind
	# First pop-up for raw input will be Origin ( lt, rt, ct )
	# Second pop-up for raw input will be Name ( arm, leg, back )

	ori = raw_input()
	system_name = raw_input()
	count = 1
	suffix = 'bind'

	'''
	Loop through joint chain
	'''

	for current_joint in joint_chain:
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, system_name, count, suffix)
		print 'Current Joint: {0} - New Name: {1}'.format(current_joint, new_name)

		# Rename Command
		# variable.rename(new_name)
		current_joint.rename(new_name)

		count = count + 1
	    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, system_name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current_joint, new_name)
	current_joint.rename(new_name)

'''
Coloring Tools:
'''

def color_blue():
	'''
	Color Controls blue

	Select object and execute command.

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.color_blue


	'''
	selected = pm.ls(selection=True, dag=True)
	count = 0
	
	for current_selected in selected:
		count = count + 1

		# first_selected = selected[0]

		#first_selected.tx
		current_selected.overrideEnabled.set(1)
		blue = 6
		current_selected.overrideColor.set(blue)

		
	print 'Currently Changed to blue: ', selected

def color_red():
	'''
	Color Controls red

	Select object and execute command.

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.color_red
	'''
	selected = pm.ls(selection=True, dag=True)
	count = 0
	
	for current_selected in selected:
		count = count + 1

		# first_selected = selected[0]

		#first_selected.tx
		current_selected.overrideEnabled.set(1)
		red = 13
		current_selected.overrideColor.set(red)

		
	print 'Currently Changed to red: ', selected

def color_yellow():
	'''
	Color Controls Yellow

	Select object and execute command.

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.color_yellow
	'''
	selected = pm.ls(selection=True, dag=True)
	count = 0
	
	for current_selected in selected:
		count = count + 1

		# first_selected = selected[0]

		#first_selected.tx
		current_selected.overrideEnabled.set(1)
		yellow = 17
		current_selected.overrideColor.set(yellow)

		
	print 'Currently Changed to yellow: ', selected

'''
Editing Attributes
'''

def add_attr():

	'''
	Adds Attributes based on Raw Input

	Select desired item and execute command.
	User will be prompted for input to name Attribute

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.add_attr()
	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected: ', selected

	first_selected = selected[0]

	# addAttr
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, keyable=True)

def mult_attr():

	'''
	This tool will add a template group of attributes

	Select item and execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.mult_attr

	'''
	selected = pm.ls(selection=True)
	print 'Currently Selected: ', selected

	first_selected = selected[0]
	# addAttr
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	# Create a group of attributes at one time.  
	# The finger attributes are an example.

def unlock_and_show():

	'''
	This tool will unlock and show all attributes

	Select desired item and execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.unlock_and_show

	'''
	selected = pm.ls(selection=True)
	print 'Currently Selected: {0}'.format(selected)

	first_selected = selected[0]
	# Unlock and Show 
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

def lock_and_hide():

	'''
	This tool will lock and hide all attributes

	Select desired item and execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.lock_and_hide
	
	'''
	selected = pm.ls(selection=True)
	print 'Currently Selected: {0}'.format(selected)

	first_selected = selected[0]
	# Unlock and Show 
	first_selected.tx.set(lock=True, keyable=False)
	first_selected.ty.set(lock=True, keyable=False)
	first_selected.tz.set(lock=True, keyable=False)
	first_selected.rx.set(lock=True, keyable=False)
	first_selected.ry.set(lock=True, keyable=False)
	first_selected.rz.set(lock=True, keyable=False)
	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)
	first_selected.v.set(lock=True, keyable=False)

'''
Creating Icon Shapes
'''

def cube():
	'''
	This tool will create a CV Curve in the shape of a cube 
	It accesses mel code to run the complex command in a quicker manner

	execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.cube
	'''
	mel_line = 'curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 ;'
	icon = pm.mel.eval(mel_line)
	print 'Control Icon Created:', icon

def arrow():

	'''
	This tool will create a CV Curve in the shape of an arrow 
	It accesses mel code to run the complex command in a quicker manner

	execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.arrow
	'''

	mel_line = 'curve -d 1 -p -4 0 0 -p -2 0 2 -p -2 0 1 -p 1 0 1 -p 1 0 -1 -p -2 0 -1 -p -2 0 -2 -p -4 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	pm.mel.eval(mel_line)

def square():

	'''
	This tool will create a CV Curve in the shape of a square 
	It accesses mel code to run the complex command in a quicker manner

	execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.square
	'''

	mel_line = 'curve -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
	pm.mel.eval(mel_line)

'''
IK System
'''
def leg_ik():
	'''
	This tool is based on a "FIVE POINT LEG SYSTEM"
	It will create a full IK system for a leg.
	It will create an RP system for the hip to ankle joints.
	It will create two separate SC systems for both the ankle to the ball and the ball to toe.

	Select root joint and execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.leg_ik
	'''
	# Given to us by the user
	joint_chain = pm.ls(selection=True, dag=True)
	print joint_chain

	# Isolate important joints.
	root_joint = joint_chain[0]
	ankle_joint = joint_chain[2]
	ball_joint = joint_chain[3]
	toe_joint = joint_chain[4]

	# Apply IK Handles
	# pm.ikHandle()
	# Name gived gthe IK Handle a name
	# What type of ik is created by default? SC
	# How do we create an RP? Set the solver (sol) flag to ikRPsolver.
	ankle_ik = pm.ikHandle(sol='ikRPsolver', sj=root_joint, ee=ankle_joint, name='lt_ankle_ik')
	ball_ik = pm.ikHandle(sol='ikSCsolver', sj=ankle_joint, ee=ball_joint, name='lt_ball_ik')
	toe_ik = pm.ikHandle(sol='ikSCsolver', sj=ball_joint, ee=toe_joint, name='lt_toe_ik')

'''
Extra Tools
'''

def snapping_tool():
	'''
	This tool moves the first selected object to the second
	- Translates and Rotates the target object.

	import dawsonSteven_hierarchy_CRI_1409
	dawsonSteven_hierarchy_CRI_1409.snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	kenny = pm.parentConstraint(target_joint, control_icon)
	pm.delete(kenny)

	print'The first selected object was moved to the second.'

def point_snapping_tool():
	'''
	This tool moves the first selected object to the second
	- Translates and Rotates the target object.

	import dawsonSteven_hierarchy_CRI_1409
	dawsonSteven_hierarchy_CRI_1409.point_snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	kenny = pm.pointConstraint(target_joint, control_icon)
	pm.delete(kenny)

	print'The first selected object was moved to the second.'

def clus_tool():
	# Given to us by the user
	selected = pm.ls(selection=True)
	print selected

	selected_curve = selected[0]

	#This will loop through the selected curve and apply a cluster the EACH CV of the curve

	for current_cv in selected_curve.cv:
	    print current_cv
	    pm.cluster(current_cv)

def free_tran():
	'''
	This tool will freeze transforms on selected item

	select item and execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.free_tran

	'''
	pm.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0)

def del_hist():
	'''
	This tool will delete history on the selected item

	select item and execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.del_dist
	'''

	pm.delete(ch=True)

def cent_piv():
	'''
	This tool will center the pivot on the selected items

	Select item and execute command
	'''

	pm.xform(cp=True)

def nuke():

	'''
	This tool will delete history, freeze transforms and center pivots 

	Select item and execute command

	import dawsonSteven_hierarchy_CRI_1409
	reload(dawsonSteven_hierarchy_CRI_1409)
	dawsonSteven_hierarchy_CRI_1409.nuke()
	'''

	pm.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0)

	pm.delete(ch=True)

	pm.xform(cp=True)







