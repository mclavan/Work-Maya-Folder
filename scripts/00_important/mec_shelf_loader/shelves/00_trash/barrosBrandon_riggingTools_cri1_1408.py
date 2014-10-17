'''
Brandon Barros
barrosBrandon_riggingTools_cri1_1408.py

Description :
	This script contains a series of rigging tools.

	Tools Included.
	- Snapping (Pole Vector, Orient, Parent (with maintain offset on and off))
	- Leg IK system
	- NUKE button (FT, CP, History)

How to Run :
	import barrosBrandon_riggingTools_cri1_1408
	reload (barrosBrandon_riggingTools_cri1_1408)

'''
print 'Rigging Tools Active'

import pymel.core as pm

def unlock_and_show_all():
	'''
	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)
	'''

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls:', control_icon

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
	print 'Channels locked and hidden'


def lock_and_hide_rotate():
	'''
	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)
	'''

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls:', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden'


def priming_tool():
	'''
	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)
	'''

	# Get selected joints.
	selected_joints = pm.ls(selection=True, dag=True)
	
	for current_joint in selected_joints:
		print 'Current Joint:', current_joint
		#Icon and pad name
		icon_name = current_joint.replace('_bind','_icon')
		local_pad_name = current_joint.replace('_bind', '_local')
		
		#Create a control icon
		control_icon = pm.circle(name=icon_name, normal=[1,0,0], radius=2)[0]


		
		#Create a group (parenting the control under the group)
		local_pad = pm.group(control_icon, name=local_pad_name)


		
		#Move the group to the target
		kill = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kill)


		#Connect control to group
		pm.orientConstraint(control_icon, current_joint)



		#Connect control to group


def joint_renamer():
	'''

	Rename a selected joint chain.
		Naming convention : 
			ori_name_count_suffix

	The user will select the root joint and then execute the tool.

	How to Run :

	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	'''

	# Get selected root joint.
	joint_system = pm.ls(selection=True, dag=True)
	print 'Selected joints have been renamed'

	#orientation_systemName_count_suffix
	#lt_arm_01_bind

	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'bind'

	# Loop through joint chain.
	for current_joint in joint_system:
		#Assembling new name
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)
		
		#Rename joint
		current_joint.rename(new_name)
		
		print'Renaming:', current_joint, 'Newname:' , new_name
		#Pushing the count forward.
		count = count + 1

	new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count-1, 'waste')
	print'Renaming:', joint_system[-1], 'Newname:' , new_name
	current_joint.rename(new_name)

	print 'Selected joints have been renamed.'


