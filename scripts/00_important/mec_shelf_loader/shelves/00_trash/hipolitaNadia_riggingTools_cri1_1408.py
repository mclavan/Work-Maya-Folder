'''

Nadia Hipolita

hipolitaNadia_riggingTools_cri1_1408.py

Description:
	This script contains a series of rigging tools.

	Tools:
	- Hiearchy 
	- Padding
	- Priming 
	- Joint Renamer 
	- Arm Control Renamer
	- Lock and Hide translations
	- Lock and Hide rotations
	- Unlock and Show 
	- Hand Attributes 3
	- Hand Attributes 4 
	- Separator Attribute 
	- Leg IK Builder 
	- Make it Blue 
	- Delete History 
	- Freeze Transformations
	- Center Pivots



How to run:

import hipolitaNadia_riggingTools_cri1_1408
reload(hipolitaNadia_riggingTools_cri1_1408)

'''
import pymel.core as pm

print 'Rigging Tools Active'

'''
Naming Conventions

Root Joints - 'ct_head_01_bind'
Root Pads - 'ct_head_00_pad'
Proxy Geo - 'ct_head_01_proxy'
Local Pad - 'ct_head_01_local'
Control Icon - 'ct_head_01_icon'

General - 'ori_bodLoc_count_suffix'
'''

def hierarchy():
	'''
	
	Creates a hierarchy of controls for the arm based on a given system.
	Select root joint chain.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.hierarchy()	

	'''
	# Input Area
	# Get Selected
	joint_system = pm.ls(selection=True, dag=True)
	print 'Joint System:', joint_system
	root_joint = joint_system [0]
	second_joint = joint_system [1]
	third_joint = joint_system [2]


	'''
	Padding the Root Joint
	'''

	# Create empty group
	root_pad = pm.group(empty=True)

	# Move group over to target joint.
	kenny = pm.pointConstraint(root_joint, root_pad)
	pm.delete(kenny)

	# Freeze Transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)


	# Parent root joint to the group
	pm.parent(root_joint, root_pad)

	'''
	Local Controls 

	'''
	# Create a control
	control_icon_1 = pm.circle(name = 'lt_middle_01_icon', normal=[1,0,0], radius=2)[0]

	# Group control
	local_pad_1 = pm.group(control_icon_1, name='lt_middle_01_local')

	# print 'Control', control_icon_1, 'Local Pad', local_pad_1
	print 'Control: {0} Local Pad: {1}'.format(control_icon_1, local_pad_1)

	# Delete History on the control icon.
	# Move control to target joint, use parent constraint and delete the constraint. 
	# driver = root_joint
	# driven = control_icon_1
	kenny = pm.parentConstraint(root_joint, local_pad_1) 
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon.
	# Driven is the target joint.  

	pm.orientConstraint(control_icon_1, root_joint)

	# Repeat Code to get other joints, make sure to change the names.
	# The Indy back can be created this way as well. 

	'''

	Control Icon 2

	'''

	# Control a control.
	# Change settings: normal x axis, radius is 2.
	control_icon_2 = pm.circle(name = 'lt_middle_02_icon', normal=[1,0,0], radius=2)[0]

	# Group control
	local_pad_2 = pm.group(control_icon_2, name='lt_middle_02_local')

	# print 'Control', control_icon_1, 'Local Pad', local_pad_1
	print 'Control: {0} Local Pad: {1}'.format(control_icon_2, local_pad_2)

	# Delete History on the control icon.
	# Move control to target joint, use parent constraint and delete the constraint. 
	# driver = root_joint
	# driven = control_icon_1
	kenny = pm.parentConstraint(second_joint, local_pad_2) 
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon.
	# Driven is the target joint.  

	pm.orientConstraint(control_icon_2, second_joint)

	'''
	Control Icon 3

	'''
	# Control a control.
	# Change settings: normal x axis, radius is 2.
	control_icon_3 = pm.circle(name = 'lt_middle_03_icon', normal=[1,0,0], radius=2)[0]

	# Group control
	local_pad_3 = pm.group(control_icon_3, name='lt_middle_03_local')

	# print 'Control', control_icon_1, 'Local Pad', local_pad_1
	print 'Control: {0} Local Pad: {1}'.format(control_icon_3, local_pad_3)

	# Delete History on the control icon.
	# Move control to target joint, use parent constraint and delete the constraint. 
	# driver = root_joint
	# driven = control_icon_1
	kenny = pm.parentConstraint(third_joint, local_pad_3) 
	pm.delete(kenny)

	# Use orient constraint.
	# Driver is the control icon.
	# Driven is the target joint.  

	pm.orientConstraint(control_icon_3, third_joint)

	'''
	Parenting

	'''

	# Last Step 
	# We need parent the controls to another as well.
	# Pad 3 to Control 2.  Pad 2 to Control 1.
	# Parent local pad to the control icon 1.
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)
	
	'''

	Lock and Hide

	'''
	# Control Icon 1
	# Translations
	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=True, keyable=False)
	control_icon_1.tz.set(lock=True, keyable=False)

	# Scale
	control_icon_1.sx.set(lock=True, keyable=False)
	control_icon_1.sy.set(lock=True, keyable=False)
	control_icon_1.sz.set(lock=True, keyable=False)

	# Visibility
	control_icon_1.v.set(lock=True, keyable=False)

	# Control Icon 2
	# Translations
	control_icon_2.tx.set(lock=True, keyable=False)
	control_icon_2.ty.set(lock=True, keyable=False)
	control_icon_2.tz.set(lock=True, keyable=False)

	# Scale
	control_icon_2.sx.set(lock=True, keyable=False)
	control_icon_2.sy.set(lock=True, keyable=False)
	control_icon_2.sz.set(lock=True, keyable=False)

	# Visibility
	control_icon_2.v.set(lock=True, keyable=False)

	# Control Icon 3
	# Translations
	control_icon_3.tx.set(lock=True, keyable=False)
	control_icon_3.ty.set(lock=True, keyable=False)
	control_icon_3.tz.set(lock=True, keyable=False)

	# Scale
	control_icon_3.sx.set(lock=True, keyable=False)
	control_icon_3.sy.set(lock=True, keyable=False)
	control_icon_3.sz.set(lock=True, keyable=False)

	# Visibility
	control_icon_3.v.set(lock=True, keyable=False)


	print 'Hierarchy Achieved. Nice.'

