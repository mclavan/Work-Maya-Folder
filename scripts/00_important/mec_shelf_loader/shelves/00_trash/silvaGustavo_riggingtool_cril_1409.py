'''
Silva Gustavo
rigging_tools.py

Description: A group of rigging related tools.

how to Run:

import silvaGustavo_riggingtool_cril_1409
reload(silvaGustavo_riggingtool_cril_1409)

'''

print 'Rigging Tools Active'

import pymel.core as pm

def tool():

	print 'Tool Active.'

def snapping_tool():
	'''
	this tool moves the first selected object to the second.
	- Translates and Rotates the target object.

	import rigging_tools
	rigging_tools.snapping_tool()
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

	import rigging_tools
	rigging_tools.point_snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	# By default commands work on selected.
	kenny = pm.pointConstraint(selected[0], selected[1])
	pm.delete(kenny)

	print 'The first selected object was moved to the second.'	


def world_icon():
	print 'Icons created.'

	# get selected
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	first_joint = selected[0]

	#create a control icon
	control_icon_1 = pm.circle(normal=[0, 1, 0], radius=2) [0]

	#move the control to the target joint.
	#delete the contstraint
	kenny = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(kenny)

	print 


def joint_renamer():
	'''
	This tool renames a selected joint chain.

	select a root joint and run the function.
	- the script will prompt you first for the orientation ('lt', 'rt', 'ct') 
	and the name of the system ('arm', 'back','leg)

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.joint_renamer()
	'''


	# Creating attributes   
	import pymel.core as pm



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
	    print 'current joint: {0} - new Name: {1}'.format(current, new_name)
	    
	    # Rename comman
	    #variable.rename(new_name)
	    current.rename(new_name)
	    
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'current joint: {0} - new Name: {1}'.format(current, new_name)

	# Rename comman
	#variable.rename(new_name)
	current.rename(new_name)


def hierarchy():
	'''
	create a hierarchy based upon a given system.

	select root joint chain and execte function.

	import rigging_tools
	rigging_tools.hierarchy()

	'''


	'''
	input
	what are we working on?
	the root joint
	'''

	joint_system = pm.ls(selection=True, dag=True)
	#print 'joint system:', joint_system 

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	padding root joint
	'''

	# create empty group
	root_pad = pm.group(empty=True, name='lt_middle_00_pad')

	# move group over to the target joint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# freeze transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	
	# parent root joint to the group
	pm.parent(root_joint, root_pad)
	

	'''
	local controls
	'''
	'''
	control 1 - root_joint
	'''
	# create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_01_icon')[0]

	#Lock and Hide
	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.tz.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=True, keyable=False)
	control_icon_1.sx.set(lock=True, keyable=False)
	control_icon_1.sy.set(lock=True, keyable=False)
	control_icon_1.sz.set(lock=True, keyable=False)
	control_icon_1.v.set(lock=True, keyable=False)
	
	# create a group.
	# grouping control during the process.
	local_pad_1 = pm.group(name='lt_middle_01_local')

	# output control and pad.
	print 'control 1 created:', control_icon_1
	print 'local pad 1 created:', local_pad_1

	# move group over to the target joint.
	# delete constrain after snapping.
	# driver: joint
	# driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)
	
	# orient constrain the joint to the control.
	# driver -> driven.
	# control -> joint
	pm.parentConstraint(control_icon_1, root_joint)




	'''
	control 2
	'''
	# create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2, name='lt_middle_02_icon',)[0]
	
	#Lock and Hide
	control_icon_2.tx.set(lock=True, keyable=False)
	control_icon_2.tz.set(lock=True, keyable=False)
	control_icon_2.ty.set(lock=True, keyable=False)
	control_icon_2.sx.set(lock=True, keyable=False)
	control_icon_2.sy.set(lock=True, keyable=False)
	control_icon_2.sz.set(lock=True, keyable=False)
	control_icon_2.v.set(lock=True, keyable=False)
	


	# create a group.
	# grouping control during the process.
	local_pad_2 = pm.group(name='lt_middle_02_local')

	# output control and pad.
	print 'control 2 created:', control_icon_2
	print 'local pad 2 created:', local_pad_2

	# move group over to the target joint.
	# delete constrain after snapping.
	# driver: joint
	# driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)
	
	# orient constrain the joint to the control.
	# driver -> driven.
	# control -> joint
	pm.parentConstraint(control_icon_2, joint_2)

	


	'''
	control 3
	'''

	# create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2, name= 'lt_middle_03_icon')[0]

	#Lock and Hide
	control_icon_3.tx.set(lock=True, keyable=False)
	control_icon_3.tz.set(lock=True, keyable=False)
	control_icon_3.ty.set(lock=True, keyable=False)
	control_icon_3.sx.set(lock=True, keyable=False)
	control_icon_3.sy.set(lock=True, keyable=False)
	control_icon_3.sz.set(lock=True, keyable=False)
	control_icon_3.v.set(lock=True, keyable=False)
	
	# create a group.
	# grouping control during the process.
	local_pad_3 = pm.group(name='lt_middle_03_local')

	# output control and pad.
	print 'control 3 created:', control_icon_3
	print 'local pad 3 created:', local_pad_3

	# move group over to the target joint.
	# delete constrain after snapping.
	# driver: joint
	# driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)
	
	# orient constrain the joint to the control.
	# driver -> driven.
	# control -> joint
	pm.parentConstraint(control_icon_3, joint_3)

	
	'''
	parent control together.
	'''

	#pad 3 (last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)







	print 'hierarchy created.'


