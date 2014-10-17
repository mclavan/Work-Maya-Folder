'''

Christina Bodden
BoddenChristina_riggingTools_cri1_1409.py

Description:

	A group of rigging related tools.

How To Run:

	import BoddenChristina_riggingTools_cri1_1409
	reload (BoddenChristina_riggingTools_cri1_1409)
	BoddenChristina_riggingTools_cri1_1409.BoddenChristina_riggingTools_cri1_1409()

'''

print 'Rigging Tools Active'

import pymel.core as pm 

	# import pymel.core as pm: affects everything below.


# --------------------------------


'''
	
	JOINT COMMANDS

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 

'''

def priming_tool():

	'''
	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 

	Description:

		Create a locally oriented control and prime for each joint in a hierarchy.

	How To Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.priming_tool()

	'''

	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected[0]

	for target_joint in selected: 
		control_icon_name = target_joint.replace ('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create a control
		# Normals set to x and radius set to 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius = 1.8, name=control_icon_name)[0]

		# Group controls (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target point

		# Delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control
		pm.orientConstraint(control_icon, target_joint)

	print 'Local Oriented Controls Created'

def snapping_tool():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	This tool moves the first selected object to the second.
		- Translates and Rotates the target object.

	How it is run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.snapping_tool()

	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected [0]
	control_icon = selected [1]

	# by default commands work on selected.
	kenny = pm.parentConstraint(selected[0], selected[1])
	pm.delete(kenny)

	# Indenting matters when it comes to the defining process.
	# Indenting means it is part of the command.

	print 'The first selected object was moved to the second.'

def point_snapping_tool():

	'''
	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		This tool moves the first selected object to the second.
			- Translates the target object.

	How it is run:

		import rigigng_tools
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.point_snapping_tool()

	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected [0]
	control_icon = selected [1]

	# by default commands work on selected.
	kenny = pm.pointConstraint(selected[0], selected[1])
	pm.delete(kenny)

	# Indenting matters when it comes to the defining process.
	# Indenting means it is part of the command.

	print 'The first selected object was moved to the second.'

	# def point_snapping_tool():

def hierarchy():

	'''
	Christina Bodden
	joint_hierarchy.py

	Description:
		Creating a joint hierarchy.

	How To Run:
		Using selection and a joint chain.

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.hierarchy()

	'''

	print 'Rigging Tools Active'

	'''

	Create a hierarchy based upon a given system.

	Select root joint chain and execute function.

	import BoddenChristina_riggingTools_cri1_1409
	reload (BoddenChristina_riggingTools_cri1_1409)
	BoddenChristina_riggingTools_cri1_1409.hierarchy()

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

	print 'Hierarchy Created.'

	# Psedo Code
	# A series of commands that are written out in plain English.
	# Plotting out what you are going to do before you do it.


	'''

	Padding Root Joint

	'''

	# Create empty group.
	# root_pad = pm.group(empty=True)

	new_pad_name = root_joint.replace('01_bind', '00_pad')
	print 'Pad Name:', new_pad_name

	root_pad = pm.group(empty=True, name=new_pad_name)

	# Move group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Pararent root joint to the group.
	pm.parent(root_joint, root_pad)

	'''

	Local Controls

	'''

	'''

	Control 1

	'''

	# Create a controls.
	# Normal=[1, 0, 0], radius=2
		# Base: control_icon_1 = pm.circle(normal=[1, 0 , 0], radius=2)

	new_group_name = root_joint.replace('01_bind', '01_icon')
	print 'Group Name:', new_group_name

	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2, name=new_group_name)

	# Create a group.
	# Grouping control during the process.
	
	new_local_name = root_joint.replace('01_bind', '01_local')
	local_pad_1 = pm.group(name=new_local_name)

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''

	Control 2

	'''

	# Create a control.
	# Normal=[1, 0 ,0], radius=2

	# Create a group.
	# Grouping control during the process.

	# move group over to te target joint.
	# Delete contraint after snapping

	# Create a controls.
	# Normal=[1, 0, 0], radius=2
	new_group_name = root_joint.replace('01_bind', '02_icon')
	print 'Group Name:', new_group_name

	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2, name=new_group_name)

	# Create a group.
	# Grouping control during the process.
	
	new_local_name = root_joint.replace('01_bind', '02_local')
	local_pad_2 = pm.group(name=new_local_name)

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_2, joint_2)

	'''

	Control 3

	'''

	# Create a controls.
	# Normal=[1, 0, 0], radius=2
	new_group_name = root_joint.replace('01_bind', '03_icon')
	print 'Group Name:', new_group_name

	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2, name=new_group_name)

	# Create a group.
	# Grouping control during the process.
	new_local_name = root_joint.replace('01_bind', '03_local')
	local_pad_3 = pm.group(name=new_local_name)

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_3, joint_3)

	'''

	Partent Control Together

	'''

	# Pad 3 (Last) -> Control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Loop Hierarchy Created.'

def joint_renamer():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		This tool renames a selected joint chain.

		Select a root joint and run the function.
			- The script with prompt you first for the Orientation ('lt', 'rt', 'ct')
				and the name of the system ('arm', 'back', 'leg')

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.joint_renamer()

	'''

	# Creating Attributes

	# Select the root koint and I will get its children.
	joint_chain = pm.ls(selection=True, dag=True)


	# dag: Grab all the children in a selected object

	# Do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind

	# First: Orientation of system
	# Second: Name of system

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
		# new_name = 'lt_arm_01_bind'
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)
		print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
		
		# Rename command
		# variable.rename(new_name)
		current.rename(new_name)
		
		count = count + 1

	# Can change the name of control icons
	# Take out dag when doing this!

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)

	print 'Joints Renamed.'

