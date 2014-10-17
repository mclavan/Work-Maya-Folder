'''
Andre Smith
book.py 

Description


How to Run:

import book 
reload(book)

'''

print 'Book has been opened.'

import pymel.core as pm

def hiearchy():
	''''
	Andre Smith
	hiearchy.py

	Description

	How to Run:
	import Smith_Andre_1405_RiggingTools
	reload(Smith_Andre_1405_RiggingTools)
	Smith_Andre_1405_RiggingTools.hiearchy()
	'''

	import pymel.core as pm

	print 'hiearchy Generated'                                                               


	# The user will select the root joint and the tool
	#     will apply the systems

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# Pad the root joint
	'''

	# Create an empty group
	pad = pm.group(empty=True, name='lt_index_01_pad')
	print 'Root Pad Created:', pad

	# Move group to root joint
	# Point contsrain group to root joint.
	#      offset off (snapping)
	temp = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(temp)

	# Freeze transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint, pad)

	# create a local oriented control for each joint
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind



	# Create control (circle)
	control_icon_1 = pm.circle(name='lt_middle_01_icon',normal=[1,0,0])[0]


	# Create group (Not EMPTY)
	local_1=pm.group(name='lt_middle_01_local')
	# This will automaticly parent the control under
	# The group


	# Move group to the target joint.
	temp=pm.parentConstraint(root_joint,local_1)
	# Use a parent constraint driver is the joint.
	#    Where driven is the group.
	#    Offset is off (snapping)


	# Destroy the constraint
	pm.delete(temp)

	# Delete History on control
	pm.delete(control_icon_1,ch=True)
	# Orient Constraint driver: control driver: joint.
	pm.orientConstraint(control_icon_1,root_joint)



	control_icon_2 = pm.circle(name='lt_middle_02_icon',normal=[1,0,0])[0]
	local_2=pm.group(name='lt_middle_02_local')
	temp=pm.parentConstraint(second_joint,local_2)
	pm.delete(temp)
	pm.delete(control_icon_2,ch=True)
	pm.orientConstraint(control_icon_2,second_joint)
	pm.parent(local_2,control_icon_1)




	control_icon_3 = pm.circle(name='lt_middle_03_icon',normal=[1,0,0])[0]
	local_3=pm.group(name='lt_middle_03_local')
	temp=pm.parentConstraint(third_joint,local_3)
	pm.delete(temp)
	pm.delete(control_icon_3,ch=True)
	pm.orientConstraint(control_icon_3,third_joint)
	pm.parent(local_3,control_icon_2)


def padding():
	'''

	import Smith_Andre_1405_RiggingTools
	reload(Smith_Andre_1405_RiggingTools)
	Smith_Andre_1405_RiggingTools.padding()

	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create a empty group
	#
	pad = pm.group(empty=True)

	# Move group to joint.
	#   and delete constraint
	temp_contraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_contraint)
	
	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

    # Parent joint to group
	pm.parent(root_joint, pad)

    # renaming
    # ct_tail_01_bind
    # ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)









	print 'pad group created.'

def priming():
	'''


	import Smith_Andre_1405_RiggingTools
	reload(Smith_Andre_1405_RiggingTools)
	Smith_Andre_1405_RiggingTools.priming()
	'''
	
	# Get Selected.
	selected = pm.ls(selection=True)
	# print 'Joints Selected:', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('bind', 'icon')
		local_pad_name = target_joint.replace('bind', '_local')

		# Create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Group control (NOT an empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad
		
		# Move group to target joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control.
		pm.orientConstraint(control_icon, target_joint)





	print 'local oriented Control Created.'
	print 'chapter 3 - the end'



	# Create a control

	

	# Move and orient control.
	# Use a parent constraint to move control to joint.

    # Constraint is no longer needed
	# Delete it.

	
	print 'Control Created.'

def fk_back():
	
    joint_chain = pm.ls(selection=True, dag=True)
    print 'Joint Chain:', joint_chain

   
    for current_joint in joint_chain:
    	control_icon = pm.circle()[0]
    	print 'Control Icon Created:', control_icon
    	
    	# Snap control icon to the current_joint.
        benny = pm.parentConstraint(current_joint, control_icon)
    	# Delete Constraint 
    	pm.delete(benny)	
    
        # OrientConstrain the control to the joint
   




    print 'FK Back Created.'
# Create a function called joint_rename
# Select the root joint and loop through all joint in
#    the joint chain.
#'ori_name_count_suffix'
# 'ct_back_01_bind'

def joint_rename():
	'''
	# Create a function called joint_rename
	# Select the root joint and loop through all joint in
	#   the joint chain.
	# 'ori_name_count_suffix'
	# 'ct_back_01_bind'

	
	import Smith_Andre_1405_RiggingTools
	reload(Smith_Andre_1405_RiggingTools)
	Smith_Andre_1405_RiggingTools.joint_rename()
	'''
	# What am I working on?
	# Get all joints in a selected joint cahin.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items selected:', joint_chain

	 # Build our new name.
	 # 'lt'
	 # 'arm'
	 # 01
	 # 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count,suffix)
		print 'Joint Name:', new_name
 
		current_joint.rename(new_name)
         
 		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)
    
	print 'Joint Chain Renamed'
 



