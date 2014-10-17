
'''
# Proxy tool
'''
# Based upon a selected joint and a piece of proxy hierarchy.

# Name the proxy geometry based on the joint.

# It will freeze transforms, delete history, center pivot proxy geometry.

# Parent Constrain proxy geometry to selected joint.


'''
# Control Icon Renamer (Very simular to joint renamer)
'''


'''
Control color.
    # color based on orientation
'''

left_icons = pm.ls('lt_*_icon')


'''
Pose Reset
'''

control_icons = pm.ls('*_icon')

for current_control in control_icons:
    current_control.rx.set(0)
    current_control.ry.set(0)
    current_control.rz.set(0)
    current_control.tx.set(0)
    current_control.ty.set(0)
    current_control.tz.set(0)








