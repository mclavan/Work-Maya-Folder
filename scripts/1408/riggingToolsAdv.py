'''
Michael Clavan
riggingToolsAdv.py

'''

import pymel.core as pm 

def create_foot_box(ori='lt', name='leg'):
	mel_line = 'curve -d 1 -p 1.14396 0.75611 2.50585 -p -1.14396 0.75611 2.50585 -p -1.14396 -0.75611 2.50585 -p 1.14396 -0.75611 2.50585 -p 1.14396 0.75611 2.50585 -p 1.14396 0.75611 -2.50585 -p 1.14396 -0.75611 -2.50585 -p 1.14396 -0.75611 2.50585 -p 1.14396 -0.75611 -2.50585 -p -1.14396 -0.75611 -2.50585 -p -1.14396 0.75611 -2.50585 -p 1.14396 0.75611 -2.50585 -p -1.14396 0.75611 -2.50585 -p -1.14396 0.75611 2.50585 -p -1.14396 -0.75611 2.50585 -p -1.14396 -0.75611 -2.50585 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
	mel_control_icon = pm.mel.eval(mel_line)
	control_icon = pm.nt.Transform(mel_control_icon)
	control_icon.rename('{0}_{1}_icon'.format(ori, name))
	return control_icon

def create_arrow(ori='lt', name='knee'):
	mel_line = 'curve -d 1 -p 0.263191 0 0.316802 -p 0.780247 0 0.614862 -p 0.0435555 0 -0.614862 -p -0.780247 0 0.614862 -p -0.263191 0 0.316802 -p -0.263191 0 1.316802 -p 0.263191 0 1.316802 -p 0.263191 0 0.316802 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	mel_control_icon = pm.mel.eval(mel_line)
	control_icon = pm.nt.Transform(mel_control_icon)
	control_icon.rename('{0}_{1}_icon'.format(ori, name))
	return control_icon

def setup():
	'''
	import riggingToolsAdv
	reload(riggingToolsAdv)
	riggingToolsAdv.setup()
	'''

	scene_file = "/Users/mclavan/Desktop/04_yeti_RFL_code.ma"
	pm.openFile(scene_file, force=True)

	leg_root = 'lt_leg_01_bind'
	rfl_root = 'lt_heel_RFL'
	pm.select(leg_root, rfl_root, r=True)
	rfl_builder()




def rfl_builder():

	'''
	Getting selected
	The leg and rfl system should already exist and be named correctly.
	The user will selected the leg root followed by the rfl root joint.
		1st selected is leg root. 
		2nd selected is the rfl root. 
	'''
	# Get Leg and RFL root joint.
	selected_joints = pm.ls(selection=True)
	leg_joints = pm.ls(selected_joints[0], dag=True)
	rfl_joints = pm.ls(selected_joints[1], dag=True)

	# string method (split)
	ori = leg_joints[0].split('_')[0]

	'''
	Leg System 
	'''
	# Build IK system

	ankle_ik = pm.ikHandle(startJoint=leg_joints[0], endEffector=leg_joints[2], 
		solver='ikRPsolver', name='{0}_ankle_ik'.format(ori))[0]
	ball_ik = pm.ikHandle(startJoint=leg_joints[2], endEffector=leg_joints[3],
		solver='ikSCsolver', name='{0}_ball_ik'.format(ori))[0]
	toe_ik = pm.ikHandle(startJoint=leg_joints[3], endEffector=leg_joints[4],
		solver='ikSCsolver', name='{0}_toe_ik'.format(ori))[0]	

	'''
	RFL System
	'''
	# Parent IKs to their respetive rfl joint.
	pm.parent(ankle_ik, rfl_joints[-1])
	pm.parent(ball_ik, rfl_joints[-2])
	pm.parent(toe_ik, rfl_joints[-3])


	# '''
	# RFL Controls
	# - Controls should a two step process. 
	# 	1) Create controls and allow the user to size controls. 
	# 	2) Use continue with rest of the process. 
	# * Note
	# 	- An added feature would be letting the user choose their own control icons.
	# '''

	# Leg box and knee control
	knee_icon = create_arrow(ori)
	leg_icon = create_foot_box(ori)
	print 'Leg Box: {0} and Knee: {1}'. format(type(leg_icon), type(knee_icon))

	# Move knee into position
	# This might be nice to position interactly.


	heel_icon = pm.circle(name='{0}_heel_icon'.format(ori))[0]
	inner_icon = pm.circle(name='{0}_innerBank_icon'.format(ori))[0]
	outer_icon = pm.circle(name='{0}_outerBank_icon'.format(ori))[0]
	toe_icon = pm.circle(name='{0}_toe_icon'.format(ori))[0]
	ball_icon = pm.circle(name='{0}_ball_icon'.format(ori))[0]

	global leg_joints, rfl_joints, leg_icons
	leg_icons = [knee_icon, leg_icon, heel_icon, outer_icon, inner_icon, toe_icon, ball_icon]


	# This will be a pausing area.  Let the user deside the overall position.
	# auto_clean_up_icons()

