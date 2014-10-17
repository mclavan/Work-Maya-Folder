'''
Jannatul Hossain
HossainJannatul_riggingTools_cri1_1408.py

Description:
	This scrip contains a series of rigging tools.
	hierarchy
	lock_and_hide
	lock_and_hide_trans
	lock_and_hide_roate
	priming_tool
	joint_renamer
	padding_tool
	separator_attribute





How to Run:
import HossainJannatul_riggingTools_cri1_1408
reload(HossainJannatul_riggingTools_cri1_1408)


'''

print 'Rigging Tools Active'

import pymel.core as pm 

def hierarchy():

	''''
	Create a hierarchy based upon a given system.
	
	Select root joint chain and execute fuction.
	
	
	
	How to Run:
	
		import HossainJannatul_riggingTools_cri1_1408
		HossainJannatul_riggingTools_cri1_1408.hierarchy()
	'''
	
	'''
	Input
		what are we working on?
		The root joint.
	
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint Syste:', joint_system
	
	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	
	'''
	Padding Root Joint
	'''
	
	# Create empty group 
	root_pad = pm.group (empty=True)
	
	
	# Move group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint , root_pad)
	pm.delete(temp_constraint)
	
	# Freeze Transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	
	# Parent root joint to the group.
	pm.parent(root_joint,root_pad)
	'''
	Local Controls
	'''
	'''
	Control 1- root_joint
	'''
	# create a control.
	# normal = [1, 0, 0], radius = 2
	control_icon_1 = pm.circle(normal = [1, 0, 0], radius = 2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group ()

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete the constrain after snapping.
	# Driver: joint
	# Driven : group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	#Driver -> Driven.
	# Control-> Joint
	pm.orientConstraint(control_icon_1, root_joint)



	'''
	Control 2 -joint_2
	'''

	# create a control.
	# normal = [1, 0, 0], radius = 2
	control_icon_2 = pm.circle(normal = [1, 0, 0], radius = 2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2= pm.group ()

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete the constrain after snapping.
	# Driver: joint
	# Driven : group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	#Driver -> Driven.
	# Control-> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3 - joint_3
	'''
	# create a control.
	# normal = [1, 0, 0], radius = 2
	control_icon_3 = pm.circle(normal = [1, 0, 0], radius = 2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3= pm.group ()

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete the constrain after snapping.
	# Driver: joint
	# Driven : group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	#Driver -> Driven.
	# Control-> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together.
	'''
	# pad 3 (last)-> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent (local_pad_2, control_icon_1)	
	
	print 'Hierarchy Created'

def lock_and_hide():
	'''
	This tool lets the user lock and hide all attributes so they 
	may not be seen or altered unless the user wishes to.
	How to Run:
	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.lock_and_hide()
	'''


	# Get selected.
	selected_controls=pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_controls:', control_icon

	print 'Channels locked and hidden.'

def lock_and_hide_trans():
	'''
	This tool lets the user lock and hide all the transfroms on the selected, so 
	they may not be alterd in anyway.It is also a way to hide away any node attribute 
	that is not needed.

	How to Run:
	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.lock_and_hide_trans
	'''

	# Get selected.
	selected_controls=pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_controls:', control_icon

	control_icon.tx.set(lock=True, keyable =False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden.'

def lock_and_hide_rotate():
	'''
	This tool hides and locks rotate attributes only.
	How to Run:
	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.lock_and_hide_rotate()
	'''

	# Get selected.
	selected_controls=pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_controls:', control_icon

	# Locking and hidning attributes.
	control_icon.rx.set(lock=True, keyable =False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden.'

def unlock_and_show():
	'''
	This tool unlocks and unhide all the attributes.
	How to Use:
	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.unlock_and_show()
	'''
	# Get selected.
	selected_controls=pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'selected_controls:', control_icon

	#Unlocking and showing all attributes.

	control_icon.rx.set(lock=False, keyable =True)
	control_icon.ry.set(lock=False, keyable =True)
	control_icon.rz.set(lock=False, keyable =True)
	control_icon.tx.set(lock=False, keyable =True)
	control_icon.ty.set(lock=False, keyable =True)
	control_icon.tz.set(lock=False, keyable =True)
	control_icon.sx.set(lock=False, keyable =True)
	control_icon.sy.set(lock=False, keyable =True)
	control_icon.sz.set(lock=False, keyable =True)
	control_icon.v.set(lock=False, keyable =True)
	print 'Channels unlocked and showen.'

def priming_tool():
	'''
	This tool creates a locally oriented control for each selected tool.

	How to Run:
	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.priming_tool

	'''	

	# Get selected joints.
	selected_joints = pm.ls(selection=True, dag=True)

	for current_joint in selected_joints:
		print 'Current Joint', current_joint
		# Icon and pad name.
	
		icon_name=current_joint.replace('_bind','_icon')
		local_pad_name = current_joint.replace('_bind','_local')

		# Create a current icon
		control_icon=pm.circle(name=icon_name, normal=[1,0,0], radius=1.8)[0]

		# Create a group (parenting the control under the group)
		local_pad=pm.group(control_icon)

		# MOve the group to the traget joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group 
		pm.orientConstraint(control_icon, current_joint)

def joint_renamer():
	'''
	Rename a selected joint chain.
		Naming convetion:
			lt_arm_01_bind
			lt_arm_03_waste

	The user will select the root joint and then execute the tool.



	How to Run:

	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.joint_renamer()

	'''

	# Input Area!!!
	# Get selected root joint.
	joint_systems = pm.ls(selection=True, dag=True)

	# Orientation_systemName_count_suffix
	# lf_arm_01_bind

	ori = raw_input()  
	name = raw_input()
	count = 1
	suffix = 'bind'

	#loop through joint chain.
	for current_joint in joint_systems:
		new_name = '{0}_{1}_0{2}_{3}'. format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		print 'Renaming:', current_joint, 'New Name:', new_name

		# Pushing the count forward.
		count = count + 1 

	# Renaming.	
	new_name = '{0}_{1}_0{2}_{3}'. format(ori, name, count-1, 'waste')
	print 'Renaming:', 'current_joint', 'New Name:', new_name
	current_joint.rename(new_name)

	print 'Selected joints has been renamed.'

def padding_tool():
	'''


	How to run:

	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected 
	root_joint = selected[0]

	# Create empty group
	# empty=True will create a empty group
	pad =pm.group(empty=True)

	# Move group to joint.
	# Delete constraint
	temp_constraint = pm.pointConstraint(root_joint,pad)
	pm.delete(temp_constraint)
	# Freeze Transforms on the group.
	pm.makeIdentity(pad,apply=True, t=1,r=1,s=1,n=0)

	# Parent joint to group.
	pm.parent(root_joint,pad)

	#renameing
	#lt_middle_01_bind
	#lt_middle_01_pad
	pad_name = root_joint.replace ('01_bind','00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def separator_attribute(): 
	'''
	Create a seperator(enum) attribute on a selected control.

	How to Run:
	import HossainJannatul_riggingTools_cri1_1408
	HossainJannatul_riggingTools_cri1_1408.separator_attribute()

	'''
	# Get selected.
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Naming and locking a empty attribute as a seperator.
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', en='.......',keyable=True)
	attribute = first_selected.attr(attribute_name)
	attribute.set(lock=True)

	print ' Attribute seperator created.'
