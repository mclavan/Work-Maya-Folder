'''
Seany Snow Tyler
rigging_tools.py

Description:

How to run:
import rigging_tools
reload (rigging_tools)

'''
def hierarchy():
	'''

	import rigging_tools
	reload (rigging_tools)
	rigging_tools.hierarchy()

	'''
	import pymel.core as pm

	print 'project generated'

	#What are we working on? 
	#The Root joint

	joint_system = pm.ls(selection=True, dag=True)
	print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	print 'Hierarchy Created'

	'''
	Padding the Root Joint

	'''

	#Create and Empty Group (Null Group)
	root_pad = pm.group(empty=True)
	print 'Null Group Created'

	#Move the Null over to the Target Joint (Select Root Joint, Snap it) 
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	print 'Snapped'

	#Delete the point constraint
	pm.delete(temp_constraint)
	print 'Deleted'

	#Freeze Transforms on the Null Group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	print "Frozen"

	#Parent the root joint to the Null Group 
	pm.parent(root_joint, root_pad)
	print 'Parent'

	

	'''
	Local Controls
	'''

	'''
	Control 1 - Root Joint
	'''

	#Create control
	#normal flag [1,0,0], radius =2 
	control_icon_1 = pm.circle(normal=[1,0,0], radius = 2)[0]
	print 'Control Icon 1 Created:' , control_icon_1

	#create a group
	#Grouping  control during the process
	local_pad_1 = pm.group()
	print 'Local Pad 1 Created:', local_pad_1

	#Move group over to the target joint (root_joint, local_pad_1)
	#Delete constraint after snapping
	temp_constraint = pm.parentConstraint(root_joint,local_pad_1)
	print "Root Joint parentConstraint'd to Local Pad 1"
	pm.delete(temp_constraint)
	print 'temp_constraint has been deleted'

	#Orient Constrain the joint to the control
	#Driver ---> Driven
	#Control ---> Joint
	pm.orientConstraint(control_icon_1,root_joint)
	print 'orientConstraint created for cI1 to rJ'

	print 'CONTROL FOR ROOT JOINT COMPLETE'


	'''
	Control 2 - Joint 2 
	''' 

	#Create control
	#normal flag [1,0,0], radius =2 
	control_icon_2 = pm.circle(normal=[1,0,0], radius = 2)[0]
	print 'Control Icon 2 Created:' , control_icon_2

	#create a group
	#Grouping  control during the process
	local_pad_2 = pm.group()
	print 'Local Pad 2 Created:', local_pad_2

	#Move group over to the target joint (joint_2, local_pad_2)
	#Delete constraint after snapping
	temp_constraint = pm.parentConstraint(joint_2,local_pad_2)
	print "Joint 2 parentConstraint'd to Local Pad 2"
	pm.delete(temp_constraint)
	print 'temp_constraint has been deleted'

	#Orient Constrain the joint to the control
	#Driver ---> Driven
	#Control ---> Joint
	pm.orientConstraint(control_icon_2,joint_2)
	print 'orientConstraint created for cI2 to j2'

	print 'JOINT 2 COMPLETE'

	'''
	Control 3 - Joint 3 
	'''
	#Create control
	#normal flag [1,0,0], radius =2 
	control_icon_3 = pm.circle(normal=[1,0,0], radius = 2)[0]
	print 'Control Icon 3 Created:' , control_icon_3

	#create a group
	#Grouping  control during the process
	local_pad_3 = pm.group()
	print 'Local Pad 3 Created:', local_pad_3

	#Move group over to the target joint (joint_3, local_pad_3)
	#Delete constraint after snapping
	temp_constraint = pm.parentConstraint(joint_3,local_pad_3)
	print "Joint 3 parentConstraint'd to Local Pad 3"
	pm.delete(temp_constraint)
	print 'temp_constraint has been deleted'

	#Orient Constrain the joint to the control
	#Driver ---> Driven
	#Control ---> Joint
	pm.orientConstraint(control_icon_3,joint_3)
	print 'orientConstraint created for cI3 to j3'

	print 'JOINT 3 COMPLETE'

	'''
	Parenting
	'''
	#Parent Pad 3 (last) ---> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	pm.parent(local_pad_1, root_pad)
	print 'Icons Parented'

	#rename
	pm.rename(local_pad_1, 'lt_finger_01_local')
	pm.rename(local_pad_2, 'lt_finger_02_local')
	pm.rename(local_pad_3, 'lt_finger_03_local')

	pm.rename(root_pad, 'lt_finger_group')

	

	print 'Hierarchy Finished'

'''
Tools
'''

def padding_tool():
	import pymel.core as pm
	'''
	import rigging_tools
	reload (rigging_tools)
	rigging_tools.padding_tool()

	'''
	selected = pm.ls(selection=True)
	#print 'Current Selected:', selected
	root_joint = selected[0]

	#create empty group
	root_pad = pm.group(empty=True)
	print 'Null group Created'

	#move group to joint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	print 'Point Constraint happened'

	#delete constraint
	pm.delete(temp_constraint)
	print 'Temp Constraint Deleted'

	#Freeze transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	print 'Frozen'

	#parent joint to group
	pm.parent(root_joint, root_pad)

	#renaming
	#lt_finger_01_bind
	#lt_finger_00_pad
	pad_name = 'lt_finger_00_pad'
	root_pad.rename(pad_name)

	print 'padding group created'


def joint_renamer():
	import pymel.core as pm

	#Get Selected

	#pm.ls(selection=True)

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected Items:', joint_chain

	#figure out naming convention
	# lt_finger_01_bind ---> lt_finger_04_waste

	ori = 'lt'
	system_name = 'finger'
	count = 1
	suffix = 'bind'

	#Loop through chain
	for current_joint in joint_chain:
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		# Rename joint
		current_joint.rename(new_name)

		count = count + 1

	new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_name)


		


def priming_tool():
	import pymel.core as pm
	
	'''
	import rigging_tools
	reload (rigging_tools)
	rigging_tools.primming_tool()

	'''

	#Get selected
	selected = pm.ls(selection=True)
	# print 'Joint Selected:', selected
	# target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		prime_pad_name = target_joint.replace('_bind', '_prime')

		#Create Control
		#normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1,0,0] , radius=1.8, name=control_icon_name)[0]
		# print 'circle made'

		#Group Control (Not and empty group)
		prime_pad = pm.group(name=prime_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created', prime_pad

		#Move group to target joint
		#and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, prime_pad)
		pm.delete(temp_constraint)
		print 'deleted'

		#Orient Constraint joint to control
		pm.orientConstraint(control_icon, target_joint)


		print 'Local Oriented Controls Created'


