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

# WHAT AM I WORKING ON!!!!
joint_chain = pm.ls(selection=True, dag=True)
print 'Joint Chain:', joint_chain

'''
Process
'''

# Naming Convention Example
# lt_arm_01_bind -> lt_arm_03_waste
# orienation_systemName_count_suffix

ori = raw_input()
system_name = raw_input()
count = 0
suffix = 'bind'


# Loop through selected.
for current_joint in joint_chain:	
	# Add one to the count.
	count = count + 1
	# Compile new name
	#  lt_arm
	# poop!!!
	# new_name = ori + '_' + system_name + '_' + str(count) + '_'
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)

	print 'New Name:', new_name

	# Rename the joint
	current_joint.rename(new_name)
	# Output to the user.


# Name the waste joint
new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
joint_chain[-1].rename(new_name)

'''
Output
'''
# Output to the user




