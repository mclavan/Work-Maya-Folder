'''
Michael Clavan
clavanMichael_riggingTools.py

Description:
	This script contains various rigging tools. 

	Tools Included
	- Snapping (Point, Orient, and Parent)
	- Hierarchy
		Creates a finger hierarchy. 
	- Padding
		Pads a root joint. 
	- Priming
		Creates a locally oriented control on selected joint. 
	- Joint Renaming
		Renames a selected joints. 
	- Lock and Hide Tools 
		- Lock & Hide Rotations
		- Lock & Hide Translation
		- Unlock and Show All 
	- Color Control Icons
		- Blue Controls on Selected. 
		- Red Controls on Selected. 
		- Yellow Controls on Selected. 
	- Create Float Attributes
	- Create Integer Attributes
	- Create Separator Attributes
	- Create Finger Attributes

How to Run:

import clavanMichael_riggingTools
reload(clavanMichael_riggingTools)

'''

print 'Rigging Toolset Activitive'

import pymel.core as pm 


def hierarchy():
	'''
	This tool will create a finger hierarchy based on a selected root joint. 
	
	How To Run:

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.hierarchy()

	'''

	print 'Hierarchy Created'

def padding_tool():
	'''
	This tool will create a world pad on the selected root joint. 
		The tool will also name the pad based upon the selected 
		joint and parent the selected root joint to the newly 
		created pad. 

	How To Run:

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.padding_tool()

	'''

	# Get selected root joint
	selected_joints = pm.ls(selection=True)
	root_joint = selected_joints[0]

	# Get the name of the group
	pad_name = root_joint.replace('01_bind', '00_pad')
	# Create Empty Group
	pad = pm.group(empty=True, name=pad_name)

	# Move group to the target root joint.
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	# Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent the root joint to the pad
	pm.parent(root_joint, pad)

	print 'Pad Created: {0} for root joint {1}.'.format(pad, root_joint)

	print 'Pad Created.'

def priming_tool():
	'''
	This tool creates a locally oriented control for each selected joint. 

	Selected a group of joints and then run the tool.

	How to Run:

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.priming_tool()
	'''

	# Get Selected joints
	selected_joints = pm.ls(selection=True)

	# Loop through all the selected joints.
	for current_joint in selected_joints:
		# Get the naming for the control and pad
		icon_name = current_joint.replace('_bind', '_icon')
		local_pad_name = current_joint.replace('_bind', '_local')

		# Create a control icon and position it down the x-axis.
		control_icon = pm.circle(name=icon_name, normal=[1, 0, 0], radius=1.8, ch=0)[0]
		# Create a empty group with the control parented.
		local_pad = pm.group(control_icon, name=local_pad_name)

		# Move pad to the target joint
		kenny = pm.parentConstraint(current_joint, local_pad)
		pm.delete(kenny)

		# Connect control back to the joint.
		pm.orientConstraint(control_icon, current_joint)

		print 'Local control created for {0}.  Control: {1} Pad {2}'.format(current_joint, control_icon, local_pad)
	print 'Locally oriented control created.'

renamer(pm.ls(selection=True,dag=True), 'rt', 'armIK', 1, 'IK')


def renamer(joint_chain, ori, name, count, suffix):
	'''
	This tool will rename all the joints from a selected root joint. 

	How to Run:

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.rename_joints()
	'''

	for current_joint in joint_chain:
		# Setup up new target name.
		new_name = '{0}_{1}_{2:02d}_{3}'. format(ori, name, count, suffix)

		# Renaming joint
		current_joint.rename(new_name)

		print 'Current Name: {0} - New Name: {1}'.format(current_joint, new_name)
		# Increment Counter
		count = count + 1


def rename_joints():
	'''
	This tool will rename all the joints from a selected root joint. 

	How to Run:

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.rename_joints()
	'''

	# Getting Selected Root joint.
	joint_chain = pm.ls(selection=True, dag=True)

	# Isolating the differnet parts of the naming convention.
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain[0:-1]:
		# Setup up new target name.
		new_name = '{0}_{1}_{2:02d}_{3}'. format(ori, name, count, suffix)

		# Renaming joint
		current_joint.rename(new_name)

		print 'Current Name: {0} - New Name: {1}'.format(current_joint, new_name)
		# Increment Counter
		count = count + 1

	# Naming the last joint in the joint chain 
	new_name = '{0}_{1}_{2:02d}_{3}'. format(ori, name, count, 'waste')
	joint_chain[-1].rename(new_name)
	print 'Current Name: {0} - New Name: {1}'.format(joint_chain[-1], new_name)

