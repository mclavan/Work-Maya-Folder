'''

Valerio Lucidi
Character Rigging 

'''

import pymel.core as pm

def hierarchy():
	'''
	create a hierarchy based on a given system. 

	select root joint chain and execute function.
    import rigging_tools
    rigging_tools.hierarchy()
	'''
	

	''' 
	Input
	What are we working on?
	The root joint. 
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint_system:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group over to target joint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group 
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group 
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal=[1, 0, 0], radius = 2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius = 2)[0]

	# Create a group. 
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'control_1_Created', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1
	
	# Move group over to the target joint.
	# Delete contraint after snapping. 
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constain the joint to the control. 
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control.
	# normal=[1, 0, 0], radius = 2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius = 2)[0]

	# Create a group. 
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'control_1_Created', control_icon_2
	print 'Local Pad 1 Created:', local_pad_2
	
	# Move group over to the target joint.
	# Delete contraint after snapping. 
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constain the joint to the control. 
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3 
	'''
	# Create a control.
	# normal=[1, 0, 0], radius = 2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius = 2)[0]

	# Create a group. 
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'control_1_Created', control_icon_3
	print 'Local Pad 1 Created:', local_pad_3
	
	# Move group over to the target joint.
	# Delete contraint after snapping. 
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constain the joint to the control. 
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)


	print 'hierarchy created'

def joint_renamer():
	'''

	joint_renamer.py

	Description:
	Practical use of loops.
	Renaming joint based upon a naming convention

	How to Run:

	import joint_renamer
	reload (joint_renamer)


	'''

	print 'Joint Renamer - Active'

	import pymel.core as pm

	'''
	Get Selected.

	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)
	print 'Selected Items:', joint_chain

	'''
	Figuring out naming convention.
	'lt_arm_01_bind' -> 'lt_arm_03_waste'
	'ct_tail_01_bind', -> 'ct_tail_06_waste'
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 1
	suffix = 'bind'



	'''
	Loop through joint chain. 
	'''
	for current_joint in joint_chain:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		# Rename joint
		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_name)

def padding_tool():
	'''

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()
	'''
	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty
	# Empty=True will create an empty group
	#
	pad = pm.group(empty=True)

	# Move group to joint.
	#	and delete contraint.
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group. 
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created.'

def priming_tool():
	'''


	import rigging_tools
	reload(rigging_tools)
	rigging_tools.priming_tool()
	'''

	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control 
		# Normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (Not an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)




	print 'Local Oriented Controls Created.'

def lock_and_hide_trans():

	# Get selected. 
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon
	control_icon.rx.set(lock=True, keyable=False) 
	control_icon.rz.set(lock=True, keyable=False) 
	control_icon.ry.set(lock=True, keyable=False) 
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
	control_icon.tx.set(lock=True, keyable=False) 
	control_icon.tz.set(lock=True, keyable=False) 
	control_icon.ty.set(lock=True, keyable=False) 
	control_icon.rx.set(lock=True, keyable=False) 
	control_icon.rz.set(lock=True, keyable=False) 
	control_icon.ry.set(lock=True, keyable=False) 
	control_icon.sx.set(lock=True, keyable=False) 
	control_icon.sy.set(lock=True, keyable=False) 
	control_icon.sz.set(lock=True, keyable=False) 
	print 'Channels locked and hidden.'


