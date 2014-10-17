'''

Emily Doubleday

doubledayEmily_riggingTools_cri1_1408.py

Description
	This script contains a series of Rigging Tools

How to Run

	import	doubledayEmily_riggingTools_cri1_1408 as doubledayEmily
	reload(doubledayEmily)

'''

print 'Rigging Tools Active'

import pymel.core as pm

def lock_and_hide():

	#Get Selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control:', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.rx.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.v.set(lock=False, keyable=False)
	print 'Channles locked and hidden.'

def lock_and_hide_trans():

	#Get Selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control:', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channles locked and hidden.'

def lock_and_hide_rotate():

	#Get Selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control:', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channles locked and hidden.'

def unlock_and_show():

	#Get Selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control:', control_icon

	control_icon.tx.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.rx.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)
	print 'Channles unlocked and showing.'

def priming_tool():

	#Get selected joints
	selected_joint = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected[0]
# issue
	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		#Create a control icon
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, name=control_icon_name)[0]

		#Create a Group (parenting the contol under the group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad


		#Move group to the target.
		temp_Constraint = pm.parentConstraint(current_joint, local_pad)
		pm.delete(temp_Constraint)

		#Orient Constraint Joint
		pm.orientConstraint(control_icon, target_joint)

def hierarchy():

	'''
	Create a Hiearchy based upon a given system.

	Select root jiont chain and execute function.

	import	doubledayEmily_riggingTools_cri1_1408 as doubledayEmily
	doubledayEmily.hierarchy()
	'''

	'''
	Input

	The Root Joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	#print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create Empty Group
	root_pad = pm.group(empty=True)

	# Move Group to Target
	temp_Constraint = pm.parentConstraint(root_joint, root_pad)
	pm.delete(temp_Constraint)

	#Freeze Groups transforms
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	#Parent Root joint
	pm.parent(root_joint, root_pad)

	'''
	Local Controls.
	'''

	'''
	Control 1 -root_joint
	'''
	#Create a Control
	#normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#Create a Group
	#grouping control during the process
	local_pad_1 = pm.group()

	#Output control and pad
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	#Move group over to the target joint.
	#Delete constraint after snapping
	#Driver: Joint
	#Driven: Group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	#Orient Constrain the joint to the control.
	#Driver -> Driven.
	#Control -> Joint.
	pm.orientConstraint(control_icon_1, root_joint)


	'''
	Control 2
	'''
	#Create a Control
	#normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#Create a Group
	#grouping control during the process
	local_pad_2 = pm.group()

	#Output control and pad
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	#Move group over to the target joint.
	#Delete constraint after snapping
	#Driver: Joint
	#Driven: Group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	#Orient Constrain the joint to the control.
	#Driver -> Driven.
	#Control -> Joint.
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	#Create a Control
	#normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#Create a Group
	#grouping control during the process
	local_pad_3 = pm.group()

	#Output control and pad
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	#Move group over to the target joint.
	#Delete constraint after snapping
	#Driver: Joint
	#Driven: Group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	#Orient Constrain the joint to the control.
	#Driver -> Driven.
	#Control -> Joint.
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent Control
	'''
	#Pad 3 (last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)


	print'Hierarchy Created'

def joint_renamer():

	print 'Joint Renamer - Active'



	'''
	Get Selected.

	pm.ls(selection=True)
	'''

	joint_chain = pm.ls(selection=True)

	print 'Selected items:', joint_chain

	'''
	Figure out naming convention.
	'lt_arm_01_bind' -> 'lt_arm_03_waste'
	'ct_tail_01_bind', -> 'ct_tail_06_waste'
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
	print 'New Name', new_name

	'''
	Loop through joint chain
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name', new_name

		#Rename joint
		current_joint.rename(new_name)
		
# Indenting issues.
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

def padding_tool():

	'''
	import	doubledayEmily_riggingTools_cri1_1408 as doubledayEmily
	reload(doubledayEmily)
	doubledayemily.padding_tool()
	'''
	selected = pm.ls(selection=True)
	# print 'Current Selection:', selected
	root_joint = selected[0]

	#Create Empty Group
	pm.group(empty=True)

	#Move Group to joint
	temp_Constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_Constraint)

	#Freeze Transforms
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#Parent Joint to Group
	pm.parent(root_joint, pad)

	#Renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'



	


