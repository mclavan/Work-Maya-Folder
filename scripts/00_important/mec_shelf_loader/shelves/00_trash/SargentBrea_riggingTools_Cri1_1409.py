'''

rigging_tools.py
Brea Sargent
'''

'''
Lesson - Joint Renamer
rigging_tools.py 

Desription:
   Practical use of loops.
   Renaming joint based upon a naming convention.

How to run

import SargentBrea_riggingTools_CRI_1409
reload(SargentBrea_riggingTools_CRI_1409)
SargentBrea_riggingTools_CRI_1409.hierarchy()


'''

print 'Rigging Tools Active'

import pymel.core as pm 

def hierarchy():
	'''
	Create a hierarchy based upon a given system.

	Select root joint chain and execute function.
	
 How to run

	import SargentBrea_riggingTools_CRI_1409
	reload(SargentBrea_riggingTools_CRI_1409)
	SargentBrea_riggingTools_CRI_1409.hierarchy()
	'''

	'''
	Input
	What are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection= True, dag=True)
	# print 'Joint System:' , joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding the Root Joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control
	# normal=[1, 0, 0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move  group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=False, keyable=True)
	control_icon_1.tz.set(lock=False, keyable=True)

	control_icon_1.rx.set(lock=False, keyable=True)
	control_icon_1.ry.set(lock=False, keyable=True)
	control_icon_1.rz.set(lock=False, keyable=True)

	control_icon_1.sx.set(lock=False, keyable=True)
	control_icon_1.sy.set(lock=False, keyable=True)
	control_icon_1.sz.set(lock=False, keyable=True)
	control_icon_1.v.set(lock=False,  keyable=True)

	'''
	Control 2
	'''
	# Create a control
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2= pm.group()

	# Output control and pad.
	print 'Control 2 Created:', control_icon_2
	print 'Local Pad 2 Created:', local_pad_2

	# Move  group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control
	# normal=[1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3= pm.group()

	# Output control and pad.
	print 'Control 3 Created:', control_icon_3
	print 'Local Pad 3 Created:', local_pad_3

	# Move  group over to the target joint.
	# Delete constrain after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control together
	'''
	# Pad 3 (Last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'Hierarchy Created.'
	

# 
def joint_renamer():
	
	'''

	How to Run:

	import SargentBrea_riggingTools_CRI_1409
	reload(SargentBrea_riggingTools_CRI_1409)
	SargentBrea_riggingTools_CRI_1409.hierarchy()
	'''

	print 'Joint Renamer - Active'

	import pymel.core as pm 

	'''
	Get selected.

	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items:', joint_chain
	'''
	Figure out naming convention.
	'lt_arm_01bind' -> 'lt_arm_03_waste'
	'ct_tail_01_bind', -> 'ct_tail_06_waste'
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'bind'



	'''
	Loop through joint chain
	'''
	for current_joint in joint_chain:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		# Rename joint
		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

def padding_tool():
	'''

	How to Run:

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Current Selected:' , selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create a empty group
	#
	pad = pm.group(empty=True)

	# Move group to joint.
	# 	and delte constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Tranforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
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
	#print 'Joints Selected:', selected
	#target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('bind', '_local')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius= 1.8,
			name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group()

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad 

		# Move group to target joint.
		#	and delete constraint.
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)

		print 'Local Oriented Controls Created.'



