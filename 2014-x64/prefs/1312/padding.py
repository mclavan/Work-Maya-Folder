'''
Exercise - Padding

Describe the steps to padding a joint.

How to Run Area:

import padding
reload(padding)


'''

import pymel.core as pm 

print 'Padding Script Active.'

'''
Input (selected)
'''
# Get the entire hiearchy of a selected joint chain.
joint_system = pm.ls(selection=True, dag=True)
print 'Joint System:', joint_system

root_joint = joint_system[0]
joint_2_bind = joint_system[1]

'''
Process
'''
'''
First Control 
'''
# Create first control icon 
# normal=[1, 0, 0] down x-axis radius=2.5
control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2.5)[0]
# Delete history on control
pm.delete(control_icon_1, ch=True)


# Create first local pad (prime)
prime_1 = pm.group()

# Parent Constraint (local orienation) move pad to 
#   the first joint.
temp_constraint = pm.parentConstraint(root_joint, prime_1, maintainOffset=False)

# Delete temp constraint
pm.delete(temp_constraint)

# Orient constraint the control to move the joint.
pm.orientConstraint(control_icon_1, root_joint, maintainOffset=False)

'''
Second Control 
'''
# Create first control icon 
# normal=[1, 0, 0] down x-axis radius=2.5
control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2.5)[0]
# Delete history on control
pm.delete(control_icon_2, ch=True)


# Create first local pad (prime)
prime_2 = pm.group()

# Parent Constraint (local orienation) move pad to 
#   the first joint.
temp_constraint = pm.parentConstraint(joint_2_bind, prime_2, maintainOffset=False)

# Delete temp constraint
pm.delete(temp_constraint)

# Orient constraint the control to move the joint.
pm.orientConstraint(control_icon_2, joint_2_bind, maintainOffset=False)


'''
Parent Area
prime_1
	control_icon_1
		prime_2
			control_icon_2
				prime_3
					control_icon_3
'''
# control_icon_1, control_icon_2, control_icon_3
# prime_1, prime_2, prime_3
pm.parent(prime_2, control_icon_1)


'''
Output
Telling the user what you changed on their scene. 
'''


