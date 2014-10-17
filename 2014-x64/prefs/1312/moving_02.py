'''
Exercise - Moving Objects - Part 2
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
joint_system = pm.ls(selection=True, dag=True)
arm_joint_1 = joint_system[0]
arm_joint_2 = joint_system[1]
arm_joint_3 = joint_system[2]


'''
Creating three control icons. 
'''
control_icon_1 = pm.circle(normal=[1, 0, 0], name='lt_arm_01_icon')[0]
control_icon_2 = pm.circle(normal=[1, 0, 0], name='lt_arm_02_icon')[0]
control_icon_3 = pm.circle(normal=[1, 0, 0], name='lt_arm_03_icon')[0]


'''
Moving control to joint. 
'''
temp_constraint = pm.parentConstraint(arm_joint_1, control_icon_1, maintainOffset=False)
pm.delete(temp_constraint)
temp_constraint = pm.parentConstraint(arm_joint_2, control_icon_2, maintainOffset=False)
pm.delete(temp_constraint)
temp_constraint = pm.parentConstraint(arm_joint_3, control_icon_3, maintainOffset=False)
pm.delete(temp_constraint)

'''
Point Constraint VS Parent Constraint 
Point will only translate object while parent will orient 
	the control too. 
'''
pm.orientConstraint(control_icon_1, arm_joint_1)
pm.orientConstraint(control_icon_2, arm_joint_2)
pm.orientConstraint(control_icon_3, arm_joint_3)


