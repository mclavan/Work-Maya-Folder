'''
Michael Clavan
rigging_tools.py


How to Run:

import rigging_tools
reload(rigging_tools)

'''


print 'hi'

import pymel.core as pm 

# Get selected
selected = pm.ls(selection=True)
print 'Selected:', selected
root_joint = selected[0]
second_joint = selected[1]
third_joint = selected[2]

# Control a control. 
# Change settings: normal x axis, radius is 2
control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1, 0, 0], radius=2)[0]

# Group control 
local_pad_1 = pm.group(control_icon_1, name='lt_middle_01_local')

# print 'Control', control_icon_1, 'Local Pad', local_pad_1

print 'Control: {0} Local Pad: {1}'.format(control_icon_1, local_pad_1)
# Delete history on control icon.

# Move control to target joint.
# Use parent constraint and delete the constraint.
kenny = pm.parentConstraint(root_joint, local_pad_1)
pm.delete(kenny)

# Use orient constraint.
# Driver is the control icon and 
#    driven is the target joint.
pm.orientConstraint(control_icon_1, root_joint)

'''
Control Icon 2
'''
# Control a control. 
# Change settings: normal x axis, radius is 2
control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1, 0, 0], radius=2)[0]

# Group control 
local_pad_2 = pm.group(control_icon_2, name='lt_middle_02_local')

# print 'Control', control_icon_1, 'Local Pad', local_pad_1

print 'Control: {0} Local Pad: {1}'.format(control_icon_2, local_pad_2)
# Delete history on control icon.

# Move control to target joint.
# Use parent constraint and delete the constraint.
kenny = pm.parentConstraint(second_joint, local_pad_2)
pm.delete(kenny)

# Use orient constraint.
# Driver is the control icon and 
#    driven is the target joint.
pm.orientConstraint(control_icon_2, second_joint)

# Parent local pad 2 to the control icon 1.
pm.parent(local_pad_2, control_icon_1)
