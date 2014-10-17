'''

Rig_Tools.py

Desc: 
	pratical use of loops
	renaming joints based upon a naming convention

How to Run:

import Rig_Tools
reload(Rig_Tools)



'''
"""
lect shiz 
# getting selection.
# use ls command to get the bjects selected in our scene.
# we are going to print out what is selected
selected = pm.ls(selection=True)
print 'selected: [0]'.  format(selected)4
"""





print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy():
	'''
	create a hierarchy based upon a given system

	Select root joint chain and execute function.

	import Rig_Tools
	Rig_Tools.hierarchy()
	'''

	'''
	Input 
	what are we working on
	the root system
	# '''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system



	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''
	# create empty group
	root_pad = pm.group(empty=True)

	# move group over to the target joint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	#freeze transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group
	pm.parent(root_joint, root_pad)
	'''
	Local Controls
	'''
	'''
	Control 1
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during process
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control Created:', control_icon_1
	print 'Local Pad Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constrain after snapping
	# Driver: joint.
	# Control: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)


	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> joint
	pm.orientConstraint(control_icon_1, root_joint)
	'''
	Control 2
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during process
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control Created:', control_icon_2
	print 'Local Pad Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constrain after snapping
	# Driver: joint.
	# Control: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)


	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> joint
	pm.orientConstraint(control_icon_2, joint_2)
	'''
	Control 3
	'''
		# Create a control
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during process
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control Created:', control_icon_3
	print 'Local Pad Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constrain after snapping
	# Driver: joint.
	# Control: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)


	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> joint
	pm.orientConstraint(control_icon_3, joint_3)


	''' 
	Parenting Controls Together
	'''
	# Pad 3 (last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'hierarchy Created'

def Joint_Renamer():

	'''

	how to run:
	import Rig_Tools
	Rig_Tools.Joint_Renamer()

	'''
	print 'Joint Renamer - Activate and Destroy inferior names'

	joint_chain =  pm.ls(selection=True, dag=True)

	print 'selected items:',  joint_chain

	''' 
	naming conventions
	'''

	ori = raw_input() 
	system_name = raw_input()
	count = 0
	suffix = 'Icon'


	'''
	Loop thorugh joint joint_chain
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
		print 'Superior Name:', new_name

		# Rename Joint
		current_joint.rename(new_name)

def padding_tool():
	'''
	import Rig_Tools
	reload(Rig_Tools)
	Rig_Tools.padding_tool()
	'''
	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	#create  empty group 
	# empty=True will create a empty group
	#
# Error
	pad = pm.group(empty=True)

	# move group to joint.
	#	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	#freeze transform on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# parent jont to group
	pm.parent(root_joint, pad)

	#renaming
	pad_name = root_joint.replace('', '')
	pad.rename(pad_name)
	print 'Paddin group Created'

def priming_tool():
	''' 
	import Rig_Tools
	reload(Rig_Tools)
	Rig_Tools.priming_tool()
	'''
	#get selected.
# Naming error
	selected = pm.ls(selection=True)
	# print 'Joints Selected:' selected
	target_joint = selected[0]

	control_icon_name = target_joint.replace('_bind', '_icon')
	local_pad_name = target_joint.replace('_bind', '_local')

	# create control
	# normal set to x and radius is 1.8
	control_icon = pm.circle(normal=[1, 0, 0], radius=1.8)[0]

	# group control (not an empty group)
	local_pad = pm.group()

	print 'Control Icon:', control_icon
	print 'Pad Created:'. local_pad

	# move group to target joint.
	#	and delete constraint
	temp_constraint = pm.parentConstraint(target_joint, local_pad)
	pm.delete(temp_constraint)

	# Orient Constraint joint to control.
	pm.orientConstraint(control_icon, target_joint)
