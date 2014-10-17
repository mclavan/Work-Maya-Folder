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
control_icon_1 = pm.circle()[0]
control_icon_2 = pm.circle()[0]

print 'Control Icon 1 is: ', control_icon_1
print 'Control Icon 2 is: ', control_icon_2

'''
Parent Control together. 
pm.parent(children, parent)
'''
pm.parent(control_icon_2, control_icon_1)

print 'Control icon 2 is parented to control icon 1.'






