'''
Lesson - Priming Tool

Create a locally oriented pad and prime for each selected joint. 


How to Run:

import lecture10
reload(lecture10)
lecture10.priming_tool()

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
	selected = pm.ls(selection=True, dag=True)
	# print selected
	# Loops through selected joints.
	for current_joint in selected:

		icon_name = current_joint.replace('_bind', '_icon')
		pad_name = current_joint.replace('_bind', '_pad')

		# Create control icon
		icon = pm.circle(radius=2, normal=[1, 0, 0], name=icon_name)[0]
		print icon
		# Create group.
		pad = pm.group(name=pad_name)
		
		# Group command will parent control upon creation. 
		temp_constraint = pm.parentConstraint(current_joint, pad)
		pm.delete(temp_constraint)
		# Move group to target joint. 


		# Constraint target joint to group. 
		pm.orientConstraint(icon, current_joint)
		# Rename control and prime group

		# Output

	print 'Localling oriented control created for selected joints.'