'''
Hannah Epling
eplingHannah_rigging_tools.py

Description:

How to Run:
import eplingHannah_rigging_tools
reload (eplingHannah_rigging_tools)

'''
print 'eplingHannah_rigging_tools has been opened.'

import pymel.core as pm

def hierarchy(): 
	'''
	How to Run:
	import eplingHannah_rigging_tools
	reload (eplingHannah_rigging_tools)
	eplingHannah_rigging_tools.hierarchy()
	'''

	print 'Hierarchy Generated'

	# The user will select the root joint and the tool 
	#	will apply the systems

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	'''	
	Pad the root joint.
	'''

	# Create an empty group.
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad

	# Move group to root joint
	# Point constrain group to root joint
	#	Offset is off (Snapping)
	temp = pm.parentConstraint(root_joint, pad)

	# Delete constraints
	pm.delete(temp)

	# Freeze transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group. 
	pm.parent(root_joint, pad)


	'''
	# Create a local oriented control for each joint
	'''
	# lt_middle_01_bind, lt_middle_02_bind, lt_middle_03_bind

	# Create control (circle)
	control_icon_1 = pm.circle(name='lf_middle_01_icon', normal=[1,0,0])[0]

	# Create group (NOT EMPTY)
	# This will automaticly parent the control under the group
	control1_pad = pm.group(name='lt_middle_01_local')
	print 'Control Pad Created:', control1_pad

	# Move group to the target joint
	# Use a parent constraint. Driver is the joint
	# 	Where Driven is the group
	# 	Offset is off (Snapping)
	temp = pm.parentConstraint(root_joint, control1_pad)

	# Delete the constraint
	pm.delete(temp)

	# Delete History on control
	pm.delete(control_icon_1, ch=True)

	# Orient Constraint. Driver: control. Driven: joint
	pm.orientConstraint(control_icon_1, root_joint)



	#Do this same process for second_joint
	control_icon_2 = pm.circle(name='lf_middle_02_icon', normal=[1,0,0])[0]

	control2_pad = pm.group(name='lt_middle_02_local')
	print 'Control Pad Created:', control2_pad

	temp = pm.parentConstraint(second_joint, control2_pad)
	pm.delete(temp)

	pm.delete(control_icon_2, ch=True)

	pm.orientConstraint(control_icon_2, second_joint)



	# Do this same process for third_joint
	control_icon_3 = pm.circle(name='lf_middle_03_icon', normal=[1,0,0])[0]

	control3_pad = pm.group(name='lt_middle_03_local')
	print 'Control Pad Created:', control3_pad

	temp = pm.parentConstraint(third_joint, control3_pad)
	pm.delete(temp)

	pm.delete(control_icon_3, ch=True)

	pm.orientConstraint(control_icon_3, third_joint)



	# Parent the controls together
	pm.parent(control2_pad, control_icon_1)
	pm.parent(control3_pad, control_icon_2)

	#Create a holding group to house the pads and controls
	middle_grp = pm.group(empty=True, name='lt_middle_grp')

	# Parent the pads and the controls under the main group
	# 	Make sure that they are not parented together
	pm.parent(pad, control1_pad, middle_grp)

	print 'Hierarchy Successfully Created'

def padding():
 	'''
	How to Run:
	import eplingHannah_rigging_tools
	reload (eplingHannah_rigging_tools)
	eplingHannah_rigging_tools.padding()
	'''

	print 'Padding Generated'

	# Select all joints in the joint chain
	selected = pm.ls(selection = True)	
	root_joint = selected[0]

	# Create group (epmty)
	pad = pm.group(empty = True)

	# Move group to the target joint
	# Use a parent constraint with Offset turned of
	#	Driver is the joint
	# 	Driven is the group(pad)
	temp = pm.parentConstraint(root_joint, pad)

	# Delete the constraint
	pm.delete(temp)

	# Delete History and Freeze Trnasforms on pad
	pm.delete(pad, ch=True)
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent the joint and group. Driver: joint. Driven: pad
	pm.parent(root_joint, pad)

	# Rename the new pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding Successfully Complete'

