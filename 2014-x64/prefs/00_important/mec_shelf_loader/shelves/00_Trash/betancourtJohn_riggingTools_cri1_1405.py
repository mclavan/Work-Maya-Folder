'''
John Betancourt
betancourtJohn_riggingTools_cri1_1405.py




Description:
	Grouping of rigging tools.




How to Run:

import betancourtJohn_riggingTools_cri1_1405.py
reload(betancourtJohn_riggingTools_cri1_1405.py)

'''









import pymel.core as pm

print 'Rigging Tools Activatedd.'











def hierarchy():
	



	import pymel.core as pm

	print 'Heirarchy Generated'


	# The user will select the root joint and the tool
	#	will apply the systems.

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_Joint = 'lt_middle_03_bind'

	

	# Create an empty group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	# Move group to root joint.
	# Point Constraint group to root joint.
	#	offset off (Snapping)
	temp = pm.parentConstraint(root_joint, pad)

	# Delete constraint
	pm.delete(temp)

	# Freeze Transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group.
	pm.parent(root_joint, pad)


	# Create a local oriented control for each joint
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind

	

	# Create control (circle)
	control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1,0,0])[0]


	# Create group (NOT EMPTY)
	#	This will automatically parent the control under
	#	 the group.
	group_01 = pm.group(empty=False, name='lt_middle_01_local')


	# Move group to the target joint.
	# Use a parent constraint driver as the joint.
	#	Where driven is the group.
	#	Offset is off (Snapping)
	temp = pm.parentConstraint(root_joint, control_icon_1)


	# Destroy the constraint
	pm.delete(temp)

	# Deleter History on control
	pm.delete(control_icon_1, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_1, root_joint)




	

	# Create control (circle)
	control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1,0,0])[0]


	# Create group (NOT EMPTY)
	#	This will automatically parent the control under
	#	 the group.
	Group_02 = pm.group(empty=False, name='lt_middle_02_local')


	# Move group to the target joint.
	# Use a parent constraint driver as the joint.
	#	Where driven is the group.
	#	Offset is off (Snapping)
	temp = pm.parentConstraint(second_joint, control_icon_2)


	# Destroy the constraint
	pm.delete(temp)

	# Deleter History on control
	pm.delete(control_icon_2, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_2, second_joint)





	

	# Create control (circle)
	control_icon_3 = pm.circle(name='lt_middle_03_icon', normal=[1,0,0])[0]


	# Create group (NOT EMPTY)
	#	This will automatically parent the control under
	#	 the group.
	Group_03 = pm.group(empty=False, name='lt_middle_03_local')


	# Move group to the target joint.
	# Use a parent constraint driver as the joint.
	#	Where driven is the group.
	#	Offset is off (Snapping)
	temp = pm.parentConstraint(third_Joint, control_icon_3)


	# Destroy the constraint
	pm.delete(temp)

	# Deleter History on control
	pm.delete(control_icon_3, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_3, third_Joint)


	pm.parent(Group_02, control_icon_1)
	pm.parent(Group_03, control_icon_2)


def padding_tool():
	


	selected = pm.ls(selection=True)

	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty-True will create an empty group

	pad = pm.group(empty=True)

	# Move group to joint.
	#	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, s=1, r=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	#renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Pad group created'


def joint_renamer():
	

	# Create a function called joint_rename
	# Select the root joint and loop through all joints in
	# the joint chain.
	# 'ori_name_count_suffix'
	#'ct_back_01_bind' 


	# What am I working on?
	# Get all joints in a selected joint chain.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected:', joint_chain

	# Build our new name.
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

	print 'Joint Chain Renamed'


def priming_tool():
	

	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Orient Controls Created'


def lock_hide_attr():
	
	select = pm.ls(selection=True)
	print 'Current Selected', selected

	for current_item in selected:
		current_item.tx.set(lock=True, keyable=False)
		current_item.ty.set(lock=True, keyable=False)
		current_item.tz.set(lock=True, keyable=False)
    
		current_item.sx.set(lock=True, keyable=False)
		current_item.sy.set(lock=True, keyable=False)
		current_item.sz.set(lock=True, keyable=False)
    
		current_item.v.set(lock=True, keyable=False)

	print 'Attr Hidden and Locked'


def unlock_show_attr():
	
	select = pm.ls(selection=True)
	print 'Current Selected', selected

	for current_item in selected:
	    current_item.tx.set(lock=False, keyable=True)
	    current_item.ty.set(lock=False, keyable=True)
	    current_item.tz.set(lock=False, keyable=True)
	    
	    current_item.sx.set(lock=False, keyable=True)
	    current_item.sy.set(lock=False, keyable=True)
	    current_item.sz.set(lock=False, keyable=True)
	    
	    current_item.v.set(lock=False, keyable=True)

 	print 'Attr Hidden and Locked'




