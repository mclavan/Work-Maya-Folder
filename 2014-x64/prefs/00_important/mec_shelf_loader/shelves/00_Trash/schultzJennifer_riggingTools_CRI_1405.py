'''
schultzJennifer_riggingTools_CRI_1405.py
Jennifer Schultz

Description:
	Hierarchy generator for project 4.

How to run:

import schultzJennifer_riggingTools_CRI_1405
reload(schultzJennifer_riggingTools_CRI_1405)

'''

import pymel.core as pm

print 'Hierarchy Generated'

# The user will select the root joint and the tool 
#	 will apply the systems.

root_joint = 'lt_middle_01_bind'
second_joint = 'lt_middle_02_bind'
third_joint = 'lt_middle_03_bind'


	

def padding_tool():

	'''
	Description: Creates pad on the joint.

	How to run:

	import schultzJennifer_riggingTools_CRI_1405
	reload(schultzJennifer_riggingTools_CRI_1405)
	
	schultzJennifer_riggingTools_CRI_1405.padding_tool()

	'''

	# Select joints.
	selected = pm.ls(selection=True)

	root_joint = selected[0]

	pad = pm.group(empty=True)

	titan = pm.pointConstraint(root_joint, pad)
	pm.delete(titan)

	pm.makeIdentity(pad, a=True, t=1, s=1, r=1, n=0)

	pm.parent(root_joint, pad)

	pad_name = root_joint.replace('01_bind', '00_pad')

	pad.rename(pad_name)

	# Empty Groups

	# Rename Groups


def priming_tool():

	'''
	Description: Creates control with local pad of the joint.

	How to run:

	import schultzJennifer_riggingTools_CRI_1405
	reload(schultzJennifer_riggingTools_CRI_1405)
	
	schultzJennifer_riggingTools_CRI_1405.priming_tool()

	'''

	# Create a local oriented control for each joint
	# lt_middle_01_bind, lt_middle_02_bind, lt_middle_03_bind

	# Select joints.
	selected = pm.ls(selection=True)

	# Create control (circle)
	control_icon_1 = pm.circle(name='lf_middle_01_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# This will automatically parent the control under the group.
	control1_pad = pm.group(name='lt_middle_01_local')
	print 'Control Pad Created:', control1_pad

	# Move the group to the target joint.
	# Use a parent constraint driver as the joint.
	#	Where driven is the group.
	#	Offset is off (Snapping)
	titanA = pm.parentConstraint(root_joint, control1_pad)

	# Destroy the constraint
	pm.delete(titanA)

	# Delete History on control
	pm.delete
	pm.delete(control_icon_1, ch=True)

	# Orient Constraint driver: control driven: joint. 
	pm.orientConstraint(control_icon_1, root_joint)


	# Do this same process for second_joint
	control_icon_2 = pm.circle(name='lf_middle_02_icon', normal=[1,0,0])[0]

	control2_pad = pm.group(name='lt_middle_02_local')
	print 'Control Pad Created:', control2_pad

	titanB = pm.parentConstraint(second_joint, control2_pad)
	pm.delete(titanB)

	pm.delete(control_icon_2, ch=True)

	pm.orientConstraint(control_icon_2, second_joint)

	# Do this same process for third_joint
	control_icon_3 = pm.circle(name='lf_middle_03_icon', normal=[1,0,0])[0]

	control3_pad = pm.group(name='lt_middle_03_local')
	print 'Control Pad Created:', control3_pad

	titanC = pm.parentConstraint(third_joint, control3_pad)
	pm.delete(titanC)

	pm.delete(control_icon_3, ch=True)

	pm.orientConstraint(control_icon_3, third_joint)

	# Parent the controls together
	pm.parent(control2_pad, control_icon_1)
	pm.parent(control3_pad, control_icon_2)


	#Create a holding group to house the pads and controls
	middle_grp = pm.group(empty=True, name='lt_middle_grp')

	# Parent the pads and the controls under the main group
	# 	Make sure that they are not parented together
	pm.parent(control1_pad, middle_grp)

def joint_rename():
	
	'''

	Description: Renames joint chain.

	
	How to run:

	import schultzJennifer_riggingTools_CRI_1405
	reload(schultzJennifer_riggingTools_CRI_1405)
	
	schultzJennifer_riggingTools_CRI_1405.joint_rename()

	Create a function called joint_rename.
	Select the root joint and loop through all the joints in the joint chain.
	'ori_name_count_suffix'
	'ct_back_01_bind'

	'''

	# What am I woking on?
	# Get all joints in a selected joint chain.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected:', joint_chain

	# Build our new name
	# 'lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 0
	suffix = 'bind'


	# Loop through joint chain

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		print 'Joint Name:', new_name

		# Rename Joint
		current_joint.rename(new_name)
		
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')	
	current_joint.rename(new_name)


	print 'Joint Chain Renamed'