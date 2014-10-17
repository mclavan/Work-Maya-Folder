'''
Ethan Holbert
holbertEthan_riggingTools_cri1_1408.py

Description:
	This script contains a series of rigging tools.


How to Run:

import holbertEthan
reload(holbertEthan)


'''

print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy
	
	selected_joints = pm.ls(selection=True)
	root_joint = selected_joints[0]
	joint_system = pm.ls(root_joint, dag=True)

	print 'Back System', joint_system

def padding_tool():
	'''

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create an empty group
	pad = pm.group(empty=True)
	
	# Move group to join.
	# and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# Renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def lock_and_hide():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon


	print 'Channels locked and hidden'

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
	print 'Channels locked and hidden'

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
	print 'Channels locked and hidden'

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
	print 'Channels locked and hidden'

def priming_tool():

	# Get selected joints.
	selected_joints = pm.ls(selection=True)

	for current_joint in selected_joints:
		print 'Current Control:', current_joint
		# Create a control icon
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8)[0]

		# Create a group (parenting the control under the group)
		local_pad = pm.group(control_icon)

		# Move the group to the target joint
		

		# Connect control to group








