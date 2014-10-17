'''
Lesson - Project Script.


How to Run:

import clavanMichael_hierarchy_cri1_1402
reload(clavanMichael_hierarchy_cri1_1402)

'''

import pymel.core as pm 

print 'Rigging Tools Activated.'

def hierarchy():
	# Create a hierarhcy function
	# 	- Included header with:
	#       - What does the tool do?
	# 		- How to user the tool?
	# 	- Print what that function does.

	print 'Hierarchy Created.'



# Create a padding_tool function
# 	- Included header with:
#       - What does the tool do?
# 		- How to user the tool?
# 	- Print what that function does.


def priming_tool():
	# Create a priming_tool function
	# 	- Included header with:
	#       - What does the tool do?
	# 		- How to user the tool?
	# 	- Print what that function does.

	# Get target joint.
	selected_joints = pm.ls(selection=True)
	print 'Selected Joints:', selected_joints

	for target_joint in selected_joints:

		'''
		_bind
		lt_arm_01_bind
		lt_arm_01_local
		lt_arm_01_icon
		'''
		control_icon_name = target_joint.replace('_bind', '_icon')
		pad_name = target_joint.replace('_bind', '_pad')

		# Create a control
		control_icon = pm.circle(normal=[1, 0, 0], radius=2, ch=False, 
			name=control_icon_name)[0]

		# Create group
		pad = pm.group(name=pad_name)

		# move group to joint.
		temp_constraint = pm.parentConstraint(target_joint, pad)
		pm.delete(temp_constraint)

		# connect the control to the joint. 
		pm.orientConstraint(control_icon, target_joint)

	print 'Local oriented control has been created on selected.'


# Create a joint_renaming function
# 	- Included header with:
#       - What does the tool do?
# 		- How to user the tool?
# 	- Print what that function does.

