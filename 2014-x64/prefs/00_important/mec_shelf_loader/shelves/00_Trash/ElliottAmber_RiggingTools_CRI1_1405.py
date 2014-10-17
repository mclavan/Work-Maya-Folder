'''
Amber Elliott
ElliottAmber_RiggingTools_CRI1_1405.py

Description:

Group of Rigging Tools

How to Run:

import ElliottAmber_RiggingTools_CRI1_1405
reload(ElliottAmber_RiggingTools_CRI1_1405)
'''

import pymel.core as pm
print 'Rigging Tools Active'

def hierarchy():
	'''
	import ElliottAmber_RiggingTools_CRI1_1405
	reload(ElliottAmber_RiggingTools_CRI1_1405)
	ElliottAmber_RiggingTools_CRI1_1405.hierarchy()
	'''

	print 'Hierarchy Generated'

	#The user will select the root joint and the tool 
	#	will apply the systems.

	root_joint='lt_middle_01_bind'
	second_joint='lt_middle_02_bind'
	third_joint='lt_middle_03_bind'

	'''
	#Pad the root joint. 
	'''

	#Create an empty group.
	pad=pm.group(empty=True,name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	#Move group to root joint.
	#Point constrain group to root joint.
	# offset off(Snapping)

	kenny=pm.pointConstraint(root_joint, pad)

	#Delete Constraint
	pm.delete(kenny)

	#Freeze transforms on group.
	pm.makeIdentity(pad,apply=True, t=1,r=1,s=1,n=0)


	#Parent root joint to group.
	pm.parent(root_joint,pad)


	#Create a local oriented control for each joint. 
	#lt_middle_01_bind,lt_middle_02_bind,lt_middle_03_bind



	'''
	Control 1
	'''
	#Create control(circle)
	control_icon_1=pm.circle(name='lt_middle_01_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local=pm.group(control_icon_1, name='lt_middle_01_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(root_joint,local)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_1,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_1,root_joint)


	'''
	control 2
	'''

	#Create control(circle)
	control_icon_2=pm.circle(name='lt_middle_02_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local2=pm.group(control_icon_2, name='lt_middle_02_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(second_joint,local2)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_2,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_2,second_joint)

	'''
	control 3
	'''
	#Create control(circle)
	control_icon_3=pm.circle(name='lt_middle_03_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local3=pm.group(control_icon_3, name='lt_middle_03_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(third_joint,local3)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_2,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_3,third_joint)

def joint_renamer():
	'''
	import ElliottAmber_RiggingTools_CRI1_1405
	reload(ElliottAmber_RiggingTools_CRI1_1405)
	ElliottAmber_RiggingTools_CRI1_1405.joint_renamer()
	'''

	'''
	#Select the root joint and loop through all joint in the joint chain.
	#'ori_name_count_suffix'
	#'ct_back_01_bind'

	import book
	book.joint_rename()
	'''

	#What am I working on?
	#Get all joints in a selected joint chain
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Item Selected:', joint_chain



	#Build our new name
	#'lt'
	#'arm'
	#01
	#'bind'

	ori=raw_input()
	name= raw_input()
	count=1
	suffix = 'bind'

	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count,suffix)
	
		print 'Joint Name:', new_name

		current_joint.rename(new_name)

		count=count+1
		
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1,'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)

	print 'Joint Chain Renamed'

def padding_tool():
	'''
	import ElliottAmber_RiggingTools_CRI1_1405
	reload(ElliottAmber_RiggingTools_CRI1_1405)
	ElliottAmber_RiggingTools_CRI1_1405.padding_tool()
	'''

	selected = pm.ls(selection=True)
	#print 'Current Selected:', selected
	root_joint=selected[0]
	print 'Current Selected:', selected

	#Create empty group
	#empty=True will create empty group

	pad=pm.group(empty=True)


	#move group to joint
	#	and delete constraint
	temp_constraint=pm.pointConstraint(root_joint,pad)
	pm.delete(temp_constraint)

	#Freese Transforms on the group

	pm.makeIdentity(pad,apply=True, t=1,r=1,s=1,n=0)

	#Parent joitn to group

	pm.parent(root_joint,pad)

	#Rename
	#ct_tail_01_bind
	#ct_tail_00_pad

	pad_name=root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)




	print 'Padding group created.'

def priming_tool():
	'''
	import ElliottAmber_RiggingTools_CRI1_1405
	reload(ElliottAmber_RiggingTools_CRI1_1405)
	ElliottAmber_RiggingTools_CRI1_1405.priming_tool()
	'''

	#Get selected

	selected=pm.ls(selection=True)
	#print 'Joints Selected:', selected

	last_control=''

	for target_joint in selected:

		control_icon_name=target_joint.replace('_bind','_icon')
		local_pad_name=target_joint.replace('_bind','_local')

		#Create Control
		#normal set to x and radius is 1.8

		control_icon=pm.circle(normal=[1,0,0], radius=1.8,
		name=control_icon_name)[0]



		#Group control(not empty group)

		local_pad=pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		#Move group to target joint
		# and delete constraint

		temp_constraint=pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		#Orient Constraint joint to control
		pm.orientConstraint(control_icon, target_joint)

		print 'Local Oriented Controls Created'

		#Parenting with a loop 


		pm.parent(local_pad,last_control)
		last_control=control_icon

