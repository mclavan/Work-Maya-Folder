'''
Christopher Milligan
milliganChristopher_riggingTools_cri1_1405.py

Description:
Contains the Padding, Renaming and Priming Tool Sets.

import milliganChristopher_riggingTools_cri1_1405
reload(milliganChristopher_riggingTools_cri1_1405)
'''

print 'Rigging Tools Start'

import pymel.core as pm
import maya.cmds as mc

# Create and define each of the tools.

def padding_tool():

	'''
	Creates pad for joint

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.padding_tool()

	'''

	# ori = raw_imput()
	# name = raw_input()
	# count = 1
	# suffix = 'pad'

	# new_pad_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)

	
	selected_joint = pm.ls(selection=True)
	print 'Joint Selected:', selected_joint

	# Create an empty group.
	pad = pm.group(empty=True, name='pad')
	print 'Root Pad Created:', pad

	cst_temp = pm.parentConstraint(selected_joint,pad, maintainOffset=False)

	pm.delete(cst_temp)
	print 'Constraint Deleted'

	print 'Pad Named'

	print 'Pad Created'





def naming_tool():

	'''
	# Create a function called joint_rename
	# Select the root joint and loop through all joints in the joint chain.
	# 'ori_name_count_suffix' ex. 'ct_back_01_bind'

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.naming_tool()
	'''
	# Get all joints in the joint chain
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Joint Chain:', joint_chain

	# Build the new name

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)
		
		print 'Joint Name:', new_name
			

		current_joint.rename(new_name)

		count = count + 1

		print 'Joint Chain Renamed'





def priming_tool():

	'''
	This tool selects all joints, creates controls, and parents to joints
	
	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.priming_tool()

	'''

	selected_joint_pt = pm.ls(selection=True, dag=True)
		
	selected_joint_pt.pop(-1)

	for priming in selected_joint_pt:

		icon = pm.circle(normal=[1,0,0])[0]
		print 'Group Created.'

		grp = pm.group()
		print 'Group Created.'

		temp = pm.parentConstraint(priming, grp, maintainOffset=False)

		pm.delete(temp)
		print 'Constraint Deleted.'

		pm.delete(icon, ch=True)

		print 'History Deleted.'

		new_name = priming.replace('bind', 'icon')
		icon.rename(new_name)
		new_name = priming.replace('bind', 'null')
		grp.rename(new_name)





def mirror_controls():
	
	'''
	Mirrors controls over specified (input determined) axis.

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.mirror_controls()

	'''
	import maya.cmds as cmd

	user_input = raw_input('Which axis will be mirrored over?')
	
	# select icons
	selected_icons = pm.ls(selection=True)
	pull = selected_icons[0]

	# duplicated icons
	duplicated = pm.duplicate(selected_icons)
	print 'Icons Duplicated'

	# Rename all the controls duplicated
	name_icons = pm.ls('*_icon1')
	print 'Duplicated controls named:', name_icons

	for selected_control in name_icons:

		side = pull[0]
		# Find out the orientation based on the original selection
		if side == 'l':
			new_ori = 'rt'
		elif side == 'r':
			new_ori = 'lt_'

		system = selected_control.split("_")[1]
		print system

		# Rename the controls
		selected_control.rename(new_ori + system + '_icon')

	# group the duplicate icons
	grp = pm.group(empty=True, name='grp')
	pm.parent(duplicated, grp)
	print 'Icons Grouped'

	# mirror icons over correct axis
	print'Select axis for duplicate mirroring.'
	pm.setAttr(grp + '.s' + user_input , -1)

	# Unparent Icons from group.
	cmd.ungroup('grp')
	print 'Controls Ungrouped.'
	print 'Objects Mirrored.'




def revive():
	'''
	Unlocks scales and rotations, makes them visible.

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.revive()

	'''
	# select controls
	selected = pm.ls(selection=True)
	print 'Current Selection:', selected

	# Set specificed attributes to unlock/unhide
	for current_item in selected:
		current_item.tx.set(lock=False, keyable=True)
		current_item.ty.set(lock=False, keyable=True)
		current_item.tz.set(lock=False, keyable=True)
		current_item.sx.set(lock=False, keyable=True)
		current_item.sy.set(lock=False, keyable=True)
		current_item.sz.set(lock=False, keyable=True)
		current_item.v.set(lock=False, keyable=True)



def fk_hide():
	'''
	Locks and hides transforms and scales

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.fk_hide()

	'''
	# Select Controls
	selected = pm.ls(selection=True)
	print 'Current Selection:', selected
	
	# Set specified attributes to lock and hide
	for current_item in selected:
		current_item.tx.set(lock=True, keyable=False)
		current_item.ty.set(lock=True, keyable=False)
		current_item.tz.set(lock=True, keyable=False)
		current_item.sx.set(lock=True, keyable=False)
		current_item.sy.set(lock=True, keyable=False)
		current_item.sz.set(lock=True, keyable=False)
		current_item.v.set(lock=True, keyable=False)




