'''
Andrew Lopez
lopezAndrew_riggingTools_cri1_1409.py

Description:
	Tools to assist in maya rigging.

How to Run:

import lopezAndrew_riggingTools_cri1_1409
reload(lopezAndrew_riggingTools_cri1_1409)

'''
print 'Rgging Tools Active'

import pymel.core as pm

def hiearchy():
	'''
	Create a hiearchy based upon given system.

	Select root joint chain and execute function
	
	import lopezAndrew_riggingTools_cri1_1409
	lopezAndrew_riggingTools_cri1_1409.hiearchy()
	'''

	'''
	Input
	What are we working on?
		The root joint.
	'''

	joint_system = pm.ls(selection=True, dag=True)
	print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding root joint
	'''

	#C reate empty group
	root_pad = pm.group(em=True)
	# Move group over to target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)
	# Freeze Transforms on group
	pm.makeIdentity(root_pad, apply=True, translate=1, rotate=1, scale=1, normal=0)
	# Parent root joint to group
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''

	'''
	Control 1 - root_joint
	'''

	# Create a control
	# normal = [1, 0, 0]
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control duing process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 Created', control_icon_1
	print 'Local Pad 1 Created', local_pad_1

	# Move group to target joint
	# Delete constraint after snapping.
	# Driver: Joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1) 
	pm.delete(temp_constraint)

	# Orient constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''

	# Create a control
	# normal = [1, 0, 0]
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control duing process.
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 2 Created', control_icon_2
	print 'Local Pad 2 Created', local_pad_2

	# Move group to target joint
	# Delete constraint after snapping.
	# Driver: Joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2) 
	pm.delete(temp_constraint)

	# Orient constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''

	# Create a control
	# normal = [1, 0, 0]
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control duing process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 Created', control_icon_3
	print 'Local Pad 3 Created', local_pad_3

	# Move group to target joint
	# Delete constraint after snapping.
	# Driver: Joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3) 
	pm.delete(temp_constraint)

	# Orient constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together.
	'''
	pm.parent(control_icon_2, control_icon_3)
	pm.parent(control_icon_1, control_icon_2)
	

	print 'Hiearchy Created'


def padding_tool():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	pad = pm.group(em=True)

	# Move group to joing
	#		and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply = True, t=1,r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	print 'Padding group created'

def joint_renamer():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.joint_renamer()
	'''
	import pymel.core as pm

	# Select the root joints and I will get its children
	joint_chain = pm.ls(selection=True, dag=True)

	#Do not worry about the waste suffix.
	#ori_name_count_suffix
	#lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'
	for current in joint_chain:
	    new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	    # Rename command
	    # varible.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	current.rename(new_name)

	print 'Joint Renamer - Active'

def priming_tool():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.priming_tool()
	'''

	# Get Selected
	selected =pm.ls(selection=True)
	print 'Joints Selected'

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create Control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1,0,0], radius=1.8, name=control_icon_name)[0]

		# Group contol (not an empty group)
		local_pad = pm.group(n=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		# 	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)




	print 'Local Oriented Controls Created'

def change_color_blue():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.change_color_blue()
	'''

	import pymel.core as pm
	# Getting the selected Object
	selected =pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object', first_selected

	# Will change selected objects color to blue
	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)	

def change_color_red():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.change_color_red()
	'''

	import pymel.core as pm
	# Getting the selected Object
	selected =pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object', first_selected

	# Will change selected objects color to red
	first_selected.overrideEnabled.set(1)
	red = 13
	first_selected.overrideColor.set(red)	

def lock_and_hide_translate():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.lock_and_hide_translate()
	'''

	import pymel.core as pm
	# Getting the selected Object
	selected =pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object', first_selected

	# Will lock and hide selected object's translate attributes
	first_selected.tx.set(lock=True, keyable=False)
	first_selected.ty.set(lock=True, keyable=False)
	first_selected.tz.set(lock=True, keyable=False)

def lock_and_hide_rotate():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.lock_and_hide_rotate()
	'''

	import pymel.core as pm
	# Getting the selected Object
	selected =pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object', first_selected

	# Will lock and hide selected object's rotate attributes
	first_selected.rx.set(lock=True, keyable=False)
	first_selected.ry.set(lock=True, keyable=False)
	first_selected.rz.set(lock=True, keyable=False)

def lock_and_hide_scale():
	'''
	import lopezAndrew_riggingTools_cri1_1409
	reload(lopezAndrew_riggingTools_cri1_1409)
	lopezAndrew_riggingTools_cri1_1409.lock_and_hide_scale()
	'''

	import pymel.core as pm
	# Getting the selected Object
	selected =pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object', first_selected

	# Will lock and hide selected object's scale attributes
	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)
