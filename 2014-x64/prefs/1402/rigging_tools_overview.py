'''
rigging_tools.py
Michael Clavan

Description:
	Grouping of rigging tools.

How to Run:

import rigging_tools
reload(rigging_tools)

'''

import pymel.core as pm

print 'Rigging Tools Active.'

def hierarchy():
	'''
	Creates a hierarchy based upon a given system. 

	Select the root joint and execute this function. 

	import rigging_tools
	rigging_tools.hierarchy()	

	'''
	'''
	Input (Joint System)
	'''
	# Get Selected Joint System
	selected = pm.ls(selection=True, dag=True)
	# Selected: [nt.Joint(u'lt_middle_01_bind'), 
	# 	nt.Joint(u'lt_middle_02_bind'), 
	# 	nt.Joint(u'lt_middle_03_bind'), 
	# 	nt.Joint(u'lt_middle_04_waste')]

	print 'Selected:', selected
	joint_1 = selected[0]
	joint_2 = selected[1]
	joint_3 = selected[2]


	'''
	Joint Padding
	'''
	# Create empty group

	# Move empty group to root joint

	# Parent root joint to pad

	# Rename pad based upon joint name


	'''
	Local Controls
	'''
	'''
	Control 1
	'''
	# Create control icon

	# Create group, grouping icon along with it.

	# parentConstrain group to joint
	# Delete constraint.

	# Connect control to finger

	# Lock and Hide transforms
	# control_1.tx.set(lock=True, keyable=False)

	# rename control and pad based on joint system


	'''
	Control 2
	'''
	# Create control icon
	
	# Create group, grouping icon along with it.
	
	# parentConstrain group to joint
	# Delete constraint.


	# Connect control to finger

	# Lock and Hide transforms
	# control_1.tx.set(lock=True, keyable=False)


	# rename control and pad based on joint system


	'''
	Control 3
	'''
	# Create control icon
	
	# Create group, grouping icon along with it.
	
	# parentConstrain group to joint
	# Delete constraint.


	# Connect control to finger

	# Lock and Hide transforms
	# control_1.tx.set(lock=True, keyable=False)


	# rename control and pad based on joint system


	'''
	Parenting
	'''
	# pad 3 to control 2

	# pad 2 to control 1


	print 'Hierarchy Created.'


def padding_tool():
	'''
	This tool creates a world pad on the selected joint system. 

	Select the root and execute the command. 

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()

	'''
	# Get selected root joint.
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create an empty group.

	# Snap group to root joint. 


	# Freeze transforms on pad

	# parent root joint to pad. 

	# Rename pad
	# lt_arm_01_bind
	# lt_arm_00_pad
	# String method

	print 'Joint system has been padded.'

def priming_tool():
	'''
	This tool creates a local oriented control and pad on the 
		selected joint system. 

	Select the joints and execute the command. 

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.priming_tool()

	'''	
	# Get selected joints
	selected_joints = pm.ls(selection=True)

	# Loop through current selected.
	for current_joint in selected_joints:
		# Create control icon
		control_icon = pm.circle(normal=[1, 0, 0])[0]
		print 'Control Created:', control_icon

		# Create group, grouping icon along with it.

		# parentConstrain group to joint
		# Delete constraint.

		# Connect control to finger

		# Rename control and pad to match joint.
	

	print 'Local pads and controls created on selected joints.'	


def joint_renamer():
	'''
	This tool renames all the joints in a joint chain.  
	Based upon a the naming convention:
		lt_arm_01_bind -> lt_arm_03_waste

	Select the root joint and execute the command. 

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.joint_renamer()
	'''

	# Get selected joint
	# Get selected root joint. 
	# How do I get the entire hierarchy of a joint chain?
	#   pm.ls(selection=True, dag=True)
	joint_system = pm.ls(selection=True, dag=True)

	print 'Joint system:', joint_system

	# Naming Convention Example
	# lt_arm_01_bind -> lt_arm_03_waste
	# orienation_systemName_count_suffix


	# Loop through selected.
	for current_joint in joint_system:
		# Add one to the count.


		# Compile new name	
		# new_name = ori + '_' + system_name + '_0' + str(count) + '_' + suffix 

		# Output to the user.


		# Rename the joint


	# Name the waste joint


	print 'Joints have been renamed.'


