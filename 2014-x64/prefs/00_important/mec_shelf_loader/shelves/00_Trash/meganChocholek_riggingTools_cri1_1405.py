'''
Megan Chocholek
meganChocholek_riggingTools_cri1_1405.py

Description: Tools and Requirements for Project 4 in CR1 - 1405.

How to Run:
import meganChocholek_riggingTools_cri1_1405
reload(meganChocholek_riggingTools_cri1_1405)
'''
print 'meganChocholek_riggingTools_cri1_1405 is now open.'

import pymel.core as pm 


def Unlock_Show_trsv():
	'''
	The hidden translate, rotate, scale, and visible values 
		of the selected object will be unlocked and no longer hidden.

	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Unlock_Show_trsv()
	'''

	print 'Unlocking initiated.'

	# Get Selected
	selected = pm.ls(selection=True)

	for icon in selected:
		# Unlock and show translate X
		icon.tx.set(lock=False,keyable=True)

		# Unlock and show translate Y
		icon.ty.set(lock=False,keyable=True)

		# Unlock and show translate Z
		icon.tz.set(lock=False,keyable=True)

		# Unlock and show rotate X
		icon.rx.set(lock=False,keyable=True)

		# Unlock and show rotate Y
		icon.ry.set(lock=False,keyable=True)

		# Unlock and show rotate Z
		icon.rz.set(lock=False,keyable=True)

		# Unlock and show scale X
		icon.sx.set(lock=False,keyable=True)

		# Unlock and show scale Y
		icon.sy.set(lock=False,keyable=True)

		# Unlock and show scale Z
		icon.sz.set(lock=False,keyable=True)

		# Unlock and show visibility
		icon.v.set(lock=False,keyable=True)

	print 'Translates, rotates, scales, and visibility have been unlocked and are now visible.'
	print 'Code Completed.'

def Lock_Hide_rsv():
	'''
	The rotate, scale, and visible values of selected object will
		be hidden from the channel box.

	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Lock_Hide_rsv()
	'''

	print'Lock and Hide (rsv) initiated.'

	# Get Selected
	selected = pm.ls(selection=True)

	for icon in selected:
		# Lock and hide rotate X
		icon.rx.set(lock=True,keyable=False)

		# Lock and hide rotate Y
		icon.ry.set(lock=True,keyable=False)

		# Lock and hide rotate Z
		icon.rz.set(lock=True,keyable=False)

		# Lock and hide scale X
		icon.sx.set(lock=True,keyable=False)

		# Lock and hide scale Y
		icon.sy.set(lock=True,keyable=False)

		# Lock and hide scale Z
		icon.sz.set(lock=True,keyable=False)

		# Lock and hide visibility
		icon.v.set(lock=True,keyable=False)

	print 'Rotates, scales, and visibility have been locked and hidden.'
	print 'Code Completed.'

def Lock_Hide_tsv():
	'''
	The translate, scale, and visible values of an object 
	 will be hidden from the channel box.

	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Lock_Hide_tsv()
	'''
	print'Lock and Hide (tsv) initiated.'

	#Get Selected
	selected = pm.ls(selection=True)

	for icon in selected:
		# Lock and hide translate X
		icon.tx.set(lock=True,keyable=False)

		# Lock and hide translate Y
		icon.ty.set(lock=True,keyable=False)

		# Lock and hide translate Z
		icon.tz.set(lock=True,keyable=False)

		# Lock and hide scale X
		icon.sx.set(lock=True,keyable=False)

		# Lock and hide scale Y
		icon.sy.set(lock=True,keyable=False)

		# Lock and hide scale Z
		icon.sz.set(lock=True,keyable=False)

		# Lock and hide visibility
		icon.v.set(lock=True,keyable=False)

	print 'Translates, scales, and visibility have been locked and hidden.'
	print 'Code Complete.'	

