'''
Exercise - Moving Objects - Part 2
Constraints

In this exercise we will use constraints to move objects. 

Create three joints in the scene and name them:
	lt_arm_01_bind
	lt_arm_02_bind
	lt_arm_03_bind

How to Run:

import moving_02
reload(moving_02)

'''

import pymel.core as pm 


'''
Creating three control icons. 
'''
control_icon_1 = pm.circle(normal=[1, 0, 0], name='lt_arm_01_icon')[0]
control_icon_2 = pm.circle(normal=[1, 0, 0], name='lt_arm_02_icon')[0]
control_icon_3 = pm.circle(normal=[1, 0, 0], name='lt_arm_03_icon')[0]

'''
Using Variables to track the joints. 
'''
selected = pm.ls(selection=True)

arm_joint_1 = 'lt_arm_01_bind'
arm_joint_2 = 'lt_arm_02_bind'
arm_joint_3 = 'lt_arm_03_bind'


# arm_joint_1 = selected[0]
# arm_joint_2 = selected[1]
# arm_joint_3 = selected[2]

'''
Moving control to joint. 
'''
# Point constraint snaps the control to the joint.
# The constraint isn't required after it moves the control.
# Delete the temp constraint after use.
temp_constraint = pm.pointConstraint(arm_joint_1, control_icon_1)
print 'Temp Constraint Created:', temp_constraint
pm.delete(temp_constraint)

temp_constraint = pm.pointConstraint(arm_joint_2, control_icon_2)
pm.delete(temp_constraint)

temp_constraint = pm.pointConstraint(arm_joint_3, control_icon_3)
pm.delete(temp_constraint)

'''
Point Constraint VS Parent Constraint 
Point will only translate object while parent will orient 
	the control too. 
'''

