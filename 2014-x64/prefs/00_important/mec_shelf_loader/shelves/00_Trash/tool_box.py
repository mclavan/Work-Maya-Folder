'''
Aaron Stoll

tool_box.py

Description:

Need:
padding
# renaming
primming
hierarchy


How to run:

import tool_box
reload(tool_box)
'''
import pymel.core as pm
print 'Tool Box Open'


def padding_tool():
	'''
	This tool creates a world pad on the selected joint system.

	Select the root and run the function.

	import tool_box
	reload(tool_box)
	tool_box.padding_tool()
	'''
	selected = pm.ls(selection=True)


	# print 'Current Selected', selected
	root_joint = selected[0]

	#create empty group
	pad = pm.group(empty=True)
	# pm.group(empty=true)
	# need to move the group to the joints
	kenny = pm.pointConstraint(root_joint, pad)
	# delete the constraint. kill kenny
	pm.delete(kenny)
	# freeeze transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	# then parent
	pm.parent(root_joint, pad)
	# need a new name
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)
	
	print 'Padding Group Created'

def priming_tool():
	'''
	This tool will create locally oriented controls
	able to control the joints of a system.

	import tool_box
	reload(tool_box)
	tool_box.priming_tool()
	''' 
	# get selected
	selected = pm.ls(selection=True)
	print 'Joints Selected', selected

	last_control = ''

	for target_joint in selected:

		# target_joint = selected[0] 

		# create a control
		# normal set to x
		# radius is 1
		
		control_icon = pm.circle(normal=[1,0,0], radius=1.8)[0]
		control_icon_name = target_joint.replace('_bind', '_icon')
		control_icon = control_icon.rename(control_icon_name)
		
		# group control (not empty)
		local_pad = pm.group()
		local_pad_name = target_joint.replace('_bind', '_local')
		local_pad = local_pad.rename(local_pad_name)
		print 'Control Icon', control_icon
		print 'Pad created:', local_pad
		# move group not control to target joint 
		kenny = pm.parentConstraint(target_joint, local_pad)
		# kill kenny
		pm.delete(kenny)
		# need to orient constraint
		pm.orientConstraint(control_icon, target_joint)

		# parent controls last control must = nothing. ex. last_control = ''

		if last_control != '':
			pm.parent(local_pad, last_control)
		last_control = control_icon



	print 'Local Oriented Controls Created'

def renaming_tool():
	'''
	this tool will rename the joints in the joint chain.
	
	Create a function called joint rename
	select root joint, loop through all joint in joint chain
	'ori_name_count_suffix'
	ct_back_01_bind
	
	how to run:
	import book
	reload(book)
	tool_box.renaming_tool()
	'''

	# what am i working on
	# get all joints in joint chain
	#renaming joints- function will rename joints in joint chain

	selected_joints = pm.ls(selection=True, dag=True)

	print 'selected joints', selected_joints
	# build new name
	# ori
	# name
	# count
	# suffix

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'
	for selected_joint in selected_joints:

	

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print 'Joint Name:', new_name
		count = count + 1
		selected_joint.rename(new_name)

	
	new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count-1, 'waste')

	print 'Joint Name:', new_name
	count = count + 1
	selected_joint.rename(new_name)
	print 'Joint Chain Renamed'


def hierarchy():
	'''
	This function creates a hierarchy for the given system

	select the root joint and run this fucntion.

	import tool_box
	reload(tool_box)
	tool_box.hierarchy():
	'''
	print 'Hierarchy Generation'


	# user will select the root joint and the tool 
	# 	will apply the systems

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'
	'''
	# pad root joint
	'''
	# create an empty group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad 

	# move group to target joint 
	# point contraint group to root joint
	# 			maintain offet off (Snapping)

	kenny = pm.pointConstraint(root_joint, pad) 

	#  kill kenny (delete the contraint)
	pm.delete(kenny)


	# freeze transforms 
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)


	# parent root joint to group 
	pm.parent(root_joint, pad)

	 
	# create local oriented control for each joint
	# lt_middle_01_bind,lt_middle_02_bind,lt_middle_03_bind


	# create control (circle)
	root_icon = pm.circle(name='lt_middle_01_icon', normal=[1,0,0])[0]

	# delete history
	pm.delete(root_icon, ch=True)

	# create a group (not empty)
	#	this will automatically parent the control under the group 
	root_local = pm.group(name='lt_middle_01_local')

	# move group to target joint
	kenny = pm.parentConstraint(root_joint, root_local)

	# use parent contraint driver = joint, driven = control 
	# maintaint offset off (Snapping)
	# kill kenny 
	pm.delete(kenny)

	 
	# orient contraint joint: driver- control, driven- joint. 
	pm.orientConstraint(root_icon, root_joint)

	# second joint---------------------------------------

	second_icon = pm.circle(name='lt_middle_02_icon',normal=[1,0,0])[0]
	pm.delete(second_icon, ch=True)
	second_local = pm.group(name='lt_middle_02_local')
	kenny = pm.parentConstraint(second_joint, second_local)
	pm.delete(kenny)

	pm.orientConstraint(second_icon, second_joint)

	#third Joint----------------------------------

	third_icon = pm.circle(name='lt_middle_03_icon',normal=[1,0,0])[0]
	pm.delete(third_icon, ch=True)
	third_local = pm.group(name='lt_middle_03_local')
	kenny = pm.parentConstraint(third_joint, third_local)
	pm.delete(kenny)

	pm.orientConstraint(third_icon, third_joint)

	#parenting the icons 
	# child- parent ex. second icon, root icon

	pm.parent(third_local, second_icon)
	pm.parent(second_local, root_icon)

	print'Controls Established'