'''
Michael Clavan
clavan.py

Description:
	Template starter script. 

How to Run:

import clavan
reload(clavan)

'''

print 'Starter Script.'	   

import pymel.core as pm 

# Getting Selection.
# Use ls command to get objects selected in our scene.
# We are going to print out what is selected. 
selected = pm.ls(selection=True)
print 'Selected: {0}'.format(selected)

# A Transform is a selectable object in Maya.
# A Transform consists of a position in 3D Space.
# Translation, Rotation, and Scale (X, Y, and Z)
# nodeType.Transform
# nt.Transform
#          0                    1                   2
#								-2					-1
# [nt.Transform(u'C'), nt.Transform(u'B'), nt.Transform(u'A')]
first_selected = selected[0]
last_selected = selected[1]
print 'First: {0} and Last: {1}'.format(first_selected, last_selected)

# I want to snap the second object to the first.
# I want to translate and rotate the target object. 
kenny = pm.parentConstraint(first_selected, last_selected)
pm.delete(kenny)

