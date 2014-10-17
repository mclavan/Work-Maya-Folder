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
joint_system = pm.ls(selection=True, dag=True)
print 'Joint System:', joint_system

# Naming Convention Example
# lt_arm_01_bind -> lt_arm_03_waste
# orienation_systemName_count_suffix

ori = 'lt'
sys_name = 'arm'
count = 0
suffix = 'bind'

# print ori + '_' + sys_name + '_' + str(count) + '_' + suffix

# print '{0}_{1}_0{2}_{3}'.format(ori, sys_name, count, suffix)

# Loop through selected.
for current_joint in joint_system:
	count = count + 1
	# Compile new name
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, sys_name, count, suffix)

	# Add one to the count.
	print 'Current Joint:', current_joint, new_name	
	# Rename the joint
	current_joint.rename(new_name)

	# Output to the user.


# Name the waste joint
new_name = '{0}_{1}_0{2}_{3}'.format(ori, sys_name, count, 'waste')
# Output to the user
joint_system[-1].rename(new_name)



