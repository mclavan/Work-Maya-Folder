def Hierarchy():
	'''
	Jovanny Zapata
	Zapata_Jovanny_riggingTools_cri1_1405.py

	Description

	How to run
	import Zapata_Jovanny_riggingTools_cri1_1405
	reload (Zapata_Jovanny_riggingTools_cri1_1405)
	'''

	import pymel.core as pm

	print 'Hierarchy Generated'


	# The user will select the root joint and the tool
	#	  will apply the system

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# Pad the root joint.
	'''

	# create an empty group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'root Pad Created:', pad

	# Move group to root joint
	# point constraint group to root joint.
	#     offset off (Snapping)
	temp = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(temp)

	# Freeze transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group.
	pm.parent(root_joint,pad)


	#create a local oriented cntrol for each joint.
	#lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind
	'''
	root_joint
	'''
	# Create control (circle)
	control_icon_1 = pm.circle(name= 'lt_middle_01_icon', nr=[1,0,0])[0]

	# create group (NOT EMPTY)
	#  This will automaticly parent the control under
	# the group.
	control_pad_1 = pm.group(empty=False, name='lt_middle_01_local') 

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	#   Where driven is the group.
	#   Offset is off (Snapping)
	temp = pm.parentConstraint(root_joint, control_icon_1)


	# Destroy the constraint
	pm.delete(temp)

	# Delete history on control
	pm.delete(ch=True)
	pm.delete(pad,ch=True)
	# orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	second_joint
	'''
	# Create control (circle)
	control_icon_2 = pm.circle(name= 'lt_middle_02_icon', nr=[1,0,0])[0]

	# create group (NOT EMPTY)
	#  This will automaticly parent the control under
	# the group.
	control_pad_2 = pm.group(empty=False, name='lt_middle_02_local') 

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	#   Where driven is the group.
	#   Offset is off (Snapping)
	temp = pm.parentConstraint(second_joint, control_icon_2)


	# Destroy the constraint
	pm.delete(temp)

	# Delete history on control
	pm.delete(ch=True)
	pm.delete(pad,ch=True)
	# orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	third_joint
	'''
	# Create control (circle)
	control_icon_3 = pm.circle(name= 'lt_middle_03_icon', nr=[1,0,0])[0]

	# create group (NOT EMPTY)
	#  This will automaticly parent the control under
	# the group.
	control_pad_3 = pm.group(empty=False, name='lt_middle_03_local') 

	# Move group to the target joint.
	# Use a parent constraint driver is the joint.
	#   Where driven is the group.
	#   Offset is off (Snapping)
	temp = pm.parentConstraint(third_joint, control_icon_3)


	# Destroy the constraint
	pm.delete(temp)

	# Delete history on control
	pm.delete(ch=True)
	pm.delete(pad,ch=True)
	# orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_3, third_joint)

	#parent the Controls
	pm.parent(control_pad_3, control_icon_2)
	pm.parent(control_pad_2, control_icon_1)

	#Group hierarchy
	Hierarchy = pm.group(empty=True, name = 'Hierarchy')

	pm.parent(pad, Hierarchy)
	pm.parent(control_pad_1, Hierarchy)

def Joint_Rename():
	'''
	# select the root joint and loop through all joint in
	# the joint chain.
	# 'ori_name_count_suffix'
	# 'ct_back_01_bind'

	import Zapata_Jovanny_riggingTools_cri1_1405
	Zapata_Jovanny_riggingTools_cri1_1405.Joint_Rename()
	'''
	import pymel.core as pm

	# What am i working on?
	# Get all joint in a selected joint chain.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected:', joint_chain

	# Build our new name.
	# 'lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori,name, count, suffix)
		print 'joint Name:', new_name

		current_joint.rename(new_name)

		count= count + 1
	
	new_name = '{0}_{1}_0{2}_{3}'.format(ori,name, count-1, 'waste')
	print 'joint Name:', new_name
	current_joint.rename(new_name)

def Padding_Tool():

	import pymel.core as pm
	
	'''
	import Zapata_Jovanny_riggingTools_cri1_1405
	reload(Zapata_Jovanny_riggingTools_cri1_1405)
	Zapata_Jovanny_riggingTools_cri1_1405.Padding_Tool
	'''

	selected =pm.ls(selection=True)
	# print 'Current Selected', selected
	root_joint = selected[0]


	# Create empty group
	# empty=True will create a empty group
	pad = pm.group(empty=True)

	# Move group to joint.
	#	and delete Constraint
	temp_constraint = pm.pointConstraint(root_joint,pad)
	pm.delete(temp_constraint)

	#Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	
	# parent joint to group
	pm.parent(root_joint, pad)

	#renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group Created'

def Priming_Tool():

	import pymel.core as pm
	'''
	import Zapata_Jovanny_riggingTools_cri1_1405
	reload(Zapata_Jovanny_riggingTools_cri1_1405)
	Zapata_Jovanny_riggingTools_cri1_1405.Priming_Tool()
	'''

	# Get Selected
	selected = pm.ls(selection=True)
	# print 'joints Selected' selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1,0,0], radius=1.8,
		 name=control_icon_name)[0]
		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon', control_icon
		print 'Pad Created', local_pad
		# Move group to target joint.
		#	and delete constraint
		temp_Constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_Constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)



	print 'Local Oriented Controls Created.'











