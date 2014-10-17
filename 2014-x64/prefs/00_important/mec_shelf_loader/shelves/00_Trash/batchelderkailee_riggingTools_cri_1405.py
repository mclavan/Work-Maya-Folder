'''
rigging_tool.pymel
kailee batchelder


discription:
	grouping of rigging tools

how to run:

import rigging_tool
reload(rigging_tool)
	'''	

import pymel.core as pm

print 'rigging tools active'

def hierarchy():
	'''

	import rigging_tool
	reload(rigging_tool)
	rigging_tool.hierarchy_tool()
	'''

	print 'Hierarchy Generated'

	import pymel.core as pm

	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	pad = pm.group(empty = True, name = 'lt_middle_00_pad')
	print 'Root Pad Created;', pad

	kenny = pm.pointConstraint(root_joint, pad)

	pm.delete(kenny)

	pm.makeIdentity(pad, apply = True, t = 1, r = 1, s = 1, n = 0)

	pm.parent(root_joint, pad)

	# Create a local oriented control for each joint
	# lt_middle_01_bind, lt_middle_02_bind, and lt_middle_03_bind

	# Create control
	control_icon_01 = pm.circle(name = 'lt_middle_01_icon',
		normal = [1, 0, 0])[0]

	# Create group (NOT EMPTY)
	#    This will automatically parent the control under
	#    the group.
	holder= pm.group(name = 'lt_middle_01_local')

	# Move group to the target joint.
	# Use parent constraint. Driver is the joint.
	#    Driven is the group.
	#    Offset is off (Snapping)
	carson = pm.parentConstraint(root_joint, holder)

	# Delete the constraint
	pm.delete(carson)

	# Delete History on control
	pm. delete(ch = True)

	# Orient Constraint driver: control, driven: joint.
	pm.orientConstraint(control_icon_01, root_joint)



	control_icon_02 = pm.circle(name = 'lt_middle_02_icon',
		normal = [1, 0, 0])[0]

	holder_02 = pm.group(name = 'lt_middle_02_holder')

	sam = pm.parentConstraint(second_joint, holder_02)

	pm.delete(sam)

	pm. delete(ch = True)

	pm.orientConstraint(control_icon_02, second_joint)


	control_icon_03 = pm.circle(name = 'lt_middle_03_icon',
		normal = [1, 0, 0])[0]

	holder_03 = pm.group(name = 'lt_middle_03_holder')

	jill = pm.parentConstraint(third_joint, holder_03)

	pm.delete(jill)

	pm. delete(ch = True)

	pm.orientConstraint(control_icon_03, third_joint)


	pm.parent(holder_03, control_icon_02)
	pm.parent(holder_02, control_icon_01)

	middle_finger = pm.group(empty = True, name = 'lt_middle_group')

	pm.parent(pad, middle_finger)
	pm.parent(holder, middle_finger)

	print 'DONE!!!!'

def padding_tool():
	'''

	import rigging_tool
	reload(rigging_tool)
	rigging_tool.padding_tool()
	'''




	selected = pm.ls(selection=True)
	#print'current selected:' selected
	root_joint = selected[0]

	#create empty group
	#empty=True will make a empty group

	pad = pm.group(empty=True)


	#move group to joint
	temp_con = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_con)



	#freez transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#parent joint to group

	pm.parent(root_joint, pad)

	#rename
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'padding group created.'

def priming_tool():
	'''

	import rigging_tool
	reload(rigging_tool)
	rigging_tool.priming_tool()
	'''
	#get selected
	selected = pm.ls(selection=True)
	#print 'joints selected:', selected
	#target_joint = selected[0]


	for target_joint in selected:
		control_icon_name = target_joint.replace(' bind', 'icon')
		local_pad_name = target_joint.replace(' bind', 'local')
		#create control
		#normal set to x and radius is 1.8
		control_icon = pm.circle(normal=[1,0,0], radius=1.8, name=control_icon_name)[0]
		#group control(not empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'control icon:', control_icon
		print 'pad created:', local_pad

		#move group not control to target joint
		#delete constraint
		temp_con = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_con)

		#oreant constraint joint to control
		pm.orientConstraint(control_icon, target_joint)






	print ' local oriented controls created'

def renaming_tool():
	'''

	import rigging_tool
	reload(rigging_tool)
	rigging_tool.renaming_tool()
	'''

	'''
	root joint - 'ct_head_01_bind'
	root pad - 'ct_head_00_pad'
	proxy geo - 'ct_head_01_proxy'
	local pad - 'ct_head_01_local'
	control icon - 'ct_head_01_icon'
	'''

	root_joint = 'ct_head_01_bind'

	proxy_name = root_joint.replace('_bind', '_proxy')

	icon_name = root_joint.replace('_bind', '_icon')
	
	root_pad_name = root_joint.replace('01_bind', '00_pad')
	print ' old name:', root_joint

	print ' proxy name:', proxy_name

	print ' control name:', icon_name

	print 'root pad name:', root_pad_name

	'''
	get selected
	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	second_selected = selected[1]

	new_proxy_name = first_selected.replace('_bind', '_proxy')

	print 'new proxy name', new_proxy_name
	second_selected.rename(new_proxy_name)
	print 'new proxy name:', second_selected

	selected = pm.ls(selection=True)
	root_joint = selected[0]

	new_pad_name = root_joint.replace('01_bind', '00_pad')
	print "pad name:", new_pad_name	
	pad = pm.group(empty=True, name=new_pad_name)

def lock_tool():
	'''

	import rigging_tool
	reload(rigging_tool)
	rigging_tool.locking_tool()
	'''
	import pymel.core as pm

	selected = pm.ls(selection=True)
	print 'current selected:', selected

	first_selected =selected[0]
	first_selected.tx.set(0)
	first_selected.ty.set(0)
	first_selected.tz.set(0)
	first_selected.t.set([0, 0,0])



