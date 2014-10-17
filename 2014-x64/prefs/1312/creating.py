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
# Creating a control icon pointing to x-axis
#                 0
# [nt.Transform(u'nurbsCircle2'), 
#                                 1
# 			nt.MakeNurbCircle(u'makeNurbCircle2')]
# ['nurbsCircle1', 'nurbsCircle2']
control_icon_1 = pm.circle(nr=[1, 0, 0], name='lt_arm_01_icon')[0]
control_icon_2 = pm.circle(nr=[1, 0, 0], name='lt_arm_02_icon')[0]
control_icon_3 = pm.circle(nr=[1, 0, 0], name='lt_arm_03_icon')[0]

print 'Control Icon Created.', control_icon_1, control_icon_2, control_icon_3

pm.delete(control_icon_1, control_icon_2, control_icon_3, ch=1)

'''
Parent Control together.
# child then parent last.  
'''
pm.parent(control_icon_2, control_icon_1)
pm.parent(control_icon_3, control_icon_2)







