'''
Lesson - Creating Groups
creating_groups.py


Creating and Parenting Groups
- We will create a series of groups in this lesson and parent them together.

- Topics Covered
Creating and Using Variables
	- Creating Maya objects and storing them into variables.

'''

import pymel.core as pm

print 'Creating Groups'

# Create two groups.
# Naming the groups 'ct_arm_01_pad1' and 'ct_arm_02_pad2'
pad1 = pm.group(empty=True, name='ct_arm_01_pad1')
pad2 = pm.group(empty=True, name='ct_arm_02_pad2')
pad3 = pm.group(empty=True, name='ct_arm_03_pad3')

print 'Pad 1:', pad1 
print 'Pad 2:', pad2
print 'Pad 3:', pad3 

# Parent the two groups gether in the proper order.
pm.parent(pad2, pad1)
pm.parent(pad3, pad2)

# Create a thrid group called 'ct_arm_01_pad3'
# Parent this pad under the second pad created earlier.


'''
# What have we acomplished here?

We have learn how to create object in Maya and parent them into a hierarchy.
- There is very little difference between groups, joints, and control icons.
- We will do the same thing to create a control system, like the back, arms, and legs.

'''

pad3 = pm.group(empty=True, name='ct_arm_03_pad3')
pad2 = pm.group(name='ct_arm_02_pad2')
pad1 = pm.group(name='ct_arm_01_pad1')