def joint_rename():
	'''
	How to Run:
	import eplingHannah_rigging_tools
	reload (eplingHannah_rigging_tools)
	eplingHannah_rigging_tools.joint_rename()
	'''
	print "Joint Chain Rename Generated"

	# The user will select the root joint and the tool will 
	#	rename the chain in the system

 	# Get all joints in a selected joint chain
	joint_chain = pm.ls(selection = True, dag = True)
	print 'Items Selected:', joint_chain

	# Build new name - ori_name_count_suffix
	# 'lt'
	# 'arm'
	# '01'
	# 'bind'
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	# Select the root joint and add a For-In loop to all joints in the chain
	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		print 'Joint Name:', new_name
		current_joint.rename(new_name)

		count = count + 1

	# Rename the end joint by changing suffix to waste
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)

	print 'Joint Chain Successfully Renamed'

def priming():
	'''
	How to Run:
	import eplingHannah_rigging_tools
	reload (eplingHannah_rigging_tools)
	eplingHannah_riggingTools_cri1_1405.priming()
	'''

	print 'Priming Generated'

	# The user will select the joint and a control will be snapped 
	#	to the system

	selected = pm.ls(selection = True)

	for target_joint in selected:
		control_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		# Create a control and a group for the local pad
		control_icon = pm.circle(normal = [1, 0, 0], radius = 1.5,
			name = control_name)[0]

		local_pad = pm.group(name = local_pad_name)

		# Parent Constraint to move the pad to the target joint
		#	Driver is joint
		#	Driven is pad
		temp = pm.parentConstraint(target_joint, local_pad)

		# Delete the constraint
		pm.delete(temp)

		# Delete History on pad
		pm.delete(local_pad, ch=True)

		#Orient Constraint. Driver: control. Driven: joint
		pm.orientConstraint(control_icon, target_joint)

	print 'Priming Successfully Completed'

def lock_and_hide():
	'''
	How to Run:
	import eplingHannah_rigging_tools
	reload (eplingHannah_rigging_tools)
	eplingHannah_rigging_tools.lock_and_hide()
	'''

	print 'Lock and Hide Generated'

	# The user will select the object desired and the tool will hide
	# 	attributes in the channel box, as well as lock them 
	
	# Grab selected
	selected = pm.ls(selection = True)
	print 'Current Selected:', selected

	for current_item in selected:
		current_item.tx.set(lock = True, keyable = False)
		current_item.ty.set(lock = True, keyable = False)
		current_item.tz.set(lock = True, keyable = False)
		    
		current_item.rx.set(lock = True, keyable = False)
		current_item.ry.set(lock = True, keyable = False)
		current_item.rz.set(lock = True, keyable = False)

		current_item.sx.set(lock = True, keyable = False)
		current_item.sy.set(lock = True, keyable = False)
		current_item.sz.set(lock = True, keyable = False)
		    
		current_item.v.set(lock = False, keyable = True)

	print 'Lock and Hide Successfully Completed'

def reset_attributes():
	'''
	How to Run:
	import eplingHannah_rigging_tools
	reload (eplingHannah_rigging_tools)
	eplingHannah_rigging_tools.reset_attributes()
	'''

	print 'Reset Generated'

	# The user will selecet the object desired and the tool will reset
	# 	all attributes to default lock and hide settings 

	# Grab selected 
	selected = pm.ls(selection = True)
	print 'Current Selected:', selected

	for current_item in selected:
		current_item.tx.set(lock = False, keyable = True)
		current_item.ty.set(lock = False, keyable = True)
		current_item.tz.set(lock = False, keyable = True)
		    
		current_item.rx.set(lock = False, keyable = True)
		current_item.ry.set(lock = False, keyable = True)
		current_item.rz.set(lock = False, keyable = True)
		    
		current_item.sx.set(lock = False, keyable = True)
		current_item.sy.set(lock = False, keyable = True)
		current_item.sz.set(lock = False, keyable = True)
		    
		current_item.v.set(lock = False, keyable = True)

	print 'Reset Successfully Completed'
	print 'All Attributes Unlocked and Showing'

def attribute():
	'''
	How to Run:
	import eplingHannah_rigging_tools
	reload (eplingHannah_rigging_tools)
	eplingHannah_rigging_tools.attribute()
	'''
	print 'Attribute Generated'

	# The user will select the object desired an an attribute will be created
	# 	in the Channel Box

	# Select Object
	selected = pm.ls(selection = True)
	print 'Current Selected:', selected

	first_selected = selected[0]

	first_selected.addAttr(raw_input(), keyable = True)

	print 'Attribute Successfully Created'