def ik_hide():
	'''
	Locks and hides transforms and scales

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.ik_hide()

	'''
	# Select Controls
	selected = pm.ls(selection=True)
	print 'Current Selection', selected

	# Set attributes to lock and hide
	for current_item in selected:
		current_item.rx.set(lock=True, keyable=False) 
		current_item.ry.set(lock=True, keyable=False)
		current_item.rz.set(lock=True, keyable=False)
		current_item.sx.set(lock=True, keyable=False)
		current_item.sy.set(lock=True, keyable=False)
		current_item.sz.set(lock=True, keyable=False)
		current_item.v.set(lock=True, keyable=False)




def add_attribute():
	'''
	Adds a defined input on selected object

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.add_attribute()

	'''
	# Select target icon/control
	selection = pm.ls(sl=True)
	print 'Current Selection:', selection

	# Receive user input (attribute name)
	added = raw_input()

	# Set the raw_input() attribute to selected
	first_selected = selection[0]
	first_selected.addAttr(added, keyable=True)





def proxygeo_hide():
	'''
	Hides proxy geometry

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.proxy_geo_hide()

	'''
	# Get input for the suffix of the Proxy geometry.
	suffix = raw_input('Suffix of proxy geo')

	# set selection to any geometry with the selected suffix.
	proxy_geo = pm.ls('*'+suffix)
	print proxy_geo

	# Turn on override and set display type for each piece of geo.
	for geo in proxy_geo:
		geo.overrideEnabled.set(1)
		geo.overrideDisplayType.set(2)




def color_change():

	'''
	Changes the color of icons / alternative selected_icons

	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.color_change()

	'''

	# Select icon
	selected_objects = pm.ls(selection=True)[0]
	print 'Selected Objects:', selected_objects

	# for each_object in selected_objects:
		# Turn on the override
	selected_objects.setAttr('overrideEnabled', 1)
	print 'Override Enabled'

	# Change color - Red
	selected_objects.setAttr('overrideColor', 13)
	print 'Color Change (red)'




def hierarchy():

	'''
	Establishes Hierarchy between predetermined points
	
	import milliganChristopher_riggingTools_cri1_1405
	reload(milliganChristopher_riggingTools_cri1_1405)
	milliganChristopher_riggingTools_cri1_1405.hierarchy()

	'''	
	import pymel.core as pm

	print 'Hierarchy Generated...'


	# The user will select the root joint.
	# The tool will apply the systems.

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''
	# Pad the root joint.
	'''

	# Create an empty group.
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	# Move group to root joint.
	# Point constrain group to root joint.
	# 	offset off (Snapping)

	temp = pm.pointConstraint(root_joint, pad, maintainOffset = False)

	# Delete unwanted constraint.
	pm.delete(temp)

	# Freeze transforms on group.
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group.
	pm.parent(root_joint, pad)
	print 'Parented root to group'

	# Create a local oriented control for each joint.
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind.


	# Create control (circle)
	control_icon_1 = pm.circle(name='lt_middle_01_Icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# This will automatically parent the control under the group.
	group_01 = pm.group()
	print 'Group Created' , group_01


	# Move group to the target joint.
	# Use a parent constraint driver in the joint.
	#	Where driven is the group.
	# Offset is off (Snapping)
	pup = pm.parentConstraint(root_joint, group_01, maintainOffset = False)
	print 'Group Moved'


	# Delete the constraint
	pm.delete(pup)


	# Delete History on control
	pm.delete(control_icon_1, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_1, root_joint, maintainOffset = False)
	print 'Orient Constraint Created'



	'''Process Repeated for second joint(lt middle02_joint)'''

	# Create control (circle)
	control_icon_2 = pm.circle(name='lt_middle_02_Icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# This will automatically parent the control under the group.
	group_02 = pm.group()
	print 'Group Created' , group_02


	# Move group to the target joint.
	# Use a parent constraint driver in the joint.
	#	Where driven is the group.
	# Offset is off (Snapping)
	krumpet = pm.parentConstraint(second_joint, group_02, maintainOffset = False)
	print 'Group Moved'


	# Delete the constraint
	pm.delete(krumpet)


	# Delete History on control
	pm.delete(control_icon_2, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_2, second_joint, maintainOffset = False)
	print 'Orient Constraint Created'



	'''Process Repeated for third joint(lt middle03_joint)'''

	# Create control (circle)
	control_icon_3 = pm.circle(name='lt_middle_03_Icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# This will automatically parent the control under the group.
	group_03 = pm.group()
	print 'Group Created' , group_03


	# Move group to the target joint.
	# Use a parent constraint driver in the joint.
	#	Where driven is the group.
	# Offset is off (Snapping)
	lemongrab = pm.parentConstraint(third_joint, group_03, maintainOffset = False)
	print 'Group Moved'


	# Delete the constraint
	pm.delete(lemongrab)


	# Delete History on control
	pm.delete(control_icon_3, ch=True)

	# Orient Constraint driver: control driven: joint.
	pm.orientConstraint(control_icon_3, third_joint, maintainOffset = False)
	print 'Orient Constraint Created'



	'''Process Parent'''

	pm.parent(group_02, control_icon_1)
	pm.parent(group_03, control_icon_2)






