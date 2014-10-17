'''
Michael Clavan
clavanMichael_riggingTools_cri1_1407.py

Description:
	Rigging Tools 

	Tools Included:
		- Hierarchy Tool
		- Joint Renamer
		- Padding Tool 
		- Priming Tool 

'''

print 'Rigging Tools Active'

def hierarchy():
	print 'Hierarchy Created'
	# Input Area
	selected = pm.ls(selection=True, dag=True)
	root_joint = selected[0]
	joint_2 = selected[1]
	joint_3 = selected[2]

	# Create control icon (nurbs circle)
	control_icon_1 = pm.circle(normal=[0, 1, 0], radius=5, name='ct_back_01_icon')[0]

	# Move the control to the target joint.
	#  We will use a point constraint because 
	#  we want to preserve the y up axis.
	kenny = pm.pointConstraint(root_joint, control_icon_1)

	# Delete the point constraint.
	#   The constraint is only used for movement.
	pm.delete(kenny)

	# Connect the control to the target joint.
	#  Use parent constraint with offset on.
	# 	Because the control and the joint do NOT 
	# 	have the same orientation.
	pm.parentConstraint(control_icon_1, root_joint, maintainOffset=True)

	'''
	FK control 2
	'''
	# Create control icon (nurbs circle)
	control_icon_2 = pm.circle(normal=[0, 1, 0], radius=5, name='ct_back_02_icon')[0]

	# Move the control to the target joint.
	kenny = pm.pointConstraint(joint_2, control_icon_2)
	# Delete the point constraint.
	pm.delete(kenny)
	# Connect the control to the target joint.
	pm.parentConstraint(control_icon_2, joint_2, maintainOffset=True)

	'''
	FK control 3
	'''
	# Create control icon (nurbs circle)
	# control_icon_3 = pm.circle(normal=[0, 1, 0], radius=5, name='ct_back_03_icon')[0]
	mel_line = 'curve -d 1 -p 1.04592 1.04592 1.04592 -p -1.04592 1.04592 1.04592 -p -1.04592 -1.04592 1.04592 -p 1.04592 -1.04592 1.04592 -p 1.04592 1.04592 1.04592 -p 1.04592 1.04592 -1.04592 -p 1.04592 -1.04592 -1.04592 -p 1.04592 -1.04592 1.04592 -p 1.04592 1.04592 1.04592 -p 1.04592 1.04592 -1.04592 -p -1.04592 1.04592 -1.04592 -p -1.04592 -1.04592 -1.04592 -p 1.04592 -1.04592 -1.04592 -p -1.04592 -1.04592 -1.04592 -p -1.04592 -1.04592 1.04592 -p -1.04592 1.04592 1.04592 -p -1.04592 1.04592 -1.04592 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;'
	control_icon_3 = pm.mel.eval(mel_line)

	# Move the control to the target joint.
	kenny = pm.pointConstraint(joint_3, control_icon_3)
	# Delete the point constraint.
	pm.delete(kenny)
	# Connect the control to the target joint.
	pm.parentConstraint(control_icon_3, joint_3, maintainOffset=True)


	'''
	Parent Control 
	'''
	# Parent control icons together.
	# Children first, then parent last.
	pm.parent(control_icon_2, control_icon_1)
	pm.parent(control_icon_3, control_icon_2)
	# 4 -> 3

def joint_renamer():
	print 'Joints Renamed'

def padding_tool():
	print 'Selected Joints padded.'

def priming_tool():
	print 'Locally oriented controls created for selected joints.'

	# Get Selected Joints

	# Loop through selected.

	# Create a control icon

	# Create a group (by selection, it will group created control)

	# Move group to the target joint.

	# Delete constraint. 

	# Orient constraint the control to the target joint 





