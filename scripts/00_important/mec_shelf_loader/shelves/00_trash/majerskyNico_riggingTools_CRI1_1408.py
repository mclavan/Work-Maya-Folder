'''
Nico Majersky
CRI1 1408
'''

print 'Rigging Tools Active'

import pymel.core as pm

def hierarchy():

	'''
	Run with:
	import Rig_Tools
	reload(Rig_Tools)
	'''

	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Pad Root Joint
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
	1
	'''
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Grouping control during process
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control Created: ', control_icon_1
	print 'Local Pad Created: ', local_pad_1


	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)


	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_1, root_joint)
	
	'''
	2
	'''
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Grouping control during process
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control Created: ', control_icon_2
	print 'Local Pad Created: ', local_pad_2


	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)


	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	3
	'''
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Grouping control during process
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control Created: ', control_icon_3
	print 'Local Pad Created: ', local_pad_3


	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)


	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_3, joint_3)


	# Pad 3
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'hierarchy Created'

def joint_renamer():

	'''
	Run with:
	import Rig_Tools
	Rig_Tools.Joint_Renamer()
	'''

	print 'Joint Renamer'

	joint_chain =  pm.ls(selection=True, dag=True)

	print 'selected items: ',  joint_chain

	''' 
	naming
	'''

	ori = raw_input() 
	system_name = raw_input()
	count = 0
	suffix = 'Icon'

	'''
	Loop through joint, "joint_chain"
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
		print 'Superior Name: ', new_name

		# Rename Joint
		current_joint.rename(new_name)

def padding_tool():
	'''
	Run with:
	import Rig_Tools
	reload(Rig_Tools)
	Rig_Tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	pad = pm.group(empty=True)

	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	pm.parent(root_joint, pad)

	#rename
	pad_name = root_joint.replace('', '')
	pad.rename(pad_name)

	print 'Padding Group Created'

def priming_tool():

	'''
	Run with:
	import Rig_Tools
	reload(Rig_Tools)
	Rig_Tools.priming_tool()
	'''

	selected = om.ls(selection=True)

	# print 'Joints Selected: ' selected
	target_joint = selected[0]

	control_icon_name = target_joint.replace('_bind', '_icon')
	local_pad_name = target_joint.replace('_bind', '_local')

	# normal is x
	control_icon = pm,circle(normal=[1, 0, 0], radius=1.8)[0]

	# group (not empty)
	local_pad = pm.group()

	print 'Control Icon:', control_icon
	print 'Pad Created:'. local_pad

	temp_constraint = pm.parentConstraint(target_joint, local_pad)
	pm.delete(temp_constraint)

	pm.orientConstraint(control_icon, target_joint)
