'''
Lesson - Priming Tool

Create a locally oriented pad and prime for each selected joint. 


How to Run:

import priming_tool
reload(priming_tool)
priming_tool.priming_tool()

'''
import pymel.core as pm

print 'Priming tool active'

def priming_tool():
	'''
	This tools creates both a locally oriented control and pad for
		each selected joint.

	Instructions:
		Select desired joints, then execute priming_tool function. 
	'''
	# Get selected joints
	selected_joints = pm.ls(selection=True)
	first_joint = selected_joints[0]

	print 'First Joint:', first_joint

	# Create control icon
	control_icon = pm.circle(nr=[1, 0, 0], radius=1.5)[0]

	print 'Control Icon Created:', control_icon

	# Create group.
	# Group command will parent control upon creation. 
	prime_group = pm.group()
	print 'Prime Group Created:', prime_group

	# Move group to target joint. 
	temp_constraint = pm.parentConstraint(first_joint, prime_group, maintainOffset=False)
	pm.delete(temp_constraint)

	# Clean control
	pm.delete(control_icon, ch=True)
	
	# Constraint target joint to group. 

	# Rename control and prime group

	# Output


	print 'Localling oriented control created for selected joints.'