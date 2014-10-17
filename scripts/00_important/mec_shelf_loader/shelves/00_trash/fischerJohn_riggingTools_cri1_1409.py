'''
John Fischer
fischerJohn_riggingTools_cri1_1409.py

Description: A group of rigging related tools.

how to Run:

import fischerJohn_riggingTools_cri1_1409
reload(fischerJohn_riggingTools_cri1_1409)

'''

print 'Rigging Tools Active'

import pymel.core as pm

def tool():
	print 'Tool Active.'

def snapping_tool():
	'''
	this tool moves the first selected object to the second.
	- Translates and Rotates the target object.

	import fischerJohn_riggingTools_cri1_1409
	fischerJohn_riggingTools_cri1_1409.snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	# By default commands work on selected.
	kenny = pm.parentConstraint(selected[0], selected[1])
	pm.delete(kenny)

	print 'The first selected object was moved to the second.'	

def point_snapping_tool():
	'''
	this tool moves the first selected object to the second.
	- Translates and Rotates the target object.

	import fischerJohn_riggingTools_cri1_1409
	fischerJohn_riggingTools_cri1_1409.point_snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	# By default commands work on selected.
	kenny = pm.pointConstraint(selected[0], selected[1])
	pm.delete(kenny)

	print 'The first selected object was moved to the second.'	


def world_icon():
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	first_joint = selected[0]

	# Create a control icon.
	control_icon_1 = pm.circle(normal=[0, 1, 0], radius=2) [0]

	# Move the control to the target joint.
	# Delete the contstraint.
	kenny = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(kenny)

	print 'Icons created.'

def hierarchy():
	'''
	Create a hierarchy based upon a given system

	Select root joint chain and execute function.

	import fischerJohn_riggingTools_cri1_1409
	fischerJohn_riggingTools_cri1_1409.hierarchy()
	'''

	'''
	Input
	What are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''
	# Create Empty Group
	root_pad = pm.group(empty=True, name='lt_middle_00_pad')

	# Move group over to target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	
	# Parent joint back to group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2, name='lt_middle_01_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group(name='lt_middle_01_local')

	# Output control and pad
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:',local_pad_1

	# Move group over to target joint.
	# Delete Constraint after snapping.
	# Driver: Joint, Driven: Group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Driver -> Driven = Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	control_icon_1.tx.set(lock=True,keyable = False)
	control_icon_1.ty.set(lock=True,keyable = False)
	control_icon_1.tz.set(lock=True,keyable = False)
	control_icon_1.sx.set(lock=True,keyable = False)
	control_icon_1.sy.set(lock=True,keyable = False)
	control_icon_1.sz.set(lock=True,keyable = False)
	control_icon_1.v.set(lock=True,keyable = False)


	'''
	Control 2
	'''
	# Create a control.
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2, name='lt_middle_02_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group(name='lt_middle_02_local')

	# Output control and pad
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:',local_pad_2

	# Move group over to target joint.
	# Delete Constraint after snapping.
	# Driver: Joint, Driven: Group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Driver -> Driven = Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	control_icon_2.tx.set(lock=True,keyable = False)
	control_icon_2.ty.set(lock=True,keyable = False)
	control_icon_2.tz.set(lock=True,keyable = False)
	control_icon_2.sx.set(lock=True,keyable = False)
	control_icon_2.sy.set(lock=True,keyable = False)
	control_icon_2.sz.set(lock=True,keyable = False)
	control_icon_2.v.set(lock=True,keyable = False)

	'''
	Control 3
	'''
	# Create a control.
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2, name='lt_middle_03_icon')[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group(name='lt_middle_03_local')

	# Output control and pad
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:',local_pad_3

	# Move group over to target joint.
	# Delete Constraint after snapping.
	# Driver: Joint, Driven: Group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Driver -> Driven = Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	control_icon_3.tx.set(lock=True,keyable = False)
	control_icon_3.ty.set(lock=True,keyable = False)
	control_icon_3.tz.set(lock=True,keyable = False)
	control_icon_3.sx.set(lock=True,keyable = False)
	control_icon_3.sy.set(lock=True,keyable = False)
	control_icon_3.sz.set(lock=True,keyable = False)
	control_icon_3.v.set(lock=True,keyable = False)

	'''
	Parent Control together.
	'''
	# Pad 3 (last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)



	print 'Hierarchy Created'

def padding_tool():
	'''

	import fischerJohn_riggingTools_cri1_1409
	reload(fischerJohn_riggingTools_cri1_1409)
	fischerJohn_riggingTools_cri1_1409.padding_tool()
	'''
	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# Empty=True will create an empty group
	pad = pm.group(empty=True)

	# Move group to joint.
	# and delete constraint.
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group.
	pm.parent(root_joint, pad)

	# Renaming
	pad_name = root_joint.replace('_bind','_pad')
	pad.rename(pad_name)

	print 'padding group created.'

def joint_renamer():
	'''
	This tool renames a selected joint chain.

	select a root joint and run the function.
	- the script will prompt you first for the orientation ('lt', 'rt', 'ct') 
	and the name of the system ('arm', 'back','leg)

	import fischerJohn_riggingTools_cri1_1409
	reload(fischerJohn_riggingTools_cri1_1409)
	fischerJohn_riggingTools_cri1_1409.joint_renamer()
	'''
	# Renaming a joint chain
	import pymel.core as pm

	#Select the root joint, and I will get its children.
	joint_chain = pm.ls(selection=True, dag=True)

	#do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
	    new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	    # Rename command
	    # variable.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)

def priming_tool():
	'''
	import fischerJohn_riggingTools_cri1_1409
	reload(fischerJohn_riggingTools_cri1_1409)
	fischerJohn_riggingTools_cri1_1409.priming_tool()
	'''

	# get selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected', selected
	target_joint = selected[0]

	control_icon_name = target_joint.replace('_bind','_icon')
	local_pad_name = target_joint.replace('_bind', '_local')

	# Create a Control
	# Normal set to x, and radius is 2
	control_icon = pm.circle(normal=[1,0,0], radius=2, name=control_icon_name)[0]

	# Group control (NOT an empty group)
	local_pad = pm.group(name=local_pad_name)

	print 'Control Icon:', control_icon
	print 'Pad Created:', local_pad
	# Move the group (not the control) to target joint.
	# and delete constraint.
	temp_constraint = pm.parentConstraint(target_joint, local_pad)
	pm.delete(temp_constraint)

	# Orient Constraint joint to control
	pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created'
