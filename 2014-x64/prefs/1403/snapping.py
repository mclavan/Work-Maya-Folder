'''
Exercise - Snapping Tool

Create a tool that will snap one object to another. 

Objectives:
- Plan out and document each step.
- Get Selected Objects 
- Use constraints to move objects. 
- Delete unused components. 
- Output what your tool has done to the scene.

How to Run:

import snapping
reload(snapping)

'''
import pymel.core as pm 

print 'hi'

# Get Selected objects. 
# Start out with hard coded names
selected = pm.ls(selection=True)
driver = selected[0]
driven = selected[1]
print 'Selected:', selected

# Use constraints to move driven to driver.
temp_constraint = pm.pointConstraint(driver, driven, mo=False)

# Delete Unused constraint
pm.delete(temp_constraint)
pm.makeIdentity(driver, apply=True, t=1, r=1, s=1, n=0)

# Inform user
print 'First Selected moved to second selected object.'

