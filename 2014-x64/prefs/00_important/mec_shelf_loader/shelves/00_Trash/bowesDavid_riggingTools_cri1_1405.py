'''
David Bowes
rigging_tools.py

description:


How to Run:
import rigging_tools
reload(rigging_tools)
'''


import pymel.core as pm

print 'Rigging Tools Active'

def hierarchy(): 
	print 'Hierarchy Generated'	
	# The user will select the root joint and the tool 
	#	will apply the systems.

	'''
	# Pad the root joint.
	'''

	# Create an empty group. 
	# Move group to root joint. 
	# Point constrain group to root joint.
	#		offset off(Snapping)
	# Delete Constraint
	# Freeze transforms on group. 
	# Parent root joint to group. 

	root_joint = 'lt_middle_01_bind'
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	temp = pm.pointConstraint(root_joint, pad)
	pm.delete(temp)
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	pm.parent(root_joint, pad)

	'''
	# Prime Control 1
	'''

	# Create control (circle)
	# Create group 
	# Move the group to the root joint
	# 	parent constraint without offset
	# Delete the constraint
	# Orient constraint icon to root joint



	control_icon_1 = pm.circle(name = 'lt_middle_01_icon')[0]
	local_pad_1 = pm.group(name = 'lt_middle_01_local')
	temp = pm.parentConstraint(root_joint, local_pad_1, maintainOffset = False)
	pm.delete(temp)
	pm.orientConstraint(control_icon_1, root_joint, maintainOffset = False)



	'''
	# Prime Control 2
	'''

	# Create control (circle)
	# Create group 
	# Move the group to the second joint
	# 	parent constraint without offset
	# Delete the constraint
	# Orient constraint icon to second joint joint

	second_joint = 'lt_middle_02_bind'

	control_icon_2 = pm.circle(name = 'lt_middle_02_icon')[0]
	local_pad_2 = pm.group(name = 'lt_middle_02_local')
	temp = pm.parentConstraint(second_joint, local_pad_2, maintainOffset = False)
	pm.delete(temp)
	pm.orientConstraint(control_icon_2, second_joint, maintainOffset = False)



	third_joint = 'lt_middle_03_bind'

	control_icon_3 = pm.circle(name = 'lt_middle_03_icon')[0]
	local_pad_3 = pm.group(name = 'lt_middle_03_local')
	temp = pm.parentConstraint(third_joint, local_pad_3, maintainOffset = False)
	pm.delete(temp)
	pm.orientConstraint(control_icon_3, third_joint, maintainOffset = False)



	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	master_group = pm.group(empty=True, name = 'project_hierarchy')
	pm.parent(pad, local_pad_1, master_group)

def padding_tool(): 
		'''
		import rigging_tools
		reload(rigging_tools)
		rigging_tools.padding_tool()
		'''


		selected = pm.ls(selection=True)
		# print 'Current Selected:', selected
		root_joint = selected[0]

		# Create empty group
		# empty=True will create a empty group  
		#
		pad = pm.group(empty=True)

		# Move group to joint. 
		# 	and delete constraint
		temp_constraint = pm.pointConstraint(root_joint, pad)
		pm.delete(temp_constraint)

		# Freeze Transforms on the group. 
		pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)



		# Parent joint to group
		pm.parent(root_joint, pad)

		# renaming
		pad_name = root_joint.replace('01_bind', '00 pad')
		pad.rename(pad_name)



		


		print 'Padding group created.'

def priming_tool():

	'''
	



	import rigging_tools
	reload(rigging_tools)
	rigging_tools.priming_tool()
	'''

	# Get Selected. 
	selected = pm.ls(selection=True)
	# print 'Joints Selected', selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_icon')


		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8)[0]
		
		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad
		# Move group to target joint. 
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control. 
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created.'

def joint_renamer(): 

	'''
	Description:
		Practical use of loops. 
		Renaming joint based upon a naming convention. 

	How to Run: 

	import joint_renamer
	reload(joint_renamer)
	rigging_tools.joint_renamer()


	'''

	print 'Joint Renamer - Active'

	'''
	Get Selected. 

	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items:', joint_chain

	'''
	Figure out naming convention.
	'lt_arm_01_bind', -> 'lt_arm_03_waste'
	'ct_tail_01_bind', -> 'ct_tail_06_waste'
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'



	'''
	Loop through joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name
		

		# Rename joint
		current_joint.rename(new_name)
		count = count + 1


	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)























