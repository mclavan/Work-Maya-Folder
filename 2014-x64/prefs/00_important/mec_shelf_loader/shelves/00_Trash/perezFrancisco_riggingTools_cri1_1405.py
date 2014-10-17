'''
Francisco Perez
Project4

Description:

The four functions need for Prjoect 4
Hierarchy
Padding tool
Joint Renaming
Priming Tool

How to Run:
import Project4
reload(Project4)
'''

import pymel.core as pm

def hierarchy_tool():
	'''
	How to Run:
		import Project4
		reload(Project4)
		Project4.hierarchy_tool()
	'''
	print 'Hierarchy Generated'


	# The user wil select the root joint and the tool 
	#	will apply the systems

	root_joint = 'lt_middle_01_bind' 
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# Pad the root joint
	'''

	# Naming for pad
	new_pad_name = root_joint.replace('01_bind', '00_pad')
	print 'Pad Name:', new_pad_name

	# Create empty Group
	pad = pm.group(empty=True, name=new_pad_name)

	# Move group to root joint
	# Point constraint with offset off
	temp_constraint = pm.pointConstraint(root_joint, pad)


	# Delete Constraint
	pm.delete(temp_constraint)

	# Freeze Transformations
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root Joint to Group
	pm.parent(root_joint, pad)

	# Create a local oriented control for each joint
	# lt_middle_01_bind, lt_middle_02_bind, lt_middle_03_bind


	'''
	Local Controls
	'''

	'''
	Control 1
	'''

	#Create Control (circle)
	control_icon_1 = pm.circle(normal=[1, 0, 0,], radius=2)[0]

	#Naming for first Local 
	local_pad_name = root_joint.replace('01_bind', '01_local')
	print 'Local Pad Name', local_pad_name

	#Create Group and parent control under group
	local_pad_1 = pm.group(name=local_pad_name)

	# Move to the target joint.
	# Parent Contrain offset is off, driver is the joint
	# Driven is the group
	temp_contraint2 = pm.parentConstraint(root_joint, local_pad_1 )

	# Delete Constraint
	pm.delete(temp_contraint2)

	# Delete History on control
	# Orient Constraint, driver is control, driven is joint
	pm.orientConstraint(control_icon_1, root_joint)

	# Lock Attributes
	control_icon_1.t.set(lock=True, keyable=False)
	control_icon_1.s.set(lock=True, keyable=False)
	control_icon_1.v.set(lock=True, keyable=False)


	'''
	Control 2
	'''

	#Create Control (circle)
	control_icon_2 = pm.circle(normal=[1, 0, 0,], radius=2)[0]
	#Naming for Second Local Pad
	local_pad_name2 = second_joint.replace('02_bind', '02_local')
	print 'Local Pad Name', local_pad_name2

	#Create Group and parent control under group
	local_pad_2 = pm.group(name=local_pad_name2)

	# Move to the target joint.
	# Parent Contrain offset is off, driver is the joint
	# Driven is the group
	temp_contraint3 = pm.parentConstraint(second_joint, local_pad_2 )

	# Delete Constraint
	pm.delete(temp_contraint3)

	# Delete History on control
	# Orient Constraint, driver is control, driven is joint
	pm.orientConstraint(control_icon_2, second_joint)

	# Lock Attributes
	control_icon_2.t.set(lock=True, keyable=False)
	control_icon_2.s.set(lock=True, keyable=False)
	control_icon_2.v.set(lock=True, keyable=False)


	'''
	Control 3
	'''

	#Create Control (circle)
	control_icon_3 = pm.circle(normal=[1, 0, 0,], radius=2)[0]

	#Naming for Third Local Pad
	local_pad_name3 = third_joint.replace('03_bind', '03_local')
	print 'Local Pad Name', local_pad_name3

	#Create Group and parent control under group
	local_pad_3 = pm.group(name=local_pad_name3)

	# Move to the target joint.
	# Parent Contrain offset is off, driver is the joint
	# Driven is the group
	temp_contraint4 = pm.parentConstraint(third_joint, local_pad_3 )

	# Delete Constraint
	pm.delete(temp_contraint4)

	# Delete History on control
	# Orient Constraint, driver is control, driven is joint
	pm.orientConstraint(control_icon_3, third_joint)

	# Lock Attributes
	control_icon_3.t.set(lock=True, keyable=False)
	control_icon_3.s.set(lock=True, keyable=False)
	control_icon_3.v.set(lock=True, keyable=False)


	# Create Local Hierarchy System

	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

def padding_tool():
	'''
	How to Run:
	import Project4
	reload(Project4)
	Project4.padding_tool()
	'''
	# What are we doing?
	# Padding joint system under a wolrd oriented Group

	# Select root joint of joint system
	selected = pm.ls(selection=True)
	print 'Selected Joint', selected

	root_joint = selected[0]

	# Naming for empty Group
	group_name = root_joint.replace('01_bind', '00_pad')
	print 'Empty Group Name', group_name
	# Create empty Group
	pad = pm.group(empty=True, name=group_name)

	# Move group to root joint with point constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	# Delete Constraint
	pm.delete(temp_constraint)

	# Freez Transformations
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent Joint to Group
	pm.parent(root_joint, pad )

def joint_rename():
	'''
	# Select the root joint and loop through all joints in the joint chain
	# 'ori_name_count_suffix'
	How to Run:
	import Project4
	reload(Project4)
	Project4.joint_rename()
	'''
	# What am I working on? 
	# Get everything in the joint chain.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected', joint_chain
	# Build our new name
	# 'lt'
	# 'arm'
	# '01'
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'
	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print 'Joint Name:', new_name

		count = count + 1

		current_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)

def priming_tool():
	'''
	How to Run:
	import Project4
	reload(Project4)
	Project4.priming_tool()
	'''

	#Get Selected
	selected = pm.ls(selection=True)
	print 'Joints Selected:', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', 'icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		#Create control wth radius of 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, 
		name=control_icon_name)[0]
		#Group the control (NOT EMPTY)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon 
		print 'Pad Created:', local_pad

		#Move Conrol over to target joint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		#Delete Constraint
		pm.delete(temp_constraint)
		#Orient Constraint joint to control
		pm.orientConstraint(control_icon, target_joint)

	print 'Local Oriented Controls Created'






















