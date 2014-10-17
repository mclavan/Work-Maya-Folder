'''
Michael Clavan
clavan.py 

Description:
	Starter Script. 

How to Run:

import clavan
reload(clavan)

'''

print 'Starter Script Active'

import pymel.core as pm 

# top_pad = pm.group(name='top', empty=True)
# mid_pad = pm.group(name='middle', empty=True)
# bottom_pad = pm.group(name='bottom', empty=True)

# pm.parent(bottom_pad, mid_pad)
# pm.parent(mid_pad, top_pad)


# Lists
#          0       1          2         3 
# names = ['Kyle', 'Kenny', 'Cartman', 'Stan']

# print 'Current Names:', names
# print 'First Person:', names[0]
# print 'Second Person:', names[1]
# print 'Last Person:', names[-1]


'''
# Selection
'''
# all_items = pm.ls()
# print 'All Item: {0}'.format(all_items)

# nt.Transform(u'top1')
# Selected: [nt.Transform(u'top1'), nt.Transform(u'middle'), nt.Transform(u'bottom')]
# selected = pm.ls(selection=True)
# print 'Selected: {0}'.format(selected)
'''
# PyMel Object
'''
#                Name
# nt(nodeType)
#    Transform is a type of node
# nt.Transform(u'top1')

'''
# Snapping Tool
'''

selected = pm.ls(selection=True)
print 'Selected: {0}'.format(selected)
target_joint = selected[0]
control_icon = selected[1]

# By default commands work on selected.
kenny = pm.parentConstraint(target_joint, control_icon)
pm.delete(kenny)






















