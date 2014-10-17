'''
Michael Clavan
lecture10_padding.py

Description:
	Padding Tool

How To Run:

import lecture10_padding_student
reload(lecture10_padding_student)
lecture10_padding_student.padding_tool()

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


	# Snap pad to joint


	# Freeze Transfroms


	# Parent.

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
	clusters = []
	for current_cv in curve_cvs:

		print 'Cluster Created:', new_cluster
		print counter, ': Selected Item:', current_cv


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

		print 'Right Icons Colored RED.'

	print 'We are looping!'



