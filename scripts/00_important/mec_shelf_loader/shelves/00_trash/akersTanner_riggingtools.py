''' 
Lesson - Joint Renamer
rigging.py

Description
	Practicle use of loops
	Renaming joint based upon a naming convention

How to Run:

import rigging
reload(rigging)


'''

print 'Rigging Tools Active'

import pymel.core as pm 


def hierarchy():
	'''
	Create a hierarchy based upon a given system

	Select root joint chain and execute function.
	
	import rigging
	reload (rigging)
	rigging.hierarchy()
	'''
	
	'''
	Imput
	what are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	print 'Joint System:', 

	root_joint = joint_system[0]
	joint_1 = joint_system[1]
	joint_2 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transformes on group 
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
	control_icon_1 = pm. circle(normal=[1, 0, 0], radius=2)
	
	# Create a group
	# Group control during the process.
	local_pad_1 = pm.group()
	
	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1
	
	# Move Group over to the target joint.
	# Delete constrain after snapping
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control
	# normal=[1, 0, 0], radius=2
	control_icon_2 = pm. circle(normal=[1, 0, 0], radius=2)
	
	# Create a group
	# Group control during the process.
	local_pad_2 = pm.group()
	
	# Output control and pad.
	print 'Control 1 Created:', control_icon_2
	print 'Local Pad 1 Created:', local_pad_2
	
	# Move Group over to the target joint.
	# Delete constrain after snapping
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_1, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_1)

	'''
	Control 3
	'''
	# Create a control
	# normal=[1, 0, 0], radius=2
	control_icon_3 = pm. circle(normal=[1, 0, 0], radius=2)
	
	# Create a group
	# Group control during the process.
	local_pad_3 = pm.group()
	
	# Output control and pad.
	print 'Control 1 Created:', control_icon_3
	print 'Local Pad 1 Created:', local_pad_3
	
	# Move Group over to the target joint.
	# Delete constrain after snapping
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constrain the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_2)
	
	'''
	Parent controls together.
	'''
	#pad 3 (Last) ->control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1) 
	
	print 'Hierarchy Created.'


def renaming():
	'''
	Lesson - Joint Renamer
	renamer.py

	Description:
	Practical use of loops.
	Renaming joint based upon a naming convention.

	How to Run:

	import rigging
	reload(rigging)
	rigging.renaming()


	'''

	print 'Joint Renamer - Active'

	import pymel.core as pm

	'''
	Get Selected.

	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items:', joint_chain

	'''
	Figure out naming convention
	'lt_middle_01_bind' -> 'lt_middle_04_waste'
	'ct_tail_01_bind', -> 'ct_tail_04_waste'
	'''

	ori = 'ct'
	system_name = 'tail'
	count = 1
	suffix = 'bind'

	

	'''
	Loop through joint chain.
	'''
	for current_joint in joint_chain:
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix) 
		print 'New_Name', new_name

		# Rename joint
		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)


def padding():
	'''
	import rigging
	reload (rigging)
	rigging.padding() 
	'''
	
	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Creat empty group
	# empty=True will create empty group
	#
	pad = pm.group(empty=True)
	# Move group to joint
	#   and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=2, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

		
	print 'Padding goup created'


def priming():
	'''
	

	import rigging
	reload(rigging)
	rigging.priming()
	'''
	
	# Get Selected
	selected = pm.ls(selection=True)
	# print 'Joints Selected', selected
	target_joint = selected[0] 

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_icon')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]


		# Group control (Not an empty group)
		local_pad = pm.group()

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to taret joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)

		print 'Local Oriented Controls Created'


def parent_loops():
	'''

	import rigging
	reload(rigging)
	rigging.parent_loops()
	'''

	print 'Lesson - Parenting'

	import pymel.core as pm

	'''
	select -r nurbsCircle1 ;
	select -r nurbsCircle2 ;
	select -r nurbsCircle3 ;
	'''

	'''
	control_1 = 'nurbsCircle1'
	control_2 = 'nurbsCircle2'
	control_3 = 'nurbsCircle3'

	print nurbsCircle1, nurbsCircle2, nurbsCircle3

	pm.parent(nurbsCircle3, nurbsCircle2, nurbsCircle1)
	'''

	selected_controls = pm.ls(selection=True)
	print 'Selected Controls:', selected_controls

	last_control = selected_controls[0]

	for current_control in selected_controls[1:]:
		print current_control
		pm.parent(current_control, last_control)	
		last_control = current_control


def if_statement():
	'''
	Lesson - if statements

	Description
		Practical examples of using an if statement in Maya.

	'''

	'''
	Basic if statement

	if condition:
		print 'Condition is True.'
	'''

	if True:
		print 'The condition is True.'

	if False:
		print 'The condition is True.'

	'''
	What is the condition?
	2 == 2

	'''


	'''
	Operators

	==  Equals
	!=  Not Equals
	>   Greater Than
	>=  Greater than or equal to
	<   Less Than
	<=  

	'''

	if 2 == 2:
		print 'The 2 is equal to 2.'



	'''
	Using multiple conditions

	and
	or 

	not	

	'''

	if 2 == 2 and 2 != 3:
		print 'This is True.'

	if 2 ==2 or 2 != 2:
		print 'This is True.'



	'''
	What is I want to react to False?
	else
	'''
	if 2 == 3:
		print 'Condition is True.'
	else:
		print 'Condition is False.'


	'''
	What if I want to have multiple paths?
	elif
	'''

	value = 1

	if value == 1:
		print 'Color is Red'
	elif value == 2:
		print 'Color is Blue'
	elif value == 3:
		print 'Color is Green'
	else:
		print 'Color is something else'

	'''
	about command
	'''

	if pm.about(windows=True):
		print 'You are using windows.'
	elif pm.about(macOS=True):
		print 'You are using osx.'
	else:
		print 'you are using a different os.'					


def xform():
	'''
	import rigging
	reload(rigging)
	rigging.xform()

	'''

	'''
	xform command - Part 1
	Intro to the xform command.

	The xform command deals	with every different way to move an 
		object in a scene.
	'''
	import pymel.core as pm

	'''
	Basic - Translation, Rotation, and Scale
	'''
	pm.xform(t=[0, 1, 0], ro=[0, 0, 0,], s=[1,1,1])

	'''
	Help Docs
	'''

	'''
	Absolute and Relative
	'''
	pm.xform(a=True, t=[0, 3, 0])

	# relative to its current position.
	pm.xform(r=True, t=[0, 3, 0])


	'''
	Object and World Space
	'''
	pm.xforms(os=True, t=[5, 0, 0])


	'''
	cvs
	'''
	control_icon = pm.circle(normal=[1, 0, 0], radius=2) [0]
	pm.xform(control_icon.cv[::2], r=True, scale=[1, 1, 1])		
















