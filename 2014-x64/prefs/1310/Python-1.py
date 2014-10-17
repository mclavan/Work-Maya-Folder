import pymel.core as pm

'''
Pymel Objects
'''
control_object = pm.circle()
control_icon = control_object[0]
print 'Control Icon Created', control_icon
# [nt.Transform(u'nurbsCircle1'), nt.MakeNurbCircle(u'makeNurbCircle1')]

control_icon.tx.set(keyable=False, lock=True)
control_icon.ty.set(keyable=False, lock=True)
control_icon.tz.set(keyable=False, lock=True)

control_icon.rx.set(0)


pm.setAttr(control_icon + '.tx', keyable=False, lock=True)


