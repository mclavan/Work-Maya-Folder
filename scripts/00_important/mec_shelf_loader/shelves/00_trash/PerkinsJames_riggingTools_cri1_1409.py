'''
James Perkins
PerkinsJames_riggingTools_cri1_1409.py

Description:
Practical rigging tools.

How to Run:

import PerkinsJames_riggingTools_cri1_1409
reload(PerkinsJames_riggingTools_cri1_1409)


'''

print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy():
	'''
	Description:
	Create a hierarchy based upon a given system.

	How to Use:
	Select root joint chain and execute function.

	How to Run:
	import PerkinsJames_riggingTools_cri1_1409
	reload(PerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.hierarchy()
	'''

	'''
	Input
	What are we working on?
	The root join.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create empty group
	root_pad = pm.group(name='lt_middle_00_pad', empty=True)

	# Move the group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze transforms on group.
	# pm.makeIdentity()
	# t = translate
	# r = rotate
	# s = scale
	# n = normal
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to the group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(name='lt_middle_01_icon', normal=[1, 0, 0], radius=2)[0]

	# Create a group
	# Grouping control during the process.
	local_pad_1 = pm.group(name='lt_middle_01_local')

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(name='lt_middle_02_icon', normal=[1, 0, 0], radius=2)[0]

	# Create a group
	# Grouping control during the process.
	local_pad_2 = pm.group(name='lt_middle_02_local')

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(name='lt_middle_03_icon', normal=[1, 0, 0], radius=2)[0]

	# Create a group
	# Grouping control during the process.
	local_pad_3 = pm.group(name='lt_middle_03_local')

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together.
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Hierarchy Created'

def joint_renamer():
	'''
	Description:
	A tool for renaming joints with proper naming conventions.

	How to Use:
	Select joint and run.

	How to Run:
	import PerkinsJames_riggingTools_cri1_1409
	reload(PerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.joint_renamer()

	'''

	print 'Joint Renamer - Active'

	'''
	Get Selected.

	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items', joint_chain

	'''
	Figure out naming convention.
	ex - 'lt_arm_01_bind' -> 'lt_arm_03_waste'
	'ct_tail_01_bind', -> 'ct_tail_06_waste'
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'

	

	'''
	Loop through joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		# Rename joint
		current_joint.rename(new_name)


	new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)



def padding_tool():
	'''
	Description:
	Tool to create pads for joint chains.

	How to Use:
	Select root joint and run.

	How to Run:
	import PerkinsJames_riggingTools_cri1_1409
	reload(PerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:',selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create an empty group.
	# 
	pad = pm.group(empty=True)

	# Move group to joint.
	#  and delete constraint.
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group.
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind would be replaced by
	# ct_tail_00_pad (does not replace information, returns a copy)
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created.'


def priming_tool():
	'''

	Description:
	A tool for adding orient constrained control circles to joints.

	How to Use:
	Select joint(s) and run.

	How to Run:
	import PerkinsJames_riggingTools_cri1_1409
	reload(rPerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.priming_tool()
	'''

	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create a control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group()

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		#	and delte constraint.
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created.'

def snapping_tool():
	'''
	This tool moves the first selected object to the secondd.
		-Translates and Rotates the target object.

	import PerkinsJames_riggingTools_cri1_1409
	reload(PerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	Gnar = pm.parentConstraint(target_joint, control_icon)
	pm.delete(Gnar)

	print 'The first selected object was moved to the second.'

def point_snapping_tool():
	'''
	This tool moves the first selected object to the secondd.
	-Translates the target object.

	import PerkinsJames_riggingTools_cri1_1409
	reload(PerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.point_snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	Gnar = pm.pointConstraint(target_joint, control_icon)
	pm.delete(Gnar)

	print 'The first selected object was moved to the second.'

def world_icon():
	'''
	Creates a control and point constrains it to a joint.

	import PerkinsJames_riggingTools_cri1_1409
	reload(PerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.world_icon()
	'''
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	first_joint = selected[0]

	# Create a control icon
	control_icon1 = pm.circle(normal=[0, 1, 0], radius=2)[0]

	# Move the control to the target joint.
	# Delete the constraint.
	Gnar = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(Gnar)
 
	print 'Icon created.'

def unlock_and_show():
	'''
	Unlocks and shows all the transform tools.

	import PerkinsJames_riggingTools_cri1_1409
	reload(PerkinsJames_riggingTools_cri1_1409)
	PerkinsJames_riggingTools_cri1_1409.unlock_and_show()
	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]
	# Lock and Hide
	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)









