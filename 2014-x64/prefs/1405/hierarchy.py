'''
hierarchy.py

Create control for the back bone.
- This will lead in to creating 

import hierarchy
reload(hierarchy)

'''

import pymel.core as pm 

print 'Rigging Tools Active'



'''
Input
- What are we working on?
'''
selected = pm.ls(selection=True, dag=True)
print 'Selected Joints:', selected

joint_1 = selected[0]
joint_2 = selected[1]
joint_3 = selected[2]


'''
Process
- What are we trying to build?
'''
'''
Control 1
'''
# Create a control
control_icon_1 = pm.circle(ch=False)[0]

# Create a group and parent control under group.
pad_1 = pm.group()

# Snap group to target joint.
# Driver is the joint.
# Driven is the group
temp = pm.parentConstraint(joint_1, pad_1, mo=False)

# Delete unused contraint
pm.delete(temp)

# Control drives joint
# Apply an orient constraint.
# Driver: control icon
# Driven is the joint.
pm.orientConstraint(control_icon_1, joint_1)

'''
Control 2
'''
# Create a control
control_icon_2 = pm.circle(ch=False)[0]

# Create a group and parent control under group.
pad_2 = pm.group()

# Snap group to target joint.
# Driver is the joint.
# Driven is the group
temp = pm.parentConstraint(joint_2, pad_2, mo=False)

# Delete unused contraint
pm.delete(temp)

# Control drives joint
# Apply an orient constraint.
# Driver: control icon
# Driven is the joint.
pm.orientConstraint(control_icon_2, joint_2)


'''
Parent Controls Together
'''
pm.parent(pad_2, control_icon_1)

'''
Output
- What have we created?
'''




	