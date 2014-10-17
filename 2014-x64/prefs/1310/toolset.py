'''
Michael Clavan
toolset.py 
clavanMichael_hierarchy_cri_1310.py 

Descript:

How to Run:

import toolset
reload(toolset)

'''

print 'toolset'

import pymel.core as pm

def hierarchy():
	'''
	Builds a finger hiearchy for the given scene. 
	Instructions:
		Select the root joint of the middle finger.
	'''

	'''
	Given
	'''
	root_joint = 'lt_middle_01_bind'
	middle_joint = 'lt_middle_02_bind'
	last_joint = 'lt_middle_03_bind'

	'''
	Process
	'''

	# A prime control will be required for each knuckle of the finger.

	# Control 1 - First Knucle

	# Create control icon.
	# Issue circle is not position correctly.
	# normal flag could be set to [1, 0, 0]
	# [nt.Transform(u'nurbsCircle1'), nt.MakeNurbCircle(u'makeNurbCircle5')]

	control_icon_1 = pm.circle(normal=[1, 0, 0], name=root_joint.replace('bind', 'icon'))[0]

	print 'Control Icons created: ', control_icon_1
	# Parent constrain it to target joint.
	temp_constraint = pm.parentConstraint(root_joint, control_icon_1)

	# Delete Constraint.
	pm.delete(temp_constraint)

	# A world oriented pad for the root joint is required.
	pad_name = root_joint.replace('bind', 'prime')
	pad_1 = pm.group(empty=True, , name=pad_name)
	# Parent constrain it to target joint.
	temp_constraint = pm.parentConstraint(root_joint, pad_1)

	# Delete Constraint.
	pm.delete(temp_constraint)

	# Parent control to pad
	pm.parent(control_icon_1, pad_1)



	'''
	Output
	'''

	print 'Hierarchy Created.'