def padding_tool():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		Create a world-oriented group that the selected joint system will be parented to.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.padding_tool()

	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create an empty group
	# What is the flag for an empty group?
	# em = empty (boolean)
	# empty=True will create an empty group

	pad = pm.group(empty=True)

	# Move group to joint.
	# Delete constraints

	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transform on group

	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent the joint to the group.

	pm.parent(root_joint, pad)

	# Renaming
	# lt_middle_01_local
	# lt_middle_00_pad

	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding Group Created.'


# --------------------------------


'''

	CONTROL ICON PRESETS

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def color_controls_blue():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		Changes the colour of the selected control(s) to blue.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.color_controls_blue()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)

	print 'Control Changed to BLUE.'

def color_controls_red():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		Changes the colour of the selected control(s) to red.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.color_controls_red()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	red = 13
	first_selected.overrideColor.set(red)

	print 'Control Changed to RED.'

def color_controls_yellow():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Changes the colour of the selected control(s) to yellow.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.color_controls_yellow()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]


	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(yellow)

	print 'Control Changed to YELLOW.'


# --------------------------------


'''

	ATTRIBUTE COMMANDS

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 
	
'''

def setting_attribute():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Setting the value of the translate attribute of an object.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.setting_attribute()

	'''

	first_selected.tx.set[0]
	first_selected.ty.set[0]
	first_selected.tz.set[0]

	first_selected.t.set([0, 0, 0])

def creating_attributes():
	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		Creates attributes as FLOATS.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_attributes()

	'''

	# Creating Attributes

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, keyable=True)

	print 'Float Attribute Created.'

def creating_attribute_seperators():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creates attribute seperators as ENUM. (----------)

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_attribute_seperators()

	'''

	# Creating Serperators
	# Enum sperators

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', en="--------------------:", keyable=True)

	print 'Enum Attribute Seperator Created.'

def unlock_and_show():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		Brings back lock and hidden attributes (Translates, Rotates, Scales, Visibility)

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.unlock_and_show()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

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

	# Ideas?
	# You can create seperate tools
		# Translates and Rotates

	# You can create a seperate tool for just locking and hiding attributes.

	print 'Attributes Unlocked and Shown.'

def lock_and_hide():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		Locks and hides attributes (Translates, Rotates, Scales, Visibility)

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.lock_and_hide()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

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

	print 'Attributes Locked and Hidden.'


# --------------------------------


'''

	NINE NASTY THINGS

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def freeze_transforms():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 

	Description:

		Freezes transforms on selected object(s).

	How To Run:

		import BoddenChristina_riggingTools_cri1_1409.py
		reload (BoddenChristina_riggingTools_cri1_1409)
		riggint_tools.freeze_transforms()

	'''

	# What is the command name?
	# How does it work?
	# What is the commands flags?

	# Create a circle, move it, and test this code!
	pm.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0)

	# flags
		# t / translate
		# r / rotate
		# s / scale
		# n / normal
		# apply

	print 'Transforms Frozen.'

