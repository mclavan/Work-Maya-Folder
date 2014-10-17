'''
Lesson - Project Script.


How to Run:

import clavanMichael_riggingTools_cri1_1404
reload(clavanMichael_riggingTools_cri1_1404)

'''

import pymel.core as pm 

print 'Rigging Tools Activated.'

def hiearchy():
	'''
	This function creates a hierarchy on a given finger system. 

	Select the finger root joint, then execute the function. 

	import clavanMichael_riggingTools_cri1_1404
	clavanMichael_riggingTools_cri1_1404.hierarhcy()
	
	'''
	# Create a hierarhcy function
	# 	- Included header with:
	#       - What does the tool do?
	# 		- How to user the tool?
	# 	- Print what that function does.
	print 'Hierarchy Created.'


def padding_tool():
	# Create a padding_tool function
	# 	- Included header with:
	#       - What does the tool do?
	# 		- How to user the tool?
	# 	- Print what that function does.

	print 'Selected Joint Padded.'

def priming_tool():
	# Create a priming_tool function
	# 	- Included header with:
	#       - What does the tool do?
	# 		- How to user the tool?
	# 	- Print what that function does.
	print 'blah.'


# Create a joint_renaming function
# 	- Included header with:
#       - What does the tool do?
# 		- How to user the tool?
# 	- Print what that function does.
def joint_renamer():
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
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	joint_chain[-1].rename(new_name)
	# Output to the user
