'''
Exercise - Snapping Tool

Create a tool that will snap one object to another. 

Objectives:
- Plan out and document each step.
- Get Selected Objects 
- Use constraints to move objects. 
- Delete unused components. 
- Output what your tool has done to the scene.

'''
import pymel.core as pm 
print 'hi'

# Get Selected objects. 
# Start out with hard coded names
selected = pm.ls(selection=True)
joint_chain = selected[0]

# Create control icon
control_icon = pm.circle(radius=2, normal=[1, 0, 0])[0]
print 'Control Icon:', control_icon

# Use constraints to move driven to driver.
# Match orientation, use parent constraint
temp = pm.parentConstraint(joint_chain, control_icon)
pm.delete(temp)

# Delete Unused constraint


# Inform user
print 'Created control', control_icon, 'and moved it to', joint_chain