#Extra

def parenting_with_pads():
	'''
	import ElliottAmber_RiggingTools_CRI1_1405
	reload(ElliottAmber_RiggingTools_CRI1_1405)
	ElliottAmber_RiggingTools_CRI1_1405.parenting_with_pads()
	'''

	print 'Hierarchy Generated'

	#The user will select the root joint and the tool 
	#	will apply the systems.

	root_joint='lt_middle_01_bind'
	second_joint='lt_middle_02_bind'
	third_joint='lt_middle_03_bind'

	'''
	#Pad the root joint. 
	'''

	#Create an empty group.
	pad=pm.group(empty=True,name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	#Move group to root joint.
	#Point constrain group to root joint.
	# offset off(Snapping)

	kenny=pm.pointConstraint(root_joint, pad)

	#Delete Constraint
	pm.delete(kenny)

	#Freeze transforms on group.
	pm.makeIdentity(pad,apply=True, t=1,r=1,s=1,n=0)


	#Parent root joint to group.
	pm.parent(root_joint,pad)


	#Create a local oriented control for each joint. 
	#lt_middle_01_bind,lt_middle_02_bind,lt_middle_03_bind



	'''
	Control 1
	'''





	#Create control(circle)
	control_icon_1=pm.circle(name='lt_middle_01_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local=pm.group(control_icon_1, name='lt_middle_01_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(root_joint,local)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_1,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_1,root_joint)


	'''
	control 2
	'''

	#Create control(circle)
	control_icon_2=pm.circle(name='lt_middle_02_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local2=pm.group(control_icon_2, name='lt_middle_02_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(second_joint,local2)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_2,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_2,second_joint)

	'''
	control 3
	'''
	#Create control(circle)
	control_icon_3=pm.circle(name='lt_middle_03_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local3=pm.group(control_icon_3, name='lt_middle_03_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(third_joint,local3)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_2,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_3,third_joint)

	'''
	Parent
	'''

	#Parenting the middle 2 local to middle 1 icon, 


	pm.parent(local2,control_icon_1)

	#then parent mmiddle 3 local to middle 2 icon.

	pm.parent(local3,control_icon_2)

	
def colored_icons():
	'''
	import ElliottAmber_RiggingTools_CRI1_1405
	reload(ElliottAmber_RiggingTools_CRI1_1405)
	ElliottAmber_RiggingTools_CRI1_1405.colored_icons()
	'''

	print 'Hierarchy Generated'

	#The user will select the root joint and the tool 
	#	will apply the systems.

	root_joint='lt_middle_01_bind'
	second_joint='lt_middle_02_bind'
	third_joint='lt_middle_03_bind'

	'''
	#Pad the root joint. 
	'''

	#Create an empty group.
	pad=pm.group(empty=True,name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	#Move group to root joint.
	#Point constrain group to root joint.
	# offset off(Snapping)

	kenny=pm.pointConstraint(root_joint, pad)

	#Delete Constraint
	pm.delete(kenny)

	#Freeze transforms on group.
	pm.makeIdentity(pad,apply=True, t=1,r=1,s=1,n=0)


	#Parent root joint to group.
	pm.parent(root_joint,pad)


	#Create a local oriented control for each joint. 
	#lt_middle_01_bind,lt_middle_02_bind,lt_middle_03_bind



	'''
	Control 1
	'''

	#Create control(circle)
	control_icon_1=pm.circle(name='lt_middle_01_icon',
		normal=[90,0,0])[0]

	#COLOR THE ICON

	selected=pm.ls(selection=True)
	first_selected=selected[0]
	print 'First Selected Object:', first_selected

	first_selected.overrideEnabled.set(1)
	blue=6
	first_selected.overrideColor.set(blue)


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local=pm.group(control_icon_1, name='lt_middle_01_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(root_joint,local)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_1,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_1,root_joint)


	'''
	control 2
	'''

	#Create control(circle)
	control_icon_2=pm.circle(name='lt_middle_02_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local2=pm.group(control_icon_2, name='lt_middle_02_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(second_joint,local2)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_2,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_2,second_joint)

	'''
	control 3
	'''
	#Create control(circle)
	control_icon_3=pm.circle(name='lt_middle_03_icon',
		normal=[90,0,0])[0]


	#Create group(Not Empty)
	#This will automaticaly parent the control under the group

	local3=pm.group(control_icon_3, name='lt_middle_03_local')



	#Move group to the target joint
	#Use a parent constraint driver is the joint.
	#	Where driven is the group.
	#	Offset is off(Snapping)

	temp=pm.parentConstraint(third_joint,local3)

	#Destroy the constraint
	pm.delete(temp)

	#Delete History on control

	pm.delete(control_icon_2,ch=True)

	#Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_3,third_joint)

	'''
	Parent
	'''

	#Parenting the middle 2 local to middle 1 icon, 


	pm.parent(local2,control_icon_1)

	#then parent mmiddle 3 local to middle 2 icon.

	pm.parent(local3,control_icon_2)
	







