'''
monday.py
Michael Clavan

How to run:

import monday
reload(monday)

'''
print 'hi'

import pymel.core as pm 

# Create a function basic_loop.
def basic_loop():

	# Creating a loop.
	# We are creating a for loop today.

	# A for loop requires a list. 
	names = ['Michael', 'Bob', 'Susan']
	#                                    ^
	# How do I print out each name. 
	for current_customer in names:
		print current_customer 


	print 'Basic loop active.'


def loop_selected():

	selected = pm.ls(selection=True)
	print 'Current Selected:', selected 

	for current_item in selected:
		print 'The current item is', current_item

	print 'Looping through selected'

def color_control_blue():
	selected = pm.ls(selection=True)

	for current_item in selected:
		current_item.overrideEnabled.set(1)
		blue = 6
		current_item.overrideColor.set(blue)
		print 'Current item is blue:', current_item

	print 'Control Colored'

def color_control(color=6):
	selected = pm.ls(selection=True)

	for current_item in selected:
		current_item.overrideEnabled.set(1)
		current_item.overrideColor.set(color)
		print 'Current item is blue:', current_item

	print 'Control Colored'

def rename_joints():

	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system
	
	# lt_arm_01_bind -> lt_arm_03_waste
	# lt   arm   01   bind
	ori = raw_input()
	system_name = raw_input()

	count = 0

	suffix = 'bind'

	for current_joint in joint_system:
		count = count + 1
		# ltarm01bind
		# poop
		# new_name = ori + '_' + system_name + '_' + count
		# format method

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		# print 'New Name:', new_name

		current_joint.rename(new_name)

		print 'Renaming:', current_joint


	print 'Joints have been renamed.'

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	# print 'New Name:', new_name
	joint_system[-1].rename(new_name)


def priming_tool():
	'''
	This tools creates both a locally oriented control and pad for
		each selected joint.

	Instructions:
		Select desired joints, then execute primming_tool function. 
	'''
	# Get selected joints
	selected_joints = pm.ls(selection=True)

	print 'Selected Joints:', selected_joints
	# Loops through selected joints.
	for current_joint in selected_joints:
		# Create control icon
		# ch=False removes construction history on the 
		#   circle.
		control_icon = pm.circle(normal=[1, 0, 0], ch=False)[0]
		print 'Control icon created:', control_icon

		# Create group.
		# Group command will parent control upon creation. 
		pad = pm.group(control_icon)

		# Move group to target joint. 
		temp_constraint = pm.parentConstraint(current_joint, pad)
		pm.delete(temp_constraint)

		# Clean control

		# Constraint target joint to group. 
		pm.orientConstraint(control_icon, current_joint)

	# pm.select(control_icon, replace=True)
	# Rename control and prime group

	# Output


	print 'Localling oriented control created for selected joints.'