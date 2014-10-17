'''
rigging_tools.py
Miqueas Proctor

Description:
	Grouping of rigging tools.

	How to Run:

	import proctorMiqueas_riggingTools_cri1_1405
	reload(proctorMiqueas_riggingTools_cri1_1405)

	'''

import pymel.core as pm

print 'rigging Tools Active'

def hierarchy():
	'''
	Miqueas Proctor
	hierarchy.py

	Description:

	How to Run:
	import proctorMiqueas_riggingTools_cri1_1405
	reload(proctorMiqueas_riggingTools_cri1_1405)
	proctorMiqueas_riggingTools_cri1_1405.hierarchy()
	'''

	import pymel.core as pm

	print 'Hirtatchy Generated'

	# The user will selecte the root joint and the tool
	#	will apply the systems.


	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# pad the root joint
	'''

	# create an empty group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	# move group to root joint
	#point constraint group to root joint
	#	offset off (snapping)
	tempConstraint = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(tempConstraint)

	# Freeze transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# parent root joint to group
	pm.parent(root_joint, pad)


	# create a local oriented control for each joint.
	# lt_middle_01_bind, lt_middle_02_bind, lt_middle_03_bind

	'''
	control 1
	'''

	# Create control (circle)
	control_icon_1 = pm.circle(name = 'lt_middle_01_icon',
			normal = [90,0,0])[0]

	# Create group( Not Empty)
	# This will automaticly parent the control under
	#	the group.
	local1 = pm.group(control_icon_1, name = 'lt_middle_01_local')

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	#	where is the group.
	# offset is off (sanpping)
	tempConstraint = pm.parentConstraint(root_joint, local1)

	# Destroy the constraint
	pm.delete(tempConstraint)

	# Delete Histroy on control
	pm.delete(control_icon_1, ch=True)

	# Orinet Constraint diver: joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	control 2
	'''

	# Create control (circle)
	control_icon_2 = pm.circle(name = 'lt_middle_02_icon',
			normal = [90,0,0])[0]

	# Create group( Not Empty)
	# This will automaticly parent the control under
	#	the group.
	local2 = pm.group(control_icon_2, name = 'lt_middle_02_local')

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	#	where is the group.
	# offset is off (sanpping)
	tempConstraint = pm.parentConstraint(second_joint, local2)

	# Destroy the constraint
	pm.delete(tempConstraint)

	# Delete Histroy on control
	pm.delete(control_icon_2, ch=True)

	# Orinet Constraint diver: joint.
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	control 3
	'''

	# Create control (circle)
	control_icon_3 = pm.circle(name = 'lt_middle_03_icon',
			normal = [90,0,0])[0]

	# Create group( Not Empty)
	# This will automaticly parent the control under
	#	the group.
	local3 = pm.group(control_icon_3, name = 'lt_middle_03_local')

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	#	where is the group.
	# offset is off (sanpping)
	tempConstraint = pm.parentConstraint(third_joint, local3)

	# Destroy the constraint
	pm.delete(tempConstraint)

	# Delete Histroy on control
	pm.delete(control_icon_3, ch=True)

	# Orinet Constraint diver: joint.
	pm.orientConstraint(control_icon_3, third_joint)

	'''
	parenting
	'''

	#parent middle_03_local pad to middle_02_icon
	pm.parent(local3, control_icon_2)

	#parent middle_02_local pad to middle_01_icon
	pm.parent(local2, control_icon_1)

	#group middle pad and middle local
	pm.group(pad, local1, name= 'middle')


def padding_tool():
	'''

	import proctorMiqueas_riggingTools_cri1_1405
	reload(proctorMiqueas_riggingTools_cri1_1405)
	proctorMiqueas_riggingTools_cri1_1405.padding_tool()
	'''

	selected = pm.ls(selection=True)
	#print 'current selected:', selected
	root_joint = selected[0]

	#create empty group
	# empty=True will create a empty group
	pad = pm.group(empty=True)

	# move group to joint
	#	and delete constraint
	tempConstraint = pm.pointConstraint(root_joint, pad)
	pm.delete(tempConstraint)

	# freeze Transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)


	# parent joint to group
	pm.parent(root_joint, pad)

	#renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'padding group created'


def priming_tool():
	'''
	import proctorMiqueas_riggingTools_cri1_1405
	reload(proctorMiqueas_riggingTools_cri1_1405)
	proctorMiqueas_riggingTools_cri1_1405.priming_tool()
	'''


	# Get selected
	selected = pm.ls(selection=True)
	# print 'joints selected:', selected
	#
	target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# group control (Not an epmrty group)
		local_pad = pm.group(name=local_pad_name)

		print 'control icon:', control_icon
		print 'pad created:', local_pad

		# move group to target joint.
		#	and delete constraint
		tempConstraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(tempConstraint)

		# orient constraint joint to control
		pm.orientConstraint(control_icon, target_joint)




	print 'local oriented controls created'


def joint_rename():
	'''
	# select the root joint and loop through all joints
	#	the joint chain.
	# 'ori_name_count_suffix'
	# 'ct_back_01_bind'

	import proctorMiqueas_riggingTools_cri1_1405
	reload(proctorMiqueas_riggingTools_cri1_1405)
	proctorMiqueas_riggingTools_cri1_1405.joint_rename()
	'''

	# What am I working on?
	# Get all in a selected joint chain
	joint_chain = pm.ls(selection = True, dag=True)
	print 'Items selected:', joint_chain



	# build our new name.
	# 'lt'
	# 'arm'
	# 01
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

		
	print 'Joint Chain Rename'