def point_snapping():
	'''
	This tool will translate the second (driven) to the first (driver) 
		selected object.
	
	How to Use:
	
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.point_snapping()

	'''

	selected = pm.ls(selection=True)
	driver = selected[0]
	driven = selected[1]

	kenny = pm.pointConstraint(driver, driven)
	pm.delete(kenny)

def orient_snapping():
	'''
	This tool will orient the second (driven) to the first (driver) 
		selected object.
	
	How to Use:
	
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.orient_snapping()

	'''

	selected = pm.ls(selection=True)
	driver = selected[0]
	driven = selected[1]

	kenny = pm.orientConstraint(driver, driven)
	pm.delete(kenny)	

def parent_snapping():
	'''
	This tool will translate and orient the second (driven) to 
		the first (driver) selected object.
	
	How to Use:
	
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.parent_snapping()

	'''

	selected = pm.ls(selection=True)
	driver = selected[0]
	driven = selected[1]

	kenny = pm.parentConstraint(driver, driven)
	pm.delete(kenny)	

def lock_and_hide_trans():
	'''
	Locks and hides translation, scale, and visibility channels. 

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.lock_and_hide_trans()
	'''
	# Get Selected
	selected_icons = pm.ls(selection=True)

	for current_icon in selected_icons:
		current_icon.tx.set(lock=True, keyable=False)
		current_icon.ty.set(lock=True, keyable=False)
		current_icon.tz.set(lock=True, keyable=False)

		current_icon.sx.set(lock=True, keyable=False)
		current_icon.sy.set(lock=True, keyable=False)
		current_icon.sz.set(lock=True, keyable=False)		
		current_icon.v.set(lock=True, keyable=False)		

	print 'Selected objects channels have been locked and hidden.'

def lock_and_hide_rotation():
	'''
	Locks and hides rotation, scale, and visibility channels. 

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.lock_and_hide_rotation()
	'''
	# Get Selected
	selected_icons = pm.ls(selection=True)

	for current_icon in selected_icons:
		current_icon.rx.set(lock=True, keyable=False)
		current_icon.ry.set(lock=True, keyable=False)
		current_icon.rz.set(lock=True, keyable=False)
		current_icon.sx.set(lock=True, keyable=False)
		current_icon.sy.set(lock=True, keyable=False)
		current_icon.sz.set(lock=True, keyable=False)		
		current_icon.v.set(lock=True, keyable=False)		

	print 'Selected objects channels have been locked and hidden.'

def lock_and_hide_scale():
	'''
	Locks and hides scale and visibility channels. 

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.lock_and_hide_scale()
	'''
	# Get Selected
	selected_icons = pm.ls(selection=True)

	for current_icon in selected_icons:
		current_icon.tx.set(lock=True, keyable=False)
		current_icon.ty.set(lock=True, keyable=False)
		current_icon.tz.set(lock=True, keyable=False)
		current_icon.rx.set(lock=True, keyable=False)
		current_icon.ry.set(lock=True, keyable=False)
		current_icon.rz.set(lock=True, keyable=False)
		current_icon.sx.set(lock=True, keyable=False)
		current_icon.sy.set(lock=True, keyable=False)
		current_icon.sz.set(lock=True, keyable=False)		
		current_icon.v.set(lock=True, keyable=False)		

	print 'Selected objects channels have been locked and hidden.'

def unlock_and_show_all():
	'''
	Reviels all channels for selected object. 

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.unlock_and_show_all()
	'''
	# Get Selected
	selected_icons = pm.ls(selection=True)

	for current_icon in selected_icons:
		current_icon.tx.set(lock=False, keyable=True)
		current_icon.ty.set(lock=False, keyable=True)
		current_icon.tz.set(lock=False, keyable=True)
		current_icon.rx.set(lock=False, keyable=True)
		current_icon.ry.set(lock=False, keyable=True)
		current_icon.rz.set(lock=False, keyable=True)
		current_icon.sx.set(lock=False, keyable=True)
		current_icon.sy.set(lock=False, keyable=True)
		current_icon.sz.set(lock=False, keyable=True)		
		current_icon.v.set(lock=False, keyable=True)		

	print 'Selected objects channels have been revieled.'