def padding_tool():

	'''
	Creates a group, snaps group to root joint, freezes transforms, parents joint to group and renames.
	Select Root Joint and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload (hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.padding_tool()

	'''

	# Get Selected 
	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create an empty group.
	pad = pm.group(empty=True)

	# Move group to joint and delete constraint
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	# Freeze Transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent
	pm.parent(root_joint, pad)

	# Rename
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding group created. Bam.'

def priming_tool():

	'''
	This tool creates a locally oriented control for each selected joint.

	Select a group of joints and then run the tool.

	How to run:

	import hipolitaNadia_riggingTools_cri1_1408
	hipolitaNadia_riggingTools_cri1_1408.priming_tool()

	'''

	# Get selected.
	selected_joints = pm.ls(selection=True)


	for current_joint in selected_joints:
		print 'Current Control:', current_joint

		# Icon and pad name. Changing names
		# new_icon_name = current_joint.replace('old', 'new')
		# print 'old', joint_name, 'new', control_name
		# icon_name = current_joint.replace('_bind', '_icon')
		# Do renaming LAST


		# Create a control icon with normal set to X
		control_icon = pm.circle(normal=[1,0,0], radius=1.8)[0]

		# Create a group (parenting the control under the group)
		local_pad = pm.group(control_icon)

		# Move the group to the target joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)

		# Rename joint
		# Could also use a name flag in the control and group
		control_icon_name = current_joint.replace('-bind', '_icon')
		print 'old', current_joint, 'new', control_icon_name
		local_pad_name = current_joint.replace('_bind', '_local')

		# Do NOT parent

	print 'Local Controls created and Primed. Bam.'

