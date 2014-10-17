'''
Luisa Reyes
reyesLuisa_riggingTools_cri1_1405.py

Description:
	Grouping of rigging tools.

How to Run:

import reyesLuisa_riggingTools_cri1_1405
reload(reyesLuisa_riggingTools_cri1_1405)

'''

import pymel.core as pm

print 'Rigging Tools Active.'

def hierarchy():
	'''
	Create a hierarchy based upon a given system.

	Select the root joint and execute this function.

	import reyesLuisa_riggingTools_cri1_1405
	reload (reyesLuisa_riggingTools_cri1_1405)
	reyesLuisa_riggingTools_cri1_1405.hierarchy()

	'''

	import pymel.core as pm

	print 'Heirarchy Generated'


	# The user will select the root joint and the tool
	#	will apply the systems.

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_Joint = 'lt_middle_03_bind'

	'''
	# Pad the root joint.
	'''

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

	'''
	first control
	'''

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
	kenny = pm.parentConstraint(root_joint, control_icon_1)


	# Destroy the constraint
	pm.delete(kenny)

	# Deleter History on control
	pm.delete(control_icon_1, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_1, root_joint)




	'''
	Second control
	'''

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
	cloud = pm.parentConstraint(second_joint, control_icon_2)


	# Destroy the constraint
	pm.delete(cloud)

	# Deleter History on control
	pm.delete(control_icon_2, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_2, second_joint)





	'''
	third control
	'''

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
	humans = pm.parentConstraint(third_Joint, control_icon_3)


	# Destroy the constraint
	pm.delete(humans)

	# Deleter History on control
	pm.delete(control_icon_3, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_3, third_Joint)

	''' Process Parent'''

	pm.parent(Group_02, control_icon_1)
	pm.parent(Group_03, control_icon_2)


def padding_tool():
	'''
	How to Run:
	import reyesLuisa_riggingTools_cri1_1405
	reload (reyesLuisa_riggingTools_cri1_1405)
	reyesLuisa_riggingTools_cri1_1405.padding_tool()
	'''


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

	print 'Padding group created'


def joint_renamer():
	'''
	import reyesLuisa_riggingTools_cri1_1405
	reload (reyesLuisa_riggingTools_cri1_1405)
	reyesLuisa_riggingTools_cri1_1405.joint_renamer()
	'''

	# Create a function called joint_rename
	# Select the root joint and loop through all joints in
	# the joint chain.
	# 'ori_name_count_suffix'
	#'ct_back_01_bind' 

	'''
	# Select the root joint and loop through all joints in
	# the joint chain.
	# 'ori_name_count_suffix'
	#'ct_back_01_bind' 

	import book
	book.joint_rename()
	'''

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
	'''
	Description: Creates control with local pad of the joint.

	How to Run:
	import reyesLuisa_riggingTools_cri1_1405
	reload (reyesLuisa_riggingTools_cri1_1405)
	reyesLuisa_riggingTools_cri1_1405.priming_tool()
	'''

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


def Lock_Hide_Attr():
	'''
	import reyesLuisa_riggingTools_cri1_1405
	reload (reyesLuisa_riggingTools_cri1_1405)
	reyesLuisa_riggingTools_cri1_1405.Lock_Hide_Attr()
	'''
	selected = pm.ls(selection=True)
	print 'Current Selected:', selected

	for current_item in selected:
		current_item.tx.set(lock=True, keyable=False)
		current_item.ty.set(lock=True, keyable=False)
		current_item.tz.set(lock=True, keyable=False)
		current_item.rx.set(lock=True, keyable=False)
		current_item.ry.set(lock=True, keyable=False)
		current_item.rz.set(lock=True, keyable=False)
		current_item.sx.set(lock=True, keyable=False)
		current_item.sy.set(lock=True, keyable=False)
		current_item.sz.set(lock=True, keyable=False)
		current_item.v.set(lock=True, keyable=False)

	print 'Attributes Locked and Hidden'


def Unlock_Show_Attr():
	'''
	import reyesLuisa_riggingTools_cri1_1405
	reload (reyesLuisa_riggingTools_cri1_1405)
	reyesLuisa_riggingTools_cri1_1405.Unlock_Show_Attr()
	'''
	selected = pm.ls(selection=True)
	print 'Current Selected:', selected

	for current_item in selected:
		current_item.tx.set(lock=False, keyable=True)
		current_item.ty.set(lock=False, keyable=True)



		current_item.tz.set(lock=False, keyable=True)
		current_item.rx.set(lock=False, keyable=True)
		current_item.ry.set(lock=False, keyable=True)
		current_item.rz.set(lock=False, keyable=True)
		current_item.sx.set(lock=False, keyable=True)
		current_item.sy.set(lock=False, keyable=True)
		current_item.sz.set(lock=False, keyable=True)
		current_item.v.set(lock=False, keyable=True)

	print 'Attributes Unlocked and Unhidden'


def Add_Attributes():
	'''
	import reyesLuisa_riggingTools_cri1_1405
	reload(reyesLuisa_riggingTools_cri1_1405)
	reyesLuisa_riggingTools_cri1_1405.Add_Attributes()
	'''
	selected = pm.ls(selection=True)
	print 'Current Selected:', selected

	first_selected = selected[0]
	first_selected.addAttr('FINGERS',
	    at='enum', en='----------:', keyable=True)
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('CURL',
	    at='enum', en='----------:', keyable=True)
	first_selected.CURL.set(lock=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)
	first_selected.addAttr('SPREAD',
	    at='enum', en='----------:', keyable=True)
	first_selected.SPREAD.set(lock=True)
	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)
	first_selected.addAttr('THUMB',
	    at='enum', en='----------:', keyable=True)
	first_selected.THUMB.set(lock=True)
	first_selected.addAttr('thumb_curl', keyable=True)
	first_selected.addAttr('thumb_drop', keyable=True)

	print 'Attrubutes Added'
