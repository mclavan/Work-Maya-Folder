'''
Exercise - Moving Objects - Part 1

Different techniques for moving objects.
1) setAttr
2) xform
Given:

Move each control to the given position. 

Control 1 to 5, 0, 0
Control 2 to 0, 5, 0
Control 3 to 0, 0, 5

How to Run:

import moving_01
reload(moving_01)

'''

import pymel.core as pm

'''
Creating three control icons. 
'''
control_icon_1 = pm.circle(normal=[1, 0, 0], name='lt_arm_01_icon')[0]
control_icon_2 = pm.circle(normal=[1, 0, 0], name='lt_arm_02_icon')[0]
control_icon_3 = pm.circle(normal=[1, 0, 0], name='lt_arm_03_icon')[0]

print 'Control Icons Created:', control_icon_1, control_icon_2, control_icon_3

'''
Pymel

control_icon_1.tx.set(5)
control_icon_2.ty.set(5)
control_icon_3.t.set([0, 0, 5])
'''

'''
Xform 
Xform can translate, rotate, and scale in one command. 
'''
pm.xform(control_icon_1, t=[5, 0, 0])
pm.xform(control_icon_2, t=[0, 5, 0])
pm.xform(control_icon_3, t=[0, 0, 5])

'''
Freeze Transforms and delete history
'''
# How do I freeze transforms???
# makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
pm.makeIdentity(control_icon_1, control_icon_2, control_icon_3, apply=True, t=1, r=1, s=1, n=0)

pm.delete(control_icon_1, ch=1)

'''
Lock and Hide scale and visibility. 
'''


'''
Color Icons 
'''




