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
arm_joint_1 = 'lt_arm_01_bind'
arm_joint_2 = 'lt_arm_02_bind'
arm_joint_3 = 'lt_arm_03_bind'

'''
Moving control to joint. 
'''

'''
Point Constraint VS Parent Constraint 
Point will only translate object while parent will orient 
	the control too. 
'''
pm.pointConstraint(arm_joint_1, control_icon_1, maintainOffset=False)
pm.pointConstraint(arm_joint_2, control_icon_2, maintainOffset=False)
pm.pointConstraint(arm_joint_3, control_icon_3, maintainOffset=False)



