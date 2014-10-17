'''
Exercise - Creating and Catching Objects

Create three controls.
Name these controls:
	lt_arm_01_icon
	lt_arm_02_icon
	lt_arm_03_icon

Parent these controls in proper order.
- Comment Each Step
- Run your script often.
	Run each line as they completed.  
- Print out what is created and the results of the script.

'''

import pymel.core as pm

print 'Exercise - Creating and Catching Objects'

# Create a function called controls.
# print hi inside the function. 
def controls():

	# How do I get the first selected item in the scene.
	selected_joints = pm.ls(selection=True)
	first_selected_joint = selected_joints[0]
	print 'Selected Joint:', first_selected_joint


	# Create three controls
	#       0                  1
	# ['nurbsCircle1', 'makeNurbsCircle1']
	# [nt.Transform(u'nurbsCircle1'), nt.MakeNurbCircle(u'makeNurbCircle1')]
	control_icon = pm.circle(normal=[1, 0, 0], radius=0.8)[0]

	# Group control.
	pad = pm.group()
	
	print 'Control Icon: ', control_icon
	print 'Pad: ', pad
	# What are we going to put these controls on?
	# Three joints in our scene.
	# parent constraint to move group to joint.
	temp_constraint = pm.parentConstraint(first_selected_joint, pad)

	# Constraint must be deleted.
	pm.delete(temp_constraint)

	# Move controls to target joints.

	print 'Whats going on.'
	''''''

'''
Creating three control icons. 
'''

'''
Parent Control together. 
'''







