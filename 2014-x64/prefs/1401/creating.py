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
control_icon_3 = pm.circle()[0]

print 'Control Icons:', control_icon_1, control_icon_2, control_icon_3
# [nt.Transform(u'nurbsCircle1'), 
#		nt.MakeNurbCircle(u'makeNurbCircle1')]

pm.delete(control_icon_1, control_icon_2, control_icon_3, 
	ch=True)

'''
Parent Control together. 
control1 -> control2 -> control3
'''
# control3 to control2
pm.parent(control_icon_3, control_icon_2)

# control2 to control1
pm.parent(control_icon_2, control_icon_1)







