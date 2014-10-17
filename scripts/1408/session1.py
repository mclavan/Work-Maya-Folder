

import pymel.core as pm

# Create a control
# Set normal flag to [1, 0, 0]
control_icon_1 = pm.circle(name='lt_middle_01_icon', radius=1.5, normal=[1, 0, 0])[0]

# Create a group
# Creating a non empty group will automaticly parent 
# 	the control icon above.
local_pad_1 = pm.group(control_icon_1, name='lt_middle_01_local')

# Parent constraint the group to the target joint.
# Delete constraint


# print 'Control Icon: ', control_icon_1, ' - Local Pad:', local_pad_1
print control_icon_1, local_pad_1

