'''
Nathan Thomas
Thomas_Nathan_CRI1_1409_rigging_tools.py

Description
	A group of rigging related tools

How to Run:

import Thomas_Nathan_CRI1_1409_rigging_tools
reload(Thomas_Nathan_CRI1_1409_rigging_tools)

NOTE: GETTING SELECTED:

start with: 

selected = pm.ls(selection=True)
	

'''

print 'Rigging Tools Active'
import pymel.core as pm

def tool():
	print 'example tool.'

	'''
	tool Description
	how to run tool
	'''

def unlock_and_show():

	'''
	Description: A shortcut for unlocking and showing attributes
	Can switch inputs around to hide and lock attributes. 


	How to Run:
	import Thomas_Nathan_CRI1_1409_rigging_tools
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.unlock_and_show()

	'''

	selected = pm.ls(selection=True)
	print 'Currently selected', selected

	first_selected = selected[0]

	# t means translate,
	# r means rotate
	# s means scale
	# v means visibility 
	# x,y,z are variables.  Lock = false means unlocked, true
	# means locked.  Keyable = true means show, false means hide. 

	# translate
	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	# rotate
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	#scale
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)	
	# visibility
	first_selected.v.set(lock=False,keyable=True)

def snapping_tool():

	'''
	Description: snaps a control to a joint, or similar objects BOTH
	ROTATION AND TRANSLATION

	How to Run:
	
	import Thomas_Nathan_CRI1_1409_rigging_tools
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.snapping_tool()

	'''
	

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	# by default, commands work on selected items, driver driven. 
	kenny = pm.parentConstraint(selected[0], selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second'

def point_snapping_tool():

	'''
	Description:moves first selected object to the second. JUST TRANSLATION
	
	How to Run:

	import Thomas_Nathan_CRI1_1409_rigging_tools
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.point_snapping_tool()

	Thomas_Nathan_CRI1_1409_rigging_tools.py.point_snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	# by default, commands work on selected items, driver driven. 
	kenny = pm.pointConstraint(selected[0], selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second'


 
	# Get Selected
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	first_joint = selected[0]

	# Create control icon
	control_icon_1 = pm.circle(normal=[0,1,0], radius = 2)[0]

	#Move control icon to target joint

	#delete constraint
	kenny = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(kenny)




	print 'Icons created'

def color_controls():
	'''
	Color Controls

	Desccription: changing the color of the control icons/anything selected

	How to Run:
	'''
	import pymel.core as pm
	selected = pm.ls(selection=True)
	print 'Currently selected', selected

	first_selected = selected[0]

	'''
	NOTE: COPY PASTE FOR EACH COLOR, OTHERWISE WILL CHANGE WHOLE SCENE
	'''


	# pick a color

			# blue

	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)

			# red

	first_selected.overrideEnabled.set(1)
	red = 13
	first_selected.overrideColor.set(red)

			# yellow

	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(yellow)

def hierarchy():
	'''
	Description: create a hierarchy based on a given system. 

	Select root joint chain and execute function. 

	How to Run:

	import Thomas_Nathan_CRI1_1409_rigging_tools
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.hierarchy()
	'''

	'''
	Input
	What are we working on?
	The root joint. 
	'''
	joint_system = pm.ls(selection=True, dag=True)

	print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	

	'''
	Padding the Root Joint
	'''	

	# Create an empty group
	'''
	Creates an empty group for you to use around icons (freeze transforms, etc)
	'''
	root_pad = pm.group(empty=True)


	# Move Group to Target Joint (snap)
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint )

	# Freeze Transforms
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)  

	# Parent constrain joint to group
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''
	
	'''
	Control 1 - the root_joint
	'''
	# create a control
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=1, name='lt_middle_00_icon')[0]

	# create a group
	# grouping control during this process
	local_pad_1 = pm.group(name='lt_middle_00_local')

	# Output control and pad
	print 'Control 1 created:', control_icon_1
	print 'Local Pad 1 created:', local_pad_1

	# move group over to the target joint
	# delete contraint after snapping
	# driver is joint, driven is group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# orient constrain the joint to the control
	# driver --> driven
	# control --> joint
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# create a control
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=1, name='lt_middle_01_icon')[0]

	# create a group
	# grouping control during this process
	local_pad_2 = pm.group(name='lt_middle_01_local')

	# Output control and pad
	print 'Control 2 created:', control_icon_2
	print 'Local Pad 2 created:', local_pad_2

	# move group over to the target joint
	# delete contraint after snapping
	# driver is joint, driven is group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# orient constrain the joint to the control
	# driver --> driven
	# control --> joint
	pm.orientConstraint(control_icon_2, joint_2)
	

	'''
	Control 3
	'''
	# create a control
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=1, name='lt_middle_02_icon')[0]

	# create a group
	# grouping control during this process
	local_pad_3 = pm.group(name='lt_middle_02_local')

	# Output control and pad
	print 'Control 3 created:', control_icon_3
	print 'Local Pad 3 created:', local_pad_3

	# move group over to the target joint
	# delete contraint after snapping
	# driver is joint, driven is group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)

	# orient constrain the joint to the control
	# driver --> driven
	# control --> joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent control togethers
	'''

	# connect pad 3 to control icon 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	'''
	# lock and hide 
	'''
	# For this, I created a new list for the control icons so I could set
	# it up in a loop. 

	# t means translate,
	# r means rotate
	# s means scale
	# v means visibility 
	# x,y,z are variables.  Lock: false means unlocked, true
	# means locked.  Keyable = true means show, false means hide. 

	control_list = [control_icon_1, control_icon_2, control_icon_3]

	for indiv_icon in control_list:
		# translate
		indiv_icon.tx.set(lock=True, keyable=False)
		indiv_icon.ty.set(lock=True, keyable=False)
		indiv_icon.tz.set(lock=True, keyable=False)
		#scale
		indiv_icon.sx.set(lock=True, keyable=False)
		indiv_icon.sy.set(lock=True, keyable=False)
		indiv_icon.sz.set(lock=True, keyable=False)	
		# visibility
		indiv_icon.v.set(lock=True, keyable=False)



	print 'Hierarchy created'

def padding_tool():

	'''
	Description:  creates a group, snapping it to a target joint, freezing
	transforms, then parenting and renaming.  

	How to run:

	import Thomas_Nathan_CRI1_1409_rigging_tools.
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.padding_tool()


	'''


	selected = pm.ls(selection=True)
	print 'Current Selected:', selected

	root_joint = selected[0]

	print 'Padding group created'

	# create empty group
	# the flag for empty group is em
	# empty=True will create empty group
	pad = pm.group(empty=True)

	# move group to joint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	# delete constraint 
	pm.delete(temp_constraint)
	# freeze transforms on said group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	# Parent group
	pm.parent(root_joint, pad)
	# renaming
	#lt_index_01_bind
	#lt_index_01_pad
	pad_name = root_joint.replace('01_bind', '01_pad')
	pad.rename(pad_name)






	print 'Padding Group Created'

def joint_renamer():
	
	'''

	Description: renames joints in scene

	How to run: 
	
	import Thomas_Nathan_CRI1_1409_rigging_tools
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.joint_renamer()

	'''
	# selection

	joint_chain = pm.ls(selection=True, dag=True, type='joint')
	print 'Selected items:', joint_chain

	# naming convention
	# figure out lt, rt, ct, etc.  Then part, then number, then bind, waste, etc. 

	ori = raw_input()
	system_name = raw_input()
	count = 1
	suffix = 'bind'

	# Loop throughout the joint chain

	for current_joint in joint_chain:
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name', new_name

		# Rename Joint
		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_name)

def priming_tool():

	'''

	Definition: creates local oriented controls.  

	How to Run:

	import Thomas_Nathan_CRI1_1409_rigging_tools
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.priming_tool()

	'''
	# Get Selected: 
	selected = pm.ls(selection=True)
	# target_joint = selected[0]

	for target_joint in selected:

	# Renaming
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Creating a Control 
		# Set Normal and set Radius
		control_icon = pm.circle(normal=[1,0,0], radius = 1.8, name=control_icon_name,)[0]


		# Grouping control (not an empty group)
		local_pad = pm.group(name=local_pad_name)


		print 'Control Icon', control_icon
		print 'Pad Created', local_pad
		# Snap group to targert joint, and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to Control
		pm.orientConstraint(control_icon, target_joint)

	print 'Local Oriented Controls Created'

def arrow_icon():

	'''
	Description:  creates an arrow icon

	How to run: 

	'''

	# arrow control icon
	import pymel.core as pm
	mel_line = 'curve -d 1 -p 0 0 -10 -p -5 0 -5 -p -10 0 0 -p -5 0 0 -p -5 0 5 -p -5 0 10 -p 0 0 10 -p 5 0 10 -p 5 0 5 -p 5 0 0 -p 10 0 0 -p 5 0 -5 -p 0 0 -10 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;' 
	pm.mel.eval(mel_line)
	print 'Control Icon Created:', icon

def square_icon():

	'''
	Description: creates a square icon

	How to run:

	'''


	# square control icon
	import pymel.core as pm
	mel_line = 'curve -d 1 -p -5 0 5 -p -5 0 0 -p 0 0 0 -p 0 0 5 -p -5 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 ' 
	pm.mel.eval(mel_line)
	print 'Control Icon Created:', icon

def cube_icon():

	'''
	Description: creates a cube icon in scene. 

	How to run:  We use the same method as for the square and arrow
	icons we created. 

	import Thomas_Nathan_CRI1_1409_rigging_tools
	reload(Thomas_Nathan_CRI1_1409_rigging_tools)
	Thomas_Nathan_CRI1_1409_rigging_tools.cube_icon

	'''

	import pymel.core as pm

	mel_line = 'curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16'
	pm.mel.eval(mel_line)

def leg_ik():

	'''
	Leg IK'

	Description: creates an Ik handle for leg (5 joints)
	'''
	import pymel.core as pm

	# Given to us by the user. 

	joint_chain = pm.ls(selection=True, dag=True)
	print joint_chain

	



	# isolate importatn joint
	root_joint = joint_chain[0]
	ankle_joint = joint_chain[2]
	ball_joint = joint_chain[3]
	toe_joint = joint_chain[4]

	# Apply the IKs
	# This command is pm.ikHandle()
	# default is single chain solver.  We need RPS for first IK. 
	# Flag for solver is:  solver (sol). So sol='ikRPsolver'
	ankle_ik = pm.ikHandle(sol='ikRPsolver', sj=root_joint, ee=ankle_joint, name='lt_ankle_ik')
	ball_ik = pm.ikHandle(sol='ikSCsolver', sj=ankle_joint, ee=ball_joint, name='lt_ball_ik')
	toe_ik = pm.ikHandle(sol='ikSCsolver',sj=ball_joint, ee=toe_joint, name='lt_toe_ik')









 
	
	



