'''

import welcome
reload(welcome)
'''

print 'Hello'
print 'Hello, again.'

import pymel.core as pm 

'''
Creating Control Icon. 
'''


# Create the circle
# What does the circle command return after 
# 	it creates a circle?
# [nt.Transform(u'nurbsCircle1'), nt.MakeNurbCircle(u'makeNurbCircle1')]
control_icon_1 = pm.circle()[0]
print 'Control Icon 1:', control_icon_1

# Then create two additional circles
control_icon_2 = pm.circle()[0]
control_icon_3 = pm.circle()[0]
print 'Control Icon 2:', control_icon_2
print 'Control Icon 3:', control_icon_3

# Move circles so they are not on top of one another.
'''
Control Icon 1: nurbsCircle1
Control Icon 2: nurbsCircle2
Control Icon 3: nurbsCircle3
pm.setAttr('object.attribute', value)


pm.setAttr(control_icon_1 + '.translateY', 5)
pm.setAttr(control_icon_2 + '.translateX', 5)
pm.setAttr(control_icon_3 + '.translateZ', 5)

'''
control_icon_1.translateY.set(5)
control_icon_2.translateX.set(5)
control_icon_3.translateZ.set(5)



# parent control icons to one another.
# control1 -> control2 -> control3
pm.parent(control_icon_2, control_icon_1)
pm.parent(control_icon_3, control_icon_2)

# Delete history and freeze transforms on control icons
pm.delete(control_icon_1, control_icon_2, control_icon_3, ch=True)
print 'History Deleted.', control_icon_1, control_icon_2, control_icon_3
pm.makeIdentity(control_icon_1, control_icon_2, control_icon_3, 
	apply=True, t=1, r=1, s=1, n=0)
print 'Transforms Frozen.', control_icon_1, control_icon_2, control_icon_3

# Lock translate, scale, and visibility channels.
'''
pm.setAttr(control_icon_1 + '.translateX', lock=True)
'''
control_icon_1.tx.set(lock=True, keyable=False)
control_icon_1.ty.set(lock=True, keyable=False)
control_icon_1.tz.set(lock=True, keyable=False)



