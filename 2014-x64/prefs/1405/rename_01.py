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
#   
joint_chain = pm.ls(selection=True, dag=True)
print 'Selected Joint Chain:', joint_chain

# Naming Convention Example
# lt_arm_01_bind -> lt_arm_03_waste
# orienation_systemName_count_suffix
ori = raw_input()
name = raw_input()
count = 1
suffix = 'bind'

# Loop through selected.
for current_joint in joint_chain:
	# print 'Active Joint:', current_joint
	# Compile new name
	# {0}
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
	print 'Joint Name:', new_name
	# Add one to the count.

	count = count + 1
	# Rename the joint

	current_joint.rename(new_name)
	# Output to the user.


# Name the waste joint
new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')
joint_chain[-1].rename(new_name)
# Output to the user




