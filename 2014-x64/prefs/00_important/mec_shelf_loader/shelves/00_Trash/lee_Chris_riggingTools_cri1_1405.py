'''
Chris Lee
Rigging_Tools.py

Description:
	This is the final compilation of four tools.

How to Run:

import Rigging_Tools
reload(Rigging_Tools)

'''
import pymel.core as pm

def joint_rename():
	'''
	import Rigging_Tools
	reload(Rigging_Tools)
	Rigging_Tools.joint_rename()
	
	'''

	'''
	 Create a function called joint_rename.
	 Select the root joint and loop through all joints in the joint chain.
	 'ori_name_count_suffox' - 'ct_back_01_bind'

	'''

	#Get all joints in a selected join chain.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected:', joint_chain
	
	#Build our new name.
	# 'lt'
	# 'arm'
	# '01'
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'
	
	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		print 'Joint Name:', new_name

		current_joint.rename(new_name)

		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)

	print 'Joint Chain Renamed'

def hierarchy():
	'''
	import Rigging_Tools
	reload(Rigging_Tools)
	Rigging_Tools.hierarchy()
	
	'''

	print 'Hierarchy Generated'

	# The user will select the root joint and the tool
	#	will apply the systems.

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'
	# Pad the root joint.


	# Create an empty group.
	pad_01 = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created', pad_01,

	# Move group to root joint.
	# Point consttrain group to root join.
	#	offset off (Snapping)
	kill = pm.pointConstraint(root_joint, pad_01)

	# Delete constraint.
	pm.delete(kill)

	# Freeze transforms on group.
	pm.makeIdentity(pad_01, apply=True, t=1, r=1, s=1, n=0)

	# Parent root join to group.
	pm.parent(root_joint, pad_01)
		
	# Create a local oriented control for each joint.
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind.


	# Create control (circle).
	control_icon_01 = pm.circle(name='lt_middle_01_icon')[0]
	control_icon_02 = pm.circle(name='lt_middle_02_icon')[0]
	control_icon_03 = pm.circle(name='lt_middle_03_icon')[0]

	#Create group (Not Empty).
	#	This will automatically parent the control under the group.
	pad_02 = pm.group(control_icon_01, name='lt_middle_01_local')
	pad_03 = pm.group(control_icon_02, name='lt_middle_02_local')
	pad_04 = pm.group(control_icon_03, name='lt_middle_03_local')

	# Move group to the target joint.
	# Use a parent constraint.
	#	Driver is the joint, driven is the group.
	#	Offst is off.
	kill00 = pm.parentConstraint(root_joint, pad_02)
	kill01 = pm.parentConstraint(second_joint, pad_03)
	kill02 = pm.parentConstraint(third_joint, pad_04)

	# Destroy the constraint.
	pm.delete(kill00, kill01, kill02)

	# Delete history on control.
	pm.delete(pad_02, pad_03, pad_04, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_01, root_joint)
	pm.orientConstraint(control_icon_02, second_joint)
	pm.orientConstraint(control_icon_03, third_joint)

def priming():
	'''
	import Rigging_Tools
	reload(Rigging_Tools)
	Rigging_Tools.priming()
	
	'''

	# Get selected.
	selected = pm.ls(selection=True, dag=True)
	
	# Print 'Joints Selected:', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control.
		# Normal set to x and radius.
		control_icon = pm.circle(normal=[1,0,0], radius=2, name=control_icon_name)[0]

		# Group control (Not empty).
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created', local_pad

		# Move group to taget joint.
		# Delete constraint.

		kill = pm.parentConstraint(target_joint, local_pad)
		pm.delete(kill)

		# Orient constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)

		print 'Local Oriented Controls Created.'


	pm.delete(local_pad)

def padding_tool():
	'''
	import Rigging_Tools
	reload(Rigging_Tools)
	Rigging_Tools.padding_tool()
	
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group.
	# Empty=True will create an empty group.
	pad = pm.group(empty=True)


	# Move group to joint, and delete constraint.
	kill = pm.pointConstraint(root_joint, pad)
	pm.delete(kill)
	
	# Freeze transforms.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group.
	pm.parent(root_joint, pad)

	# Renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created'