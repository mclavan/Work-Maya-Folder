'''
Edward Bushnell
rigging_tools.py


Description:
	A group of rigging related tools.

How to Run:

import rigging_tools
reload(rigging_tools)


'''

print 'Rigging Tools Active.'

import pymel.core as pm

def heirarchy():
	'''
	Create a heirarchy based on a given system.

	Select root joint chain and execute function.

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.heirarchy()
	'''
	'''
	Input
	What are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection = True, dag = True)
	# print 'Joint System', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	joint_4 = joint_system[3]

	'''

	'Padding the Root Joint'
	'''
	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group over to target joint.  
# Misspelled constraint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group.
	pm.parent(root_joint, root_pad)


	print 'Heirarchy Created.'


	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal = [1, 0, 0], radius = 2
	control_icon_1 = pm.circle(normal=[0, 0, 1], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad
	print 'Control icon 1:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete contraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint  
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2 - joint_2
	'''
	# Create a control.
	# normal = [1, 0, 0], radius = 2
	control_icon_2 = pm.circle(normal=[0, 0, 1], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad
	print 'Control icon 2:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete contraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint  
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3 - joint_3
	'''
	# Create a control.
	# normal = [1, 0, 0], radius = 2
	control_icon_3 =  pm.circle(normal=[0, 0, 1], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad
	print 'Control icon 3:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete contraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint  
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)




def point_snapping_tool():
	'''
	This tool moves the first selected object to the second.
		- Translates and rotates the target object.

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.point_snapping_tool()
	'''

	selected = pm.ls(selection = True)
	print 'Selected: {0}'.format(selected)

	# By default commands work on selcted   
	betty = pm.pointConstaint(selected[0], selected[1])
	pm.delete(betty)

	print 'The first selected object was moved to the second.'


def world_icon():
	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()
	'''
	selected = pm.ls(selection = True)
	print 'Selected: {0}'.format(selected)

	first_joint = 'Selected: {0}'.format(selected)

	# Create a control icon to the target joint.
	control_icon_1 = pm.circle(normal = [0, 1, 0], radius = 2)[0]

	# Move the control to the target joint.
	# Delete the constraint.
	betty = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(betty)

	print 'Icon created'

def color_controls():
	'''
	this tool changes the color of the selected control icon
	
	select control icon and run function.

	'''
	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.color_controls()	
	'''

	selected = pm.ls(selection = True)
	print 'Selected: {0}'.format(selected)

	pm.setAttr( ".overrideEnabled", 1)







def joint_renamer():
	'''
	This tool renames a selected joint chain

	Select a root joint and run the function.
	- the scripts will prompt you first for the orentation ('lt', 'rt', 'ct') and
		the name of the system ('arm', 'back', 'leg')

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.joint_renamer()
	'''


	# Select the root Joint
	joint_chain = pm.ls(selection = True, dag = True)

	# Do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count= 1
	suffix = 'bind'


	for current in joint_chain:
	    new_name = '{0}_{1}_{2:0d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	    # Rename command
	    # variable.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:0d}_{3}'.format(ori, name, count -1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)


def icon_renamer():
	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.icon_renamer()
	'''


	# Select the root Joint
	icon = pm.ls(selection = True, dag = True)

	# Do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count= 1
	suffix = 'icon'


	for current in icon:
	    new_name = '{0}_{1}_{2:0d}_{3}'.format(ori, name, count, suffix)
	    print 'Current icon: {0} - New Name: {1}'.format(current, new_name)
	    
	    # Rename command
	    # variable.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:0d}_{3}'.format(ori, name, count -1, 'icon')
	print 'Current Icon: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)

def padding_tool():

	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()
	'''

	selected = pm.ls(selection = True)
	# print 'Current selected:', selected
	root_joint = selected[0]

	# Create empty group
	# what is the correct flag?
	# empty=True will create a empty group
	# 
	pad = pm.group(empty=True)

	# Move joint to group
	# 	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# freeze transforms on the group
	pm.makeIdentity(root_joint, pad)

	# Parent the joint
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created.'


def priming_tool():
	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.priming_tool()
	'''
	#  Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected', selected
	target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# Normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1,0,0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created', local_pad
		# Move group to target
		# 	and delete constraint
		temp_constraint= pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


		print 'Local Oriented Controls Created.'



def loop_tool():

	
	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.loop_tool()
	'''
	
	
	'''
	Loop Basics
	for loop
	'''
	selected = pm.ls(selection = True)
	print 'Selected: {0}'.format(selected)


	# Requires a list
	customer = ['Michael', 'Bob','Susan']
	# 
	for customer in customers:
		print 'Serving Customer', customer

		selected = ls(selection=True)

		for current_item in selected:

			print 'Current Item:', current_item
			new_name = current_item + '_proxy'
			current_item, rename(new_name)