def delete_history():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Deleting the history of selected object(s).

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.delete_history()

	'''

	# Deleting objects in Maya
		# pm.delte() Delete 3D Objects
		# pm.deleteUI() Delete Interface Objects
		# pm.deleteAttr() Deletes Attributes
		# constructionHistory (ch)
	# pm.delete()
			# flags
			# constructionHistory (ch)
			# staticChannels (sc)
			# channels (c)

	pm.delete(ch=True)

	print 'History Deleting.'

def center_pivot():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 

	Description:

		Centering the pivot of an object(s) to its origin.

	How To Run:

		import BoddenChristina_riggingTools_cri1_1409.py
		reload (BoddenChristina_riggingTools_cri1_1409)
		riggint_tools.center_pivot()

	'''

	# pm.xform() What flag centers pivot?

	pm.xform(cp=True)

		# cp / centerpivot 
		# boolean

	# The xform command is used as a translation.
	# It can be used to center the pivot of an object.

	print 'Pivot is Centered.'


# --------------------------------


'''

	CREATING NURBS PRIMITIVES

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 

'''

def creating_circles():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creating a NURBS circle on the grid.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_circles()

	'''

	# Creating Circles

	# pm.commandName()
	pm.circle()
	# flag radius
	pm.circle(radius=2)
	# multiple flags
	pm.circle(sections=16, radius=3, normal=[1, 0, 0])[0]
	# list (multilpe values)
	pm.circle(normal=[1, 0, 0])

	# Flags
	# r / radius
	# nr / normal ??? Explain in your own words!
	# s / sections

	print 'Circle Created.'

def creating_cubes():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creating a NURBS cube on the grid.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_cubes()

	'''
	
	mel_line = 'curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 ;'
	pm.mel.eval(mel_line)

	print 'Cube NURBS Created.'

def creating_squares():
	
	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creating a NURBS square on the grid. (Not i pieces)

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_squares()

	'''

	#MEL:
	# curve -d 1 -p -2 0 2 -p -2 0 -2 -p 2 0 -2 -p 2 0 2 -p -2 0 2 -k 0 -k 1 -k 2 -k 3 -k 4 ;

	mel_line = 'curve -d 1 -p -2 0 2 -p -2 0 -2 -p 2 0 -2 -p 2 0 2 -p -2 0 2 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
	pm.mel.eval(mel_line)

	print 'Square NURBS Created.'

def creating_arrows():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creating a NURBS arrow on the grid.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_arrows()

	'''

	mel_line = 'curve -d 1 -p -3 0 1 -p -3 0 -1 -p 0 0 -1 -p 0 0 -2 -p 3 0 0 -p 0 0 2 -p 0 0 1 -p -3 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	pm.mel.eval(mel_line)

	print 'Arrow NURBS Created.'


# --------------------------------


'''

	CVs

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 

'''

def cv_selection():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Selecting the cv's of a control icon.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.cv_selection()

	'''

	# Given by the user.


	# Can select all the cv of a control
		# [0] <- all the cv
		# [::2] <- every other cv

	# Can be used to manipulate control icons

	selected = pm.ls(selection=True)

	selected_curve = selected[0]
	pm.select(selected_curve.cv, replace=True)

def other_cv_selection():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Selecting every other cv of a control icon.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.other_cv_selection()

	'''

	# Given by the user.


	# Can select all the cv of a control
		# [0] <- all the cv
		# [::2] <- every other cv

	# Selects every other cv of a control

	selected = pm.ls(selection=True)

	selected_curve = selected[0]
	pm.select(selected_curve.cv[::2], replace=True)


# --------------------------------


'''

	CONSTRAINTS

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def parent_constraint():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Parent constrainting a joint to a control. (Driver, Driven)

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.parent_constraint()

	'''

	# Works on selected (Driver, Driven)
	pm.parentConstraint()

	# Not Snapping
	pm.parentConstraint(maintainOffset=True)

	selected = pm.ls(selection=True)
	pm.parentConstraint(selected[0], selected[1])

	# Flags
	# maintainOffset(mo) Boolean

	# Indenting matters when it comes to the defining process.
	# Indenting means it is part of the command.

	print 'Object Parent Constraint.'

