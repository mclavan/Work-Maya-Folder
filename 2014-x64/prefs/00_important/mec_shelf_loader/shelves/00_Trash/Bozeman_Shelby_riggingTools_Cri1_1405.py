'''
Bozeman_Shelby_riggingTools_Cri1_1405.py
Shelby Bozeman

Description:
	Grouping of rigging tools.

How to Run:

import Bozeman_Shelby_riggingTools_Cri1_1405
reload(Bozeman_Shelby_riggingTools_Cri1_1405)

'''

print 'Rigging tools active'

import pymel.core as pm 

def hierarchy():
	'''
	Description: 
	Creates hierarchy based off a given system.
	Select the root joint and execute this function.

	How to Run:
	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.hierarchy()

	'''

	print 'Rigging tools active'

	import pymel.core as pm 

	# The user will select the root joint and the tool.
	#	  will apply the systems.

	root_joint = "lt_middle_01_bind"
	joint_2 = "lt_middle_02_bind"
	joint_3 = "lt_middle_03_bind"
	joint_4 =  "lt_middle_04_waste"

	# Pad the root joint.

	# # Create an EMPTY group.
	# pad = pm.group(empty=True, name='lt_middle_00_pad')
	# print 'Root Pad Created:', pad

	# # Point constraint group to root joint.
	# # Make sure offset is off(snapping)
	# temp = pm.pointConstraint(root_joint, pad)

	# # Delete the constraint.
	# pm.delete(temp)

	# # Freeze transforms on group.
	# pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# # Parent foot joint to group.
	# pm.parent(root_joint, pad)

	'''
	Local controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2

	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()
	 
	# Output control and pad.
	print 'Control 1 created:', control_icon_1
	print 'Local Pad 1 created', local_pad_1

	# Move group over to target joint.
	# Delete constrain after snapping.
	# Driver : Joint
	# Driven : Group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint) 

	# Orient constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_1, root_joint)
	'''
	Control 2 - joint_2
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2

	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()
	 
	# Output control and pad.
	print 'Control 2 created:', control_icon_2
	print 'Local Pad 2 created', local_pad_2

	# Move group over to target joint.
	# Delete constrain after snapping.
	# Driver : Joint
	# Driven : Group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint) 

	# Orient constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3- joint_3
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2

	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()
	 
	# Output control and pad.
	print 'Control 3 created:', control_icon_3
	print 'Local Pad 3 created', local_pad_3

	# Move group over to target joint.
	# Delete constrain after snapping.
	# Driver : Joint
	# Driven : Group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint) 

	# Orient constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Control 4- joint_4
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2

	control_icon_4 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_4 = pm.group()
	 
	# Output control and pad.
	print 'Control 4 created:', control_icon_4
	print 'Local Pad 4 created', local_pad_4

	# Move group over to target joint.
	# Delete constrain after snapping.
	# Driver : Joint
	# Driven : Group
	temp_constraint = pm.parentConstraint(joint_4, local_pad_4)
	pm.delete(temp_constraint) 

	# Orient constrain the joint to the control.
	# Driver -> Driven.
	# Control -> Joint.
	pm.orientConstraint(control_icon_4, joint_4)


	'''
	Parent Control together.
	'''

	# Pad 4(Last) -> control 3
	# Pad 3 , -> control 2
	# Pad 2, -> control 1

	pm.parent(local_pad_4, control_icon_3)
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	print 'hierarchy created'


def joint_renamer():
	'''
	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.joint_renamer()

	Description:
	Practical use of loops.
	Renaming joint based upon a naming convention.

	How to run:

	import joint_renamer
	reload(joint_renamer)
	'''

	print 'Joint Renamer Active'

	import pymel.core as pm

	'''
	Get selected.

	'''
	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items:', joint_chain

	'''
	Figure out naming convention.
	'lt_arm_01_bind'-> 'lt_arm_03_waste'
	'ct_tail_01_bind'-> 'ct_tail_06_waste'
	'''

	ori = raw_input()
	system = raw_input()
	count= 1
	suffix = 'bind'


	'''
	Loop through joint chain.
	'''
	for current_joint in joint_chain:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system, count, suffix)
		print 'New name:', new_name

		# Rename Joint

		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system, count-1, 'waste')
	current_joint.rename(new_name)


def padding_tool():
	'''



	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.padding_tool()

	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
# Missing [0]
	root_joint = selected[0]

	# Create Empty group
	# empty=True will create empty group

	pad = pm.group(empty=True)
	# Move group to joint
	# and delete constraint.
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent constraint joint to group.
	pm.parent(root_joint, pad)

	# Renaming
	pad_name(root_joint,pad)

	# renaming
	# ct_tail_01_bind
	#ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'


def priming_tool():
	'''
	import Bozeman_Shelby_riggingTools_Cri1_1405
	load(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.priming_tool()
	'''

	# Get selected.
	selected = pm.ls(selection=True)
	# print 'Joints selected:', Selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('bind', 'icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create a control
		# Normal set to x and radius is 1.8
# Missing Commas
		control_icon = pm.circle(normal=[1, 0 ,0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT empty group)
		local_pad = pm.group()

		print 'Control Icon:', control_icon
		print 'Pad_created:', local_pad

		# Move group to target joint
		#    and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)


	print 'Local Oriented Controls Created. '


def color_control_RED():
	'''
	Description:
	Change Color to Red.
	'''

	


	import pymel.core as pm


	pm.color(ud = 1)

def color_control_BLUE():
	'''
	Description:

	Change Color to Blue.


	How to Run:
	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.hierarchy()
	'''

	import pymel.core as pm


	pm.color(ud = 2)

def color_control_YELLOW():
	'''
	Description: 
	Allows you to change control color to Yellow.

	How to Run:
	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.yellow()
	
	'''

	import pymel.core as pm


	pm.color(ud = 1)

def Hide_Show_Poly_tool():
	'''
		Description: 

	By Clicking this control, it allows you to hide or show your polygons.

	How to Run:
	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.Hide_Show_Poly_tool()
	'''

	import pymel.core as pm

# Missing comma
	hidepoly = pm.modelEditor('modelPanel4', q=True, pm=True)

	if hidepoly:
		pm.modelEditor('modelPanel4', e=True, pm=True)

	else:
		pm.modelEditor('modelPanel4', e=True, pm=True)

def Freeze_Transform():
	'''
	Description:

	Allows you to freeze transformations.

	How to Run:
	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.Freeze_Transform()
	'''


	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

def circle():
	'''
	Description:

	Allows you to create a Nurbs Circle.

	How to Run:

	import Bozeman_Shelby_riggingTools_Cri1_1405
	reload(Bozeman_Shelby_riggingTools_Cri1_1405)
	Bozeman_Shelby_riggingTools_Cri1_1405.circle()
	'''
	pass

