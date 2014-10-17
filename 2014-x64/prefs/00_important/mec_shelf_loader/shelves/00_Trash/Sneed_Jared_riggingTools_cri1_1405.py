'''
Jared Sneed
sneedJared_riggingTools_cri1_1405.py

Description: The padding tool will create a world-oriented group that the selected 
			joint system will be parented to

How to Run:
import sneedJared_riggingTools_cri1_1405
reload(sneedJared_riggingTools_cri1_1405)
'''

import pymel.core as pm

print 'Rigging Tools Active'

def heirarchy():
	'''
	Jared Sneed
	sneedJared_riggingTools_cri1_1405.py

	Description: A script that makes the control icons for the finger joints. The script
	groups them, them parents them, names them, freezes transforms, and
	deletes history.

	HOW TO RUN:
	import sneedJared_riggingTools_cri1_1405
	reload(sneedJared_riggingTools_cri1_1405)
	sneedJared_riggingTools_cri1_1405.heirarchy()
	'''

	import pymel.core as pm

	print 'Hierarchy Generated'

	# The user will select the root joint and the tool
	#	will apply systems

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# Pad root joint.
	'''

	# Create an empty group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created', pad

	# Move group to root joint
	# Point contrain group to root joint
	#	maintain offset off (Snapping)
	kenny = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(kenny)

	# Freeze Transforms
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint, pad)



	# Create a local oriented control for each joint.
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind



	# First Joint -------------------------------------------------------------------

	# Create control (Circle)
	control_01_icon = pm.circle(name='lt_middle_01_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#	This will automatically parent the control under 
	# 	the group.
	root_local = pm.group(control_01_icon, name='lt_middle_01_local');


	# Move group to the target joint
	# Use a Parent constrain driver is the joint
	#	Where driver is the group
	# 	Offset is off (Snapping)
	kenny = pm.parentConstraint(root_joint, root_local)
	# Delete the constraint 
	pm.delete(kenny)

	# Delete History on control
	pm.delete(control_01_icon, ch=True)

	# Orient Constraint driver: control
	#					driven: joint
	pm.orientConstraint(control_01_icon, root_joint)



	# Second Joint -------------------------------------------------------------------

	# Create control (Circle)
	control_02_icon = pm.circle(name='lt_middle_02_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#	This will automatically parent the control under 
	# 	the group.
	second_local = pm.group(control_02_icon, name='lt_middle_02_local');


	# Move group to the target joint
	# Use a Parent constrain driver is the joint
	#	Where driver is the group
	# 	Offset is off (Snapping)
	kenny = pm.parentConstraint(second_joint, second_local)
	# Delete the constraint 
	pm.delete(kenny)

	# Delete History on control
	pm.delete(control_02_icon, ch=True)

	# Orient Constraint driver: control
	#					driven: joint
	pm.orientConstraint(control_02_icon, second_joint)


	# Third Joint -------------------------------------------------------------------

	# Create control (Circle)
	control_03_icon = pm.circle(name='lt_middle_03_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	#	This will automatically parent the control under 
	# 	the group.
	third_local = pm.group(control_03_icon, name='lt_middle_03_local');


	# Move group to the target joint
	# Use a Parent constrain driver is the joint
	#	Where driver is the group
	# 	Offset is off (Snapping)
	kenny = pm.parentConstraint(third_joint, third_local)
	# Delete the constraint 
	pm.delete(kenny)

	# Delete History on control
	pm.delete(control_03_icon, ch=True)

	# Orient Constraint driver: control
	#					driven: joint
	pm.orientConstraint(control_03_icon, third_joint)

	# Pad Parenting -----------------------------------------------------------------

	# Parent Pads together 
	pm.parent('lt_middle_03_local', 'lt_middle_02_local');
	pm.parent('lt_middle_02_local', 'lt_middle_01_local');

def joint_renamer():

	
	# What am I working on?
	# Get all joints in a selected joint chain
	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected Items', joint_chain

	# Build our new name
	# 'lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print 'Joint Name', new_name

		count = count + 1

		current_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name', new_name
	current_joint.rename(new_name)


	print 'Joint Renamed Active'

def padding():
	'''
	Jared Sneed
	sneedJared_riggingTools_cri1_1405.py

	Description The priming tools will create a locally oriented control 
	and prime for each joint in a hierarchy. 

	HOW TO RUN:
	import sneedJared_riggingTools_cri1_1405
	reload(sneedJared_riggingTools_cri1_1405)
	sneedJared_riggingTools_cri1_1405.padding()
	'''

	selected = pm.ls(selection=True)
	# print 'current_slected', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create empty group
	pad =pm.group(empty=True)

	# move group joint.
	#	and delete constraint
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	#Freeze Transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to the group
	pm.parent(root_joint, pad)

	# Rename the group
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding Group Created'

def primer():
	'''
	Jared Sneed
	sneedJared_riggingTools_cri1_1405.py

	Description: The priming tools will create a locally oriented control
	and prime for each joint in a hierarchy.

	HOW TO RUN:
	import sneedJared_riggingTools_cri1_1405
	reload(sneedJared_riggingTools_cri1_1405)
	sneedJared_riggingTools_cri1_1405.primer()
	'''

	# Get Selected
	selected = pm.ls(selection=True)
	# print 'Joint Selected:', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control icon
			# Normal set to x
			# Radius set to 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]


		# Group icon (Filled)
		local_pad = pm.group(name=local_pad_name)


		# Move group to target joint (Snapping)
			# Parent Constrain
		kenny = pm.parentConstraint(target_joint, local_pad)

		# Delete Constraint
		pm.delete(kenny)

		# OrientConstrain
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Control Created'