def orient_constraint():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Orients the rotation of the target object.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.orient_constraint()

	'''

	# This constraint works just like the parent constraint.
	# Except that is onle orients the target object.
	# pm.orientConstraint()

	# Not Snapping
	pm.orientConstraint(maintainOffset=True)

	print 'Object Orient Constraint.'


# --------------------------------


'''

	ADVANCED

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def ik_fk_builder():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Constructing the IK / FK systems.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.ik_fk_builder()

	'''

	# Get selected
	selected = pm.ls(selection=True)

	bind_joint_chain = selected[0]

	# Duplicated the joint chain
	ik_root_joint = pm.duplicate(bind_joint_chain, rc=True)[0]
	fk_root_joint = pm.duplicate(bind_joint_chain, rc=True)[0]

	# Rename my joint Chains
	joint_renamer(ik_joint_chain, 'lt', 'armIk')
	joint_renamer(ik_joint_chain, 'lt', 'armIk')

def joint_renamer(joint_chain, ori, system_name):

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		FOR THE IK / FK BUILDER!

		This tool renames a selected joint chain.

		Select a root joint and run the function.
			- The script with prompt you first for the Orientation ('lt', 'rt', 'ct')
				and the name of the system ('arm', 'back', 'leg')


		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.joint_renamer()

	'''

	# Creating Attributes

	# Select the root koint and I will get its children.
	joint_chain = pm.ls(selection=True, dag=True)


	# dag: Grab all the children in a selected object

	# Do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind

	# First: Orientation of system
	# Second: Name of system

	# ori = raw_input()
	# system name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
		# new_name = 'lt_arm_01_bind'
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)
		print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
		
		# Rename command
		# variable.rename(new_name)
		current.rename(new_name)
		
		count = count + 1

	# Can change the name of control icons
	# Take out dag when doing this!

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)

	print 'Joints Renamed.'

def constraint_rfl():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Constrainting the RFL system to the leg root joint.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.constraint_rfl()

	'''

	selected = pm.ls(selection=True)

	leg_joint_root = selected[0]
	rfl_joint_root = selected[1]

	leg_system = pm.ls(leg_joint_root, dag=True)
	rfl_system = pm.ls(rfl_joint_root, dag=True)

	ankle_ik = pm.ikHandle(sj=leg_system[0], ee=leg_system[2], sol='ikRPsolver')[0]
	ball_ik = pm.ikHandle(sj=leg_system[2], ee=leg_system[3], sol='ikSCsolver')[0]
	toe_ik = pm.ikHandle(sj=leg_system[3], ee=leg_system[4], sol='ikSCsolver')[0]

		# Create a control for:
		# RFL Heel
	heel_icon = pm.circle()[0]
	kenny = pm.parentConstraint(rfl_system[0], heel_icon)
	pm.delete(kenny)

	# Parent control together
		# toe -> heel
		# ball -> toe
	# pm.parent(toe_icon, heel_icon)
	# pm.parent(ball_icon, toe_icon)

		# RFL Toe
	toe_icon = pm.circle()[0]
	kenny = pm.parentConstraint(rfl_system[1], heel_icon)
	pm.delete(kenny)

	# Parent control together
		# toe -> heel
		# ball -> toe
	# pm.parent(toe_icon, heel_icon)
	# pm.parent(ball_icon, toe_icon)

		# RFL Ball
	ball_icon = pm.circle()[0]
	kenny = pm.parentConstraint(rfl_system[2], heel_icon)
	pm.delete(kenny)

	# Parent control together
		# toe -> heel
		# ball -> toe
	pm.parent(toe_icon, heel_icon)
	pm.parent(ball_icon, toe_icon)

	# Make sure to freeze transforms on controls.

	# Parent the IKs to the correct control.
	pm.parent(ankle_ik, rfl_system[-1])
	pm.parent(ball_ik, rfl_system[-2])
	pm.parent(toe_ik, rfl_system[-3])


# --------------------------------


'''

	GENERAL TOOLS 

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def grouping():
			
	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creating a named empty group.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.grouping()

	'''

	# pm.group()
		# Flags
		# Empty (em)
			# Create an empty group (with no objects in it)
			# n
			# Assign given name to new group node.

	# We create an empty group because they can be used as pads when doing a proxy rig.

	pm.group()
	pm.group(empty=True)
	pm.group(empty=True, name='Bob')

	print 'Objects Grouped.'

def parenting():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Parenting groups together under a hierarchy.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.parenting()

	'''

	# Parenting
	pm.group(name='Top', empty=True)
	pm.group(name='Middle', empty=True)
	pm.group(name='Bottom', empty=True)

	# What is the order for parenting?
	pm.parent('Bottom', 'Middle')

		# Spelling is important when parenting!

	# Can I parent all three of these with one command?
	# No. When parenting more than two at a time, you will get to children and one parent.
		# You will always have to go in and move the children manualy eventually.
	pm.parent('Bottom', 'Middle', 'Top')

	print 'Objects Parented.'


# --------------------------------


