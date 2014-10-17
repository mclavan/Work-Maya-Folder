'''
Amber Fabian
Fabian_Amber_riggingTools_CRI1_1408py

How to Run:

import Fabian_Amber_riggingTools_CRI1_1408
reload(Fabian_Amber_riggingTools_CRI1_1408)


'''

print 'Rigging Tools Activity'

import pymel.core as pm

def hierarchy():
	'''

	Create a hierarchy based on a given system.

	Select root joint chain and execute function.


	import Fabian_Amber_riggingTools_CRI1_1408
	Fabian_Amber_riggingTools_CRI1_1408.hierarchy()
	'''

	'''
	Input
	What are we working on?
	the root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create an empty group
	root_pad = pm.group(empty=True)

	# Move group to target joint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint, root_pad)

	'''

	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
		# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a Group
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 Created:' , control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constraint after snapping
	# Driver: joint, Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
		# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a Group
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 2 Created:' , control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constraint after snapping
	# Driver: joint, Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a Group
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 Created:' , control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constraint after snapping
	# Driver: joint, Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent controls together
	'''
	# Pad 3 (last) --> Control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)


	print 'Hierarchy Created'


def padding_tool():

	'''
	import Fabian_Amber_riggingTools_CRI1_1408
	reload(Fabian_Amber_riggingTools_CRI1_1408)
	Fabian_Amber_riggingTools_CRI1_1408.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create an empty group
	pad = pm.group(empty=True)

	# Move group to joint.
	# And delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)



	print 'Padding group created.'

def priming_tool():
	'''
	import Fabian_Amber_riggingTools_CRI1_1408
	reload(Fabian_Amber_riggingTools_CRI1_1408)
	Fabian_Amber_riggingTools_CRI1_1408.priming_tool()
	'''

	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]


		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		# 	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to Control.
		pm.orientConstraint(control_icon, target_joint)




	print 'Local Oriented Controls Created.'




def delete_history():
	'''
	import Fabian_Amber_riggingTools_CRI1_1408
	reload(Fabian_Amber_riggingTools_CRI1_1408)
	Fabian_Amber_riggingTools_CRI1_1408.delete_history()
	'''

	# Delete Command delets objects in 3D space.
	#	The ch flag is for deleting construction history.
	pm.delete(ch=True)

	print 'History has been deleted on all selected objects.'

def unlock_and_show():
	'''
	Unlock and make keyable all channels of the first object.

	import Fabian_Amber_riggingTools_CRI1_1408
	reload(Fabian_Amber_riggingTools_CRI1_1408)
	Fabian_Amber_riggingTools_CRI1_1408.unlock_and_show()
	'''

	pm.ls(selection=True)
	first_selected = selected[0]

	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)	
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)
	

	print 'first selected object has all channels shown.'


def rename():
	'''
	Naming Conventions

	Root Joint - 'lt_middle_01_bind'
	Root Pad - 'lt_middle_00_pad'
	Proxy Geo - 'lt_middle_01_proxy'
	Local Pad - 'lt_middle_01_local'
	Control Icon - 'lt_middle_01_icon'

	

	root_joint = 'lt_middle_01_bind'

	proxy_name = root_joint.replace('_bind', '_proxy')
	icon_name = root_joint.replace('_bind', '_icon')
	root_pad_name = root_joint.replace('01_bind', '00_pad')


	print 'Old Name: ', root_joint
	print 'New Name: ', proxy_name
	print 'Control Name:', icon_name
	print 'Root Pad Name:', root_pad
	'''

	'''
	Get selected
	
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	second_selected = selected [1]

	new_proxy_name = first_selected.replace('_bind', '_proxy')
	print 'New Proxy Name:', new_proxy_name
	second_selected.rename(new_proxy_name)
	print  'New Prxy Name:', second_selected
	'''

	selected = pm.ls(selection=True)
	root_joint = selected [0]

	new_pad_name = root_joint.replace('01_bind', '00_pad')
	print 'Pad Name:', new_pad_name
	pad = pm.group(empty = True, name = new_proxy_name)








