'''
Dion Adams
AdamsDion_riggingTools_1408.py

Description:
	Grouping of rigging tools.

How to Run:

import pymel.core as pm

import adamsDion_riggingTools_cri1_1408 
reload(adamsDion_riggingTools_cri1_1408)

	'''


print 'Rigging Tools Active'

import pymel.core as pm

def lock_and_hide_trans():
	'''
	locks and hide tranformations

	Select joints and geometry and execute this function 

	import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.lock_and_hide_trans()

    ''' 

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)

	print 'Channels locked and hidden'

def lock_and_hide_rotates():
	'''
	locks and hide rotations

	Select joints and geometry and execute this function 

	import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.lock_and_hide_rotates()

    ''' 

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)
	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)
	control_icon.v.set(lock=True, keyable=False)

	print 'Channels locked and hidden'

def unlock_and_show_trans():
	'''
	Unlocks and Show tranformations

	Select joints and geometry with hidden transforms and execute this function 

	import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.unlock_and_show_trans()

    ''' 

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon

	control_icon.tx.set(lock=False, keyable=True)
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)

	print 'Channels locked and hidden'

def unlock_and_show_rotates():
	'''
	Unlocks and Show tranformations

	Select joints and geometry with hidden rotates and execute this function 

	import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.unlock_and_show_rotates()

    ''' 

	# get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Control', control_icon




	control_icon.rx.set(lock=False, keyable=True)
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)

	print 'Channels locked and hidden'

def priming_tool():
	'''
	import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.priming_tool()

    '''


	# Get selected joints.
	selected_joints = pm.ls(selection=True, dag=True)
	
	for current_joint in selected_joints:
		control_icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		print'Current Control:', current_joint
		

		# Create a control icon.
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		# Create a group (parenting the control under the group)
		local_pad = pm.group(name=local_pad_name)



		print'pad created:', local_pad

		# Move the group to the target joint
		temp_constraint = pm.parentConstraint(current_joint, local_pad)
		pm.delete(temp_constraint)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)

def hierarchy():
    '''

    import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.hierarchy()

    Create a hierarchy based upon a given system.

    Select root joint chain and execute funtion.

    '''

    '''
    Input
    What are we working on?
    The root joint.
    ''' 
    joint_system = pm.ls(selection=True, dag=True)
    # print 'Joint System:', joint_system

    root_joint = joint_system[0]
    joint_2 = joint_system[1]
    joint_3 = joint_system[2]

    '''
    Padding Root Joint
    '''
    # Create empty group
    root_pad = pm.group(empty=True)

    # Move group over to the target joint.
    temp_constraint = pm.pointConstraint(root_joint, root_pad)
    pm.delete(temp_constraint)

    # Freeze Transforms on group 
    pm.makeIdentity(root_pad, apply=True, t=1, s=1, n=0)

    # Parent root joint to the group.
    pm.parent(root_joint, root_pad)


    '''
    Local Controls
    '''
    '''
    Control 1 - root_joint
    '''
    # Create a control.
    # normal=[1,0,0], radius=2
    control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

    # Create a group.
    # Grouping control during the process.
    local_pad_1 = pm.group()

    # Output control and pad.
    print 'Control 1 Created:', control_icon_1
    print 'Local Pad 1 Created:', local_pad_1

    # Move group over to the target joint.
    # Delete constrain after snapping. 
    # Driver: joint 
    # Driven: group
    temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
    pm.delete(temp_constraint)

    # Orient Consttain the joint to the control.
    # Driver -> Driven.
    # Control -> Joint
    pm.orientConstraint(control_icon_1, root_joint)

  

    '''
    Control 2
    '''
     # Create a control.
    # normal=[1,0,0], radius=2
    control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

    # Create a group.
    # Grouping control during the process.
    local_pad_2 = pm.group()

    # Output control and pad.
    print 'Control 2 Created:', control_icon_2
    print 'Local Pad 2 Created:', local_pad_2

    # Move group over to the target joint.
    # Delete constrain after snapping. 
    # Driver: joint 
    # Driven: group
    temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
    pm.delete(temp_constraint)

    # Orient Consttain the joint to the control.
    # Driver -> Driven.
    # Control -> Joint
    pm.orientConstraint(control_icon_2, joint_2)

    '''
    Control 3
    '''
     # Create a control.
    # normal=[1,0,0], radius=2
    control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

    # Create a group.
    # Grouping control during the process.
    local_pad_3 = pm.group()

    # Output control and pad.
    print 'Control 3 Created:', control_icon_3
    print 'Local Pad 3 Created:', local_pad_3

    # Move group over to the target joint.
    # Delete constrain after snapping. 
    # Driver: joint 
    # Driven: group
    temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
    pm.delete(temp_constraint)

    # Orient Consttain the joint to the control.
    # Driver -> Driven.
    # Control -> Joint
    pm.orientConstraint(control_icon_3, joint_3)

    '''
    Parent control together.
    '''

    # Pad 3 (last) -> control 2
    pm.parent(local_pad_3, control_icon_2)
    pm.parent(local_pad_2, control_icon_1)



    print 'hierarchy Created.'

def padding_tool():
	'''
	import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.padding_tool()

    Create pads for joint chain

    Select the root_joint in a joint chain and exectute this function.

	'''

	selected = pm.ls(selection=True)
	#print 'Current selected:', selected 
	root_joint = selected[0]

	# Create empty group.
	# empty=True will create a empty group.
	#
	pad = pm.group(empty=True)

	# Move group to joint.
	#    and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze transforms onthe group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming 
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created'

def joint_renamer():
	'''
	import adamsDion_riggingTools_cri1_1408 
    adamsDion_riggingTools_cri1_1408.joint_renamer()

    Renames joints

    Select joints and execute this function.

	'''
	'''


	Get selected.

	pm.ls(selection=True)

	'''

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected items;', joint_chain
	'''
	Figure out naming convention.
	'lt_arm_01_bind' -> 'lt arm_04_waste'
	''' 

	ori = raw_input()
	system_name = raw_input()
	count = 1
	suffix = 'bind'

	

	'''
	loop through joint_chain.
	'''
	for current_joint in joint_chain:
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name

		# Rename joint
		current_joint.rename(new_name)
		count = count + 1

	new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_name)




