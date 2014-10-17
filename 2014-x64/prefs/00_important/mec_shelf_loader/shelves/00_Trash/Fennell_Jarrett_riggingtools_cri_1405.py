'''
Jarrett Fennell
Fennell_Jarrett_riggingtools_cri_1405.py

Description:
A scripting book of functions


How to Run:

import Fennell_Jarrett_riggingtools_cri_1405
reload (Fennell_Jarrett_riggingtools_cri_1405)

'''


import pymel.core as pm
print 'Here are my Rigging Tools'

def joint_rename():
	''' 
	#create a function called joint_rename
	# select the root joint and loop through all joints in the joint chain
	# 'ori_name_count_suffix'
	# 'ct_back_o1_bind'
	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.joint_rename();

	'''

	#what am I working on?
	#get all joints in a selected joint chain

	joint_chain = pm.ls(selection=True, dag=True)
	print 'Item Selected:', joint_chain
	
	#build our new name.
	#'lt'
	#'arm'
	#'01'
	#'bind'

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'
	for current_joint in joint_chain:
		
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		
		print 'Joint Name:', new_name

		count = count + 1

		current_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)


	print 'Joint Chain Renamed'

def hierarchy():
	'''
	This tool will create a pad on the root joint, then create an 
	icon for each joint except the end joint, then create a hierarchy 
	and rename the icons for their associated joint. 
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.hierarchy();
	'''
	
	# The user will select the root joint and the tool.
	# will apply the systems.

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# pad the root joint.
	'''

	# Creat an empty group.
	pad = pm.group(empty=True, name = 'lt_middle_00_pad')
	print 'Root Pad Created:', pad


	# Move group to root joint.
	# Point constrain group to root joint.
	# Offset off (snapping)

	temp = pm.pointConstraint(root_joint, pad)



	# Delete contraint
	pm.delete(temp)

	# Freeze transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group

	pm.parent(root_joint, pad)

	# Create a local oriented control for each joint.
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind

	# Create control (circle)
	control_icon1 = pm.circle(name = 'lt_middle_01_icon', radius=1.2, normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	icon1 = pm.group(name='lt_middle_01_pad')




	# This will automatically parent the control under the group

	# Move Group to the target joint
	temp = pm.pointConstraint(root_joint, icon1)
	pm.delete(temp)

	# Use a parent constrain driver is the joint where driven is the group
	temp = pm.parentConstraint(root_joint, icon1)


	# Offset is off (snapping)

	# Delete the constraint
	pm.delete(temp)

	# Delete history on control
	pm.delete(icon1, ch=True)

	# Orient Constraint driver: control driven: joint

	#repeat for the following joints and icons
	#note the change in joint and icon number

	pm.orientConstraint(control_icon1, root_joint)

	control_icon2 = pm.circle(name = 'lt_middle_02_icon', radius=1.2, normal=[1,0,0])[0]
	icon2 = pm.group(name='lt_middle_02_pad')
	temp = pm.pointConstraint(second_joint, icon2)
	pm.delete(temp)
	temp = pm.parentConstraint(second_joint, icon2)
	pm.delete(temp)
	pm.delete(icon2, ch=True)
	pm.orientConstraint(control_icon2, second_joint)

	pm.parent(icon2, control_icon1)

	control_icon3 = pm.circle(name = 'lt_middle_03_icon', radius=1.2, normal=[1,0,0])[0]
	icon3 = pm.group(name='lt_middle_03_pad')
	temp = pm.pointConstraint(third_joint, icon3)
	pm.delete(temp)
	temp = pm.parentConstraint(third_joint, icon3)
	pm.delete(temp)
	pm.delete(icon3, ch=True)
	pm.orientConstraint(control_icon3, third_joint)

	pm.parent(icon3, control_icon2)

def padding_tool():
	'''
	This tool creates a pad on the root joint of a joint chain hierarchy

	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.padding_tool();


	'''
	selected = pm.ls(selection=True)
	#print 'Current Selected:', selected
	root_joint = selected[0]

	#create empty group
	#empty =True to create empty group

	pad= pm.group(empty=True)

	#move the group to the joint
	#delete constraint
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	#freeze transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#parent joint to group
	pm.parent(root_joint, pad)

	#rename
	#ct_tail_01_bind
	#ct_tail_00_pad

	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created'

def priming_tool():
	'''

	This tool makes a local oriented control and pad on the selected joint systems

	select the joints and execute the command

	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)
	Fennell_Jarrett_riggingtools_cri_1405.priming_tool();
	'''

	#get selected joints
	selected_joints = pm.ls(selection=True)

	#loop through current selected
	for current_joint in selected_joints:
		#create control icon
		control_icon = pm.circle(normal=[1, 0, 0])[0]

		print 'control created', control_icon

		#create group and group the icon along with it

		local_pad = pm.group()
		#parent constrain the group to the joint

		temp = pm.parentConstraint(current_joint, local_pad)	
		#delete the constraint
		pm.delete(temp)

		#connect the control to the joint
		pm.orientConstraint(control_icon, current_joint)


		#rename the control and pad to match the joint
		new_control_name = current_joint.replace('_bind', '_icon',)
		new_pad_name = current_joint.replace('_bind', '_local')
		control_icon.rename(new_control_name)
		local_pad.rename(new_pad_name)

def lock_hide_fk():
	''' 
	#this function will lock and hide all necessary channel on a fk system

	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.lock_hide_fk();

	'''
	selected = pm.ls(selection=True)
	print 'Current Selection:', selected

	for current_item in selected:
	    current_item.tx.set(lock=True, keyable=False)
	    current_item.ty.set(lock=True, keyable=False)
	    current_item.tz.set(lock=True, keyable=False)
	    current_item.sx.set(lock=True, keyable=False)
	    current_item.sy.set(lock=True, keyable=False)
	    current_item.sz.set(lock=True, keyable=False)
	    current_item.v.set(lock=True, keyable=False)

def lock_hide_ik():
	''' 
	#this function will lock and hide all necessary channel on a ik system

	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.lock_hide_ik();

	'''
	selected = pm.ls(selection=True)
	print 'Current Selection:', selected

	for current_item in selected:
	    current_item.rx.set(lock=True, keyable=False)
	    current_item.ry.set(lock=True, keyable=False)
	    current_item.rz.set(lock=True, keyable=False)
	    current_item.sx.set(lock=True, keyable=False)
	    current_item.sy.set(lock=True, keyable=False)
	    current_item.sz.set(lock=True, keyable=False)
	    current_item.v.set(lock=True, keyable=False)

def unlock_unhide_fk():
	''' 
	#this function will unlock and unhide all necessary channels on a fk system

	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.unlock_unhide_fk();

	'''
	selected = pm.ls(selection=True)
	print 'Current Selection:', selected

	for current_item in selected:
	    current_item.tx.set(lock=False, keyable=True)
	    current_item.ty.set(lock=False, keyable=True)
	    current_item.tz.set(lock=False, keyable=True)
	    current_item.sx.set(lock=False, keyable=True)
	    current_item.sy.set(lock=False, keyable=True)
	    current_item.sz.set(lock=False, keyable=True)
	    current_item.v.set(lock=False, keyable=True)

def unlock_unhide_ik():
	''' 
	#this function will unlock and unhide all necessary channels on a ik system
	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.unlock_unhide_ik();

	'''
	selected = pm.ls(selection=True)
	print 'Current Selection:', selected

	for current_item in selected:
	    current_item.rx.set(lock=False, keyable=True)
	    current_item.ry.set(lock=False, keyable=True)
	    current_item.rz.set(lock=False, keyable=True)
	    current_item.sx.set(lock=False, keyable=True)
	    current_item.sy.set(lock=False, keyable=True)
	    current_item.sz.set(lock=False, keyable=True)
	    current_item.v.set(lock=False, keyable=True)


def blue_icon():
	''' 
	This tool will color an asset blue 
	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.joint_rename();

	'''
	selected_icon = pm.ls(selection=True)
	
	for current_icon in selected_icon:
		
		first_selected = selected_icon[0]

		print 'first selected icon:', first_selected
		first_selected.overrideEnabled.set(1)
		first_selected.overrideColor.set(6)


def red_icon():
	''' 
	This tool will color an icon blue 
	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.red_icon();

	'''
	selected_icon = pm.ls(selection=True)
	
	for current_icon in selected_icon:
		
		first_selected = selected_icon[0]

		print 'first selected icon:', first_selected
		first_selected.overrideEnabled.set(1)
		first_selected.overrideColor.set(13)


def yellow_icon():
	''' 
	This tool will color an icon blue 
	
	import Fennell_Jarrett_riggingtools_cri_1405
	reload (Fennell_Jarrett_riggingtools_cri_1405)

	Fennell_Jarrett_riggingtools_cri_1405.yellow_icon();

	'''
	selected_icon = pm.ls(selection=True)
	
	for current_icon in selected_icon:
		
		first_selected = selected_icon[0]

		print 'first selected icon:', first_selected
		first_selected.overrideEnabled.set(1)
		first_selected.overrideColor.set(17)

		


	