'''
Michael Clavan
lecture10_padding.py

Description:
	Padding Tool

How To Run:

import lecture10_padding
reload(lecture10_padding)
lecture10_padding.padding_tool()

'''

print 'Padding Tool Active'

import pymel.core as pm 

def padding_tool():
	'''
	Based on the select joint this tool will 
		create a world oriented group or 
		pad and parent the selected joint 
		to the pad. 

	1) Select the root joint of a system.
	2) Activate the tool. 
	'''

	'''
	Input
	'''	
	# Get the first select joint.
	root_joint = pm.ls(selection=True)[0]

	'''
	Process
	'''
	# Group
	pad = pm.group(empty=True)

	# Snap pad to joint
	temp_constraint = pm.pointConstraint(root_joint, pad, maintainOffset=False)
	pm.delete(temp_constraint)

	# Freeze Transfroms
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent.
	pm.parent(root_joint, pad)

	'''
	Output
	'''
	print 'Pad Created', pad, ' on Root Joint:', root_joint
	# print 'Joint Pad Created.'

def loop_testing():

	'''
	Given/Input
	'''
	# Selected objects in the scene
	selected_items = pm.ls(selection=True)

	'''
	Process
	'''
	counter = 1
	# I want to know all the thing selected in the scene.
	for current_item in selected_items:
		print counter, ': Selected Item:', current_item
		counter = counter + 1

	print 'We are looping!'

def loop_testing_clusters():

	'''
	Given/Input
	'''
	# Get CVS on a selected curve.
	selected_curve = pm.ls(selection=True)[0]
	curve_cvs = selected_curve.cv



	'''
	Process
	'''
	counter = 1
	# I want to know all the thing selected in the scene.
	for current_cv in curve_cvs:
		new_cluster = pm.cluster(current_cv, relative=False)
		print 'Cluster Created:', new_cluster
		print counter, ': Selected Item:', current_cv
		counter = counter + 1

	print 'We are looping!'

def loop_testing_2():

	'''
	Given/Input
	'''
	# Selected objects in the scene
	selected_items = pm.ls(selection=True)

	# Get Control icons in the scene.
	control_icons = pm.ls('*_icon')
	lt_control_icons = pm.ls('lt_*_icon')
	rt_control_icons = pm.ls('rt_*_icon')

	selected_icons = pm.ls('*_icon', selection=True)



	'''
	Process
	'''
	# I want to know all the thing selected in the scene.
	for current_item in rt_control_icons:
		current_item.overrideEnabled.set(1)
		current_item.overrideColor.set(13)
		print 'Right Icons Colored RED.'
		current_item.tx.set(keyable=False, lock=True)
	print 'We are looping!'


def joint_renaming():
	'''
	orientation = 'lt', 'rt', or 'ct'
	system_name = 'arm', 'back', 'leg'
	counter = 1
	suffix = 'bind', 'waste'

	'lt_arm_01_bind'
	'ct_back_04_bind'
	'rt_arm_03_waste'

	'''

	'''
	'lt'+'arm'
	'ltarm'
	'lt' + '_' +'arm'
	'lt_arm'
	'''



	'''
	Given/Input
	'''
	# Selected objects in the scene
	selected_items = pm.ls(selection=True)

	'''
	Process
	'''
	orientation = raw_input()
	system_name = raw_input()
	counter = 1
	suffix = 'bind'

	# orienation + system_name + counter + suffix
	# orientation + '_' + system_name + '_' + str(counter) + '_' + suffix
	# 'lt_arm_1_bind'

	
	binding_joints = selected_items[0:-1]
	# I want to know all the thing selected in the scene.
	for current_item in binding_joints:
		new_name = '{0}_{1}_0{2}_{3}'.format(orientation, system_name, counter, suffix)
		print counter, ': Selected Item:', current_item, new_name
		counter = counter + 1
		current_item.rename(new_name)

	print 'We are looping!'

	suffix = 'waste'
	new_name = '{0}_{1}_0{2}_{3}'.format(orientation, system_name, counter, suffix)
	selected_items[-1].rename(new_name)
