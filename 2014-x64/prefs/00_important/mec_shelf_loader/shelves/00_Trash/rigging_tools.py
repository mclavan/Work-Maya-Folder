'''
rigging_tools.py
Lianna Pacheco

Description:
	Grouping of rigging tools.

How to Run:

'''


import pymel.core as pm

print 'Rigging Tools Activate.'

# The user will select the root joint and the tool.
# Will apply the systems.
root_joint = 'lt_middle_01_bind'
second_joint = 'lt_middle_02_bind'
def hierarchy():

	'''
	Create a hierarchy based upon  given system.

	Select root joint chain and execute function.

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.hierarchy()
	'''

	'''
	Input
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_join = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	# Padding Root Joint.
	'''

	# Create an empty group.
	root_pad = pm.group(empty=True)

	# Move group to root joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze transforms on group.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# parent root joint to group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control (Circle)
	# Normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group (NOT EMPTY)
	# This will automaticly parent the control under.
	local_pad_1 = pm.group()

	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driver: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driver
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a Control.
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0,0], radius=2)[0]

	# Create a Control.
	# Normal=[1, 0, 0], radius=2
	local_pad_2 = pm.group()

	# Output Contro; and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driver: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control.
	# Normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driver: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together.
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)


	print 'Hierarchy Created'


def padding_tool():

	'''
	This tool creates a world pad on the selected joint system.

	Select the root and execute the command.

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()

	'''

	selected = pm.ls(selection=True)
	# print 'Current Selection:', selected
	root_joint = selected[0]

	# Created empty group.
	# Empty=True will create a empty group.
	pad = pm.group(empty=True)

	# Move group to joint.
	# And delete temp_constraint.
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transform on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group.
	pm.parent(root_joint, pad)

	# Renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'



def joint_renamer():
	'''
	joint_renamer.py

	Practical use of loops.
	Renaming joint based upan a naming convention.

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.joint_renamer()

	'''

	print 'Joint Renamer - Activate'

	import pymel.core as pm

	'''
	Get Selected
	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)
	print 'Selected items:', joint_chain

	'''
	Figure out naming convention.
	'lt_arm_01_bind' -> 'lt_arm_03_waste'
	'ct_tail_01_bind', -> 'ct_tail_06_waste'
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'


	'''
	Loop through joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		# Rename joint
		current_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)


def priming_tool():
	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.priming_tool()
	'''



	# Get selected.
	selected = pm.ls(selection=True)
	# Print 'Joints Selected:', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create Control
		# Normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, 
			name=control_icon_name) [0]

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		# And deleted contraint.
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient contraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


		print 'Local Orient Controls Created.'