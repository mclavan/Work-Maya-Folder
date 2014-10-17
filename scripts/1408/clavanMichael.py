'''
Michael Clavan
clavanMichael_riggingTools_cri1_1408.py 

Description:
	This script contains a series of rigging tools. 


How to Run:

import clavanMichael
reload(clavanMichael)


'''

print 'Rigging Tools Active'

import pymel.core as pm

def lock_and_hide():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon


	print 'Channels locked and hidden.'

def lock_and_hide_trans():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)	
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)				
	print 'Channels locked and hidden.'

def lock_and_hide_rotate():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)	
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)				
	print 'Channels locked and hidden.'

def unlock_and_show():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon
	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)				
	print 'Channels locked and hidden.'

def priming_tool():

	# Get selected joints. 
	selected_joints = pm.ls(selection=True)

	for current_joint in selected_joints:
		print 'Current Control:', current_joint
		# Icon and pad name.
		icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control icon
		control_icon = pm.circle(name=icon_name, normal=[1, 0, 0], radius=1.8)[0]  

		# Create a group (parenting the control under the group)
		local_pad = pm.group(control_icon, name=local_pad_name)

		# Move the group to the target joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():
	'''
	Rename a selected joint chain.  
		Naming convention:
			lt_arm_01_bind
			lt_arm_03_waste

	The user will select the root joint and then execute the tool.

	How to Run:

	import clavanMichael
	clavanMichael.joint_renamer()

	'''

	# Input Area!!!
	# Get selected root joint.
	joint_system = pm.ls(selection=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	# Loop through joint chain.
	for current_joint in joint_system:
		# Assembling new name
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		print 'Renaming: ', current_joint, 'New Name: ', new_name
		
		# Pusing the count forward.
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Renaming: ', current_joint, 'New Name: ', new_name
	current_joint.rename(new_name)

	print 'Selected joints has been renamed.'









