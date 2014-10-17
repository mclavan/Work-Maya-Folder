'''
Huston Petty
pettyHuston_riggingTools_cri1_1408.py

Description:
	Various rigging tools.

How to Run:
	import pettyHuston_riggingTools_cri1_1408 as hp 
	reload(hp)

'''

print 'Welcome to Skynet'

import pymel.core as pm

#------------REQUIRED------------

def hierarchy():
	'''
	How to run:
		hp.hierarchy()

		- Select root joint of desired joint chain

	'''

	# Get selected 
	selected_joints = pm.ls(dag=True, selection=True)
	root_joint = selected_joints[0]
	joint2 = selected_joints[1]
	joint3 = selected_joints[2]

	'''
	Padding

	'''
	# Create an empty group
	root_pad = pm.group(em=True)

	# Local orient empty group to root joint and delete constraint
	temp_pad_constraint = pm.parentConstraint(root_joint, root_pad)
	pm.delete(temp_pad_constraint)

	# Freeze Transforms
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint under empty group
	pm.parent(root_joint, root_pad)

	# Rename
	pad_name = root_joint.replace("01_bind", "00_pad")
	root_pad.rename(pad_name)


	'''
	Local Controls

	'''
	#---------------------------Control 1-----------------------------
	
	# Create icon
	control_icon1 = pm.circle(normal=[1, 0, 0], radius=2)[0]
	
	# Create icon pad
	local_pad1 = pm.group(control_icon1)

	# Delete History
	pm.delete(control_icon1, ch=True)

	# Rename
	control_name = root_joint.replace("_bind", "_icon")
	local_name = root_joint.replace("_bind", "_local")
	control_icon1.rename(control_name)
	local_pad1.rename(local_name)

	# Local orient to joint and delete constraint
	temp_constraint = pm.parentConstraint(root_joint, local_pad1, mo=False)
	pm.delete(temp_constraint)

	# Constrain joint to icon
	pm.orientConstraint(control_icon1, root_joint, mo=True)

	#---------------------------Control 2-----------------------------
	
	# Create icon
	control_icon2 = pm.circle(normal=[1, 0, 0], radius=2)[0]
	
	# Create icon pad and parent to previous icon
	local_pad2 = pm.group(control_icon2)
	pm.parent(local_pad2, control_icon1)

	# Delete History
	pm.delete(control_icon2, ch=True)

	# Rename
	control_name = joint2.replace("_bind", "_icon")
	local_name = joint2.replace("_bind", "_local")
	control_icon2.rename(control_name)
	local_pad2.rename(local_name)

	# Local orient to joint and delete constraint
	temp_constraint = pm.parentConstraint(joint2, local_pad2, mo=False)
	pm.delete(temp_constraint)

	# Constrain joint to icon
	pm.orientConstraint(control_icon2, joint2, mo=True)

	#---------------------------Control 3-----------------------------
	
	# Create icon
	control_icon3 = pm.circle(normal=[1, 0, 0], radius=2)[0]
	
	# Create icon pad and parent to previous icon
	local_pad3 = pm.group(control_icon3)
	pm.parent(local_pad3, control_icon2)

	# Delete History
	pm.delete(control_icon3, ch=True)

	# Rename
	control_name = joint3.replace("_bind", "_icon")
	local_name = joint3.replace("_bind", "_local")
	control_icon3.rename(control_name)
	local_pad3.rename(local_name)

	# Local orient to joint and delete constraint
	temp_constraint = pm.parentConstraint(joint3, local_pad3, mo=False)
	pm.delete(temp_constraint)

	# Constrain joint to icon
	pm.orientConstraint(control_icon3, joint3, mo=True)

