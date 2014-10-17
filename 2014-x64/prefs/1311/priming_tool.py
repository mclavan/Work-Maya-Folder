'''
Lesson - Priming Tool

Create a locally oriented pad and prime for each selected joint. 


How to Run:

import priming_tool
reload(priming_tool)

'''

import pymel.core as pm

def priming_tool():
	'''
	This tools creates both a locally oriented control and pad for
		each selected joint.

	Instructions:
		Select desired joints, then execute primming_tool function. 
	'''
	# Get selected joints
	selected_joint = pm.ls(selection=True)

	current_joint = selected_joint[0]
	'''
	lt_arm_06_bind
	lt_arm_08_bind
	lt_arm_011_bind
	lt_arm_012_bind
	lt_arm_013_bind
	'''

	# Create control icon	
	control_icon = pm.circle(normal=[1, 0, 0], radius=1.5)[0]
	# Create group.
	prime_group = pm.group(control_icon)	
	# Group command will parent control upon creation. 
	
	# Move group to target joint. 
	temp_constraint = pm.parentConstraint(current_joint, prime_group)
	pm.delete(temp_constraint)	
	
	# Clean control
	pm.delete(control_icon, ch=1)
	# Constraint target joint to group. 
	pm.orientConstraint(control_icon, current_joint)
	# Rename control and prime group
	'''
	# Output
	'''

	print 'Localling oriented control created for selected joints.'