def Priming():
	'''
	The user selects the root joint, then the tool will create a local
		oriented control for the joints in the selected chain.

	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Priming()
	'''
	print 'Priming Initiated.'

	# Get seleted
	selected = pm.ls(selection=True)

	for current_joint in selected:
		control_icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control 
		control_icon = pm.circle(normal=[1, 0, 0], radius=1, name=control_icon_name)[0]
		print 'Control Icon:', control_icon

		# Create a group that is not empty 
		local_pad = pm.group(name=local_pad_name)
		print 'Pad Created:', local_pad

		# Parent constraint group to joint
		zombie = pm.parentConstraint(current_joint, local_pad)
		print 'Constraint created. Careful! Its a hunter!'

		# Kill the constraint
		pm.delete(zombie)
		print 'BOOM! HEADSHOT!'
		print 'Constraint terminated.'

		# Orient constraint control to joint
		pm.orientConstraint(control_icon, current_joint)
		print 'Controls oriented.'

	print 'Priming Successful.'
	print 'Code Complete.'

def Joint_Rename():
	'''
	# Select the root joint and loop through all joint in the joint chain.
	# 'ori_name_count_suffix'
	# 'ct_back_01_bind'
	
	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Joint_Rename()
	'''
	print 'Joint Rename Initiated'


	# Get all joints in a selected joint chain
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items Selected:', joint_chain

	# Build a new name
	# 'lt'
	# 'arm'
	# 01
	#'bind'

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
	current_joint.rename(new_name)


	print 'Joint Chain Renamed.'

def Padding():
	'''
	The user selects the root joint, then the tool will pad 
		the joints in the chain.

	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Padding()
	'''

	#Get Selected
		# Get selected
	selected = pm.ls(selection=True)
	root_joint = selected[0]

	# Create the pad group
	pad = pm.group(empty=True)

	# Create a point constraint
	carol_ann = pm.pointConstraint(root_joint, pad)
	print 'Constraint created.'
	print 'Dont go near the light, Carol Ann!'

	# Destroy the constraint
	pm.delete(carol_ann)
	print 'Carol Ann entered the light. Constraint deleted.'

	# Freeze transformations
	pm.makeIdentity(pad, a=True, t=1, s=1, r=1, n=0)

	# Put joint into pad group
	pm.parent(root_joint, pad)

	# Rename pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Joints Successfully Padded.'
	print 'Code Complete.'

