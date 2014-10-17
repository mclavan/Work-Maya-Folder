'''
Exercise - Moving Objects 
Constraints

In this exercise we will use constraints to move objects. 

Create three joints in the scene and name them:
	lt_arm_01_bind
	lt_arm_02_bind
	lt_arm_03_bind

'''

import pymel.core as pm 
'''
Using Variables to track the joints. 
'''
selected = pm.ls(selection=True)

arm_joint_1 = selected[0]
arm_joint_2 = selected[1]
arm_joint_3 = selected[2]


'''
Creating three control icons. 
'''
control_icon_1 = pm.circle(r=2, normal=[1, 0, 0], name='lt_back_01_icon')[0]
control_icon_2 = pm.circle(r=2, normal=[1, 0, 0], name='lt_back_02_icon')[0]
control_icon_3 = pm.circle(r=2, normal=[1, 0, 0], name='lt_back_03_icon')[0]


'''
Moving control to joint. 
'''

'''
Point Constraint VS Parent Constraint 
Point will only translate object while parent will orient 
	the control too. 
'''
# Driver and Driven
temp_constraint = pm.parentConstraint(arm_joint_1, control_icon_1)
pm.delete(temp_constraint)
temp_constraint = pm.parentConstraint(arm_joint_2, control_icon_2)
pm.delete(temp_constraint)
temp_constraint = pm.parentConstraint(arm_joint_3, control_icon_3)
pm.delete(temp_constraint)
'''
Affected Objects 
Freeze Transforms and delete history on moved objects. 
'''