def hierarchy():
	'''
	Create a hierarchy based on a given system

	Select root joint chain and execute function

	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	'''

	'''
	Inout
	What are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	print 'Joint System:' , joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group over to the target joint
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
	Control 1 - root joint
	'''
	# Create a control
	# normal=[1,0,0], radius =2
	control_icon_1 = pm.circle(normal=[1,0,0], r=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 created:', control_icon_1
	print 'Local Pad 1 created:', local_pad_1

	# Move group over to the target joint.
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	# Delete constrain after snapping.
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	#Driver --> Control Driven --> Joint
	pm.orientConstraint(control_icon_1, root_joint)
	'''
	Control 2
	'''
	# Create a control
	# normal=[1,0,0], radius =2
	control_icon_2 = pm.circle(normal=[1,0,0], r=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 1 created:', control_icon_2
	print 'Local Pad 1 created:', local_pad_2

	# Move group over to the target joint.
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	# Delete constrain after snapping.
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	#Driver --> Control Driven --> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control
	# normal=[1,0,0], radius =2
	control_icon_3 = pm.circle(normal=[1,0,0], r=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 1 created:', control_icon_3
	print 'Local Pad 1 created:', local_pad_3

	# Move group over to the target joint.
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	# Delete constrain after snapping.
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	#Driver --> Control Driven --> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together
	'''
	# Pad 3 --> Control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Hierarchy Created'


def name_replace():
	'''

	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	Naming Conventions

	Root Joint - 'ct_head_01_bind'
	Root Pad - 'ct_head_00_pad'
	Proxy Geo - 'ct_head_01_proxy'
	Local Pad - 'ct_head_01_local'
	Control Icon - 'ct_head_01_icon'
	'''

	root_joint = 'ct_head_01_bind'

	proxy_name = root_joint.replace('_bind', '_proxy')
	icon_name = root_joint.replace('_bind', '_icon')
	root_pad_name = root_joint.replace('01_bind', '00_pad')

	print 'Old Name:', root_joint
	print 'New Name:', proxy_name
	print 'Control Name:', icon_name
	print 'Pad Name:', root_pad_name

	'''
	Get selected
	
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	second_selected = selected[1]

	new_proxy_name = first_selected.replace('_bind', '_proxy')
	print 'New Proxy Name', new_proxy_name
	second_selected.rename(new_proxy_name)
	print 'New Proxy Name', second_selected
	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	new_pad_name = root_joint.replace('01_bind', '00_pad')

	print 'Pad Name:', new_pad_name



	
	# pad = pm.group(name=)


def hand_attr():
	'''
	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	This function will define all attributes for a standard bipedal humanoid hand, and key them appropriately.
	This function assumes that all joint systems in the hand are properly named
	'''
	

	# Get selected
	
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Define separator attributes and float attributes for the fingers
	# Lock the separator attributes so that they cannot be keyed

	first_selected.addAttr('FINGERS', at='enum', en='---------', keyable=True)
	first_selected.FINGERS.set(lock=True)

	first_selected.addAttr('CURL', at='enum', en='---------', keyable=True)
	first_selected.CURL.set(lock=True)

	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('ring_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', at='enum', en='---------', keyable=True)
	first_selected.SPREAD.set(lock=True)

	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('ring_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	first_selected.addAttr('THUMB', at='enum', en='---------', keyable=True)
	first_selected.THUMB.set(lock=True)

	first_selected.addAttr('thumb_curl', keyable=True)
	first_selected.addAttr('thumb_spread', keyable=True)
	first_selected.addAttr('thumb_drop', keyable=True)

	# Bind the necessary attributes to the finger attributes through the node editor


def basic_if():
	'''
	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	Not meant as a usable function. Purely for reference to the basics of if statements

	Basic if statement

	if condition :
		print 'The condition is True.'
	'''

	if True:
		print'The condition is True.'

	if False:
		print'The condition is True.'

	'''
	What is the condition?

	2==2 (double equal signs is equality in Python. one = assigns value from one side to another)

	'''

	'''
	Operators

	== Equals
	!= Not Equals
	> = Greater than
	>= Greater than or equal to
	< = Less than
	<= Less than or equal to
	'''

	if 2==2:
		print 'The 2 is equal to 2.'

	'''
	Using multiple conditions

	and
	or

	Not
	'''

	if 2==2 and 2!=3:
		print'This is true.'

	'''
	What if I want to react to false?
	'''
	if 2==3:
		print'Condition is true.'
	else:
		print'Condition is False'

	'''
	What if I want to have multiple paths
	elif
	'''

	value = 1
	if vlue ==1: 
		print'Color is red'
	elif value==2:
		print 'color is Blue'
	elif value==3:
		print'Color is Green'

	'''
	about command
	'''

	if pm.about(windows=True):
		print'You are using windows.'
	elif pm.about(macOS=True):
		print'You are using osx.'
	else:
		print 'You are using a different os.'


def rfl():
	'''

	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	This function is a work in progress and is not currently functionable.


	Create a standard rfl system on a selected joint chain
		Adds the necessary attributes for an rfl
			HEEL-----------
				heel_pivot
				heel_rotate

			INNER BANK---------
				inner_bank
				inner_bank_rotate

			OUTER BANK--------
				outer_bank
				outer_bank_rotate
			TOE--------
				toe_pivot
				toe_rotate

			BALL--------
				ball_pivot
				ball_rotate

	This function assumes that the rfl joint chain has already been created and positioned.
	This function assumes that the control icon for the foot has already been created and placed.
	This function also renames the joint system, so naming the joints when you create them is unnecessary.


	How to run : 
	import barrosBrandon
	barrosBrandon.rfl()
	'''

	'''
	Rename the joint system
	'''
	# Get selected root joint.
	joint_system = pm.ls(selection=True, dag=True)
	print 'Selected joints have been renamed'

	#orientation_systemName_count_suffix
	#lt_arm_01_bind

	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'rfl'


def rename_gui():
	
	'''
	This function will display the renaming Interface

	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	This function is not bound to the renamer tool yet, so it simply creates the basic ui desired for renaming
	'''
	
	'''
	Setting up the Interface
	'''

	# Make window

	window_object = pm.window(title='Rename', sizeable=False)

	# Show window

	window_object.show()

	# Main Layout
	main_layout = pm.columnLayout()

	# Make orientation layout and buttons
	pm.frameLayout(label='Orientation', width = 600)
	pm.rowColumnLayout(nc=3)

	left_button = pm.checkBox(label='Left', width = 200)
	right_button = pm.checkBox(label='Right', width = 200)
	center_button = pm.checkBox(label='Center', width = 200)
	pm.setParent(main_layout)

	# Make name / suffix layout and name fields

	second_layout = pm.rowColumnLayout(nc=2)
	
	pm.frameLayout(label='Name', width=300)
	pm.nameField()
	pm.setParent(second_layout)

	pm.frameLayout(label='Suffix', width=300)
	pm.nameField()
	pm.setParent(main_layout)

	# Make accept / decline name layout and buttons

	button_layout = pm.rowColumnLayout(nc=2, columnWidth= [[1,300],[2,300]])
	
	accept_button = pm.button(label='Accept', width = 100)
	decline_button = pm.button(label='Decline', width = 100)
	pm.setParent(main_layout)

	'''
	Programming the Interface
	'''

	# Setting up orientation button values


def nuke():
	'''
	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	barrosBrandon.nuke()

	This function will run the following operations : 
		freeze Transforms
		delete History
		center pivot 
	'''
	# Freeze transforms
	pm.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

	# Delete history
	pm.delete(all=True, constructionHistory=True)

	# Center Pivot
	pm.xform(cp=True)


def leg_ik():

	'''
	How to run
	import barrosBrandon_riggingTools_cri1_1408
	reload(barrosBrandon_riggingTools_cri1_1408)

	barrosBrandon.leg_ik()

	This function will create a standard ik system on a bipedal leg system.

	Select the root joint and then run the operation.
	'''

	#Get Selected

	selected_joints = pm.ls(selection=True)
	print 'Selected Joints:', selected_joints


	#Get Root Joint

	root_joint = selected_joints[0]
	print 'Root Joint:', root_joint

	#Get the hierarchy

	leg_system = pm.ls(root_joint, dag=True)
	print 'Leg System:', leg_system

	#Get Ankle Joint
	ankle_joint = leg_system[2]
	print 'Ankle Joint:', ankle_joint

	#Apply RPIK
	pm.ikHandle(name= 'leg_ik', startJoint= root_joint, endEffector = ankle_joint, sol='ikRPsolver')

	#Get Ball Joint
	ball_joint = leg_system[3]
	print 'Ball Joint:', ball_joint

	#Apply SCIK
	pm.ikHandle(name= 'ball_ik', startJoint= ankle_joint , endEffector = ball_joint)

	#Get Toe Joint
	toe_joint = leg_system[4]
	print 'Toe Joint:', toe_joint

	#Apply SCIK
	pm.ikHandle(name= 'toe_ik', startJoint= ball_joint , endEffector = toe_joint)
	











	








	
