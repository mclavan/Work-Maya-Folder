'''
Lesson - Project Script.


How to Run:

import clavanMichael_hierarchy_cri_1312
reload(clavanMichael_hierarchy_cri_1312)

'''

import pymel.core as pm 

print 'Rigging Tools Activated.'

def hierarchy():
	'''
	Rebuilds the given hiearchy.

	Select the root joint and execute the function.

	import ??
	'''
	# Create a hierarhcy function
	# 	- Included header with:
	#       - What does the tool do?
	# 		- How to user the tool?
	# 	- Print what that function does.

	print 'Hiearchy Created.'

def padding_tool():
	'''
	# Create a padding_tool function
	# 	- Included header with:
	#       - What does the tool do?
	# 		- How to user the tool?
	# 	- Print what that function does.

	import clavanMichael_hierarchy_cri_1312
	reload(clavanMichael_hierarchy_cri_1312)
	clavanMichael_hierarchy_cri_1312.padding_tool()

	'''
	'''
	Input Area
	Get the selected root joint!
	'''
	root_joint = pm.ls(selection=True)[0]

	'''
	Process
	'''
	# Create group, empty group.
	pad = pm.group(empty=True)

	# Use a point constraint to move the pad. 
	temp_constraint = pm.pointConstraint(root_joint, pad, maintainOffset=False)
	
	# Delete the temp constraint.
	pm.delete(temp_constraint)
	
	# freeze transforms
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# parent joint to pad
	pm.parent(root_joint, pad)

	# rename pad to mirror joints name.
	# replace method
	# rt_leg_01_bind -> rt_leg_00_pad
	new_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(new_name)
	
	'''
	Output
	'''
	print 'Root Joint Padded.'


# Create a priming_tool function
# 	- Included header with:
#       - What does the tool do?
# 		- How to user the tool?
# 	- Print what that function does.



# Create a joint_renaming function
# 	- Included header with:
#       - What does the tool do?
# 		- How to user the tool?
# 	- Print what that function does.

