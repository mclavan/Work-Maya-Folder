'''
rigging_tools.py
Michael Clavan

Description:
	Grouping of rigging tools.

How to Run:

import clavanMichael_riggingTools_cri1_1402
reload(clavanMichael_riggingTools_cri1_1402)

'''

import pymel.core as pm

print 'Rigging Tools Active.'

def hierarchy():
	'''
	Creates a hierarchy based upon a given system. 

	Select the root joint and execute this function. 

	import clavanMichael_riggingTools_cri1_1402
	clavanMichael_riggingTools_cri1_1402.hierarchy()	

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
	root_pad = pm.group(empty=True)

	# Move empty group to root joint
	temp_constraint = pm.pointConstraint(joint_1, root_pad)
	pm.delete(temp_constraint)

	# Parent root joint to pad
	pm.parent(joint_1, root_pad)

	# Rename pad based upon joint name
	root_pad_name = joint_1.replace('01_bind', '00_pad')
	root_pad.rename(root_pad_name)

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
	control_1.tx.set(lock=True, keyable=False)
	control_1.ty.set(lock=True, keyable=False)
	control_1.tz.set(lock=True, keyable=False)
	control_1.sx.set(lock=True, keyable=False)
	control_1.sy.set(lock=True, keyable=False)
	control_1.sz.set(lock=True, keyable=False)
	control_1.v.set(lock=True, keyable=False)

	# rename control and pad based on joint system
	new_control_name = joint_1.replace('_bind', '_icon')
	new_pad_name = joint_1.replace('_bind', '_local')
	control_1.rename(new_control_name)
	pad_1.rename(new_pad_name)

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

	# Lock and Hide transforms
	# control_1.tx.set(lock=True, keyable=False)
	control_2.tx.set(lock=True, keyable=False)
	control_2.ty.set(lock=True, keyable=False)
	control_2.tz.set(lock=True, keyable=False)
	control_2.sx.set(lock=True, keyable=False)
	control_2.sy.set(lock=True, keyable=False)
	control_2.sz.set(lock=True, keyable=False)
	control_2.v.set(lock=True, keyable=False)

	# rename control and pad based on joint system
	new_control_name = joint_2.replace('_bind', '_icon')
	new_pad_name = joint_2.replace('_bind', '_local')
	control_2.rename(new_control_name)
	pad_2.rename(new_pad_name)

	'''
	Control 3
	'''
	# Create control icon
	control_3 = pm.circle(normal=[1, 0, 0])[0]
	
	print 'Control 2 Created:', control_3
	# Create group, grouping icon along with it.
	pad_3 = pm.group()
	
	# parentConstrain group to joint
	temp = pm.parentConstraint(joint_3, pad_3)
	# Delete constraint.
	pm.delete(temp)

	# Connect control to finger
	pm.orientConstraint(control_3, joint_3)

	# Lock and Hide transforms
	# control_1.tx.set(lock=True, keyable=False)
	control_3.tx.set(lock=True, keyable=False)
	control_3.ty.set(lock=True, keyable=False)
	control_3.tz.set(lock=True, keyable=False)
	control_3.sx.set(lock=True, keyable=False)
	control_3.sy.set(lock=True, keyable=False)
	control_3.sz.set(lock=True, keyable=False)
	control_3.v.set(lock=True, keyable=False)

	# rename control and pad based on joint system
	new_control_name = joint_3.replace('_bind', '_icon')
	new_pad_name = joint_3.replace('_bind', '_local')
	control_3.rename(new_control_name)
	pad_3.rename(new_pad_name)

	'''
	Parenting
	'''
	# pad 3 to control 2
	pm.parent(pad_3, control_2)
	# pad 2 to control 1
	pm.parent(pad_2, control_1)

	print 'Hierarchy Created.'


def padding_tool():
	'''
	This tool creates a world pad on the selected joint system. 

	Select the root and execute the command. 

	import clavanMichael_riggingTools_cri1_1402
	reload(clavanMichael_riggingTools_cri1_1402)
	clavanMichael_riggingTools_cri1_1402.padding_tool()

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


def priming_tool():
	'''
	This tool creates a local oriented control and pad on the 
		selected joint system. 

	Select the joints and execute the command. 

	import clavanMichael_riggingTools_cri1_1402
	reload(clavanMichael_riggingTools_cri1_1402)
	clavanMichael_riggingTools_cri1_1402.priming_tool()

	'''	
	# Get selected joints
	selected_joints = pm.ls(selection=True)

	# Loop through current selected.
	for current_joint in selected_joints:
		# Create control icon
		control_icon = pm.circle(normal=[1, 0, 0])[0]

		print 'Control Created:', control_icon
		# Create group, grouping icon along with it.
		local_pad = pm.group()

		# parentConstrain group to joint
		temp = pm.parentConstraint(current_joint, local_pad)
		# Delete constraint.
		pm.delete(temp)

		# Connect control to finger
		pm.orientConstraint(control_icon, current_joint)

		# Rename control and pad to match joint.
		new_control_name = current_joint.replace('_bind', '_icon')
		new_pad_name = current_joint.replace('_bind', '_local')
		control_icon.rename(new_control_name)
		local_pad.rename(new_pad_name)		


def joint_renamer():
	'''
	This tool renames all the joints in a joint chain.  
	Based upon a the naming convention:
		lt_arm_01_bind -> lt_arm_03_waste

	Select the root joint and execute the command. 

	import clavanMichael_riggingTools_cri1_1402
	reload(clavanMichael_riggingTools_cri1_1402)
	clavanMichael_riggingTools_cri1_1402.joint_renamer()
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

