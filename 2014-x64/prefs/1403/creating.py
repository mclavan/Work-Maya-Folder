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

How to Run:

import creating
reload(creating)
'''

import pymel.core as pm

print 'Exercise - Creating and Catching Objects'


'''
Creating three control icons. 
'''
# What is the command for creating a control icon?
# circle
control_icon_1 = pm.circle(r=2)[0]

# Control 2
control_icon_2 = pm.circle(radius=4)[0]

# Control 3
control_icon_3 = pm.circle(radius=6)[0]

print 'Control Icons Created:', control_icon_1, control_icon_2, control_icon_3

'''
Parent Control together. 
'''
pm.parent(control_icon_2, control_icon_1)
pm.parent(control_icon_3, control_icon_2)






