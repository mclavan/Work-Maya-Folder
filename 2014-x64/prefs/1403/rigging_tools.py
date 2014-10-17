'''
Michael Clavan
rigging_tools.py

Description:
	???

How To Run:

import rigging_tools
reload(rigging_tools)
'''

import pymel.core as pm 

print 'Riggging Tools - Active.'

# Get the selected root joint.
joint_system = pm.ls(selection=True)
root_joint = joint_system[0]
joint_2 = joint_system[1]
joint_3 = joint_system[2]

print 'Root Joint:', root_joint

'''
Joint Pad
- Need a root joint and create a group. 
'''

# # Create an empty group.
# root_pad = pm.group(empty=True)
# print 'Root Pad Created:', root_pad

# # Move empty group to the joint.
# temp_constraint = pm.parentConstraint(root_joint, root_pad, mo=False)
# pm.delete(temp_constraint)

# # Freeze transforms on the group.
# pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

# # Parent root joint to the group.
# pm.parent(root_joint, root_pad)


'''
Finger Controls
'''
'''
Control 1
'''
# Create a control 
control_icon_1 = pm.circle(normal=[1, 0, 0], radius=1.8)[0]

# Create a group
# Creating a normal group will automaticly parent the 
#    control to the group.
local_pad_1 = pm.group(control_icon_1)

# Move the pad to the target joint. 
# 	Using a parent constraint.
temp_constraint = pm.parentConstraint(root_joint, local_pad_1)

# Delete unused constraint
pm.delete(temp_constraint)

# Orient constraint the 
#   Driver will be the control.
#   Driven will be the joint.
pm.orientConstraint(control_icon_1, root_joint)

# The curve looks incorrect!
# It is not point down the correct axis and it too small.

# Delete history on control.

'''
Control 2
'''
# Create a control 
control_icon_2 = pm.circle(normal=[1, 0, 0], radius=1.8)[0]

# Create a group
# Creating a normal group will automaticly parent the 
#    control to the group.
local_pad_2 = pm.group(control_icon_2)

# Move the pad to the target joint. 
# 	Using a parent constraint.
temp_constraint = pm.parentConstraint(root_joint, local_pad_1)

# Delete unused constraint
pm.delete(temp_constraint)

# Orient constraint the 
#   Driver will be the control.
#   Driven will be the joint.
pm.orientConstraint(control_icon_1, root_joint)

# The curve looks incorrect!
# It is not point down the correct axis and it too small.

# Delete history on control.