def hierarchy_loop():
	'''
	How to run:
		hp.hierarchy_loop()

		- Select root joint of desired joint chain

	'''

	# Get selected 
	selected_joints = pm.ls(dag=True, selection=True)
	root_joint = selected_joints[0]
	selected_joints.pop(-1)

	'''
	Padding

	'''

	# create empty group

	root_pad = pm.group(em=True)

	# snap to joint
	temp_pad_constraint = pm.parentConstraint(root_joint, root_pad)
	pm.delete(temp_pad_constraint)

	# Freeze transforms
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint under pad
	pm.parent(root_joint, root_pad)

	# Rename
	pad_name = root_joint.replace('01_bind', '00_pad')
	root_pad.rename(pad_name)

	'''
	Local Controls

	'''

	last_item = ''

	for indiv_joint in selected_joints:
		# Create an icon
		control_icon = pm.circle(normal=[1, 0, 0], radius=2)[0]
		# Group icon
		local_pad = pm.group(control_icon)

		# Parent local pad to previous loop's icon if there is one
		if last_item != '':
			pm.parent(local_pad, last_item)

		last_item = control_icon

		# Delete History on Icon
		pm.delete(control_icon, ch=True)

		# Renaming
		control_name = indiv_joint.replace("_bind", "_icon")
		local_name = indiv_joint.replace("_bind", "_local")
		control_icon.rename(control_name)
		local_pad.rename(local_name)


		# Move control to icon
		temp_constraint = pm.parentConstraint(indiv_joint, local_pad, mo=False)
		pm.delete(temp_constraint)

		# Orient Constraint
		pm.orientConstraint(control_icon, indiv_joint, mo=True)

def priming():
	'''
	How to run:
		hp.priming()

		- Select root joint of desired joint chain

	'''

	# Get bind joints of chain
	selected_joints = pm.ls(sl=True, dag=True)
	selected_joints.pop(-1)

	last_item = ''

	for indiv_joint in selected_joints:
		# Create Icon
		circle_icon = pm.circle(nr=[1, 0, 0], r=1.5)[0]
		
		# Group Icon in sdk group
		sdk_grp = pm.group(circle_icon)
		
		# Group sdk group in local group
		local_pad = pm.group(sdk_grp)
		
		# Parent local group to previous loop's Icon
		if last_item != '':
			pm.parent(local_pad, last_item)
		
		# Making current loop's icon able to be parented
		last_item = circle_icon

		# Local Snap to joint and delete constraint
		temp_constraint = pm.parentConstraint(indiv_joint, local_pad)
		pm.delete(temp_constraint)

		# Constrain joint to icon
		pm.orientConstraint(circle_icon, indiv_joint)

		# Rename
		icon_name = indiv_joint.replace("_bind", "_icon")
		circle_icon.rename(icon_name)
		sdk_name = indiv_joint.replace("_bind", "_sdk")
		sdk_grp.rename(sdk_name)
		local_name = indiv_joint.replace("_bind", "_local")
		local_pad.rename(local_name)

def padding():
	'''
	How to run:
		hp.padding()

		- Select root joint of desired joint chain

	'''

	# Get selected root
	joint_system = pm.ls(sl=True, dag=True)
	root_joint = joint_system[0]

	# Create empty group
	root_pad = pm.group(em=True)

	# Local Orient to root joint and delete constraint
	temp_pad_constraint = pm.parentConstraint(root_joint, root_pad)
	pm.delete(temp_pad_constraint)

	# Freeze Transforms
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint under empty group
	pm.parent(root_joint, root_pad)

	# Rename
	pad_name = root_joint.replace("01_bind", "00_pad")
	root_pad.rename(pad_name)

def joint_renamer():
	'''
	How to run:
		hp.joint_renamer()

		- Select root joint of desired joint chain

	'''

	# Get Selected
	joint_system = pm.ls(dag=True, selection=True)
	
	# Define Naming conventions
	name_request = pm.promptDialog(
		t='Rename Joint Chain', 
		m='Enter New Name', 
		ma='left',
		tx='Ex: orientation_partName',
		st='text', 
		b=['Ok', 'Cancel'], 
		db='Ok', 
		cb='Cancel',
		ds='Cancel',
		bgc=[.6, .6, .6])
	if name_request == 'Ok':
		global name
		name = pm.promptDialog(query=True, text=True)

		count = 1
		suffix = 'bind'

		for indiv_joint in joint_system:
			new_name = '{0}_{1:02d}_{2}'.format(name, count, suffix)

			indiv_joint.rename(new_name)

			count = count + 1


		new_name = '{0}_{1:02d}_{2}'.format(name, count-1, 'waste')
		indiv_joint.rename(new_name)

		print 'Joints Renamed Successfully'
	else:
		print 'Canceled; Joints Not Named'

