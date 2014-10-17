'''
Catching Results
'''
import pymel.core as pm
'''
Control Icons
The circle and curve command are creating spline curves in the scene.
Any time a Maya command creates something in a scene an object or results is sent back.
'''

# Run this line.
pm.curve(p=[(-1, 0, 1), (1, 0, 1), (1, 0, -1), (-1, 0, -1), (-1, 0, 1)],k=[0, 1, 2, 3, 4],d=1)
# You will see the below line in the script editor.
# Result: nt.Transform(u'curve1') # 


# Lets just focus on the name 'curve1' for now.
# This line is telling you that 'curve1' was created.
# We will cover the rest of line later.


# OBJECTS
# You may have heard of Object Oriented Programming or OOP.  
# What this mean is 



# What does this mean?
# Results means that something was created and Maya is informing you what has been created.
# nt.Transform(u'curve1') - This is the curve you created.
# u'curve1' is the name of the curve you created.
# Transform is the type of 'curve1' 
# nt is the library.

# Reading this out would sound like this.
# The Transform node curve1 was created.

'''
Using Variables
'''
control_icon = pm.curve(p=[(-1, 0, 1), (1, 0, 1), (1, 0, -1), (-1, 0, -1), (-1, 0, 1)],k=[0, 1, 2, 3, 4],d=1)
prime_pad = pm.group(empty=True)
print control_icon
print prime_pad

# Parenting
# Lets parent the control icon to the parent.
pm.parent(control_icon, prime_pad)

# Lets create a series of groups and parent them togther.
group_1 = pm.group(empty=True, name='top_grp')
group_2 = pm.group(empty=True, name='middel_grp')
group_3 = pm.group(empty=True, name='bottom_grp')
pm.parent(group_2, group_1)
pm.parent(group_3, group_2)


# Snapping Control Icons.
# Open the scene control snapping
control_icon_full = pm.circle()
print control_icon_full
# The circle returned two items.
# Check out the Anatomy of a control icon podcast.
# We only need the transform of the second control icon
control_icon_1 = control_icon_full[0]
print control_icon_1

selected_joint = pm.ls(selection=True)[0]
snap_constraint = pm.parentConstraint(selected_joint, control_icon_1)
pm.delete(snap_constraint)






# We can not use these variables to more the objects together.




'''
Selection
'''

