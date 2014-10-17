'''
Lesson - Renaming

Rename a joint chain. 

How to Run:

import rename_01
reload(rename_01)

'''

import pymel.core as pm 

print 'Lesson - Renaming'

# Get selected root joint. 
# How do I get the entire hierarchy of a joint chain?
#   pm.ls(selection=True, dag=True)
joint_chain = pm.ls(selection=True, dag=True)
# print 'Joints:', joint_chain

# Naming Convention Example
# lt_arm_01_bind -> lt_arm_03_bind
# orienation_systemName_count_suffix
ori = raw_input()
name = raw_input()
count = 0
suffix = 'bind'

# Loop through selected.
for current_joint in joint_chain:
	count = count + 1
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
	print 'New Name:', new_name	
	current_joint.rename(new_name)
	# Compile new name

	# Add one to the count.

	# Rename the joint

	# Output to the user.


# Name the waste joint
new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')
# Output to the user
joint_chain[-1].rename(new_name)




