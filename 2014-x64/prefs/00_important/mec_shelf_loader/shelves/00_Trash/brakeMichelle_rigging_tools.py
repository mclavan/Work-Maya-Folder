'''
Michelle Brake
brakeMichelle_rigging_tools.py

Description:
Script containing necessary requirements for Project 4 - Rigging Tools.

How to run:
import brakeMichelle_rigging_tools
reload(brakeMichelle_rigging_tools)
'''

import pymel.core as pm

def hierarchy():
	'''
	How to run:
	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.hierarchy()
	'''
	print 'Hierarchy Generated'

	# The user will select the root joint and the tool will apply the systems.
	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	Pad the root joint.
	'''
	# Create an empty group.
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	# Move group to root joint.
	# Point constrain group to root joint.
	# 	offset off (Snapping)
	kenny = pm.parentConstraint(root_joint, pad)

	# Delete constraint
	pm.delete(kenny)
	print 'Oh, my God!  You killed Kenny!'
	print 'You bastards!!'

	# Freeze transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint, pad)

	'''
	Create a local oriented control for each joint
	lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind
	'''
	'''
	root_joint
	'''
	# Create control (circle)
	control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# 	This will automatically parent the control under the group.
	group1 = pm.group(empty=False, name='lt_middle_01_local')

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	# 	Where driven is the pad.
	# 	Offset is off (Snapping)
	kenny = pm.parentConstraint(root_joint, group1)

	# Destroy the constraint
	pm.delete(kenny)
	print 'Oh, my God!  You killed Kenny!'
	print 'You bastards!!'

	# Delete history on control
	pm.delete(control_icon_1, ch=True)
	pm.makeIdentity(control_icon_1, apply=True, t=1, r=1, s=1, n=0)

	# Orient constraint driver:  control driven:  joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	second_joint
	'''
	# Create control (circle)
	control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# 	This will automatically parent the control under the group.
	group2 = pm.group(empty=False, name='lt_middle_02_local')

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	# 	Where driven is the pad.
	# 	Offset is off (Snapping)
	kenny = pm.parentConstraint(second_joint, group2)

	# Destroy the constraint
	pm.delete(kenny)
	print 'Oh, my God!  You killed Kenny!'
	print 'You bastards!!'

	# Delete history on control
	pm.delete(control_icon_2, ch=True)
	pm.makeIdentity(control_icon_2, apply=True, t=1, r=1, s=1, n=0)

	# Orient constraint driver:  control driven:  joint
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	third_joint
	'''
	# Create control (circle)
	control_icon_3 = pm.circle(name='lt_middle_03_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# 	This will automatically parent the control under the group.
	group3 = pm.group(empty=False, name='lt_middle_03_local')

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	# 	Where driven is the pad.
	# 	Offset is off (Snapping)
	kenny = pm.parentConstraint(third_joint, group3)

	# Destroy the constraint
	pm.delete(kenny)
	print 'Oh, my God!  You killed Kenny!'
	print 'You bastards!!'

	# Delete history on control
	pm.delete(control_icon_3, ch=True)
	pm.makeIdentity(control_icon_3, apply=True, t=1, r=1, s=1, n=0)

	# Orient constraint driver:  control driven:  joint
	pm.orientConstraint(control_icon_3, third_joint)

	# Parent icon to local
	pm.parent(group2, control_icon_1)
	pm.parent(group3, control_icon_2)

	#Create a holding group to house the pads and controls
	middle_group = pm.group(empty=True, name='lt_middle_group')

	# Parent the pads and the controls under the main group
	# 	Make sure that they are not parented together
	pm.parent(pad, control1_pad, middle_grp)

def joint_rename():
	'''
	Select the root joint and loop through all the joint in the joint chain
	'ori_name_count_suffix'
	'ct_back_01_bind'

	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.joint_rename()
	'''
	# What am I working on?
	# Get all joints in a selected joint chain
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Joint Chain:', joint_chain

	# Build our new name
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
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)

	print 'Joint Chain Renamed'

def padding():
	'''
	The user is going to select the root joint.
	The tool will pad all joints in the chain.

	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.padding()
	'''

	# Get selected
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create pad group
	pad = pm.group(empty=True)

	# Create point constraint
	kenny = pm.pointConstraint(root_joint, pad)

	# Destroy the constraint
	pm.delete(kenny)
	print 'Oh, my God!  You killed Kenny!'
	print 'You bastards!!'

	# Freeze transformations
	pm.makeIdentity(pad, a=True, t=1, s=1, r=1, n=0)

	# Put joint into pad group
	pm.parent(root_joint, pad)

	# Rename pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Joint Padded'

def priming():
	'''
	The user is going to select the root joint.
	The tool will add a locally-oriented control for each joint in the chain.

	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.priming()
	'''

	# Get seleted
	selected = pm.ls(selection=True)

	for current_joint in selected:
		control_icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create control circle
		control_icon = pm.circle(normal=[1, 0, 0], radius=1, name=control_icon_name)[0]
		print 'Control Icon:', control_icon

		# Control group (not empty)
		local_pad = pm.group(name=local_pad_name)
		print 'Pad Created:', local_pad

		# Parent constraint group to joint
		kenny = pm.parentConstraint(current_joint, local_pad)

		# Destroy the constraint
		pm.delete(kenny)
		print 'Oh, my God!  You killed Kenny!'
		print 'You bastards!!'

		# Orient constraint control to joint
		pm.orientConstraint(control_icon, current_joint)

	print 'Joint Primed'

def lock_hide_tsv():
	'''
	An object will be selected and lock and hide the translate, scale, and visible values from the channel box.

	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.lock_hide_tsv()
	'''

	#Call up selected
	selected = pm.ls(selection=True)

	for icon in selected:
		# Lock and hide translate X
		icon.tx.set(lock=True,keyable=False)

		# Lock and hide translate Y
		icon.ty.set(lock=True,keyable=False)

		# Lock and hide translate Z
		icon.tz.set(lock=True,keyable=False)

		# Lock and hide scale X
		icon.sx.set(lock=True,keyable=False)

		# Lock and hide scale Y
		icon.sy.set(lock=True,keyable=False)

		# Lock and hide scale Z
		icon.sz.set(lock=True,keyable=False)

		# Lock and hide visibility
		icon.v.set(lock=True,keyable=False)

	print 'Translates, scales, and visibility have been locked and hidden.'

def lock_hide_rsv():
	'''
	An object will be selected and lock and hide the rotate, scale, and visible values from the channel box.

	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.lock_hide_rsv()
	'''

	# Call up selected
	selected = pm.ls(selection=True)

	for icon in selected:
		# Lock and hide rotate X
		icon.rx.set(lock=True,keyable=False)

		# Lock and hide rotate Y
		icon.ry.set(lock=True,keyable=False)

		# Lock and hide rotate Z
		icon.rz.set(lock=True,keyable=False)

		# Lock and hide scale X
		icon.sx.set(lock=True,keyable=False)

		# Lock and hide scale Y
		icon.sy.set(lock=True,keyable=False)

		# Lock and hide scale Z
		icon.sz.set(lock=True,keyable=False)

		# Lock and hide visibility
		icon.v.set(lock=True,keyable=False)

	print 'Rotates, scales, and visibility have been locked and hidden.'

def unlock_show_trsv():
	'''
	An object will be selected and unlock and show the translate, rotate, scale, and visible values that have been hidden from the channel box.

	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.unlock_show_trsv()
	'''

	# Call up selected
	selected = pm.ls(selection=True)

	for icon in selected:
		# Unlock and show translate X
		icon.tx.set(lock=False,keyable=True)

		# Unlock and show translate Y
		icon.ty.set(lock=False,keyable=True)

		# Unlock and show translate Z
		icon.tz.set(lock=False,keyable=True)

		# Unlock and show rotate X
		icon.rx.set(lock=False,keyable=True)

		# Unlock and show rotate Y
		icon.ry.set(lock=False,keyable=True)

		# Unlock and show rotate Z
		icon.rz.set(lock=False,keyable=True)

		# Unlock and show scale X
		icon.sx.set(lock=False,keyable=True)

		# Unlock and show scale Y
		icon.sy.set(lock=False,keyable=True)

		# Unlock and show scale Z
		icon.sz.set(lock=False,keyable=True)

		# Unlock and show visibility
		icon.v.set(lock=False,keyable=True)

	print 'Translates, rotates, scales, and visibility have been unlocked and are shown.'

def create_attribute():
	'''
	User will select an icon and attributes for index curl, middle curl, and pinky curl will be created.

	import brakeMichelle_rigging_tools
	brakeMichelle_rigging_tools.create_attribute()
	'''

	# Call up selected
	selected = pm.ls(selection=True)
	print 'Current selected:', selected

	first_selected = selected[0]

	# Create a locked attribute to act as a header for the fingers
	first_selected.addAttr('FINGERS', at='enum', en='----------', keyable=True)
	first_selected.FINGERS.set(lock=True)

	# Create a locked attribute to act as a header for the curl
	first_selected.addAttr('CURL', at='enum', en='----------', keyable=True)
	first_selected.CURL.set(lock=True)

	# Create attribute for index curl
	first_selected.addAttr('index_curl', keyable=True)

	# Create attribute for middle curl
	first_selected.addAttr('middle_curl', keyable=True)

	# Create attribute for pinky curl
	first_selected.addAttr('pinky_curl', keyable=True)

	# Create a locked attribute to act as a header for the spread
	first_selected.addAttr('SPREAD', at='enum', en='----------', keyable=True)
	first_selected.SPREAD.set(lock=True)

	# Create attribute for index spread
	first_selected.addAttr('index_spread', keyable=True)

	# Create attribute for middle spread
	first_selected.addAttr('middle_spread', keyable=True)

	# Create attribute for pinky spread
	first_selected.addAttr('pinky_spread', keyable=True)

	# Create a locked attribute to act as a header for the thumb
	first_selected.addAttr('THUMB', at='enum', en='----------', keyable=True)
	first_selected.THUMB.set(lock=True)

	# Create attribute for thumb spread
	first_selected.addAttr('thumb_spread', keyable=True)

	# Create attribute for thumb drop
	first_selected.addAttr('thumb_drop', keyable=True)
