'''
keithNiles_riggingTools_cri1_1405.py

Niles Keith

Description:
	Grouping of rigging tools.


How to Run:

import keithNiles_riggingTools_cri1_1405
reload(keithNiles_riggingTools_cri1_1405)

'''

import pymel.core as pm 

print 'Rigging Tools Activated.'


def hierarchy():

	'''
	Create a hierarchy based upon a given system

	Select root joint chain and exectue function

	import keithNiles_riggingTools_cri1_1405
	reload (keithNiles_riggingTools_cri1_1405)
	keithNiles_riggingTools_cri1_1405.hierarchy()
	'''


	'''
	Padding the Root joint
	'''

	# The user will select the root joint and the tool
	#	will apply the systems. 


	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	# Pad the root joint

	# Create an empty group
	pad = pm.group(empty=True, name = 'lt_middle_00_pad')
	print 'Root Pad Created:', pad

	# Move group to root joint
	# Point constrain group to root joint
	#	offset off (snapping)
	tempConstraint = pm.pointConstraint(root_joint, pad)

	# Delete constraint
	pm.delete(tempConstraint)

	# Frezze Transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint,pad)

	'''
	# Create a local oriented control for each joint.
	# lt_middle_01 bind, lt_middle_02_bind, lt_middle_03_bind
	'''

	'''
	Control 1
	'''

	# Create control (circle)
	control_icon_01 = pm.circle(name = 'lt_middle_01_icon', 
		normal= [90, 0, 0])[0]

	# Create group (NOT EMPTY)
	#	This will automaticaly parent the control under the group
	local1 = pm.group(control_icon_01, name = 'lt_middle_01_local')

	# Move the group to the target joint
	#	Use a parent constraint, driver is the joint, driven is the pad
	# 		Maintain offset unchecked
	temp = pm.parentConstraint(root_joint, local1)

	# Delete the constraint
	pm.delete(temp)

	# Delete History on the control
	pm.delete(control_icon_01, ch=True)

	# Orient Constraint driver: control- Driver, joint- Driven
	pm.orientConstraint(control_icon_01, root_joint)


	'''
	Control 2
	'''

	# Create control (circle)
	control_icon_02 = pm.circle(name = 'lt_middle_02_icon', 
		normal = [90, 0 ,0])[0]

	# Create group (NOT EMPTY)
	#	This will automaticaly parent the control under the group
	local2 = pm.group(control_icon_02, name = 'lt_middle_02_local')

	# Move the group to the target joint
	#	Use a parent constraint, driver is the joint, driven is the pad
	# 		Maintain offset unchecked
	temp = pm.parentConstraint(second_joint, local2)

	# Delete the constraint
	pm.delete(temp)

	# Delete History on the control
	pm.delete(control_icon_02, ch=True)

	# Orient Constraint driver: control- Driver, joint- Driven
	pm.orientConstraint(control_icon_02, second_joint)

	'''
	Control 3
	'''


	# Create control (circle)
	control_icon_03 = pm.circle(name = 'lt_middle_03_icon', 
		normal = [90, 0, 0])[0]

	# Create group (NOT EMPTY)
	#	This will automaticaly parent the control under the group
	local3 = pm.group(control_icon_03, name = 'lt_middle_03_local')

	# Move the group to the target joint
	#	Use a parent constraint, driver is the joint, driven is the pad
	# 		Maintain offset unchecked
	temp = pm.parentConstraint(third_joint, local3)

	# Delete the constraint
	pm.delete(temp)

	# Delete History on the control
	pm.delete(control_icon_03, ch=True)

	# Orient Constraint driver: control- Driver, joint- Driven
	pm.orientConstraint(control_icon_03, third_joint)


	'''
	Parenting
	'''


	#Parent middle_02_local pad to middle_01_icon
	pm.parent(local2, control_icon_01)

	#Parent middle_03_local pad to middle_02_icon
	pm.parent(local3, control_icon_02)


	# Create empty group
	master = pm.group(empty=True, name= 'lt_middle_group')


	# Parent middle pad and middle local group to lt_middle_group
	pm.parent(pad, master)
	pm.parent(local1, master)


	print 'done.'



def padding_tool():
	'''

	import keithNiles_riggingTools_cri1_1405
	reload(keithNiles_riggingTools_cri1_1405)
	keithNiles_riggingTools_cri1_1405.padding_tool()

	'''
	selected = pm.ls(selection=True)
	#print 'Current selected:', selected
	root_joint = selected[0]

	#Create empty group
	#epmty=True will create an empty group
	#
	pad = pm.group(empty=True)

	#Move group to joint
	#	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)


	#Freeze Transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#Parent joint to group
	pm.parent(root_joint, pad)

	#Renaming
	#ct_tail_01_bind
	#ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created.'



def priming_tool():
	'''
	import keithNiles_riggingTools_cri1_1405
	reload(keithNiles_riggingTools_cri1_1405)
	keithNiles_riggingTools_cri1_1405.priming_tool()
	'''

	#Get Selected
	selected = pm.ls(selection=True)
	#print 'Joints Selected:', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')


		#Create Control
		#normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8, 
			name=control_icon_name)[0]

		#Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad


		#Move group to target joint
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		#Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created.'



def joint_renamer():
	'''
	import keithNiles_riggingTools_cri1_1405
	reload(keithNiles_riggingTools_cri1_1405)
	keithNiles_riggingTools_cri1_1405.joint_renamer()
	'''

	'''
	Get Selected

	pm.ls(selection=True)
	'''

	joint_chain = pm.ls(selection=True, dag=True)
	print 'Selected items:', joint_chain

	ori = raw_input()
	system_name = raw_input()
	count= 1
	suffix = 'bind'

	'''
	Loop through joint chain
	'''
	for current_joint in joint_chain:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		#Rename joint
		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count - 1, 'waste')
	current_joint.rename(new_name)






