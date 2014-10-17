'''
rigging_tools.py
Michael Clavan

Description:
	Grouping of rigging tools.

How to Run:

import rigging_tools
reload(rigging_tools)
rigging_tools.hierarchy()

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
	# Get Selected Joint Sytem
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
	Local Controls
	'''
	'''
	Control 1
	'''
	# Create control icon
	control_1 = pm.circle(normal=[1, 0, 0])[0]

	print 'Control 1 Created:', control_1
	# Create group, grouping icon along with it.
	pad_1 = pm.group()

	# parentConstrain group to joint
	temp = pm.parentConstraint(joint_1, pad_1)
	# Delete constraint.
	pm.delete(temp)

	# Connect control to finger
	pm.orientConstraint(control_1, joint_1)

	# Lock and Hide transforms
	# control_1.tx.set(lock=True, keyable=False)

	# rename control and pad based on joint system

	'''
	Control 2
	'''
	# Create control icon
	control_2 = pm.circle(normal=[1, 0, 0])[0]
	
	print 'Control 2 Created:', control_2
	# Create group, grouping icon along with it.
	pad_2 = pm.group()
	
	# parentConstrain group to joint
	temp = pm.parentConstraint(joint_2, pad_2)
	# Delete constraint.
	pm.delete(temp)

	# Connect control to finger
	pm.orientConstraint(control_2, joint_2)

	'''
	Control 3
	'''

	'''
	Parenting
	'''
	# pad 3 to control 2
	pm.parent(pad_3, control_2)
	# pad 2 to control 1
	pm.parent(pad_2, control_1)


	'''
	Joint Padding
	'''


	print 'Hierarchy Created.'


def padding():
	'''
	This tool creates a world pad on the selected joint system. 

	Select the root and execute the command. 

	import snapping
	reload(snapping)
	snapping.padding()

	'''
	# Get selected root joint.
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create an empty group.
	pad = pm.group(empty=True)

	# Snap group to root joint. 
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms on pad
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# parent root joint to pad. 
	pm.parent(root_joint, pad)

	print 'Joint system has been padded.'

	# lt_arm_01_bind
	# lt_arm_00_pad
	# String method
	pad_name = root_joint.replace('01_bind', '00_pad')

	print 'Pad Name:', pad_name
	pad.rename(pad_name)

def joint_renamer():

	# Get selected joint
	# Get selected root joint. 
	# How do I get the entire hierarchy of a joint chain?
	#   pm.ls(selection=True, dag=True)
	joint_system = pm.ls(selection=True, dag=True)

	print 'Joint system:', joint_system

	# Naming Convention Example
	# lt_arm_01_bind -> lt_arm_03_waste
	# orienation_systemName_count_suffix
	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'

	# Loop through selected.
	for current_joint in joint_system:
		# Add one to the count.
		count = count + 1
		# Compile new name	
		# new_name = ori + '_' + system_name + '_0' + str(count) + '_' + suffix 
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, system_name, count, suffix)
		# Output to the user.
		print 'New name:', new_name

		# Rename the joint
		current_joint.rename(new_name)



	# Name the waste joint
	new_name = ori + '_' + system_name + '_0' + str(count) + '_' + 'waste'
	print 'New Name:', new_name
	joint_system[-1].rename(new_name)

	print 'Joints have been renamed.'

