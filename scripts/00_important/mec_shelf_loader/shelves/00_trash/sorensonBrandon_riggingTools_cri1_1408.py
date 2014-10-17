'''
Sorenson Brandon
sorensonBrandon_riggingTools_cri1_1408.py

Description:
	This script contains a series of rigging tools.

How to run:
	
	import pymel.core as pm

	import sorensonBrandon_riggingTools_cri1_1408
	reload(sorensonBrandon_riggingTools_cri1_1408)
	sorensonBrandon_riggingTools_cri1_1408.def_Name_Here()

'''

print 'Rigging Tools Active'

import pymel.core as pm

def lock_and_hide():

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_control', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)

	# Locks everything.

	print 'Channels locked and hidden.'

def unlock_and_unhide_trans():

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_control', control_icon

	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)

	# Unlocks the tanslation channels 

	print 'Translation Channels unlocked and unhidden.'

def unlock_and_unhide_rotate():

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_control', control_icon

	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)

	# Unlocks the Rotation channels 

	print 'Rotate Channels unlocked and unhidden.'

def lock_and_hide_trans():

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_control', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)

	print 'Translation Channels locked and hidden.'

def lock_and_hide_rotate():

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_control', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)

	print 'Rotation Channels locked and hidden.'

def priming_tool():

	# Get selected joints 

	selected_joints = pm.ls(selection=True, dag=True)
	selected_joints.pop(-1)

	# Loop thru all the selected joints 

	for current_joint in selected_joints:
		print 'current_joint', current_joint
		# Icon and pad name

		icon_name = current_joint.replace('_bind','_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control icon 

		control_icon = pm.circle(name= icon_name, normal=[1,0,0], radius=1.8)[0]

		# Create a group (parenting the control under the group)

		local_pad = pm.group(control_icon, name= icon_name)

		# Move the group to the target joint

		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group

		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():
	'''
	Renamed a selected joint chain.

		Naming convention
			lt_arm_01_bind 
			lt_arm_02_bind
			lt_arm_03_waste

	Select the root joint and then execute the tool 

	How to run:

	import sorensonBrandon
	sorensonBrandon.joint_renamer()

	'''

	# Get selected root joint.

	joint_system = pm.ls(selection =True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

		# raw_input opens dialog for renaming the selected 

	# Loop through joint chain 

	for current_joint in joint_system:

		# Assembling new name

		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

			# In the third section above the :02d is two diget numbering 

		# Rename joint

		current_joint.rename(new_name)

		# Pushing the count forward

		count = count + 1

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')	

	print 'renaming ',current_joint, 'New Name: ', new_name

	current_joint.rename(new_name)

	print 'selected joints has been renamed'

def padding_tool():

	'''

	Creates a padding group for selectd joint. 

	Select a joint and execute the funtion.

	How to run.

	import pymel.core as pm

	import sorensonBrandon_riggingTools_cri1_1408
	reload(sorensonBrandon_riggingTools_cri1_1408)
	sorensonBrandon_riggingTools_cri1_1408.padding_tool()

	'''
	selected = pm.ls(selection=True)
	# print 'Current Select:', slected
	root_joint = selected[0]

	# Creat empty Group, pm.group(empty=True) makes a empty group

	pad = pm.group(empty=True)

	# Move Empty Group to the Selected Joint, then delete constriant.

	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transoforms on the empty group. 

	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to the empty group. 

	pm.parent(root_joint, pad)

	# Renaming 

	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created'

def hierarchy():

	'''
	Creats a hierarchy from the choosen system.

  	Select root joint chain and execute function.

	impport sorensonBrandon_riggingTools_cri1_1408
	sorensonBrandon_riggingTools_cri1_1408.hierarchy()

	'''
 
	'''
	Input 
	
	Working on the root joint.

	'''

	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding root joint.
	'''
	# Creat empty group 

	root_pad = pm.group(empty=True)

	# Move group over to the target joint 

	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze transforms on group 

	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group 

	pm.parent(root_joint, root_pad)

	'''
	Local Controls 
	'''
	'''
	Control 1  root_joint
	'''
	# Creat a control
	# normal=[1, 0, 0], radius=2

	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)

	# Creat a group.
	# Group control during the process.

	local_pad_1 = pm.group()

	# Output control and Pad. 
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move the group over to the target joint.
	# Delete the constriant after the move. 
	# Driver: joint - Driven: group
		# root_joint, local_pad_1

	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Creat an orientConstraint. joint to control.
	# Driver to Driven (Control to Joint)

	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2  joint_2
	'''
	# Creat a control
	# normal=[1, 0, 0], radius=2

	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)

	# Creat a group.
	# Group control during the process.

	local_pad_2 = pm.group()

	# Output control and Pad. 
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move the group over to the target joint.
	# Delete the constriant after the move. 
	# Driver: joint - Driven: group
		# joint_2, local_pad_2

	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Creat an orientConstraint. joint to control.
	# Driver to Driven (Control to Joint)

	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3  joint_3
	'''
	# Creat a control
	# normal=[1, 0, 0], radius=2

	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)

	# Creat a group.
	# Group control during the process.

	local_pad_3 = pm.group()

	# Output control and Pad. 
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move the group over to the target joint.
	# Delete the constriant after the move. 
	# Driver: joint - Driven: group
		# joint_3, local_pad_3

	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Creat an orientConstraint. joint to control.
	# Driver to Driven (Control to Joint)

	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent controls together.
	'''
	# last pad to control 2

	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	'''
	Rename pads and controls.
	'''
	#If your reading this i could not figure out how to get the naming to work. 

	# Pads need to be named orientation(ct, lf, rt, ...), system_name(arm, leg, back, ...), count(start at 0) then end with 'pad'.
	# Controls need to be named orientation(ct, lf, rt, ...), system_name(arm, leg, back, ...), count(start at 0) then end with 'icon'.
	joint_system = pm.ls(selection =True, dag=True)
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = raw_input()

		# raw_input opens dialog for renaming the selected 

	# Loop through joint chain 

	for current_joint in joint_system:

		# Assembling new name

		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

			# In the third section above the :02d is two diget numbering 

		# Rename joint

		current_joint.rename(new_name)

		# Pushing the count forward

		count = count + 1

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')	

	print 'renaming ',current_joint, 'New Name: ', new_name

	current_joint.rename(new_name)
  
	print 'Hierarchy Created'