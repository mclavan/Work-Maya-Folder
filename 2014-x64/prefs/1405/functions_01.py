'''
Lesson - Functions

This exercise will introduce functions. 

How to Run:

import functions_01
reload(functions_01)

'''

import pymel.core as pm 
import book

print 'Lesson - Function practice.'


def create_controls():
	control_icon_1 = pm.circle(normal=[0, 1, 0])[0]
	control_icon_2 = pm.circle(normal=[0, 1, 0])[0]

	control_icon_1.ty.set(2.5)
	control_icon_2.ty.set(5)

	pm.parent(control_icon_2, control_icon_1)

	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=True, keyable=False)
	control_icon_1.tz.set(lock=True, keyable=False)
	control_icon_1.sx.set(lock=True, keyable=False)
	control_icon_1.sy.set(lock=True, keyable=False)
	control_icon_1.sz.set(lock=True, keyable=False)
	control_icon_1.v.set(lock=True, keyable=False)


'''








control_icon_2.tx.set(lock=True, keyable=False)
control_icon_2.ty.set(lock=True, keyable=False)
control_icon_2.tz.set(lock=True, keyable=False)
control_icon_2.sx.set(lock=True, keyable=False)
control_icon_2.sy.set(lock=True, keyable=False)

control_icon_2.sz.set(lock=True, keyable=False)

control_icon_2.v.set(lock=True, keyable=False)
'''

