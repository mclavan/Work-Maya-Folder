'''
Exercise - Selection
selection.py 

Getting selected items in the scene.
'''

import pymel.core as pm

'''
ls command
pm.ls()
'''

# Use the ls command to get everything in Maya.
# Print out all Maya's objects.
all_maya_object = pm.ls()
print "All Maya's Objects:", all_maya_object


# Use the selection flag to get all items selected in Maya.
selected_items = pm.ls(selection=True)
print 'Selected Items:', selected_items

# Print out the first item selected.

# Print out the last item selected.

# Print out everything but the first item.

# Print out evrything but the last item.


# Use the selection and dag flag to print out a joints hierarchy.
joint_system = pm.ls(selection=True, dag=True)
print 'Joint System:', joint_system

# Print out the root joint.

# Print out all the joints but the waste joint.