def joint_renamer():

	'''

	Renames a selected joint chain.
		Naming Convention:
			lt_arm_01_bind
			lt_arm_03_waste

	User selects the root joint and then execute the tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	hipolitaNadia_riggingTools_cri1_1408.joint_renamer

	'''

	# Input Area
	# Get selected root joint.
	joint_system = pm.ls(selection=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = 'lt'

	# Can use ori = raw_input() instead of 'lt' to change.  But don't overuse!

	name = 'arm'
	count = 1
	suffix = 'bind'

	#Loop through joint chain.
	for current_joint in joint_system:

		#Assembling a new name
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

		# Rename Joints
		current_joint.rename(new_name)

		print 'Renaming:', current_joint, 'New Name:', new_name

		# Pushing the count forward
		count = count + 1

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')

	print 'Renaming:', current_joint, 'New Name:', new_name 
	current_joint.rename(new_name)
	# You could also put joint_system[-1] to rename the last joint specifically


	print 'Selected joints have been renamed. Bam.'

def arm_control_renamer():

	'''

	Renames a selected group of controls.
		Naming Convention:
			lt_arm_01_icon


	User selects the starting controla and runs the tool.  User must input the orientation of the control.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload (hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.arm_control_renamer()

	'''

	# Input Area
	# Get selected root joint.
	control_group = pm.ls(selection=True, dag=True)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'icon'

	#Loop through joint chain.
	for current_control in control_group:

		#Assembling a new name
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

		# Rename Joints
		current_control.rename(new_name)

		print 'Renaming:', current_control, 'New Name:', new_name

		# Pushing the count forward
		count = count + 1

	print 'Selected controls have been renamed. Bam.'

def lock_hide_trans():
	'''
	This tool locks and hides the translations on a selected object.
	Select object and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.lock_hide_trans()

	''' 

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls [0]
	print 'Selected Control:', control_icon

	control_icon.tx.set(lock=True, keyable=False)
	control_icon.ty.set(lock=True, keyable=False)
	control_icon.tz.set(lock=True, keyable=False)

	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)

	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden. Bam.'

def lock_hide_rotate():
	'''

	This tool locks and hides the rotations on a selected object.
	Select object and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.lock_hide_rotate()  

	'''

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls [0]
	print 'Selected Control:', control_icon

	control_icon.rx.set(lock=True, keyable=False)
	control_icon.ry.set(lock=True, keyable=False)
	control_icon.rz.set(lock=True, keyable=False)

	control_icon.sx.set(lock=True, keyable=False)
	control_icon.sy.set(lock=True, keyable=False)
	control_icon.sz.set(lock=True, keyable=False)

	control_icon.v.set(lock=True, keyable=False)
	print 'Channels locked and hidden. Bam.'

def unlock_and_show():
	'''

	This tool unlocks and shows any channels that were locked and hidden.
	Select object and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.unlock_and_show()  


	'''

	# Get selected.
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls [0]
	print 'Selected Control:', control_icon

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
	print 'Channels unlocked and shown. Ba-bam.'

