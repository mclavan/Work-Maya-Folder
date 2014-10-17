'''

Mario Mediavilla

mediavilaMario_riggingTools_cri1_1408.py

Description:
	This script contrains a series of regging tools.


How to Run:

import mediavillaMario_riggingTools_cri1_1408
reload(mediavillaMario_riggingTools_cri1_1408)


'''


print 'Rigging Tools Active'

import pymel.core as pm


def hierarchy():
	'''

	Create a hierarchy based upon given system.

	Select root joint chain and execture function.

	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.hierarchy(); 

	'''

	joint_system = pm.ls(selection=True, dag=True)
	# print ' Joint System: ' , joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''

	Padding Root Joint

	'''

	# Create empty group.
	root_pad = pm.group(empty=True)

	# Move group over to the target joint.
	temp_constraint = pm.parentConstraint(root_joint,root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(root_pad,apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.
	pm.parent(root_joint,root_pad)

	'''
	Local Controls
	'''

	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal=[1,0,0], radius = 2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Crate a group
	# Grouping control during the process
	local_pad_1 = pm.group()


	# Output control and pad.
	print 'Control 1 Created: ', control_icon_1
	print 'Local Pad 1 Created: ', local_pad_1

	# Move group over to the target point.
	# Delete contrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Contrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)



	'''
	Control 2
	'''
	# Create a control.
	# normal=[1,0,0], radius = 2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Crate a group
	# Grouping control during the process
	local_pad_2 = pm.group()


	# Output control and pad.
	print 'Control 2 Created: ', control_icon_2
	print 'Local Pad 2 Created: ', local_pad_2

	# Move group over to the target point.
	# Delete contrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Contrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control.
	# normal=[1,0,0], radius = 2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Crate a group
	# Grouping control during the process
	local_pad_3 = pm.group()


	# Output control and pad.
	print 'Control 3 Created: ', control_icon_3
	print 'Local Pad 3 Created: ', local_pad_3

	# Move group over to the target point.
	# Delete contrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Contrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent controls
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3,control_icon_2)
	# Pad 2 (Last) -> control 1
	pm.parent(local_pad_2,control_icon_1)



	print ' Hierarchy Created'

def padding_tool():
	'''
	Create a pad system for the finger joints

	Select Root Joint to execute function

	How to Run:
	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.padding_tool()

	'''

	# This selected the root joint to let me start creating the pad
	selected = pm.ls(selection=True)

	# print 'Current Selected: ', selected
	root_joint = selected[0]

	# Create empty group
	# ----Flag----
	# empty=True will make an empty group
	pad = pm.group(empty=True)

	# Move group to joint.
	temp_constraint = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(temp_constraint)

	# Freeze Tranforms on the group
	pm.makeIdentity(pad,apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# Renaming pad
	# lt_middle_00_pad
	pad_name = root_joint.replace('01_bind','00_pad')
	pad.rename(pad_name)

	print 'Padding group created.' 

def priming_tool():

	'''
	Create the icon control system for the joints

	Select Root Joint and then start shift selecting the joints in order from root to waste be sure to delete the waste icon

	How to Run:
	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.priming_tool()

	'''

	# Get selected joints.
	# If you do dag=True it will select the children in the hierchy and will do most of the joint automaticly and 
	# do the contriants but the first one has to be deleted or something else
	selected_joint = pm.ls(selection=True)

	for current_joint in selected_joint:
		print 'Current Joint', current_joint

		#Icon and pad name
		icon_name = current_joint.replace('_bind','_icon')
		local_pad_name = current_joint.replace('_bind','_local')

		# Create a control icon		
		control_icon = pm.circle(name=icon_name,normal=[1,0,0], radius=1.8)[0]

		# Create a group(parenting the control under the group)
		local_pad = pm.group(name=local_pad_name)

		# Move the group to the target joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():

	'''
	Rename a selected joint chain.
		naming convention:
			lt_arm_01_bind
			lt_arm_03_waste

	The user will select the root joint and then execute the tool.


	How to Run:

	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.joint_renamer()

	'''
	# INPUT AREA!
	# Get selected root joint.
	joint_system = pm.ls(selection=True, dag=True)

	# orientation_systemName_count_suffix
	# lt.arm_01_bind
	# you can do raw_input but don't
	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'bind'

	# Loop through join chain.
	for current_joint in joint_system:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		# Increases the number by one each time
		print 'Renaming: ', current_joint, 'New Name: ', new_name

		# Pushing the count forward
		count = count + 1


	# Another way to select the last joint is by doing Joint_system -1	
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Renaming: ', current_joint, 'New Name: ', new_name
	current_joint.rename(new_name)


	print 'Selected joints has been renamed'


def lock_and_hide_trans():
	'''

	This hides both transforms and scale

	Select object you want there transforms and scale and visibility to be locked

	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.lock_and_hide_trans(); 

	'''

	#Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control ', control_icon

	#Translate
	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)

	#Scale
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)

	#Visiblity
	control_icon.v.set(lock=True, keyable=False)

	print 'Channel locked and hidden.'

def lock_and_hide_rotate():
	'''

	This hides both rotate and scale

	Select object you want there rotate and scale and visibility to be locked

	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.lock_and_hide_rotate(); 

	'''

	#Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control ', control_icon

	#Rotate
	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)

	#Scale
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)

	#Visiblity
	control_icon.v.set(lock=True, keyable=False)

	print 'Channel locked and hidden.'

def unlock_and_show():
	'''

	This reveals and unlocks all the control keys you might have hidden in your object

	Select object you want all there controls to be shown again

	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.unlock_and_show(); 

	'''

	#Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control ', control_icon

	#Translate
	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)

	#Rotate
	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)

	#Scale
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)

	#Visiblity
	control_icon.v.set(lock=False, keyable=True)

	print 'Channel locked and hidden.'


def icon_color_red():
	'''
	This will make the selected icons into the color red


	How to Run:
	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.icon_color_red(); 

	'''

	# Select the icon or icons you want to color, they way it works is that if you do it on the parent of a group it will go down to the children
	color_selection = pm.ls(selection=True)

	# You then go to the attribute editor

	# Afterwards you go to the display area

	# There you go to the Draw Overrides

	# Enable Overrides 

	for target_selection in color_selection:
		pm.setAttr(target_selection+'.overrideEnabled',1)
		pm.setAttr(target_selection+'.overrideColor',13)

def icon_color_blue():
	'''
	This will make the selected icons into the color blue


	How to Run:
	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.icon_color_blue(); 

	'''

	# Select the icon or icons you want to color, they way it works is that if you do it on the parent of a group it will go down to the children
	color_selection = pm.ls(selection=True)

	# You then go to the attribute editor

	# Afterwards you go to the display area

	# There you go to the Draw Overrides

	# Enable Overrides 

	for target_selection in color_selection:
		pm.setAttr(target_selection+'.overrideEnabled',1)
		pm.setAttr(target_selection+'.overrideColor',6)

def icon_color_green():
	'''
	This will make the selected icons into the color green


	How to Run:
	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.icon_color_green(); 

	'''
	# Select the icon or icons you want to color, they way it works is that if you do it on the parent of a group it will go down to the children
	color_selection = pm.ls(selection=True)

	# You then go to the attribute editor

	# Afterwards you go to the display area

	# There you go to the Draw Overrides

	# Enable Overrides 

	for target_selection in color_selection:
		pm.setAttr(target_selection+'.overrideEnabled',1)
		pm.setAttr(target_selection+'.overrideColor',14)

def icon_color_yellow():
	'''
	This will make the selected icons into the color yellow


	How to Run:
	import mediavillaMario_riggingTools_cri1_1408
	reload(mediavillaMario_riggingTools_cri1_1408)
	mediavillaMario_riggingTools_cri1_1408.icon_color_yellow(); 

	'''
	# Select the icon or icons you want to color, they way it works is that if you do it on the parent of a group it will go down to the children
	color_selection = pm.ls(selection=True)

	# You then go to the attribute editor

	# Afterwards you go to the display area

	# There you go to the Draw Overrides

	# Enable Overrides 

	for target_selection in color_selection:
		pm.setAttr(target_selection+'.overrideEnabled',1)
		pm.setAttr(target_selection+'.overrideColor',17)






