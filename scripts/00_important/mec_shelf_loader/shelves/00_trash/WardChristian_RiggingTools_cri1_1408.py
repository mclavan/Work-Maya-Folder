'''
Christian Ward
wardChristian_RiggingTools_cri1_1408.py

Description:
	Contains Rigging Tools.

How to Run:

import wardChristian_RiggingTools_cri1_1408
reload(wardChristian_RiggingTools_cri1_1408)

'''

print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy():
	'''

	Create a hierarchy based upon given system.

	Select root joint chain and execute function.

	import wardChristian_RiggingTools_cri1_1408
	wardChristian_RiggingTools_cri1_1408.hierarchy()
	'''

	'''
	Input
	What are working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'joint System', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''
	root_pad = pm.group(empty=True)

	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	pm.makeIdentity(root_pad,apply=True, t=1, r=1, s=1, n=0)

	pm.parent(root_joint, root_pad)



	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	local_pad_1 = pm.group()

	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	pm.orientConstraint(control_icon_1, root_joint)


	'''
	Control 2
	'''

	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	local_pad_2 = pm.group()

	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''

	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	local_pad_3 = pm.group()

	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together.
	'''

	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print "Hierarchy created."

def padding_tool():
	'''
	import wardChristian_RiggingTools_cri1_1408
	reload(wardChristian_RiggingTools_cri1_1408)
	wardChristian_RiggingTools_cri1_1408.padding_tool()
	'''

	selected = pm.ls(selection=True)
	root_joint = selected[0]

	pad = pm.group(empty=True)

	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	pm.parent(root_joint, pad)

	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created'

def lock_and_hide():

	select_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon


	print 'Channels loced and hidden.'

def lock_and_hide_trans():

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

def unlock_and_show_trans():

	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon

	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)
	print 'Channels locked and hidden.'

def unlock_and_show_rotate():

	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control: ', control_icon

	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)
	print 'Channels locked and hidden.'

def priming_tool():
	selected_joints = pm.ls(selection=True)

	for current_joint in selected_joints:
			print 'Current Control:', current_joint

			icon_name = current_joint.replace('_bind', '_icon')

			local_pad_name = current_joint.replace('_bind', '_local')

			control_icon = pm.circle(normal=[1, 0, 0], radius=1.8)[0]

			local_pad = pm.group(control_icon)

			kenny = pm.parentConstraint(current_joint, local_pad)

			pm.delete(kenny)

			pm. orientContraint(control_icon, current_joint)



'''
Constraints


pm.parentConstraint('driver', 'driven')
pm.parentConstraint('driver', 'driven', maintainOffset=False)

parentConstraint -mo -weight 1;
pm.parentConstraint('driver', 'driven', mo=True)
'''

def joint_renamer():
	'''
	Renames all joints of a joint hierarchy.

	Select the root joint and execute the function.


	import wardChristian_RiggingTools_cri1_1408
	reload(wardChristian_RiggingTools_cri1_1408)
	wardChristian_RiggingTools_cri1_1408.joint_renamer()
	'''

	joints = pm.ls(selection=True, dag=True)

	'''
	Naming convention
	orientation
	name
	count
	suffix
	lt_arm_01_bind -> lt_arm_03_waste
	'''
	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'bind'


	for current_joint in joints:
	
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

		print 'Name Changes:', new_name

		current_joint.rename(new_name)

		count = count + 1


joints = pm.ls(selection=True)


for current_joint in joints[0:-1]:
    
    icon_name = current_joint.replace('_bind', '_icon')
    pad_name = current_joint.replace('_bind', '_pad')

    control_icon = pm.circle(name = icon_name, radius=1.8, normal=[1,0,0])[0]
    
    pad = pm.group(name = pad_name)
    
    kenny = pm.parentConstraint(current_joint, pad)
    
    pm.delete(kenny)
    