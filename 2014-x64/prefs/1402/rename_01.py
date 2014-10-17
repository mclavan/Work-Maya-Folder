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

print 'Joint system:', joint_system

# Naming Convention Example
# lt_arm_01_bind -> lt_arm_03_waste
# orienation_systemName_count_suffix
ori = raw_input()
system_name = raw_input()
count = 0
suffix = 'bind'

# Loop through selected.
for current_joint in joint_system:
	# Add one to the count.
	count = count + 1
	# Compile new name	
	# new_name = ori + '_' + system_name + '_0' + str(count) + '_' + suffix 
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, system_name, count, suffix)
	# Output to the user.
	print 'New name:', new_name

	# Rename the joint
	current_joint.rename(new_name)



# Name the waste joint
new_name = ori + '_' + system_name + '_0' + str(count) + '_' + 'waste'
print 'New Name:', new_name
joint_system[-1].rename(new_name)

# Output to the user




