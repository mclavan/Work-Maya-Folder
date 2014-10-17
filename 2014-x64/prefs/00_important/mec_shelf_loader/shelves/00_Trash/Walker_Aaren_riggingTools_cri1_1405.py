import pymel.core as pm 

def hierarchy(): 
	'''
	Aaren Walker
	hierarchy.py

	discription:

	How to Run:
	import hierarchy
	relaoad(hierarchy)
	hierarchy.hierarchy()
	'''

	import pymel.core as pm

	print 'Hierarchy Generated'


	# The user will select the root joint and the tool 
	#	will apply the system.

	root_joint = 'lt_middle_01_bind'
	second_joint='lt_middle_02_bind'
	third_joint= 'lt_middle_03_bind'

	# Pad the root joint.

	# Create an empty group.
	pad = pm.group(empty=True, name = 'lt_middle_00_pad')

	print 'Root Pad Created:', pad

	# Move group to target joint.
	# point constraint group to root joint.
	#		offset off(snapping)
	kenny = pm.parentConstraint(root_joint, pad)


	# Delete Constraint 
	pm.delete(kenny)

	# Freeze transformations. 
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	# Parent root joint to group.
	pm.parent(root_joint,pad)


	# create a local oriented control for each joint.
	#lt_middle_01_bind,lt_middle_02_bind,lt_middle_03_bind.

	'''
	control 1
	''' 

	# create control(circle)
	control_icon_1 = pm.circle(name= 'lt_middle_01_icon',  normal=[1, 0, 0])[0]




	# create group(NOT EMPTY)
	#		This will automatically parent the controll under the group. 
	control_icon_pad1 = pm.group(name = 'lt_middle_01_pad')




	#Move group to the target joint. 
	# 		Use a parent constraint driver is the joint.
	#		Driven is the group.
	#		offset off(snapping)
	kenny = pm.parentConstraint(root_joint, control_icon_pad1)



	# delete the constraint(kenny)
	pm.delete(kenny)

	# Delete History on the control 
	pm.delete(control_icon_1, ch=True)
	# Orient constraint: driver: control, driven: joint.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''

	# create control(circle)
	control_icon_2 = pm.circle(name= 'lt_middle_02_icon',  normal=[1, 0, 0])[0]



	# create group(NOT EMPTY)
	#		This will automatically parent the controll under the group. 
	control_icon_pad2 = pm.group(name = 'lt_middle_02_pad')


	#Move group to the target joint. 
	# 		Use a parent constraint driver is the joint.
	#		Driven is the group.
	#		offset off(snapping)
	kenny = pm.parentConstraint(second_joint, control_icon_pad2)

	# delete the constraint(kenny)
	pm.delete(kenny)




	# Delete History on the control 
	pm.delete(control_icon_2, ch=True)

	# Orient constraint: driver: control, driven: joint.
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	control 3
	'''


	# create control(circle)
	control_icon_3 = pm.circle(name= 'lt_middle_03_icon',  normal=[1, 0, 0])[0]


	# create group(NOT EMPTY)
	#		This will automatically parent the controll under the group. 
	control_icon_pad3 = pm.group(name = 'lt_middle_03_pad')


	#Move group to the target joint. 
	# 		Use a parent constraint driver is the joint.
	#		Driven is the group.
	#		offset off(snapping)
	kenny = pm.parentConstraint(third_joint, control_icon_pad3)

	# delete the constraint(kenny)
	pm.delete(kenny)



	# Delete History on the control 
	pm.delete(control_icon_3, ch=True)


	# Orient constraint: driver: control, driven: joint.
	pm.orientConstraint(control_icon_3, third_joint)


def renaming_tool():
	'''
	# Create a function called joint_rename.
	# Select the root joint and loop through all joints in the joint chain. 
	#'ori_name_count_suffix'


	How to Run:
	import hierarchy
	hierarchy.renaming_tool()
	'''
	# What am I working on?
	# get all joints in the joint chain.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected:', joint_chain

	# Build our new name
	# 'lt'
	# 'arm'
	# 01
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'


	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print 'Joint Name:', new_name

		current_joint.rename(new_name)

		count = count + 1 


	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')

	print 'Joint Name:', new_name
	count = count + 1 







	current_joint.rename(new_name)


	print 'Joint Chain Renamed'

def padding_tool():
	'''

	import hierarchy
	reload(hierarchy)
	hierarchy.padding_tool()

	'''


	selected = pm.ls(selection=True)
	# print 'Current selection', selected 

	root_joint = selected[0]
	#create empty group
	# empty = True
	pad = pm.group(empty=True)

	# move group to joint.
		#delete constraint.
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)	

	# Freeze transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	# parent joint to group.
	pm.parent(root_joint,pad)


	#rename 
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding Group Created' 
	# # create group(NOT EMPTY)
	# #		This will automatically parent the controll under the group. 
	# control_icon_pad1 = pm.group(name = 'lt_middle_01_pad')




	# #Move group to the target joint. 
	# # 		Use a parent constraint driver is the joint.
	# #		Driven is the group.
	# #		offset off(snapping)
	# kenny = pm.parentConstraint(root_joint, control_icon_pad1)



	# # delete the constraint(kenny)
	# pm.delete(kenny)



def priming_tool():
	'''
	import hierarchy
	reload(hierarchy)
 
	'''
	# Get selected
	selected = pm.ls(selection=True)
	# print 'Joints selected', selected
	# target_joint = selected[0]
	for target_joint in selected:
		
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		#create control
		#normal set to x radius is 1.8 
		control_icon = pm.circle(normal=[1,0,0], radius=1.8,
			name= control_icon_name)[0] 
		#group control (NOT EMPTY GROUP)
		local_pad = pm.group(name= local_pad_name)

		print 'control_icon'
		print 'pad created'
		# Move group to target joint
			# Delete kenny

		kenny = pm.parentConstraint(target_joint, local_pad)
		pm.delete(kenny)

		#orientConstraint joint to control 
		pm.orientConstraint(control_icon, target_joint)



		print 'Local Oriented Controls Created'