def Hierarchy():
	'''
	The user selects the root joint and the tool will generate a hierarchy 
		for the selected joint chain.

	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Hierarchy()
	'''

	print 'Hierarchy Generated.'

	import pymel.core as pm 


	#The user will select the root joint and the tool will apply the systems.
	selected = pm.ls(selection=True, dag=True)
	root_joint = selected[0]
	second_joint = selected[1]	
	third_joint = selected[2]


	'''
	Pad the root joint.
	'''

	#Rename
	root_pad_name = root_joint.replace('01_bind', '00_pad')

	#Create empty group.
	root_pad = pm.group(empty=True)
	root_pad.rename(root_pad_name)
	#print 'Root Pad Created:', root_pad


	#Move Group to root joint.
	#Point Constraint to root joint (driver, driven)
	#	offset off (Snapping)
	kenny = pm.parentConstraint(root_joint, root_pad)
	print 'Parent constraint Kenny created.'


	#Delete Constraints
	pm.delete(kenny)
	print 'You killed Kenny! You bastard! Whatever. Constraints deleted.'


	#Freeze transforms.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	print 'Transforms frozen. Apparently they cant let it go.'


	#Parent root joint to the group
	pm.parent(root_joint, root_pad)
	print 'Successfully parented, unlike Bruce Wayne.'


	'''
	Create a local orient control for each joint.
	lt_middle_01_bind, lt_middle_02_bind, lt middle_03_bind
	'''



	#Create control (circle)

	#Rename
	control1_name = root_joint.replace('*_bind', '*_icon')
	control1_pad_name = root_joint.replace('*_bind', '*_pad')


	control_icon_1 = pm.circle(normal=[0, 0, 1])[0]
	control_icon_1.rename(control1_name)
	control1_pad = pm.group(empty=False)
	control1_pad.rename(control1_pad_name)
	print 'Control 1 with pad created.'

	carl = pm.parentConstraint(root_pad, control_icon_1)
	print 'Parent constraint Carl created.'

	pm.delete(carl)

	print 'Carl deleted. Nobody liked him anyways.'
	pm.makeIdentity(control_icon_1, apply=True, t=1, r=1, s=1, n=0)
	pm.delete(control_icon_1, ch=True)
	print 'Transforms frozen. History deleted.'

	pm.orientConstraint(control_icon_1, root_pad)
	print 'Successfully oriented.'


	#Create group (NOT EMPTY)
	#	This will automatically parent the control under the group
	pm.group(empty=False, name='lt_middle_01_local')
	print 'Group created.'


	#Move group to the target joint.
	#Use a parent constraint. Driver is the joint. 
	#	Driven is the group. Offset is off (Snapping)
	#Kill the constraint
	#delete history on control
	#Orient Constraint. Driver is Control. Driven is the Joint
	# LOL Pass the joint, dude


	'''
	Second Joint
	'''

	#Rename
	control2_name = second_joint.replace('*_bind', '*_icon')
	control2_pad_name = second_joint.replace('*_bind', '*_pad')

	control_icon_2 = pm.circle(normal=[1, 0, 0])[0]
	control_icon_2.rename(control2_name)

	control2_pad = pm.group(empty=False)
	control2_pad.rename(control2_pad_name)
	print 'Control 2 and pad created.'

	skynet = pm.parentConstraint(second_joint, control2_pad)
	print 'Parent constraint Skynet created. Oh shit.'

	pm.delete(skynet)
	print 'Skynet deleted. Phew, that was a close one!'


	pm.makeIdentity(control_icon_2, apply=True, t=1, r=1, s=1, n=0)
	pm.delete(control_icon_2, ch=True)
	print 'Transforms frozen. History deleted.'

	pm.orientConstraint(control_icon_2, second_joint)
	print 'Successfully oriented.'



	'''
	Third Joint
	'''

	#Rename
	control3_name = third_joint.replace('*_bind', '*_icon')
	control3_pad_name = third_joint.replace('*_bind', '*_pad')
	control_icon_3 = pm.circle(normal=[1, 0, 0])[0]
	control_icon_3.rename(control3_name)

	control3_pad = pm.group(empty=False)
	control3_pad.rename(control3_pad_name)
	print 'Control 3 and pad created.'

	jack = pm.parentConstraint(third_joint, control3_pad)
	print 'Parent constraint Jack created.'

	pm.delete(jack)

	print 'Jack deleted. Spoiler Alert: Rose lets go.'
	pm.makeIdentity(control_icon_3, apply=True, t=1, r=1, s=1, n=0)
	pm.delete(control_icon_3, ch=True)
	print 'Transforms frozen. History deleted.'

	pm.orientConstraint(control_icon_3, third_joint)
	print 'Successfully oriented.'


	'''
	Parenting
	'''

	pm.parent(control2_pad, control_icon_1)
	pm.parent(control3_pad, control_icon_2)

	print 'Controls 2 and 3 parented.'

	#Rename
	middle_grp_name = root_joint.replace('*_bind', '*_grp')

	middle_grp = pm.group(empty=True)
	middle_grp.rename(middle_grp_name)

	pm.parent(root_pad, control1_pad, middle_grp)

	print 'Control hierarchy created.'

def Create_Attribute():
	'''
	The user selects a finger chain and the tool will create attributes for 
		the selected fingers.

	import meganChocholek_riggingTools_cri1_1405
	meganChocholek_riggingTools.Create_Attribute()
	'''
	import pymel.core as pm

	print 'Attributes initiated.'
	
	# Get selected
	selected = pm.ls(selection=True)
	print 'Current selected:', selected

	first_selected = selected[0]

	# Create a locked attribute to act as a header for the fingers
	first_selected.addAttr('FINGERS', at='enum', en='----------', keyable=True)
	first_selected.FINGERS.set(lock=True)

	# Create a locked attribute to act as a header for the curl
	first_selected.addAttr('CURL', at='enum', en='----------', keyable=True)
	first_selected.CURL.set(lock=True)

	# Create attribute for the finger curls 
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	# Create a locked attribute to act as a header for the spread
	first_selected.addAttr('SPREAD', at='enum', en='----------', keyable=True)
	first_selected.SPREAD.set(lock=True)

	# Create attribute for the finger spreads
	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	# Create a locked attribute to act as a header for the thumb
	first_selected.addAttr('THUMB', at='enum', en='----------', keyable=True)
	first_selected.THUMB.set(lock=True)

	# Create attribute for thumb spread
	first_selected.addAttr('thumb_spread', keyable=True)

	# Create attribute for thumb drop
	first_selected.addAttr('thumb_drop', keyable=True)

	print 'Attributes Successfully Created.'
	print 'Code Complete.'