#------------EXTRA---------------

def icon_renamer():
	'''
	How to run:
		hp.icon_renamer()

		- Select desired icons in desired counting order (01, 02, 03, etc.)
		- ONLY SELECT FOR SINGLE SYSTEM (lt_arm, ct_back, rt_leg, etc.) 

	'''

	# Get Selected
	selected_icons = pm.ls(selection=True)
	
	# Define Naming conventions
	name_request = pm.promptDialog(
		t='Rename Icons', 
		m='Enter New Name', 
		ma='left',
		tx='Ex: orientation_partName',
		st='text', 
		b=['Ok', 'Cancel'], 
		db='Ok', 
		cb='Cancel',
		ds='Cancel',
		bgc=[.6, .6, .6])
	if name_request == 'Ok':
		global name
		name = pm.promptDialog(query=True, text=True)

		count = 1
		suffix = 'icon'

		for indiv_icon in selected_icons:
			new_name = '{0}_{1:02d}_{2}'.format(name, count, suffix)

			indiv_icon.rename(new_name)

			count = count + 1

		print 'Icons Renamed Successfully'
	else:
		print 'Canceled; Icons Not Named'

def icon_color_all():
	'''
		How To Run:
			hp.icon_color_indiv()

			- Colors all icons in scene without need of selection
			- ONLY WORKS IF ICONS ARE NAMED PROPERLY  

	'''

	# Get different icon orientation groups
	left_side = pm.ls('lt_*_icon')
	right_side = pm.ls('rt_*_icon')
	center_side = pm.ls('ct_*_icon')
	advBack = pm.ls('advBack_*_icon')

	# Define color values
	blue = 6
	red = 13
	yellow = 17
	light_blue = 18

	#-----------------Left Side Loop---------------
	for left_icon in left_side:
		left_icon.overrideEnabled.set(1)
		left_icon.overrideColor.set(blue)

	#-----------------Right Side Loop---------------

	for right_icon in right_side:
		right_icon.overrideEnabled.set(1)
		right_icon.overrideColor.set(red)

	#-----------------Center Loop---------------

	for center_icon in center_side:
		center_icon.overrideEnabled.set(1)
		center_icon.overrideColor.set(yellow)

	#-----------------Advanced Back Loop---------------

	for adv_icon in advBack:
		adv_icon.overrideEnabled.set(1)
		adv_icon.overrideColor.set(light_blue)

	print 'All Icons Colored'

def icon_color_indiv():
	'''
		How To Run:
			hp.icon_color_indiv()

			- Selected desired icons and run
			- ONLY WORKS IF ICONS ARE NAMED PROPERLY  

	'''
	
	selected_icons = pm.ls(sl=True)
	print selected_icons

	blue = 6
	red = 13
	yellow = 17
	light_blue = 18

	for each in selected_icons:
		if 'lt' in str(each):
			print 'this is a left icon'
			each.overrideEnabled.set(1)
			each.overrideColor.set(blue)
		elif 'rt' in str(each):
			print 'this is a right icon'
			each.overrideEnabled.set(1)
			each.overrideColor.set(red)
		elif 'ct' in str(each):
			print 'this is a center icon'
			each.overrideEnabled.set(1)
			each.overrideColor.set(yellow)
		elif 'advBack' in str(each):
			print 'this is an advBack icon'
			each.overrideEnabled.set(1)
			each.overrideColor.set(light_blue)

	print 'Icon(s) Colored Successfully'

