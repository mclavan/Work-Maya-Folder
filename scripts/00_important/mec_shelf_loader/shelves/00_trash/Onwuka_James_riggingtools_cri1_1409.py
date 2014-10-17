'''
James Onwuka
Onwuka_James_riggingtools_cri1_1409.py

Description:
	Variety of rigging tools.

How To Run:

import Onwuka_James_riggingtools_cri1_1409
reload(Onwuka_James_riggingtools_cri1_1409)


'''

import pymel.core as pm

print 'Rigging Tools Active'


def joint_renamer():
	'''
	Renames all joints of a joint hirearchy.

	Select the root joint and excecute the function.
	root_joint = joints[0]
	#second_joint = joints[1]
	#third_joint = joints[2]
	Onwuka_James_riggingtools_cri1_1409.joint_renamer()
	'''
	joints= pm.ls(selection=True, dag=True)

	'''
	Naming Conventioin
	orientation
	name
	count
	suffix
	lt_arm_01_bind -> lt_arm_03_waste
	'''

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix ='bind'

	for current_joint in joints:
		# print 'Joint: ', current_joint
		# Adding Strings
		# Python string method
		# Python string method format example
		
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)

		print 'Name Change:', new_name

		#Rename Object
		current_joint.rename(new_name)
		
		count = count + 1 


		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count-1, 'waste')
		print 'Name Change:', new_name
		joints[-1].rename(new_name)

def priming_tool():
	# ON selected joints.
	# Create a local oriented control.
	joints = pm.ls(selection=True)

	# Loop through selected joints
	for current_joint in joints:
	    # Rename control and delete history
	    # ct_back_01_bind -> ct_back_01_icon
	    icon_name = current_joint.replace('_bind', 'icon')
	    pad_name = current_joint.replace('_bind', '_pad')     
	    # Create a circle
	    control_icon = pm.circle(name=icon_name, radius=1.8)


	    # Create a group
	    pad = pm.group(name=pad_name)
	    
	    # Snap group to target joint.
	    # Snapping using parent constraint
	    kenny = pm.parentConstraint(current_joint, pad)
	    
	    # Delete parent constraint
	    pm.delete(kenny)
	    
	    
	    # Orient Constraint joint to control
	    pm.orientConstraint(control_icon, current_joint)

def snap_item():
	'''
	This tool move one object to another.
	- Only translates object.

	The first object is the driver, while the
	second is the driven.


	'''
	items = pm.ls(selection=True)
	first_item = items[0]
	second_item = items[1]
	print 'Current Items:' , items 
	print 'Item 1:', first_item 
	print 'Item 2:', second_item

	# Using point constraint to translate object.
	kenny = pm.pointConstraint(first_item, second_item)
	# Delet constaint 
	pm.delete(kenny)
	print 'Selected Item Snapped.'

def hirearchy():
	'''
	Onwuka
	Onwuka.py

	description:
		This is a starter script.

	How to Run:

	import Onwuka
	reload(Onwuka)

	'''

	import pymel.core as pm 

	print 'Starter Script'

	root_joint='lt_middle_01_bind'
	joint_2 ='lt_middle_01_bind'
	joint_3 ='lt_middle_01_bind'

	# Create a group and name it 'lt_middle_00_pad'.
	pad = pm.group(empty=True, name='lt_middle_00_pad')

	print 'Root_Joint:', root_joint,' and pad:', pad

	# Move the group to the root joint.

	# A pointConstrain only tanslates

# what is our driver: ?? amd driven: ??

	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	# Freeze Transforms (We havenot done this yet.)

	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent the root joint to the group.

	# We are parenting the root joint to the pad 

	# Parent command works childeren first then father last 

	pm.parent(root_joint, pad)

	print 'Pad Created:', pad,' and move to', root_joint

	# What is next?
	# Create a local oriented control for each finger joint
	# Rotation and size needed to match the joint.
	# Do not forget to use zero index. [0]
	
	control_icon_1 = pm.circle(radius=1.9, normal=[1,0,0],
		name='lt_middle_01_icon')[0]

	# Create a group for the control (NOT empty)

	local_pad_1 = pm.group(name='lt_middle_01_local')

	# Use parent to constraint to move local "pad " to joint.

	kenny = pm.parentConstraint(root_joint, local_pad_1)

	# Delete constraint