def hand_attribute_3():
	'''

	Creates the attributes for a hand with three fingers control icon.
	Select icon and run tool.

	How to run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload (hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.hand_attribute_3()

	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Create a enum attribute
	attribute_name='FINGERS'
	first_selected.addAttr(attribute_name, at='enum', en='---------------:', keyable=True)

	# Locking the Attribute
	attribute=first_selected.attr(attribute_name)
	attribute.set(lock=True)

	attribute_name_02 = 'CURL'
	first_selected.addAttr(attribute_name_02, at='enum', en='---------------:', keyable=True)
	attribute_02=first_selected.attr(attribute_name_02)
	attribute_02.set(lock=True)

	# Create float attribute
	attribute_name_03 = 'index_curl'
	first_selected.addAttr(attribute_name_03, keyable=True, min=-360, max=360)

	attribute_name_04 = 'middle_curl'
	first_selected.addAttr(attribute_name_04, keyable=True, min=-360, max=360)

	attribute_name_05 = 'pinkie_curl'
	first_selected.addAttr(attribute_name_05, keyable=True, min=-360, max=360)

	attribute_name_06 = 'SPREAD' 
	first_selected.addAttr(attribute_name_06, at='enum', en='---------------:', keyable=True)
	attribute_06=first_selected.attr(attribute_name_06)
	attribute_06.set(lock=True)

	attribute_name_07 = 'index_spread'
	first_selected.addAttr(attribute_name_07, keyable=True, min=-360, max=360)

	attribute_name_08 = 'middle_spread'
	first_selected.addAttr(attribute_name_08, keyable=True, min=-360, max=360)

	attribute_name_09 = 'pinkie_spread'
	first_selected.addAttr(attribute_name_09, keyable=True, min=-360, max=360)

	attribute_name_10 = 'THUMB'
	first_selected.addAttr(attribute_name_10, at='enum', en='---------------:', keyable=True)	
	attribute_10 = first_selected.attr(attribute_name_10)
	attribute_10.set(lock=True)

	attribute_name_11 = 'thumb_curl'
	first_selected.addAttr(attribute_name_11, keyable=True, min=-360, max=360)

	attribute_name_12 = 'thumb_spread'
	first_selected.addAttr(attribute_name_12, keyable=True, min=-360, max=360)

	attribute_name_13 = 'thumb_drop'
	first_selected.addAttr(attribute_name_13, keyable=True, min=-360, max=360)

	# Lock and Hide
	first_selected.tx.set(lock=True, keyable=False)
	first_selected.ty.set(lock=True, keyable=False)
	first_selected.tz.set(lock=True, keyable=False)

	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)

	first_selected.v.set(lock=True, keyable=False)

	print 'Attributes Created. Bam.'

def hand_attribute_4():
	'''

	Creates the attributes for a hand with four fingers control icon.
	Select icon and run tool.

	How to run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload (hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.hand_attribute_4()

	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Create a enum attribute
	attribute_name='FINGERS'
	first_selected.addAttr(attribute_name, at='enum', en='---------------:', keyable=True)

	# Locking the Attribute
	attribute=first_selected.attr(attribute_name)
	attribute.set(lock=True)

	attribute_name_02 = 'CURL'
	first_selected.addAttr(attribute_name_02, at='enum', en='---------------:', keyable=True)
	attribute_02=first_selected.attr(attribute_name_02)
	attribute_02.set(lock=True)

	# Create float attribute
	attribute_name_03 = 'index_curl'
	first_selected.addAttr(attribute_name_03, keyable=True, min=-360, max=360)

	attribute_name_04 = 'middle_curl'
	first_selected.addAttr(attribute_name_04, keyable=True, min=-360, max=360)

	attribute_name_05 = 'ring_curl'
	first_selected.addAttr(attribute_name_05, keyable=True, min=-360, max=360)

	attribute_name_06 = 'pinkie_curl'
	first_selected.addAttr(attribute_name_06, keyable=True, min=-360, max=360)

	attribute_name_07 = 'SPREAD' 
	first_selected.addAttr(attribute_name_07, at='enum', en='---------------:', keyable=True)
	attribute_07=first_selected.attr(attribute_name_07)
	attribute_07.set(lock=True)

	attribute_name_08 = 'index_spread'
	first_selected.addAttr(attribute_name_08, keyable=True, min=-360, max=360)

	attribute_name_09 = 'middle_spread'
	first_selected.addAttr(attribute_name_09, keyable=True, min=-360, max=360)

	attribute_name_10 = 'ring_spread'
	first_selected.addAttr(attribute_name_10, keyable=True, min=-360, max=360)

	attribute_name_11 = 'pinkie_spread'
	first_selected.addAttr(attribute_name_11, keyable=True, min=-360, max=360)

	attribute_name_12 = 'THUMB'
	first_selected.addAttr(attribute_name_12, at='enum', en='---------------:', keyable=True)	
	attribute_12= first_selected.attr(attribute_name_12)
	attribute_12.set(lock=True)

	attribute_name_13 = 'thumb_curl'
	first_selected.addAttr(attribute_name_13, keyable=True, min=-360, max=360)

	attribute_name_14 = 'thumb_spread'
	first_selected.addAttr(attribute_name_14, keyable=True, min=-360, max=360)

	attribute_name_15 = 'thumb_drop'
	first_selected.addAttr(attribute_name_15, keyable=True, min=-360, max=360)

	# Lock and Hide
	first_selected.tx.set(lock=True, keyable=False)
	first_selected.ty.set(lock=True, keyable=False)
	first_selected.tz.set(lock=True, keyable=False)

	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)

	first_selected.v.set(lock=True, keyable=False)

	print 'Attributes Created. Bam.'

