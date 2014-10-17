'''
Description:

How to run

import Alanis_Jimenez_Adrian_riggingTools_cri1_1405
reload (Alanis_Jimenez_Adrian_riggingTools_cri1_1405)

'''
'''
Hierarchy Tool 
'''
import pymel.core as pm 
def hierarchy_tool():
	'''
	import Alanis_Jimenez_Adrian_riggingTools_cri1_1405
	reload (Alanis_Jimenez_Adrian_riggingTools_cri1_1405)
	Alanis_Jimenez_Adrian_riggingTools_cri1_1405.hierarchy_tool()
	'''
	#The user will select the root joint and the tool will apply the system

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	thehird_joint = 'lt_middle_03_bind'

	'''
	Pad the root joint.
	'''

	# Create an empty group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	print 'Root Pad Created:', pad 

	# Move group to root joint.
	# Point constrain group to root joint.
	temp = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(temp)

	# Freeze transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint, pad)

	'''
	Local Controls
	'''
	'''
	Control 1 - root_joint
	'''
	# Create a control
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control in pad.
	print 'Control 1 Created:', control_icon_1
	print ' Local Pad 1 Created:', local_pad_1


	# Move group over to the target joint.
	# Delete contrain after snapping.
	temp_contraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_contraint)
	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_1, root_joint)

	'''
	Control 2
	'''
	# Create a control
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control in pad.
	print 'Control 2 Created:', control_icon_2
	print ' Local Pad 2 Created:', local_pad_2


	# Move group over to the target joint.
	# Delete contrain after snapping.
	temp_contraint = pm.parentConstraint(second_joint, local_pad_2)
	pm.delete(temp_contraint)
	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_2, second_joint)

	'''
	Control 3
	'''
	# Create a control
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2)[0]

	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control in pad.
	print 'Control 3 Created:', control_icon_3
	print ' Local Pad 3 Created:', local_pad_3


	# Move group over to the target joint.
	# Delete contrain after snapping.
	temp_contraint = pm.parentConstraint(third_joint, local_pad_3)
	pm.delete(temp_contraint)
	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_3, third_joint)

	'''
	Parent controls together.
	'''
	pm.parent(local_pad_3, control_icon_2)
	pm.parent (local_pad_2, control_icon_1)

'''
Padding Tool 
'''
def padding_tool():
	'''
	import Alanis_Jimenez_Adrian_riggingTools_cri1_1405
	reload (Alanis_Jimenez_Adrian_riggingTools_cri1_1405)
	Alanis_Jimenez_Adrian_riggingTools_cri1_1405.padding_tool()
	'''
	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'
	# Create an empty group
	pad = pm.group(empty=True, name='lt_middle_00_pad')
	
	#Print the group pad is created
	print 'Root Pad Created:', pad 

	# Move group to root joint with a point constrain(group to root joint.)
	temp = pm.pointConstraint(root_joint, pad)

	# Delete Constraint
	pm.delete(temp)

	#Freeze transforms on group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to group
	pm.parent(root_joint, pad)


	#rename the group
	#lt_middle_01_bind
	#lt_middle_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

'''
Joint Renaming Tool
'''

def renaming_tool():
	'''
	import Alanis_Jimenez_Adrian_riggingTools_cri1_1405
	reload (Alanis_Jimenez_Adrian_riggingTools_cri1_1405)
	Alanis_Jimenez_Adrian_riggingTools_cri1_1405.renaming_tool()
	'''
	import pymel.core as pm
	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'
	#Get all joints in a selected joint chain.
	joint_chain = pm.ls(selection=True, dag=True)
	print 'Items selected:', joint_chain
	
	#build the new name
	ori = 'lt'
	name = 'middle'
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		print 'Joint Name:', new_name

		count = count + 1

		current_joint.rename(new_name)
	
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint Name:', new_name
	current_joint.rename(new_name)

	print 'Joint Chain Renamed'
'''
Priming Tool
'''
def priming_tool():
	'''
	import Alanis_Jimenez_Adrian_riggingTools_cri1_1405
	reload (Alanis_Jimenez_Adrian_riggingTools_cri1_1405)
	Alanis_Jimenez_Adrian_riggingTools_cri1_1405.priming_tool()
	'''
	# Get selected.
	selected = pm.ls(selection=True)
	# print 'Joint Selected', selected
	# target_joint = selected[0]
	for target_joint in selected:
		#Naming for the controls and pads matching their respective joints.
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		#Create control
		control_icon = pm.circle(normal=[1, 0, 0], radius=1.8,
			name=control_icon_name)[0]

		#Group control (NOT and empty group)
		local_pad = pm.group(name=local_pad_name)

		print'Control Icon:', control_icon
		print'Pad Created:', local_pad

		#Move group to target joint.
		#	and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# Orient Constraint joint to control
		pm.orientConstraint(control_icon, target_joint)



	print 'Local Oriented Controls Created'
'''
Lock and Hide Attributes Tool
'''

def lock_hide_rsv():
	'''
	import Alanis_Jimenez_Adrian_riggingTools_cri1_1405
	reload (Alanis_Jimenez_Adrian_riggingTools_cri1_1405)
	Alanis_Jimenez_Adrian_riggingTools_cri1_1405.lock_hide_rsv()
	'''

	#This tool will lock the Rotates and the Scales

	selected = pm.ls(selection=True)
	print 'selected',selected

	for icon in selected:

		icon.rx.set(lock=True,keyable=False)
		icon.ry.set(lock=True,keyable=False)
		icon.rz.set(lock=True,keyable=False)
		icon.sy.set(lock=True,keyable=False)
		icon.sx.set(lock=True,keyable=False)
		icon.sz.set(lock=True,keyable=False)
		icon.v.set(lock=True,keyable=False)
		print 'Icon R,S,V locked and hidden', icon

'''
Unlock and Show attributes Tool
'''

def unlock_show_trsv():
	'''
	import rigging_tools
	reload (rigging_tools)
	rigging_tools.unlock_show_trsv()
	'''

	#This tool will unlock the Translates, Rotates and the Scales

	selected = pm.ls(selection=True)
	print 'selected',selected

	for icon in selected:

		icon.tx.set(lock=False,keyable=True)
		icon.ty.set(lock=False,keyable=True)
		icon.tz.set(lock=False,keyable=True)
		icon.rx.set(lock=False,keyable=True)
		icon.ry.set(lock=False,keyable=True)
		icon.rz.set(lock=False,keyable=True)
		icon.sy.set(lock=False,keyable=True)
		icon.sx.set(lock=False,keyable=True)
		icon.sz.set(lock=False,keyable=True)
		icon.v.set(lock=False,keyable=True)
		print 'Icon T,R,S,V unlocked and showing', icon

