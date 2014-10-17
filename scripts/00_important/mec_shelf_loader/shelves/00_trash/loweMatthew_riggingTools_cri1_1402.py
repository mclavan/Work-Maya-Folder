'''Header - info'''
	'''
	Rigging tools

	Matthew Lowe

	Description - Multi function script:

	-Hierarchy tool-
	Create a hierarchy based upon a given system.
	Select root joint chain and execute function.

	-Joint renamer tool-
	Renaming a joint based upon a naming convention

	-Padding tool-
	Creates offset pads on a seleted joint chain.

	-Priming tool-
	Creates a local oriented control for use in animation 
	for a selected joint chain

	-Unlock and Show-
	unlock and make keyable all channels in the first selected object

	-Control mirror tool-

	This tool is going to be useful for mirroring any controls based
	upon selection.

	How to Run:

	import loweMatthew_riggingTools_cri1_1402
	reload(loweMatthew_riggingTools_cri1_1402)

	'''

import pymel.core as pm

print 'Rigging tools Active'

def hierarchy():
	'''
	Create a hierarchy based upon a given system.

	Select root joint chain and execute function.

	import loweMatthew_riggingTools_cri1_1402
	loweMatthew_riggingTools_cri1_1402.hierarchy()

	'''

	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	
	# Padding Root Joint
	# Create empty group.
	root_pad = pm.group(name = root_joint.replace('bind','pad'),empty=True)


	# Move group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	
	# parent root joint to the group.
	pm.parent(root_joint, root_pad)

	# Local Controls
	
	# Control 1 - root_joint
	
	# Create a control.
	# normal = [1, 0, 0], radius=1
	control_icon_1 = pm.circle(name = root_joint.replace('bind', 'icon'), normal=[1,0,0], radius=2) [0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group(name = root_joint.replace('bind', 'local'))

	# Output control and pad
	print 'Control 1 Created:', control_icon_1
	print 'Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient contrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	# lock and hide translations and scales
	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=True, keyable=False)
	control_icon_1.tz.set(lock=True, keyable=False)
	control_icon_1.sx.set(lock=True, keyable=False)
	control_icon_1.sy.set(lock=True, keyable=False)
	control_icon_1.sz.set(lock=True, keyable=False)
	control_icon_1.v.set(lock=True, keyable=False)
	
	# Control 2
	
	# Create a control.
	# normal = [1, 0, 0], radius=1
	control_icon_2 = pm.circle(name = joint_2.replace('bind', 'icon'),normal=[1,0,0], radius=2) [0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group (name = joint_2.replace('bind', 'local'))

	# Output control and pad
	print 'Control 2 Created:', control_icon_2
	print 'Pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient contrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	# lock and hide translations and scales
	control_icon_2.tx.set(lock=True, keyable=False)
	control_icon_2.ty.set(lock=True, keyable=False)
	control_icon_2.tz.set(lock=True, keyable=False)
	control_icon_2.sx.set(lock=True, keyable=False)
	control_icon_2.sy.set(lock=True, keyable=False)
	control_icon_2.sz.set(lock=True, keyable=False)
	control_icon_2.v.set(lock=True, keyable=False)

	# Control 3
	
	# Create a control.
	# normal = [1, 0, 0], radius=1
	control_icon_3 = pm.circle(name = joint_3.replace('bind', 'icon'), normal=[1,0,0], radius=2) [0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group(name = joint_3.replace('bind', 'local'))

	# Output control and pad
	print 'Control 3 Created:', control_icon_3
	print 'Pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient contrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	# lock and hide translations and scales
	control_icon_3.tx.set(lock=True, keyable=False)
	control_icon_3.ty.set(lock=True, keyable=False)
	control_icon_3.tz.set(lock=True, keyable=False)
	control_icon_3.sx.set(lock=True, keyable=False)
	control_icon_3.sy.set(lock=True, keyable=False)
	control_icon_3.sz.set(lock=True, keyable=False)
	control_icon_3.v.set(lock=True, keyable=False)

	# Parent control together.
	
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Hierarchy Created'

def joint_renamer():
	'''
	Renaming a joint based upon a naming convention
	execute:
	import loweMatthew_riggingTools_cri1_1402
	reload (loweMatthew_riggingTools_cri1_1402)
	loweMatthew_riggingTools_cri1_1402.joint_renamer()
	Get selected
	'''
	joint_chain = pm.ls(selection=True, dag=True)
	
	# print 'Selected items', joint_chain
	# Figure out naming convention.
	# 'lt_arm01_bind' -> ' lt_arm_03_waste'
	
	ori = raw_input()
	system_name = raw_input()
	count = 1
	suffix = 'bind'

	new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
	print 'New name:', new_name

	# Loop through joint chain.

	for current_joint in joint_chain:
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New name:', new_name
		
		# Rename joint

		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count-1, waste)
	current_joint.rename(new_name)

def padding_tool():
	'''
	creates offset pads on a seleted joint chain.

	execute:

	impor	t loweMatthew_riggingTools_cri1_1402
	reloa	d(loweMatthew_riggingTools_cri1_1402)
	loweM	atthew_riggingTools_cri1_1402.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create an empty group
	pad = pm.group(empty=True)

	# Move group to joint.
	# Delete constraints
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	# Parent joint to group
	pm.parent(root_joint, pad)

	# Renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created'

def priming_tool():
	'''

	Creates a local oriented control for use in animation for a selected joint chain

	execute:

	import loweMatthew_riggingTools_cri1_1402
	reload (loweMatthew_riggingTools_cri1_1402)
	loweMatthew_riggingTools_cri1_1402.priming_tool()
	'''
	# Get Selected
	selected = pm.ls(selection=True)
	print 'Joints Selected', selected
	target_joint = selected[0]

	
	for target_joint in selected:

		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create a Control
		# normal = x and radius = 2
		control_icon = pm.circle ( normal = [1,0,0], radius = 2, 
			name = control_icon_name)[0]
		# Group Control (NOT an empty group)
		local_pad = pm.group ( name = local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad
		# Move group to target joint.
		# delete constraint
		temp_constraint = pm.parentConstraint (target_joint, local_pad)
		pm.delete (temp_constraint)

		# Orient Constraint Joint to Control
		pm.orientConstraint(control_icon, target_joint)

	print 'Local Oriented Controls Created.'

def unlock_and_show():
	'''
	unlock and make keyable all channels in the first selected object

	import loweMatthew_riggingTools_cri1_1402
	reload (loweMatthew_riggingTools_cri1_1402)
	loweMatthew_riggingTools_cri1_1402.unlock_and_show()

	'''

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)

	print 'First selected object has all channels shown and they are keyable'

def control_mirror():
	'''
	mirroring Controls
	this tool is going to be useful for mirroring any controls based
	upon selection.

	execute: First select object or objects then run:

	import loweMatthew_riggingTools_cri1_1402
	reload (loweMatthew_riggingTools_cri1_1402)
	loweMatthew_riggingTools_cri1_1402.control_mirror()
	'''
	# Get selected 
	selected = pm.ls(selection=True)
	print 'Target Selected', selected

	for target_selection in selected:
		
		# duplicate selected 
		target_copy = pm.duplicate(rr=True)
		print 'Selected Target has been Duplicated'

		# create empty group
		temp_group = pm.group(empty=True)
		print 'empty group has been made'

		# parent selection to group
		pm.parent(target_copy, temp_group)
		print 'target has been grouped'

		# change scale channel to -x
		pm.setAttr(temp_group + '.sx', -1)
		print 'Group has been mirrored on X axis'

		# un-parent selected from group and delete temp group
		pm.parent(target_copy, world=True)
		pm.delete(temp_group)
		print 'Copys have been unparented and temp group has been delete'

		# freeze transforms on selected
		pm.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
		print 'duplicate and mirror was successful'