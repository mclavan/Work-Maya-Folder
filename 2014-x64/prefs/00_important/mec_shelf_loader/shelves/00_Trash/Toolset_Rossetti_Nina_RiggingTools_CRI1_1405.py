import pymel.core as pm

def Hierarchy():
	
	'''
	Nina Rossetti
	hierarchy.py

	Description:
	This is a script to make the hierarchy for a simple joint with a pad and
	icons.

	How to Run:
	import hierarchy
	reload (hierarchy)
	'''

	

	print 'Hierarchy Generated'


	# The user will select the root joint and the tool will apply the systems.


	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# Pad the root joint.
	'''

	# Create an empty group.
	pad = pm.group(empty=True, name='lt_middle_00_pad') 
	print'Root Pad Created:', pad

	# Move group to root joint.
	# Point Constrain group to root joint.
	#	offset off (snapping)
	kenny = pm.pointConstraint(root_joint, pad) 

	# Delete Constraint 
	pm.delete(kenny)

	# Freeze Transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	pm.delete(ch=True)

	# Parent root joint to group
	pm.parent(root_joint, pad)

	'''
	# Create a local oriented control for each joint
	# lt_middle_01_bind,lt_middle_02_bind,lt_middle_03_bind,lt_middle_04_waste
	'''

	# Create control (circle)
	control_icon_1 = pm.circle(name='lt_middle_01_icon', nr=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#	this will automact parent the control under the group.
	pm.group(name='lt_middle_01_local')

	# Move group to the target joint
	# Use a Parent Constraint driver is the joint. 
	#	where driven is the icon.
	# Offset is off (snapping)
	kenny=pm.parentConstraint(root_joint, control_icon_1)

	# Delete the constrint
	pm.delete(kenny)

	# Delete History on control
	pm.delete(ch=True)

	# Orient Constraint driver:control driven:joint
	pm.orientConstraint(control_icon_1, root_joint)


	'''
	2nd
	'''

	# Create control (circle)
	control_icon_2 = pm.circle(name='lt_middle_02_icon', nr=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#	this will automact parent the control under the group.
	pm.group(name='lt_middle_02_local')

	# Move group to the target joint
	# Use a Parent Constraint driver is the joint. 
	#	where driven is the icon.
	# Offset is off (snapping)
	kenny=pm.parentConstraint(second_joint, control_icon_2)

	# Delete the constrint
	pm.delete(kenny)

	# Delete History on control
	pm.delete(ch=True)

	# Orient Constraint driver:control driven:joint
	pm.orientConstraint(control_icon_2, second_joint)

	lt_middle_01_icon= 'lt_middle_01_icon'
	lt_middle_02_local='lt_middle_02_local'
	pm.parent(lt_middle_02_local, lt_middle_01_icon)


	'''
	3rd
	'''

	# Create control (circle)
	control_icon_3 = pm.circle(name='lt_middle_03_icon', nr=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#	this will automact parent the control under the group.
	pm.group(name='lt_middle_03_local')

	# Move group to the target joint
	# Use a Parent Constraint driver is the joint. 
	#	where driven is the icon.
	# Offset is off (snapping)
	kenny=pm.parentConstraint(third_joint, control_icon_3)

	# Delete the constrint
	pm.delete(kenny)

	# Delete History on control
	pm.delete(ch=True)

	# Orient Constraint driver:control driven:joint
	pm.orientConstraint(control_icon_3, third_joint)

	lt_middle_03_local= 'lt_middle_03_local'
	lt_middle_02_icon= 'lt_middle_02_icon'
	pm.parent(lt_middle_03_local, lt_middle_02_icon)

	'''
	Parent Groups
	'''
	lt_middle_00_pad='lt_middle_00_pad'
	lt_middle_01_local='lt_middle_01_local'


	pm.group(empty=True,name='hierarchy')
	hierarchy='hierarchy'
	pm.parent(lt_middle_00_pad, hierarchy)
	pm.parent(lt_middle_01_local, hierarchy)


def joint_rename():
	'''
	# Create a function called joine_rename
	# Select the root_joint and loop through all joints in the chain.
	# 'ori_name_count_suffix'
	# 'ct_back_01_bind'

	import book
	book.joint_rename()
	'''

	# What am I working on?
	# Get all joints in a selected joint chain
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Joint Chain:', joint_chain

	#Build our new name
	# 'Lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print 'Joint Name:', new_name

		count = count + 1


	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)

	print 'Joint Chain Renamed'

def Padding():
	
	import pymel.core as pm

	'''
	import Toolset
	reload (Toolset)
	Toolset.Padding_Tool
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected', selected
	root_joint = selected[0]


	# Create Empty group
	# empty=True will create a empty group
	root_pad = pm.group(empty=True)

	# Move group to target joint
	# Delete constraint
	kenny = pm.pointConstraint(root_joint, root_pad)
	pm.delete(kenny)

	#Freeze transforms on the group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	#Parent root joint to the group
	pm.parent(root_joint, root_pad)

	#Rename
	pad_name =root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding Group Made'

def Priming():
	
	import pymel.core as pm

	'''
	import ToolSet.py
	reload(ToolSet)
	ToolSet.Priming_Tool()
	'''

	# Get Selected
	selected = pm.ls(selection=True)
	print 'joints Selected', selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# normal set to x and radius is 1.8
# Missing comma
		control_icon = pm.circle(normal=[1,0,0], radius=1.8, 
		 name=control_icon_name)[0]
		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon', control_icon
		print 'Pad Created', local_pad
		# Move group to target joint.
		#	and delete constraint
		kenny = pm.parentConstraint(target_joint, local_pad)
		pm.delete(kenny)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)



	print 'Local Oriented Controls Created.'