def finalize_leg_system(leg_joints, rfl_joints, leg_icons, ori='lt'):

	# Parent RFL Controls
	knee_icon = leg_icons[0]
	leg_icon = leg_icons[1]
	heel_icon = leg_icons[2]
	outer_icon = leg_icons[3]
	inner_icon = leg_icons[4]
	toe_icon = leg_icons[5]
	ball_icon = leg_icons[6]

	pm.parent(ball_icon, toe_icon)	
	pm.parent(toe_icon, inner_icon)
	pm.parent(inner_icon, outer_icon)
	pm.parent(outer_icon, heel_icon)
	pm.parent(heel_icon, leg_icon)
	
	# Constrain the RFL joints to the RFL controls.
	pm.parentConstraint(heel_icon, rfl_joints[0], maintainOffset=True)
	pm.parentConstraint(inner_icon, rfl_joints[1], maintainOffset=True)
	pm.parentConstraint(outer_icon, rfl_joints[2], maintainOffset=True)
	pm.parentConstraint(toe_icon, rfl_joints[3], maintainOffset=True)
	pm.parentConstraint(ball_icon, rfl_joints[4], maintainOffset=True)

	# Group systems together
	# pm.select(cl=True)
	rfl_grp = pm.group(leg_icons[1], leg_icons[0], rfl_joints[0], name='{0}_rfl_grp'.format(ori))
	print 'RFL Group: {0}'.format(rfl_grp)


def auto_clean_up_icons():
	clean_up_icons(leg_joints, rfl_joints, leg_icons)
	finalize_leg_system(leg_joints, rfl_joints, leg_icons)

def clean_up_icons(leg_joints, rfl_joints, leg_icons):
	
	# Snaps the pivot points for each control icon to the target_joint
	target_joints = [leg_joints[2]]
	target_joints.extend(rfl_joints[0:-1])

	print 'Target Joints: {0}'.format(target_joints)

	for i, current_icon in enumerate(leg_icons[1:]):
		print 'Working on Icon: {0} --> {1}'.format(current_icon, target_joints[i])
		joint_pivots = target_joints[i].getPivots(worldSpace=True)
		current_icon.setPivots(joint_pivots[0], worldSpace=True)

	# Make sure to clean each control.
	pm.makeIdentity(leg_icons, apply=True, t=1, r=1, s=1, n=0)
	pm.delete(leg_icons, ch=True)


def create_leg_controls(leg_joints, rfl_joints):
	'''
	RFL Controls
	- Controls should a two step process. 
		1) Create controls and allow the user to size controls. 
		2) Use continue with rest of the process. 
	* Note
		- An added feature would be letting the user choose their own control icons.
	'''

	# Leg box and knee control
	knee_icon = create_arrow()
	leg_box = create_foot_box()
	print 'Leg Box: {0} and Knee: {1}'. format(type(leg_box), type(knee_icon))

	# Move knee into position
	# This might be nice to position interactly.	




	

