'''
Michael Clavan
clavanMichael_riggingTools.py

Description:
	Various Rigging Tools 

How to Run:

import clavanMichael_riggingTools
reload(clavanMichael_riggingTools)

'''

import pymel.core as pm 


print 'Rigging Tools Activated.'


def hierarchy():
	'''
	The function will create a given hierarchy. 

	Select the root of a finger then run the function. 

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.hierarchy()
	'''

	# Get selected joints in the scene.
	joint_selected = pm.ls(selection=True, dag=True)

	print 'Selected Joints:', joint_selected
	root_joint = joint_selected[0]
	joint_2 = joint_selected[1]
	joint_3 = joint_selected[2]
	
	'''
	Padding the joint system. 
	'''

	# Create an empty group.
	# doGroup 0 1 1;
	pad = pm.group(empty=True)
	print 'Pad Created:', pad 


	# Moving empty group to root joint.
	# This will be a world oriented group.
	# parent or point constraint.
	temp_constraint = pm.parentConstraint(root_joint, pad)
	
	# The constraints flag is deleting the pad as well.
	# pm.delete(pad, constraints=True)
	# pm.delete(constraints=True)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	# This will make the group world.
	# makeIdentity
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.
	# parent command
	pm.parent(root_joint, pad)

	# Rename world group to reflect the joint.
	new_name = root_joint.replace('01_bind', '00_pad')
	print 'New Pad Created', new_name
	pad.rename(new_name)

	# 
	# pm.rename(pad, new_name)

	'''
	Creating Control system
	'''
	# Create Control Icon
	# Change the normal and radius flag to match scene.
	# Research ch flag.

	# Create Group

	# Parent Constraint to the joint.

	# Delete Constraint

	# Orient Constraint Control to the joint.




	# Parent Control System
	# Pad to the parent
	# Pad3 to Control2
	# Pad2 to Control1




	print 'Hierarchy Created.'

