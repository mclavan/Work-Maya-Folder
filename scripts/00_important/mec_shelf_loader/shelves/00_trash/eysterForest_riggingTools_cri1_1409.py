'''
Forest Eyster
eysterForest_riggingTools_cri1_1409.py

Description:
	A group of rigging related tools.

How to Run:

import eysterForest_riggingTools_cri1_1409
reload(eysterForest_riggingTools_cri1_1409)

'''
print 'Rigging Tools Active'

import pymel.core as pm

# Main 4 Hierarchy Iteams

def hierarchy():

	'''
	Create a hierachy based upon a given system

	Select root joint chain and excute fuction
	
	import eysterForest_riggingTools_cri1_1409
	reload(eysterForest_riggingTools_cri1_1409)
	eysterForest_riggingTools_cri1_1409.hierarchy()
	'''

	'''
	Input
	What are we working on?
	The root joint.
	'''
	joint_system = pm.ls(selection=True, dag=True)
	# print 'Joint System: ', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''	
	Nameing Conventions

	Root Joint - 'lt_middle_01_bind'
	Root Pad - 'lt_middle_00_pad'
	Proxy Geo - 'lt_middle_01_proxy'
	Local Pad - 'lt_middle_01_local'
	Conrtol Icon - 'lt_middle_01_icon'

	'''

	'''
	Padding Root Joint
	'''
	# Create a empty group
	new_pad_name = root_joint.replace('01_bind', '00_pad')
	root_pad = pm.group(empty=True, name=new_pad_name)

	# Move group over to the target joint.

	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on group.

	freeze_group = pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.

	pm.parent(root_joint, root_pad)

	# Rename

	joint_parent_group = root_pad

	'''
	Local Controls
	'''

	'''
	Control 1 - Root Joint
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	new_icon_name = root_joint.replace('bind', 'icon')
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2, name=new_icon_name)

	# Create a group.
	# Grouping control during the process.
	new_local_name = root_joint.replace('bind', 'local')
	local_pad_1 = pm.group(name=new_local_name)

	# Output control and pad.
	print 'Control 1 Created:', control_icon_1
	print 'Local Pad 1 Created:', local_pad_1

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver - Joint
	# Driven - Group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	new_icon_name = root_joint.replace('01_bind', '02_icon')
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2, name=new_icon_name)

	# Create a group.
	# Grouping control during the process.
	new_local_name = root_joint.replace('01_bind', '02_local')
	local_pad_2 = pm.group(name=new_local_name)

	# Output control and pad.
	print 'Control 1 Created:', control_icon_2
	print 'Local Pad 1 Created:', local_pad_2

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver - Joint
	# Driven - Group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	Control 3
	'''
	# Create a control.
	# normal=[1, 0, 0], radius=2
	new_icon_name = root_joint.replace('01_bind', '03_icon')
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2, name=new_icon_name)

	# Create a group.
	# Grouping control during the process.
	new_local_name = root_joint.replace('01_bind', '03_local')
	local_pad_3 = pm.group(name=new_local_name)

	# Output control and pad.
	print 'Control 1 Created:', control_icon_3
	print 'Local Pad 1 Created:', local_pad_3

	# Move group over to the target joint.
	# Delete constrain after snapping.
	# Driver - Joint
	# Driven - Group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# Orient Constraint the joint to the control.
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, joint_3)

	# Lock and Hide 

	'''
	Parent Controls Together
	'''
	# Pad 3 (Last) -> Control 2
	pm.parent(local_pad_3, control_icon_2)
	
	# Pad 2 -> Control 1
	pm.parent(local_pad_2, control_icon_1)

	# Rename
	control_parent_group = local_pad_1

	'''
	Group Everything
	'''
	# # Control Group and Joint Group
	new_master_group = root_joint.replace('lt_middle_01_bind', 'master_hierarchy_grp')
	pm.group(joint_parent_group, control_parent_group, name=new_master_group)

	print 'Hierarchy Created'

def padding_tool():
	'''
	Description:
		This wiil crete a clean pad for our joint chain

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.padding_tool()
	'''

	print 'Start the Padding'

	selected = pm.ls(selection=True)
	# print 'Current Selected:' selected
	root_joint = selected[0]

	# Create empty group
	# empty=Trure will crate a empty group
	pad = pm.group(empty=True)

	# Move group to joint, and delete constraint
	temp_constraint = pm.parentConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group.
	pm.parent(root_joint, pad)

	# renaming
	# lt_middle_01_bind
	# lt_middle_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print'Padding group created.'

def priming_tool():
	'''
	Description:
		This will create a control and pad to the selected joint
		rename control and pad by replacing each title ending
		group the control and pad
		parent constraint the local pad to the target joint then delete it
		orient constraint the target joint to the control icon
		then it will repeat the process till there are no more joints that end with bind

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.priming_tool()
	'''
	# Select Object
	selected = pm.ls(selection=True)
	# print 'Joint Selected: ', selected
	# target_joint = selected[0]

	# Rename
	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create control
		# Normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint, and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control
		pm.orientConstraint(control_icon, target_joint)

	print 'Local Oriented Controls Created.'

def joint_renamer():

	'''
	This tool renaming a selected joint chain.

	selecte a root joint and run the fuction.
	- The script will prompt you first for the orientation (lt', 'rt', 'ct'),
		the name of the system ('arm', 'back', 'leg', ... ), and

	import eysterForest_riggingTools_cri1_1409
	reload(eysterForest_riggingTools_cri1_1409)
	eysterForest_riggingTools_cri1_1409.joint_renamer()

	'''


	# Selected the root joints and I will get its childern.
	joint_chain = pm.ls(selection=True, dag=True)

	# Do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
	    new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	    # Rename Command
	    # varible.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)

	current.rename(new_name)

# Lock and Hide Systems

def lock_and_hide():
	'''
	Description:
		This will lock and hide the first selected object's attrubutes

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.lock_and_hide()

	'''

	print 'Lock and Hide'

	selected = pm.ls(selection=True)
	print 'Selected: ', selected

	first_selected = selected[0]

	# Lock and Hide
	first_selected.tx.set(lock=True, keyable=False)
	first_selected.ty.set(lock=True, keyable=False)
	first_selected.tz.set(lock=True, keyable=False)
	first_selected.rx.set(lock=True, keyable=False)
	first_selected.ry.set(lock=True, keyable=False)
	first_selected.rz.set(lock=True, keyable=False)
	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)
	first_selected.v.set(lock=True, keyable=False)

def unlock_and_show():
	'''
	Description:
		This will unlock and show the first selected object's attrubutes

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.unlock_and_show()

	'''

	print 'Unlock and Show'

	selected = pm.ls(selection=True)
	print 'Selected: ', selected

	first_selected = selected[0]

	# Unlock and Show
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

# Color Icon Changers

def color_control_blue():
	'''
	Description:
		This will change the color of the selected control to blue

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.color_control_blue()

	'''

	print 'Blue Control'

	selected = pm.ls(selection=True)
	print 'Selected: ', selected

	first_selected = selected[0]

	# first_selected
	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)

def color_control_red():
	'''
	Description:
		This will change the color of the selected control to red

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.color_control_red()

	'''

	print 'Red Control'

	selected = pm.ls(selection=True)
	print 'Selected: ', selected

	first_selected = selected[0]

	# first_selected
	first_selected.overrideEnabled.set(1)
	red = 13
	first_selected.overrideColor.set(red)

def color_control_yellow():
	'''
	Description:
		This will change the color of the selected control to yellow

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.color_control_yellow()

	'''

	print 'Yellow Control'

	selected = pm.ls(selection=True)
	print 'Selected: ', selected

	first_selected = selected[0]

	# first_selected
	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(yellow)

# Create Attrubutes Hand Icon

def create_fingers():
	'''
	Description:
		This wiil create an IKFK switch, Finger curl, finger spread, and thumb curl 
			for our and hand control.

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.create_fingers()

	'''

	print 'Finger Attrubutes'

	selected = pm.ls(selection=True)
	print 'Selected: ', selected

	first_selected = selected[0]

	# addAttr
	first_selected.addAttr('IKFK', keyable=True)

	first_selected.addAttr('FINGERS', at='enum', en='---------------', keyable=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', at='enum', en='---------------', keyable=True)
	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	first_selected.addAttr('THUMB', at='enum', en='---------------', keyable=True)
	first_selected.addAttr('thumb_curl', keyable=True)

# Create Icons

# def create_spur():
	'''
	Description
		this will create an spur icon at the origin

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.create_spur()

	'''
	
	print 'Spur is in the process'	

	mel_spur = '''circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 1.15862e-08 -s 8 -ch 1; objectMoveCommand;
	select -r nurbsCircle1.cv[6] ;
	select -tgl nurbsCircle1.cv[0] ;
	select -tgl nurbsCircle1.cv[2] ;
	select -tgl nurbsCircle1.cv[4] ;
	scale -ws -r -p 0cm 0cm 0cm 0.0857551 0.0857551 0.0857551 ;
	'''
	pm.mel.eval(mel_spur)

	print 'Spur is created'

def create_cube():
	'''
	Description:
		this will create a CV cube curve away from the origin

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.create_cube()

	'''
	print 'Cube is in the process'

	mel_cube = 'curve -d 1 -p 4.280117 0.5 0.5 -p 4.280117 0.5 -0.5 -p 4.280117 -0.5 -0.5 -p 4.280117 -0.5 0.5 -p 4.280117 0.5 0.5 -p 3.280117 0.5 0.5 -p 3.280117 -0.5 0.5 -p 4.280117 -0.5 0.5 -p 4.280117 -0.5 -0.5 -p 3.280117 -0.5 -0.5 -p 3.280117 -0.5 0.5 -p 3.280117 0.5 0.5 -p 3.280117 0.5 -0.5 -p 3.280117 -0.5 -0.5 -p 4.280117 -0.5 -0.5 -p 4.280117 0.5 -0.5 -p 3.280117 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;'
	pm.mel.eval(mel_cube)

	print "Cube Creation"

def create_arrow():
	'''
	Description
		this will create an arrow icon away from the origin

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.create_arrow()

	'''

	print 'Arrow is in the process'

	mel_arrow = 'curve -d 1 -p -7 0 0 -p -5 0 2 -p -5 0 1 -p -2 0 1 -p -2 0 -1 -p -5 0 -1 -p -5 0 -2 -p -7 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	pm.mel.eval(mel_arrow)

	print 'Arrow is created'

def create_square():
	'''
	Description
		this will create an arrow icon at the origin

	How to Run:
		import eysterForest_riggingTools_cri1_1409
		reload(eysterForest_riggingTools_cri1_1409)
		eysterForest_riggingTools_cri1_1409.create_square()

	'''

	print 'Square is in the process'

	mel_line = 'curve -d 1 -p -0.5 0 -0.5 -p -0.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 -0.5 -p -0.5 0 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
	pm.mel.eval(mel_line)

	print 'Square is created'