# Misspell
	pm.delete(kenny)

	# Orient constraint the "control" to the finger.

	pm.orientConstraint(control_icon_1, root_joint)


	'''
	Parenting
	
	'''
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'I have a new name'

def icon_renamer():

	'''

	Rename all selected icons


	'''


	joints= pm.ls(selection=True)


	'''
	Naming convention
	Orientation
	Name
	Count
	Suffix

	ex. lt_arm_01_bind -> lt_arm_03_waste

	'''

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = icon

	for current_joint in joints:
	    #print 'Joint: ', current_joint
	    #Adding strings
	    #Python string method
	    #python string method format example
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print 'Name Change: ', new_name

		#Rename Object
		current_joint.rename(new_name)

		count = count + 1

def joint_padder():
	
	# Define the selection
	joints = pm.ls(selection=True)[0]

	# Explain what the group is 
	mover = pm.group()

	# Move group to selection
	kenny = pm.pointConstraint(mover, joints)

	# Delete constraint
	pm.delete(kenny)

	# Freeze transforms

	pm.makeIdentity(mover, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to pad

	pm.parent(joints, mover)

	# Suffix left should be like Example lt_arm_01_bind --> lt_arm_00_pad      pad_name = lt_arm_00_pad

	pad_name = joints.replace('01_bind', '00_pad')


	mover.rename(pad_name)

def control_color_red_tool():
	'''
	import onwuka_james_riggingtools_cri1_1409
	reload(onwuka_james_riggingtools_cri1_1409)
	onwuka_james_riggingtools_cri1_1409.control_color_red_tool()

	Color controls in a chain individually or as one every control under selection wull become control_color_red_tool
	'''

	print 'Control color editor'

	#selecting current control chain and its children
	control_chain = pm.ls(selection=True, dag=True)
	root_control = control_chain[0]

	print 'Control color selected:', control_chain

	# For loop will turn on display color override for the current control in the chain.
	# It will then color it to the color calue un the override control.
	# After it changes color, the loop moves down to the next control all the to the final control.
	for colored_control in control_chain:
		pm.stAttr(root_control.overrideEnabled,1)
		root_control.pm.overrideColor.set(13)

	# Printing out line to tell user that all controls under and including the selected controls have become desired color
	original_sel = pm.ls(selection=True)
	print 'All colors in chain starting with', original_sel, 'are now RED'

def control_color_blue_tool():
	'''
	import onwuka_james_riggingtools_cri1_402
	reload(onwuka_james_riggingtools_cri1_402)
	onwuka_james_riggingtools_cri1_402.control_color_blue_tool()

	Color controls in a chain individually or as one every control under selection wull become control_color_red_tool
	'''

	print 'Control color editor'

	#selecting current control chain and its children
	control_chain = pm.ls(selection=True, dag=True)
	root_control = control_chain[0]

	print 'Control color selected:', control_chain

	# For loop will turn on display color override for the current control in the chain.
	# It will then color it to the color calue un the override control.
	# After it changes color, the loop moves down to the next control all the to the final control.
	for colored_control in control_chain:
		pm.stAttr(root_control.overrideEnabled,1)
		root_control.pm.overrideColor.set(6)

	# Printing out line to tell user that all controls under and including the selected controls have become desired color
	original_sel = pm.ls(selection=True)
	print 'All colors in chain starting with', original_sel, 'are now RED'

# def control_color_yellow_tool():)

# 	# Printing out line to tell user that all controls under and including the selected controls have become desired color
# 	original_sel = pm.ls(selection=True)
# 	print 'All colors in chain starting with', original_sel, 'are now RED'

# def enum_tool(): print 'Created locked attribute named"', name,'"'
	
def float_tool():
	'''
	import onwuka_james_riggingtools_cri1_1409
	reload(onwuka_james_riggingtools_cri1_1409)
	onwuka_james_riggingtools_cri1_1409.float_tool()

	this script will allow the user to create individual attributes on a control.
	the user can choose if they want the attributes to be a label or an editable attribute.
	'''

	print 'Create float tool selected'

	# Determines what was selected by user and creates a list of the item
	selected = pm.ls(selection=True)
	root_control.addAttr(name, keyable = True)
	print 'Created editable attribute named "', name, '"'