'''
	
	PRESETS

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def print_selected():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py 

	Description:

		Enables you to set a selection command as TRUE (yes) or FALSE (no)

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409.py 
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.print_selected()

	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	# print 'Currently Selected: {0}'.format(selected)


# --------------------------------


'''

	RIGGING LAYOUT

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def creating_ikhandles():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creating IKs (RP / SC) for leg joints.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_ikhandles()

	'''

	# Isolate important joints.
	root_joint = joint_chain[0]
	ankle_joint = joint_chain[2]
	ball_joint = joint_chain[3]
	toe_joint = joint_chain[4]

	# Apply IK Handles
		# pm.ikHandle()
		# sj = start joint
		# ee = end effector

	# Name names the ik handle
	# What type of ik is created by default? SC
	# How do I create a RP?
		# Set the solver (sol) flag to ikRPsolver
	
	# Spline ik can be created using the curve (c) flag
	
	ori = raw_input()

	ankle_ik = pm.ikHandle(sol='ikRPsolver', sj=root_joint, ee=ankle_joint, name='{0}_ankle_ik'.format(ori))
	ball_ik = pm.ikHandle(sol='ikSCsolver', sj=ankle_joint, ee=ball_joint, name='{1}_ball_ik'.format(ori))
	toe_ik = pm.ikHandle(sol='ikSCsolver', sj=ball_joint, ee=toe_joint, name='{2}_toe_ik'.format(ori))

def creating_clusters():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Creates a spine cluster to selected joints.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.creating_clusters()

	'''

	# Given to us by the user.

	selected = pm.ls(selection=True)

	selected_curve = selected[0]

	for current_cv in selected_curve.cv:
		print current_cv
		pm.cluster(current_cv, name = lt_joint_ik)


# --------------------------------


'''

	BASICS 

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

'''

def basic_if_statement():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description.:

		Using IF statements in Maya as True or False conditions.

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.basic_if_statement()

	'''

	# Think about Excel.
		# =IF(what is the condition, [if it is true], [then what is the solution])

	if True:
		print 'The Condition is True'

	if False:
		print 'The Condition is False'

	'''

	Operations: 

	== Equals
	!= Not Equals 
	> Greater Than
	>= Greater thank or Equal to
	< Less Thanks
	<= Less Than or Equal to

	'''

	if 2 == 2 and 2 != 3:
		print 'This Condition is True'

	if 2 == 2 or 2!= 3:
		print 'This Condition is True'

	if not 2 == 2:
		print 'This Condition is False'

	'''

	Else:

	'''

	if 2 == 3:
		print 'Condition is True'
	else:
		print 'Condition is False'

	'''

	Elif:

	'''

	# if value == 1:
	# 	print 'Colour is Red'

	# elif value == 2:
	# 	print 'Colour is Blue'

	# elif value == 3:
	# 	print 'Colour is Green'	

	# else:
	# 	print 'Colour is Something Else'


	'''

	About command

	'''

	if pm.about(windows=True):
		print 'You are Using Windows.'

	elif pm.about(macOS=True):
		print 'You are using osx.'

	else:
		print 'You are Using a Different os.'


	'''

	Validating selection

	'''

	# How do I find out how many items are selected in Maya?
	selected = pm.ls(selection=True)


	'''

	False statements
	
	'''

	'''

	False
	0
	None 
	[]
	{}
	()
	''

	Everything else is True

	'''

	# How do I find out how many items are selected in Maya?
	selected = pm.ls(selection=True)

	amount_selected = len(selected)
	print 'Current Items Selected:', amount_selected

	# if selected:
	# 	print 'You have at least one item selected.'

	# if amount_selected == 1:
	# 	print 'You have one item selected.'

	if amount_selected == 1:
		print' You have one item selected.'
	elif amount_selected == 2:
		print 'You have two items selected.'
	elif amount_selected > 2:
		print 'You have more than two items selected.'
	else:
		print 'You have nothing selected.'


	'''

	Using Find Method

	'''

	# Do you have a root joint selected?
		#lt_arm_01_bind

	selected = pm.ls(selection=True)[0]
	# selected = 'lt_arm_01_bind'
	is_bind_joint = selected.find('_01_bind')

	if is_bind_joint > -1:
		print 'You Have a Root bind Joint.'

def looping_basics():

	'''

	Christina Bodden
	BoddenChristina_riggingTools_cri1_1409.py

	Description:

		Runs the commands in a loop until all the commands are done. (Uses lists)

	How to Run:

		import BoddenChristina_riggingTools_cri1_1409
		reload (BoddenChristina_riggingTools_cri1_1409)
		BoddenChristina_riggingTools_cri1_1409.looping_basics()

	'''

	customers = ['Michael', 'Bob', 'Susan']

	for customer in customers:
		print 'Serving Customer:', customer

	selected = pm.ls(selection=True)

	for current_item in selected:
		print 'Current Item:', current_item
		new_name = current_item + '_proxy'
		current_item.rename(new_name)

