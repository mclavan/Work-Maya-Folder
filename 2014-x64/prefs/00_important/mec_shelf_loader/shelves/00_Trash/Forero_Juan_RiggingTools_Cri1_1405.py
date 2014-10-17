'''
Juan
toolset.py

Description:
Hierarchy functions made to be added to shelf.

How to Run:
import toolset
reload(toolset)
'''

print 'toolset activated'

import pymel.core as pm 

def hierarchy(): 
	print 'Hierarchy Generated'
	import pymel.core as pm 

	# The user will select the root joint and the tool
	#	will apply the systems.

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# Pad the root joint.
	'''

	# Create an empty group.

	pad = pm.group(empty=True, name = 'lt_middle_00_pad')
	print 'Root Pad Created', pad 

	# Move group to root joint.
	# Point constrain group to root joint.
	# 	  offset off (Snapping)
	temp = pm.pointConstraint(root_joint, pad) 

	# Delete Constraint

	pm.delete(temp)

	# Freeze transforms on group.
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group.
	pm.parent(root_joint, pad) 



	# Create a local oriented control for each joint.
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind


	# Create control (circle)
	control_icon_1 = pm.circle(name='lt_middle_01_icon', nr=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#   This will automaticly parent the control under
	#   the group
	control_pad_1 = pm.group(name='lt_middle_01_local',empty=False)

	# Move group to the target joint.
	# Use a parent to constraint driver is the joint.
	#   Where driven is the group.
	#   Offset is off (Snapping)
	temp = pm.parentConstraint(root_joint, control_icon_1)

	# Destroy the constraint
	pm.delete(temp)

	# Delete History on control
	pm.delete(ch=True)
	pm.delete(pad, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	second_joint
	'''

	# Create control (circle)
	control_icon_2 = pm.circle(name='lt_middle_02_icon', nr=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#   This will automaticly parent the control under
	#   the group
	control_pad_2 = pm.group(name='lt_middle_02_local',empty=False)

	# Move group to the target joint.
	# Use a parent to constraint driver is the joint.
	#   Where driven is the group.
	#   Offset is off (Snapping)
	temp = pm.parentConstraint(second_joint, control_icon_2)

	# Destroy the constraint
	pm.delete(temp)

	# Delete History on control
	pm.delete(ch=True)
	pm.delete(pad, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_2, second_joint)


	'''
	third_joint
	'''

	# Create control (circle)
	control_icon_3 = pm.circle(name='lt_middle_03_icon', nr=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#   This will automaticly parent the control under
	#   the group
	control_pad_3 = pm.group(name='lt_middle_03_local',empty=False)

	# Move group to the target joint.
	# Use a parent to constraint driver is the joint.
	#   Where driven is the group.
	#   Offset is off (Snapping)
	temp = pm.parentConstraint(third_joint, control_icon_3)

	# Destroy the constraint
	pm.delete(temp)

	# Delete History on control
	pm.delete(ch=True)
	pm.delete(pad, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_3, third_joint)

	# Parent the controls

	pm.parent(control_pad_3, control_icon_2)
	pm.parent(control_pad_2, control_icon_1)

	# Group Hierarchy

	Hierarchy = pm.group(empty=True, name='Hierarchy')

	pm.parent(pad, Hierarchy)
	pm.parent(control_pad_1, Hierarchy)





def padding_tool():

	'''
	Description:
	Create a pad group with the joints inside.

	How to Run:

	import toolset
	reload(toolset)
	toolset.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# Print'Current Selection', selected

	root_joint = selected[0]

	# Create empty group
	# empty=True will create an empty group 
	#
	pad = pm.group(empty=True)

	# Move group to joint
	#   and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad) 
	pm.delete(temp_constraint)

	# Freeze Transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad) 

	# renaming 

	pad_name = root_joint.replace('lt_middle_01_bind', 'lt_middle_00_pad')
	pad.rename(pad_name)

	print 'Padding Group created'


def joint_renamer():

	'''
	Description:
	Create a pad group with the joints inside.

	How to Run:

	import toolset
	reload(toolset)
	toolset.joint_renamer()
	'''

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items:', joint_chain

	# Figure out naming convention


	# Build are new name.
	# 'lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind' 

	# Loop through joint chain.

	for current_joint in joint_chain:

			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix) 

		print 'Joint Name', new_name 

		# Rename Joint

		current_joint.rename(new_name)

		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste') 

	print 'Joint Name', new_name 

	current_joint.rename(new_name)

	print 'Joint Chain Renamed'


def priming_tool():

	'''
	Description:
	Create circles to control the joints.

	How to Run:

	import toolset
	reload(toolset)
	toolset.priming_tool()
	'''

	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected 
	# target_joint = selected[0]

	
	for target_joint in selected: 
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad created:', local_pad


		# Move group to target joint. 
		#   and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)



	print 'Local Oriented Controls Created.'



