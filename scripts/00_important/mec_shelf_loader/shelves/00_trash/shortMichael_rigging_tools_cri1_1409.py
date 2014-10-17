'''
Michael Short
shortMichael_rigging_tools_cri1_1409.py

Description:
	A group of rigging related tools.

How to Run:

import shortMichael_rigging_tools_cri1_1409
reload(shortMichael_rigging_tools_cri1_1409)

'''

print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy():
	'''
	Create hierarchy based on a given system.

	Select root joint chain and execute function.

	import shortMichael_rigging_tools_cri1_1409
	reload(shortMichael_rigging_tools_cri1_1409)
	shortMichael_rigging_tools_cri1_1409.hierarchy()
	'''

	joint_system = pm.ls(selection=True, dag=True)
	#print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create empty group.
	root_pad = pm.group(empty=True, name='lt_middle_00_pad')

	# Move group to target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''

	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_01_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group(name='lt_middle_01_pad')

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group to target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	# Lock and hide translation, scale, and visibility.
	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=True, keyable=False)
	control_icon_1.tz.set(lock=True, keyable=False)
	control_icon_1.sx.set(lock=True, keyable=False)
	control_icon_1.sy.set(lock=True, keyable=False)
	control_icon_1.sz.set(lock=True, keyable=False)
	control_icon_1.v.set(lock=True, keyable=False)

	'''
	Control 2
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_02_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group(name='lt_middle_02_pad')

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group to target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	# Lock and hide translation, scale, and visibility.
	control_icon_2.tx.set(lock=True, keyable=False)
	control_icon_2.ty.set(lock=True, keyable=False)
	control_icon_2.tz.set(lock=True, keyable=False)
	control_icon_2.sx.set(lock=True, keyable=False)
	control_icon_2.sy.set(lock=True, keyable=False)
	control_icon_2.sz.set(lock=True, keyable=False)
	control_icon_2.v.set(lock=True, keyable=False)

	'''
	Control 3
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_03_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group(name='lt_middle_03_pad')

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group to target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	# Lock and hide translation, scale, and visibility.
	control_icon_3.tx.set(lock=True, keyable=False)
	control_icon_3.ty.set(lock=True, keyable=False)
	control_icon_3.tz.set(lock=True, keyable=False)
	control_icon_3.sx.set(lock=True, keyable=False)
	control_icon_3.sy.set(lock=True, keyable=False)
	control_icon_3.sz.set(lock=True, keyable=False)
	control_icon_3.v.set(lock=True, keyable=False)

	'''
	Parent control together.
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Hierarchy Created.'

def lock_and_hide():

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]
	# Lock and Hide
	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)


def tool():
	print 'Tool Active.'

def snapping_tool():
	'''
	This tool moves the first selected object to the second.
		- Translates and Rotates the target object.

	import shortMichael_rigging_tools_cri1_1409
	reload(shortMichael_rigging_tools_cri1_1409)
	shortMichael_rigging_tools_cri1_1409.snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	kenny = pm.parentConstraint(selected[0], selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second.'

def point_snapping_tool():
	'''
	This tool moves the first selected object to the second.
		- Translates and Rotates the target object.

	import shortMichael_rigging_tools_cri1_1409
	reload(shortMichael_rigging_tools_cri1_1409)
	shortMichael_rigging_tools_cri1_1409.point_snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	kenny = pm.pointConstraint(selected[0], selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second.'

def world_icon():

	# Get selected.
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	first_joint = selected[0]

	# Create control icon.
	control_icon_1 = pm.circle(normal=[0, 1, 0], radius=2)[0]

	# Move control icon to target joint.

	# Delete constraint.
	kenny = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(kenny)

	print 'Icons created.'

def padding_tool():
	'''
	Michael Short
	padding_tool

	Description:
		This tool creates and empty group and moves and parents it to the selected joint. It then gives it the appropriate name.

	How to Run:

	import shortMichael_rigging_tools_cri1_1409
	reload(shortMichael_rigging_tools_cri1_1409)
	shortMichael_rigging_tools_cri1_1409.padding_tool()
	'''

	# Create empty group.
	pad = pm.group(empty=True)

	# Move group to target joint.
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.
	pm.parent(root_joint, pad)

	# Renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def priming_tool():
	'''
	Michael Short
	priming_tool

	Description:
		This tool creates and names a localy oriented control icon on any selected joints.

	How to Run:

	import shortMichael_rigging_tools_cri1_1409
	reload(shortMichael_rigging_tools_cri1_1409)
	shortMichael_rigging_tools_cri1_1409.priming_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected[0]

	
	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')


		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created.', local_pad

		# Move group to target joint and delete constraints.
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)

		print 'Local Oriented Controls Created.'
