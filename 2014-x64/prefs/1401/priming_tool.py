'''
Lesson - Priming Tool

Create a locally oriented pad and prime for each selected joint. 


How to Run:

import priming_tool
reload(priming_tool)

'''
import pymel.core as pm 

print 'Priming Tool Active.'

def priming_tool():
	'''
	This tools creates both a locally oriented control and pad for
		each selected joint.

	Instructions:
		Select desired joints, then execute primming_tool function. 
	'''
	# Get selected joints
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Create control icon
	control_icon = pm.circle()[0]

	print 'Selected', selected, 'Control Created', control_icon

	# Create group.
	# Group command will parent control upon creation. 
	pad = pm.group()

	# Move group to target joint. 
	temp_constraint = pm.parentConstraint(first_selected, pad)
	pm.delete(temp_constraint)
	
	# Clean control
	pm.delete(control_icon, ch=True)

	# Constraint target joint to group. 
	pm.orientConstraint(control_icon, first_selected)

	# Rename control and prime group
	# lt_arm_01_bind
	# control icon
	icon_name = first_selected.replace('_bind', '_icon')
	# print 'Joint Name', first_selected, ', Icon Name', icon_name
	control_icon.rename(icon_name)

	# lt_arm_01_bind -> lt_arm_01_pad
	pad_name = first_selected.replace('_bind', '_pad')
	pad.rename(pad_name)

	# Output


	print 'Localling oriented control created for selected joints.'