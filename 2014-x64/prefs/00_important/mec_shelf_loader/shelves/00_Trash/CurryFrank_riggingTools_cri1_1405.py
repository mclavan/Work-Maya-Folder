'''

Frank Curry
Heirarchy Creation Tools

CurryFrank_rigging_tools.py

How to Run:
	import rigging_tools
	reload(rigging_tools)

'''

print 'Rigging Tools Active'

import pymel.core as pm

def heirarchy():
	
	'''
	
	Create a heirarchy based upon a given system.

	Select root joint chain and execute function.
	import rigging_tools
	rigging_tools.heirarchy()
	
	'''

	'''
	
	Input
	What are we working on?
	the root joint.
	
	'''
	
	joint_system = pm.ls(selection=True, dag=True)
	
	# print "Joint System:", joiint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	
	Padding root joint
	
	'''

	# Creating an empty group.
	root_pad = pm.group(empty=True)

	# Move group over th the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	
	# Parent root joint back the the group.
	pm.parent(root_joint, root_pad)

	'''
	
	Loacal Controls
	
	'''
	 
	'''
	
	Control 1 - root_joint
	
	'''
	
	# Create a control. 
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]
	 
	# Create  a group.
	# Grouping control during a prosses
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1
	
	# Move group over th the target joint.
	# Delete constraint after snapping
	# Driver: joint
	# Driven: group

	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Draver --> Driven.
	# Control --> Joint.
	pm.orientConstraint(control_icon_1, root_joint)


	'''
	
	Control 2
	
	'''
 	
 	# Create a control. 
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]
	 
	# Create  a group.
	# Grouping control during a prosses
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2
	
	# Move group over th the target joint.
	# Delete constraint after snapping
	# Driver: joint
	# Driven: group

	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Draver --> Driven.
	# Control --> Joint.
	pm.orientConstraint(control_icon_2, joint_2)


	'''
	
	Control 3
	
	'''
	
	# Create a control. 
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2,)[0]
	 
	# Create  a group.
	# Grouping control during a prosses
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3
	
	# Move group over th the target joint.
	# Delete constraint after snapping
	# Driver: joint
	# Driven: group

	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Draver --> Driven.
	# Control --> Joint.
	pm.orientConstraint(control_icon_3, joint_3)
	
	'''
	
	Parent controls together
	
	'''
	
	# Parent Pad 3 --> control 2
	pm.parent(local_pad_3, control_icon_2)
	
	# Parent Pad 2 --> control 1
	pm.parent(local_pad_2, control_icon_1)
	
	# Naming of groups

def joint_rename():
	
	'''
	
	# Select the root joint and loop through all joint in
	#	the joint chain.
	# 'ori_mane_count_suffix'
	# 'ct_back_01_bind'

	import book
	book.joint_rename()

	'''

	# Get all joints in a selected joint chain
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected:', joint_chain

	# Build our new name.
	# 'lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	
	
	for curent_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print "joint Name:", new_name

		count = count + 1

		curent_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'end')
	
	print 'Joint Name:', new_name
	
	curent_joint.rename(new_name)

	print "Joint Chain Renamed."
	
	# Padding tool of joints.

def pad_tool():

	'''

	Selection of joints.
	Cration of pads for joionts.
	Orientation of pads

	'''


	print 'heirarchy Created'


