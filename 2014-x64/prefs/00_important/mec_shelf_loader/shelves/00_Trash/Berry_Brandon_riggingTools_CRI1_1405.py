'''
Berry_Brandon_riggingTools_CRI1_1405.py
Brandon Berry

Description:
	Grouping of rigging tools

How to run:
import Berry_Brandon_riggingTools_CRI1_1405
reload(Berry_Brandon_riggingTools_CRI1_1405)
'''

import pymel.core as pm

def hierarchy():
	'''
	Creates a hierarchy based upon a given system
	
	Select the root joint and execute this function

	import Berry_Brandon_riggingTools_CRI1_1405
	reload(Berry_Brandon_riggingTools_CRI1_1405)
	Berry_Brandon_riggingTools_CRI1_1405.hierarchy()

	Works for the (Left Middle) Finger Joint System
	'''

	import pymel.core as pm

	# The user will select the root joint and the tool
	#	will apply the systems

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	# Pad the root joint.
	# Create an empty group

	pad = pm.group(empty = True, name = 'lt_middle_00_pad')
	print 'Root Pad Created;', pad

	# Move group to target joint
	# Point Constrain group to root joint.
	#	offset off (Snapping)
	Spoink = pm.pointConstraint(root_joint, pad)

	# Delete constraint
	pm.delete(Spoink)

	# Freeze transforms on group
	pm.makeIdentity(pad, apply = True, t = 1, r = 1, s = 1, n = 0)

	#Parent root joint to group.
	pm.parent(root_joint, pad)

	# Create a local oriented control for each joint
	# rt_middle_01_bind, rt_middle_02_bind, and rt_middle_03_bind

	# Create control
	control_icon_01 = pm.circle(name = 'lt_middle_01_icon',
		normal = [1, 0, 0])[0]

	# Create group (NOT EMPTY)
	#    This will automatically parent the control under
	#    the group.
	local_01 = pm.group(name = 'lt_middle_01_local')

	# Move group to the target joint.
	# Use parent constraint. Driver is the joint.
	#    Driven is the group.
	#    Offset is off (Snapping)
	Tabitha = pm.parentConstraint(root_joint, local_01)

	# Delete the constraint
	pm.delete(Tabitha)

	# Delete History on control
	pm. delete(ch = True)

	# Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_01, root_joint)



	control_icon_02 = pm.circle(name = 'lt_middle_02_icon',
		normal = [1, 0, 0])[0]

	local_02 = pm.group(name = 'lt_middle_02_local')

	Beverly = pm.parentConstraint(second_joint, local_02)

	pm.delete(Beverly)

	pm. delete(ch = True)

	pm.orientConstraint(control_icon_02, second_joint)


	control_icon_03 = pm.circle(name = 'lt_middle_03_icon',
		normal = [1, 0, 0])[0]

	local_03 = pm.group(name = 'lt_middle_03_local')

	LaVerne = pm.parentConstraint(third_joint, local_03)

	pm.delete(LaVerne)

	pm. delete(ch = True)

	pm.orientConstraint(control_icon_03, third_joint)


	pm.parent(local_03, control_icon_02)
	pm.parent(local_02, control_icon_01)

	Sign_Language = pm.group(empty = True, name = 'lt_middle_group')

	pm.parent(pad, Sign_Language)
	pm.parent(local_01, Sign_Language)

	print 'Hierarchy Generated (with Pads).'


def colorBlue_tool():
	'''
	import Berry_Brandon_riggingTools_CRI1_1405
	reload(Berry_Brandon_riggingTools_CRI1_1405)
	Berry_Brandon_riggingTools_CRI1_1405.colorBlue_tool()
	'''

	# Get all left control icons
	icon_list = pm.ls(selection = True)
	for indiv_icon in icon_list:
		# turn overrideEnabled on 
		# change the overrideColor to blue 

		indiv_icon.overrideEnabled.set(1)
		indiv_icon.overrideColor.set(5)

def colorRed_tool():
	'''
	import Berry_Brandon_riggingTools_CRI1_1405
	reload(Berry_Brandon_riggingTools_CRI1_1405)
	Berry_Brandon_riggingTools_CRI1_1405.colorRed_tool()
	'''
	# Get all right control icons
	icon_list = pm.ls(selection = True)
	for indiv_icon in icon_list:
		# turn overrideEnabled on 
		# change the overrideColor to red 

		indiv_icon.overrideEnabled.set(1)
		indiv_icon.overrideColor.set(4)



def padding_tool():
	'''
	import Berry_Brandon_riggingTools_CRI1_1405
	reload(Berry_Brandon_riggingTools_CRI1_1405)
	Berry_Brandon_riggingTools_CRI1_1405.padding_tool()

	Works for Tail Joint System
	'''

	selected = pm.ls(selection = True, dag = True)
	print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	pad = pm.group(empty = True, name = 'ct_tail_00_pad')

	# Move group to joint using parent constraint.
	Tim = pm.pointConstraint(root_joint, pad)
	
	#  Delete parent constraint.
	pm.delete(Tim)

	# Freeze transforms on the group.
	pm.makeIdentity(pad, apply = True, t = 1, r = 1, s = 1, n = 0)

	# Parent joint system to group
	pm.parent(root_joint, pad)

	print 'Padding complete'




def priming_tool():
	'''
	import Berry_Brandon_riggingTools_CRI1_1405
	reload(Berry_Brandon_riggingTools_CRI1_1405)
	Berry_Brandon_riggingTools_CRI1_1405.priming_tool()

	Works with Right Arm Joint System
	'''

	#Get selected.
	selected = pm.ls(selection = True)
	
	# print 'Joints selected:', selected
	#target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# Normal set to X and radius set is 1.5
		control_icon = pm.circle(normal = [1, 0, 0], radius = 1.5,
			name=control_icon_name)[0]

		# Group control (NOT EMPTY)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Parent constrain group to target joint
		# 	then delete contraint.
		Bill = pm.parentConstraint(target_joint, local_pad)
		pm.delete(Bill)

		# Orient constrain control to joint
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created. Well done.'




def renaming_tool():
	'''
	import Berry_Brandon_riggingTools_CRI1_1405
	reload(Berry_Brandon_riggingTools_CRI1_1405)
	Berry_Brandon_riggingTools_CRI1_1405.renaming_tool()

	Works for the Back Joint System
	'''

	# Get selected
	joint_chain = pm.ls(selection = True, dag = True)
	
	print 'Spinal Cord Selected', joint_chain

	# Establish naming convention
	'ct_spine_01_bind', 'ct_spine_06_bind_waste'

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'

	# Loop through joint chain
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name
		
		# Rename
		current_joint.rename(new_name)

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

	print 'Assets renamed.'









