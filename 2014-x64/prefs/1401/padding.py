'''
Exercise - Padding

Describe the steps to padding a joint.

'''

import pymel.core as pm 

print 'Padding Script Active.'

# What is my input???
# What am I working on?
# Work on the first selected.
selected = pm.ls(selection=True)

print 'Selected', selected

first_selected = selected[0]

'''
Group
'''
world_group = pm.group(empty=True)

print 'World group created.', world_group

'''
Snap group to the joint. 
'''
temp_constraint = pm.pointConstraint(first_selected, world_group)
pm.delete(temp_constraint)

'''
Freeze Transforms on group. 
'''
pm.makeIdentity(world_group, apply=True, t=1, r=1, s=1, n=0)

'''
Parent joint to the group. 
'''
pm.parent(first_selected, world_group)

'''
Renaming group to mirror joint. 
'''

# What have I done?