def color_icons_blue():
	'''
	Colors selected controls blue. 

	Select the controls and then execute the code.

	How to Run:
	
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.color_icons_yellow()

	'''
	# Get selected
	selected_icons = pm.ls(selection=True)

	for current_icon in selected_icons:
		current_icon.overrideEnabled.set(1)
		blue = 6
		current_icon.overrideColor.set(blue)

def color_icons_red():
	'''
	Colors selected controls red. 

	Select the controls and then execute the code.

	How to Run:
	
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.color_icons_yellow()
	'''
	# Get selected
	selected_icons = pm.ls(selection=True)

	for current_icon in selected_icons:
		current_icon.overrideEnabled.set(1)
		red = 13
		current_icon.overrideColor.set(red)

def color_icons_yellow():
	'''
	Colors selected controls yellow. 

	Select the controls and then execute the code.

	How to Run:

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.color_icons_yellow()
	'''
	# Get selected
	selected_icons = pm.ls(selection=True)

	for current_icon in selected_icons:
		current_icon.overrideEnabled.set(1)
		yellow = 17
		current_icon.overrideColor.set(yellow)


def create_float_attribute():
	'''
	Creates a quick float attributes.  
	The tool will prompt you for the name of the attribute. 

	How to Run:
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.create_float_attribute()
	'''

	# Get selected
	selected_control_icons = pm.ls(selection=True)
	control_icon = selected_control_icons[0]

	attribute_name = raw_input()
	control_icon.addAttr(attribute_name, keyable=True)

def create_integer_attribute():
	'''
	Creates a quick interget attributes.  
	The tool will prompt you for the name of the attribute. 

	How to Run:
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.create_float_attribute()
	'''

	# Get selected
	selected_control_icons = pm.ls(selection=True)
	control_icon = selected_control_icons[0]

	attribute_name = raw_input()
	control_icon.addAttr(attribute_name, attributeType='int', keyable=True)

def create_separator_attribute():
	'''
	Creates a quick separator attributes.  
	The tool will prompt you for the name of the attribute. 

	How to Run:
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.create_float_attribute()
	'''

	# Get selected
	selected_control_icons = pm.ls(selection=True)
	control_icon = selected_control_icons[0]

	attribute_name = raw_input()
	control_icon.addAttr(attribute_name, attributeType='enum', en='------------', keyable=True)
	attribute = control_icon.attr(attribute_name)
	attribute.set(lock=True)

def create_finger_attributes():
	'''
	Creates a series of attributes for a hand's finger system.


	How to Run:
	import clavanMichael_riggingTools
	clavanMichael_riggingTools.create_finger_attributes()
	'''

	# Get Selected:
	selected_icon = pm.ls(selection=True)
	control_icon = selected_icon[0]

	control_icon.addAttr('FINGERS', at='enum', en='-----------', keyable=True)
	control_icon.FINGERS.set(lock=True)
	control_icon.addAttr('CURL', at='enum', en='-----------', keyable=True)
	control_icon.CURL.set(lock=True)

	control_icon.addAttr('index_curl', keyable=True)
	control_icon.addAttr('middle_curl', keyable=True)
	control_icon.addAttr('pinky_curl', keyable=True)

	control_icon.addAttr('SPREAD', at='enum', en='-----------', keyable=True)
	control_icon.SPREAD.set(lock=True)
	control_icon.addAttr('index_spread', keyable=True)
	control_icon.addAttr('middle_spread', keyable=True)
	control_icon.addAttr('pinky_spread', keyable=True)

	control_icon.addAttr('THUMB', at='enum', en='-----------', keyable=True)
	control_icon.THUMB.set(lock=True)
	control_icon.addAttr('thumb_curl', keyable=True)
	control_icon.addAttr('thumb_spread', keyable=True)
	control_icon.addAttr('thumb_drop', keyable=True)

def separator_attribute():
	'''
	Create a separator (enum) attribute on a selected control. 

	import clavanMichael_riggingTools
	clavanMichael_riggingTools.separator_attribute()
	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Create a float attribute
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', 
	    en="---------------:", keyable=True)
	attribute = first_selected.attr(attribute_name)
	attribute.set(lock=True)

