'''
Exercise - Snapping Tool

Create a tool that will snap one object to another. 

Objectives:
- Plan out and document each step.
- Get Selected Objects 
- Use constraints to move objects. 
- Delete unused components. 
- Output what your tool has done to the scene.

import snapping
reload(snapping)

'''
import pymel.core as pm 

# Get Selected objects. 
# Start out with hard coded names
selected = pm.ls(selection=True)
driver = selected[0]
driven = selected[1]

# IF statments

# Use constraints to move driven to driver.
temp_constraint = pm.parentConstraint(driver, driven)

# Delete Unused constraint
pm.delete(temp_constraint)

# Inform user
print 'Moving:', driven, ' to the ', driver


