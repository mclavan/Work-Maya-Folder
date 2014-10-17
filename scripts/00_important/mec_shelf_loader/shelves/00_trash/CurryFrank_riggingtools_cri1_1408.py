'''
Frank Cury
CurryFrank_riggingtools_cri1_1408.py

Descriptin:
        This contains a series of rigging tools.

How to Run:

import CurryFrank_riggingtools_cri1_1408
reload(CurryFrank_riggingtools_cri1_1408)

'''

import pymel.core as pm

print 'Rigging tools active'

def joint_renamer():
	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.joint_renamer()

	'''

	'''
	Tool name: 'jNam'

	Rename a selected joint chain.
		Naming convention
			lt_arm_01_bind
			lt_arm_03_end

	The user will select the root joint and then execute.

	'''

	# Input Area
	# Get selected root joint.
	joint_system = pm.ls(selection=1, dag=1)

	# orientation_systemName_count_suffix
	# lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'


	# Loop through joint chain.
	for current_joint in joint_system:

		# Assembling new name
		new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)

		# Rename joint
		current_joint.rename(new_name)

		print 'Renaming: ', current_joint, 'New Name: ', new_name
		
		# Pushing the cout forward.
		count = count + 1

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count - 1, 'end')
	print 'Renaming: ', current_joint, 'New Name: ', new_name
	current_joint.rename(new_name)

	print 'Selected joints have been named'

def lock_and_hide_trans():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.lock_and_hide_trans()

	'''

	#Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]

	control_icon.tx.set(lock=1, keyable=0)
	control_icon.ty.set(lock=1, keyable=0)
	control_icon.tz.set(lock=1, keyable=0)
	control_icon.sx.set(lock=1, keyable=0)
	control_icon.sy.set(lock=1, keyable=0)
	control_icon.sz.set(lock=1, keyable=0)
	control_icon.v.set(lock=1, keyable=0)

	print 'Selected Control', control_icon

def lock_and_hide_rotate():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.lock_and_hide_rotate()

	'''

	#Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]

	control_icon.rx.set(lock=1, keyable=0)
	control_icon.ry.set(lock=1, keyable=0)
	control_icon.rz.set(lock=1, keyable=0)
	control_icon.sx.set(lock=1, keyable=0)
	control_icon.sy.set(lock=1, keyable=0)
	control_icon.sz.set(lock=1, keyable=0)
	control_icon.v.set(lock=1, keyable=0)

	print 'Selected Control', control_icon

def unlock_and_show_tool():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.unlock_and_show_tool()

	'''

	#Get selected
	selected_controls = pm.ls(selection=True)
	control_icon = selected_controls[0]

	control_icon.tx.set(lock=0, keyable=1)
	control_icon.ty.set(lock=0, keyable=1)
	control_icon.tz.set(lock=0, keyable=1)
	control_icon.rx.set(lock=0, keyable=1)
	control_icon.ry.set(lock=0, keyable=1)
	control_icon.rz.set(lock=0, keyable=1)
	control_icon.sx.set(lock=0, keyable=1)
	control_icon.sy.set(lock=0, keyable=1)
	control_icon.sz.set(lock=0, keyable=1)
	control_icon.v.set(lock=0, keyable=1)

	print 'Selected Control', control_icon

def priming_tool():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.priming_tool()
	
	'''

	'''
	Creates ik handles on a joint chain.
	Tool Name: Hndl

	'''

	# Get selected joints
	selected_joints = pm.ls(selection=1, dag=1)
	selected_joints.pop(-1)

	for current_joint in selected_joints:
		print 'Current Control:', current_joint

		# Icon and pad name.
		icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_pad')

		# Create a control icon
		control_icon = pm.circle(name=icon_name, normal=[1, 0, 0], radius=1.8)[0]

		# Create a group (parenting the control under the group)
		local_pad = pm.group(control_icon, name=local_pad_name)

		# Move the group to the target joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control to group
		pm.orientConstraint(control_icon, current_joint)

def pad_tool():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.pad_tool()

	'''

	'''
	For pad tool, the user will select the root joint.
	Tool Name: jPad

	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:', selected
	root_joint = selected[0]

	# Create empty group
	# empty=True will create a empty group
	
	local_pad_name = root_joint.replace('_bind', '_pad')

	pad = pm.group(empty=True, name=local_pad_name)

	# Move group to joint.
	#	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent joint to group
	pm.parent(root_joint, pad)

def colorBlue_tool():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.colorBlue_tool()

	'''

	selected = pm.ls(selection=1)
	first_selected = selected[0]
	print 'Selected Object:', first_selected

	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)

def colorRed_tool():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.colorRed_tool()

	'''
	
	selected = pm.ls(selection=1)
	first_selected = selected[0]
	print 'Selected Object:', first_selected

	first_selected.overrideEnabled.set(1)
	red = 13
	first_selected.overrideColor.set(red)

def colorYellow_tool():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.colorYellow_tool()

	'''
	
	selected = pm.ls(selection=1)
	first_selected = selected[0]
	print 'Selected Object:', first_selected

	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(yellow)

def attributes_tool():

	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.attributes_tool()

	'''

	# Create a group of attributes at one time.  
	# The finger attributes are an example.

	selected = pm.ls(selection=1)
	first_selected = selected[0]
	print 'Selected Object:', first_selected

	first_selected.addAttr('FINGERS', keyable=True, at='enum', en='----------------')
	first_selected.FINGERS.set(lock=True)

	first_selected.addAttr('CURL', keyable=True, at='enum', en='----------------')
	first_selected.CURL.set(lock=True)
	first_selected.addAttr('index_curl', keyable=True, min=-10, max=10)
	first_selected.addAttr('middle_curl', keyable=True, min=-10, max=10)
	first_selected.addAttr('pinky_curl', keyable=True, min=-10, max=10)

	first_selected.addAttr('SPREAD', keyable=True, at='enum', en='----------------')
	first_selected.SPREAD.set(lock=True)
	first_selected.addAttr('index_spread', keyable=True, min=-10, max=10)
	first_selected.addAttr('middle_spread', keyable=True, min=-10, max=10)
	first_selected.addAttr('pinky_spread', keyable=True, min=-10, max=10)

	first_selected.addAttr('THUMB', keyable=True, en='------------------')
	first_selected.THUMB.set(lock=True)
	first_selected.addAttr('thumb_curl', keyable=True, min=-10, max=10)
	first_selected.addAttr('thumb_drop', keyable=True, min=-10, max=10)

def seperator_attribute():
	
	'''
	How to run:

	import CurryFrank_riggingtools_cri1_1408
	reload(CurryFrank_riggingtools_cri1_1408)
	CurryFrank_riggingtools_cri1_1408.seperator_attribute()

	'''
	
	# raw_input will be the name of seperator, put name in caps

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', en="----------------", keyable=1)

	lockAtt = first_selected.attr(attribute_name)
	lockAtt.set(lock=1)




