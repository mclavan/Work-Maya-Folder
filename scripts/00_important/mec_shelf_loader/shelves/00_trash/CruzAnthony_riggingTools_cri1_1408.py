'''
Anthony Cruz
CruzAnthony_riggingTools_cri1_1408.py

Description:
	print 'Rigging Tools Active'


How to Run:

import CruzAnthony_riggingTools_cri1_1408
reload(CruzAnthony_riggingTools_cri1_1408)


'''

print 'Rigging Tools Active'

import pymel.core as pm

def lock_and_hide():
	
	# Get Selected
	selected_control = pm.ls(selection=True)
	control_icon = selected_control[0]
	print 'selected_control', control_icon


	print 'Channels locked and hidden.'

def lock_and_hide_trans():
	
	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.lock_and_hide_trans()

	'''

	# Get Selected
	selected_control = pm.ls(selection=True)
	control_icon = selected_control[0]
	print 'selected_control', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	print 'Channels locked and hidden.'

def lock_and_hide_scale():

	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.lock_and_hide_scale()
	
	'''
	
	# Get Selected
	selected_control = pm.ls(selection=True)
	control_icon = selected_control[0]
	print 'selected_control', control_icon

	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	print 'Channels locked and hidden'

def unlock_and_show_all():

	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.unlock_and_show_all()
	
	'''
	
	# Get Selected
	selected_control = pm.ls(selection=True)
	control_icon = selected_control[0]
	print 'selected_control', control_icon

	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)

def priming_tool():

	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.priming_tool()
	
	'''

	# Get selected
	selected = pm.ls(selection=True, dag=True)
	# current_joint = selected[0]

	for current_joint in selected:
		control_icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, 
			name=control_icon_name)[0]

		# Group a control (parenting the control under the group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon', control_icon
		print 'Pad Created', local_pad

		# Move groupd to target joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Orient constraint joint to control
		pm.orientConstraint(control_icon, current_joint)

	print 'Local Oriented Controls Created'

def lock_and_hide_Rotate():
	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.lock_and_hide_Rotate()
	
	'''

	# Get Selected
	selected_control = pm.ls(selection=True)
	control_icon = selected_control[0]
	print 'selected_control', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	print 'Channels locked and hidden'

def lock_and_hide_vis():
	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.lock_and_hide_vis()
	
	'''

	# Get Selected
	selected_control = pm.ls(selection=True)
	control_icon = selected_control[0]
	print 'selected_control', control_icon

	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden'

def hierarchy():

	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.hierarchy()
	
	'''

	selected = pm.ls(selection=True, dag=True)
	
	joint_1 = selected[0]
	joint_2 = selected[1]
	joint_3 = selected[2]

	'''
	Padding the root joints
	'''

	# Create an empty group
	root_pad = pm.group(empty=True)

	# Move the group to target joint
	temp_constraint = pm.pointConstraint(joint_1, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transformations on the group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent the root joint to the group
	pm.parent(joint_1, root_pad)


	root_pad_name = joint_1.replace('01_bind','00_pad')
	root_pad.rename(root_pad_name)

	'''
	Control #1
	'''
	# Create a control
	control_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group
	pad_1 = pm.group()

	# Move the group to the target joint
	temp = pm.parentConstraint(joint_1, pad_1)
	pm.delete(temp)

	# Orient Constraint the joint to the control
	pm.orientConstraint(control_1, joint_1)

	# Rename the pad and the control
	new_control_name = joint_1.replace('_bind', '_icon')
	new_pad_name = joint_1.replace('_bind', '_local')
	control_1.rename(new_control_name)
	pad_1.rename(new_pad_name)

	'''
	Control #2
	'''
	# Createa control
	control_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group
	pad_2 = pm.group()

	# Move the group to the target joint
	temp = pm.parentConstraint(joint_2, pad_2)
	pm.delete(temp)

	# Orient Constraint the joint to the control
	pm.orientConstraint(control_2, joint_2)

	# Rename the pad and the control
	new_control_name = joint_2.replace('_bind', '_icon')
	new_pad_name = joint_2.replace('_bind', '_local')
	control_2.rename(new_control_name)
	pad_2.rename(new_pad_name)
	

	'''
	Control #3
	'''
	# Createa control
	control_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group
	pad_3 = pm.group()

	# Move the group to the target joint
	temp = pm.parentConstraint(joint_3, pad_3)
	pm.delete(temp)

	# Orient Constraint the joint to the control
	pm.orientConstraint(control_3, joint_3)

	# Rename the pad and the control
	new_control_name = joint_3.replace('_bind', '_icon')
	new_pad_name = joint_3.replace('_bind', '_local')
	control_3.rename(new_control_name)
	pad_3.rename(new_pad_name)

	'''
	Parenting
	'''
	# Parent the controls and icons together
	pm.parent(pad_3, control_2)
	pm.parent(pad_2, control_1)

	print 'Hierarchy Created'

def padding_tool():

	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.padding_tool()
	
	'''

	# Get selected
	selected = pm.ls(selection=True)
	# print 'Current Selected', selected

	root_joint = selected[0]

	# Create an empty group
	pad = pm.group(empty=True)

	# Move the group to the joint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transformations 
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent the joint to the group
	pm.parent(root_joint, pad)

	# Rename
	pad_name = root_joint.replace('00_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created'

def renaming_tool():

	'''
	How to Run

	import CruzAnthony_riggingTools_cri1_1408
	reload(CruzAnthony_riggingTools_cri1_1408)
	CruzAnthony_riggingTools_cri1_1408.renaming_tool()
	
	'''

	# Get selected
	selected = pm.ls(selection=True)

	joint_chain = pm.ls(selection=True)
	# print 'Selected items', joint_chain


	# Naming Convention Example
	# lt_arm_01_bind -> lt_arm_03_waste
	# orienation_systemName_count_suffix
	ori = raw_input()
	name = raw_input()
	count = 00
	suffix = 'bind'

	# Loop through the selected

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)
		print 'New Name', new_name
		current_joint.rename(new_name)

	# Name the waste joint
	new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, 'waste')

	# Output to the user
	joint_chain[-1].rename(new_name)