def separator_attribute():
	'''

	Creates a separator between attributes.  
	Select control icon and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload (hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.separator_attribute()

	'''

	selected=pm.ls(selection=True)
	first_selected=selected[0]

	attribute_name=raw_input()
	first_selected.addAttr(attribute_name, at='enum', en='---------------:', keyable=True)

	print 'Attribute Created.'

def leg_ik_builder():
	
	'''

	This tool creates the IK system for the leg.  
	Select the joint chain in the leg and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	hipolitaNadia_riggingTools_cri1_1408.ik_system_builder()

	'''
	selected_joints = pm.ls(selection=True)
	print 'Selected Joints:', selected_joints

	# Get the root joint.
	root_joint = selected_joints[0]

	# Get the hierarchy
	leg_system = pm.ls(root_joint, dag=True)
	print 'Leg System:', leg_system

	ankle_joint = leg_system[2]
	ball_joint = leg_system[3]
	toe_joint = leg_system[4]

	# Creating the IK
	# Rotate-Plane IK
	leg_ik = pm.ikHandle(startJoint=root_joint, endEffector=ankle_joint, sol='ikRPsolver')[0]
	print 'Leg IK', leg_ik

	# Single-Chain IK
	ankle_ik = pm.ikHandle(startJoint=ankle_joint, endEffector=ball_joint)[0]
	print 'Ankle IK', ankle_ik
	ball_ik = pm.ikHandle(startJoint=ball_joint, endEffector=toe_joint)[0]
	print 'Ball IK', ball_ik

	print 'Leg System IKs Complete. Bam.'


# These tools created to get a python path for shelf buttons.

def make_it_blue():
	'''
	This is a tool for changing the color of any control to blue.
	Select control and run tool.
	I like blue.


	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.make_it_blue()  


	'''

	# Get Selected
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	# Accessing an object's attribute
	# Window, Attribute Spreadsheet, overrideColor (to see numbers for desired color)
	first_selected.overrideEnabled.set(1)
	blue=6
	first_selected.overrideColor.set(blue)

	print 'It is blue now.'

def delete_history():
	'''

	This tool deletes history on a selected object or muliple objects.
	Select object or objects and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.delete_history()  

	'''

	pm.delete(all=True, constructionHistory=True)

	print 'History Destroyed on all objects.  Bwa ha ha!'

def freeze_transform():
	'''

	This tool freezes transformations on a selected object.
	Select object and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.freeze_transform() 

	'''
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	print 'Transformations have been frozen.  Let it Go.'

def center_pivot():
	'''
	This tool centers pivots on a selected object or objects.
	Select object or objects and run tool.

	How to Run:

	import hipolitaNadia_riggingTools_cri1_1408
	reload(hipolitaNadia_riggingTools_cri1_1408)
	hipolitaNadia_riggingTools_cri1_1408.center_pivot() 

	'''

	pm.xform(centerPivots=True) 

	print 'Pivots have been centered. Bam.'


	




























	
		

		













	


