'''
Dianelys Ramos
Ramos_Dianelys_riggingTools_Cri1-1408

Description:
	Contains several rigging tools used in the project.


How to Run:

import Ramos_Dianelys_riggingTools_Cri1_1408
reload(Ramos_Dianelys_riggingTools_Cri1_1408)


'''

print 'Rigging Tools Active'

import pymel.core as pymel

def lock_and_hide ():

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls: ', control_icon


	print 'Channels locked and hide'

def lock_and_hide_trans():

	# Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls: ', controls_icon

	control_icon.tx.set(lock=True, keyable=False)
	controls_icon.ty.set(Lock=True, keyabde=False)
	controls_icon.tz.set(Lock=True, keyable=False)
	controls_icon.sx.set(Lock=True, keyable=False)
	controls_icon.sy.set(Lock=True, keyable=False)
	controls_icon.sz.set(Lock=True, keyable=False)
	controls_icon.v.set(Lock=True, keyable=False)
	print 'Channels locked and hide'

def lock_and_hide_rotate():

	# Get selected
	selected_controls = pm.ls(selection=True)
	controls_icon = selected_controls[0]
	print 'Select Controls: ', controls_icon
	control_icon.tx.set(lock=False, keyable=True) 
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.rx.set(lock=False, keyable=True) 
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)
	print 'Chaneels locked and hide'

def unlock_and_show():

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]
	print 'Selected Controls: ', control_icon
	control_icon.tx.set(lock=False, keyable=True) 
	control_icon.ty.set(lock=False, keyable=True)
	control_icon.tz.set(lock=False, keyable=True)
	control_icon.rx.set(lock=False, keyable=True) 
	control_icon.ry.set(lock=False, keyable=True)
	control_icon.rz.set(lock=False, keyable=True)
	control_icon.sx.set(lock=False, keyable=True)
	control_icon.sy.set(lock=False, keyable=True)
	control_icon.sz.set(lock=False, keyable=True)
	control_icon.v.set(lock=False, keyable=True)
	print 'Channels locked and hide'

def priming_tool():

# Get selected.
	selected_controls = pm.ls(selection=True)

	for current_control in selected_controls:
		print 'Current Joint:', current_control
		# Icon and pad name
		new_icon_name = current_joint.replace('-bind', '_icon')
		local_pad_name = current_joint.replace('-bind', '_local')
		# Create a control icon
		control_icon = pm.circle(normal=[1, 0, 0], radius= 1.8)[0]

		# Create a group (parenting the control under the group)
		local_pad = pm.group(control_icon)
	
		# Move the group to the target joint 
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)


def joint_remnamer():
	'''
	Rename a selected joint chain
		naming convention:
			lt_arm_01_bind
			lt_arm_03_bind

	The user will select the root joint and then execute the tool.
	How to Run:

	import Ramos_Dianelys_riggingTools_Cri1_1408
	Ramos_Dianelys_riggingTools_Cri1_1408.joint_renamer()

	'''

	# input Area!!!
	# Get selected root joint
	joint_system = pm.ls(selected=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'bind'

	# Loop through joint chain
	for current_joint in joint_system: 
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)


		print 'Renaing: ', current_control, 'New Name: ', new_name

		# Pushing the count forward.
		count = count + 1

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')
		print 'Renaing: ', current_joint, 'New Name: ', new_name
		current_joint.rename(new_name)




	print'Selected joints have been renamed.'




def padding_tool():
	''''

	import Ramos_Dianelys_Rigging_Tools
	reload Ramos_Dianelys_Rigging_Tools
	Ramos_Dianelys_Rigging_Tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	# pringt 'Current Selected:' ,selected
	root_joint = selected[0]

	# create empty group
	# empty=True will create an empty group
	#
	pad = pm.group(empty=True)

	# Move group to joint 
	# and delete constraint 
	temp_constraint = pm.pointConstraint(root_joingt, pad)
	pm.delete(temp_constraints)

	#freeze trainsforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# parent joint to group
	pm.parent(root_joint, pad)

	# renaming 
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding Group Created'


def hierarchy():

	'''
	import Ramos_Dianelys_Rigging_Tools
	reload(Ramos_Dianelys_Rigging_Tools)
	Ramos_Dianelys_Rigging_Tools.hierarchy()
	'''

	import pymel.core as pm

	print 'Starter Script'

	root_joint = 'lt_middle_01_bind'
	joint_2 = 'lt_middle_02_bind'
	joint_3 = 'lt_middle_03_bind'

	# create a group and name it 'lt_middle_00_pad'.
	pad = pm.group(empty=True, name='lt_middle_00_pad')

	print 'Root Joint', root_joint, 'and pad', pad

	# move the group to the root joint
	# a pointConstraint only translates
	# what is out driver: ?? and driven: ??
	kenny = pm.pointConstraint(root_joint, pad)
# Kenny misspelled it should be kenny
	pm.delete(kenny)

	# freeze transforms (We have not done this yet)
	pm.makeIdentity(apply=True, t=1, r=1, s=1, normal=0)

	# parent the root joint to the group
	# we are parenting the root joint to the pad
	# parent comman works children first then father last

# Syntax error in hierarchy 
# p,.parent(root_joint, pad)	
	pm.parent(root_joint, pad)

	print 'Pad Created:', pad, 'and move to', root_joint

	# what is next?
	# create a local oriented control for each finger joint

	# create a circle icon
	# rotation and size need to match the joint
	# do not forget to use the zero index [0]
	control_icon_1=pm.circle(radius=1.9, normal=[1,0,0],
		name='lt_middle_01_icon')[0]

	# create a group for the control (not empty)
	local_pad_1 = pm.group(name='lt_middle_01_local')

	# use parent constraint to moce local pad to joint
	dixy = pm.parentConstraint(root_joint, local_pad_1)

	# delete constraint
	pm.delete(dixy)

	# orient constraint the "control" to the finger
	pm.orientConstraint(control_icon_1, root_joint)


	# create a circle icon
	# rotation and size need to match the joint 
	# do not forget to use the zero idex [0]
	control_icon_2=pm.circle(radius=1.9, normal=[1,0,0],
		name='lt_middle_02_icon')[0]

	#create a group for the control (not empty)
	local_pad_2 = pm.group(name='lt_middle_02_local')

	# use parent constraint to move local pad to joint
	dixy = pm.parentConstraint(joint_2, local_pad_2)

	# delete constraint 
	pm.delete(dixy)

	# orient constraint the "control" to the finger
	pm.orientConstraint(control_icon_2, joint_2)

	# create a circle icon
	# rotation and size need to match the joint
	# do not forget to use the zero index [0]
	control_icon_3=pm.circle(radius=1.9, normal=[1,0,0],
		name='lt_middle_03_icon')[0]

	# create a group for the control (not empty)
	local_pad_3 = pm.group(name='lt_middle_03_local')

# Moved thrid control to the first joint instead of the third.
#	dixy = pm.parentConstraint(root_joint, local_pad_3)

	# use parent constraint to moce local pad to joint
	dixy = pm.parentConstraint(joint_3, local_pad_3)

	# delete constraint
# delete not delere
	pm.delete(dixy)

	# orient constraint the "control" to the finger
	pm.orientConstraint(control_icon_3, joint_3)


	'''
	parenting
	Children then parent 

	'''
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)