def padding_all_roots():
	'''
	How to run:
		hp.padding_all_roots()

		- Needs no selectionn just run
		- DO NOT USE IF SCENE CONTAINS ANY ALREADY PADDED SYSTEMS

	'''

	# Get all root joints
	selected_roots = pm.ls('*01_bind')
	print selected_roots

	for indiv_root in selected_roots:
		# Create empty group
		root_pad = pm.group(em=True)

		# Local Orient to root joint and delete constraint
		temp_pad_constraint = pm.parentConstraint(indiv_root, root_pad)
		pm.delete(temp_pad_constraint)

		# Freeze Transforms
		pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

		# Parent root joint under empty group
		pm.parent(indiv_root, root_pad)

		# Rename
		pad_name = indiv_root.replace("01_bind", "00_pad")
		root_pad.rename(pad_name)

	print 'All Joints Systems Padded'

def lock_and_hide_trans():
	'''
	How to run:
		hp.lock_and_hide_trans()

		- Select control icons and run

	'''

	# Get Selected
	selected = pm.ls(sl=True)
	print 'Selected Controls: {0}'.format(selected)

	for each in selected:
		# Lock and Hide
		each.tx.set(lock=True, keyable=False)
		each.ty.set(lock=True, keyable=False)
		each.tz.set(lock=True, keyable=False)
		each.sx.set(lock=True, keyable=False)
		each.sy.set(lock=True, keyable=False)
		each.sz.set(lock=True, keyable=False)
		each.v.set(lock=True, keyable=False)

	print 'Channels Locked and Hidden Successfully'

def lock_and_hide_rotate():
	'''
	How to run:
		hp.lock_and_hide_rotate()

		- Select control icons and run

	'''

	# Get Selected
	selected = pm.ls(sl=True)
	print 'Selected Controls: {0}'.format(selected)

	for each in selected:
		# Lock and Hide
		each.rx.set(lock=True, keyable=False)
		each.ry.set(lock=True, keyable=False)
		each.rz.set(lock=True, keyable=False)
		each.sx.set(lock=True, keyable=False)
		each.sy.set(lock=True, keyable=False)
		each.sz.set(lock=True, keyable=False)
		each.v.set(lock=True, keyable=False)

	print 'Channels Locked and Hidden Successfully'

def unlock_and_show_vis():
	'''
	How to run:
		hp.unlock_and_show_vis()

		- Select control icons and run

	'''

	# Get selected
	selected = pm.ls(sl=True)
	print 'Selected Controls: {0}'.format(selected)

	for each in selected:
	# Unlock and show
		each.v.set(lock=False, keyable=True)
	
	print 'Channels Unlocked and Shown Successfully'

def unlock_and_show_default():
	'''
	How to run:
		hp.unlock_and_show_default()

		- Select a control icon and run

	'''

	# Get selected
	selected = pm.ls(sl=True)
	print 'Selected Controls: {0}'.format(selected)

	for each in selected:
		# Unlock and show
		each.tx.set(lock=False, keyable=True)
		each.ty.set(lock=False, keyable=True)
		each.tz.set(lock=False, keyable=True)
		each.rx.set(lock=False, keyable=True)
		each.ry.set(lock=False, keyable=True)
		each.rz.set(lock=False, keyable=True)
		each.sx.set(lock=False, keyable=True)
		each.sy.set(lock=False, keyable=True)
		each.sz.set(lock=False, keyable=True)
		each.v.set(lock=False, keyable=True)
		

	print 'Channels Unlocked and Shown Successfully'

def unlock_and_show_all():
	'''
	How To Run:
		hp.unlock_and_show_all()

		-Unlocks and shows all attributes for all icons in a scene, when named properly

	'''
	# Get all icons in scene
	all_icons = pm.ls('*_icon')

	for each in all_icons:
		# Unlock and show
		each.tx.set(lock=False, keyable=True)
		each.ty.set(lock=False, keyable=True)
		each.tz.set(lock=False, keyable=True)
		each.rx.set(lock=False, keyable=True)
		each.ry.set(lock=False, keyable=True)
		each.rz.set(lock=False, keyable=True)
		each.sx.set(lock=False, keyable=True)
		each.sy.set(lock=False, keyable=True)
		each.sz.set(lock=False, keyable=True)
		each.v.set(lock=False, keyable=True)

	print 'All Channels For All Icons Unlocked and Show Successfully'


			















	






	
