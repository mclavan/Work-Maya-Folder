'''
Exercise - Snapping Tool

Create a tool that will snap one object to another. 

Objectives:
- Plan out and document each step.
- Get Selected Objects 
- Use constraints to move objects. 
- Delete unused components. 
- Output what your tool has done to the scene.

import snapping
reload(snapping)
snapping.snap_tool()

'''
import pymel.core as pm 

print 'hi'

def snap_tool():
	# Get Selected objects. 
	# Start out with hard coded names
	selected = pm.ls(selection=True)
	driver = selected[0]
	driven = selected[1]

	print 'Driver:', driver, ', Driven:', driven
	# Use constraints to move driven to driver.
	temp_constraint = pm.parentConstraint(driver, driven)
	pm.delete(temp_constraint)

	# Delete Unused constraint


	# Inform user

	print 'Snapped.  OH Yeah!'


def padding():
	'''
	This tool creates a world pad on the selected joint system. 

	Select the root and execute the command. 

	import snapping
	reload(snapping)
	snapping.padding()

	'''
	# Get selected root joint.
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create an empty group.
	pad = pm.group(empty=True)

	# Snap group to root joint. 
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms on pad
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# parent root joint to pad. 
	pm.parent(root_joint, pad)

	print 'Joint system has been padded.'

	# lt_arm_01_bind
	# lt_arm_00_pad
	# String method
	pad_name = root_joint.replace('01_bind', '00_pad')

	print 'Pad Name:', pad_name
	pad.rename(pad_name)

