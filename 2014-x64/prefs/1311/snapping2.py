'''
Exercise - Snapping Tool

Create a tool that will snap one object to another. 

Objectives:
- Plan out and document each step.
- Get Selected Objects 
- Use constraints to move objects. 
- Delete unused components. 
- Output what your tool has done to the scene.

How To Run:

import snapping
reload(snapping)

'''
import pymel.core as pm 

print 'Snapping Tool Active'

# Get Selected objects. 
# Start out with hard coded names
selected = pm.ls(selection=True)
print 'Selected Items:', selected 

#                                0 								1  
# Selected Items: [nt.Joint(u'lt_middle_01_bind'), nt.Transform(u'nurbsCircle1')]
# Joint and Control Icon
target_joint = selected[0]
control_icon = pm.circle(normal=[1, 0, 0])[0]

'''
Control Snapping
'''
# Use constraints to move driven to driver.
temp_constraint = pm.parentConstraint(target_joint, control_icon)
# Delete Unused constraint
pm.delete(temp_constraint)

'''
Local Pad
'''
# Result: nt.Transform(u'null1') # 
prime_group = pm.group(world=True, empty=True)
# Use constraints to move driven to driver.
temp_constraint = pm.parentConstraint(target_joint, prime_group)
# Delete Unused constraint
pm.delete(temp_constraint)

# What do I parent to whom?
pm.parent(control_icon, prime_group)


# Inform user
print first_selected, ' is snapped to ', second_selected


