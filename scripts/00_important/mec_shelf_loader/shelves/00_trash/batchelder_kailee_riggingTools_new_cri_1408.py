'''
kailee_batchelder
batchelder_kailee_rigging_tools.pymel



discription:
	grouping of rigging tools

how to run:

import batchelder_kailee
reload(batchelder_kailee)
'''	

print 'rigging tools active'

import pymel.core as pm



def hierarchy():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tools.hierarchy_tool()
	'''
	joint_system =pm.ls(selection=True, dag=True)
	

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	print 'Hierarchy Created.'

	import pymel.core as pm

	

	root_pad = pm.group(empty = True, name = 'lt_middle_00_pad')
	print 'Root Pad Created;', pad

	todd= pm.pointConstraint(root_joint, root_pad)

	pm.delete(todd)

	pm.makeIdentity(root_pad, apply = True, t = 1, r = 1, s = 1, n = 0)

	pm.parent(root_joint, root_pad)

	
	control_icon_1 = pm.circle(normal = [1,0,0], radius=2)[0]
		

	
	local_pad_1 = pm.group()

	
	bob = pm.parentConstraint(root_joint, local_pad)

	
	pm.delete(bob)

	

	
	pm.orientConstraint(control_icon_01, root_joint)



	control_icon_02 = pm.circle(normal = [1,0,0], radius=2)[0]
		

	
	local_pad_2 = pm.group()

	
	tammy = pm.parentConstraint(joint_2, local_pad_2)

	
	pm.delete(tammy)

	
	pm.orientConstraint(control_icon_2, root_joint_2)


	control_icon_03 = pm.circle(normal = [1,0,0], radius=2)[0]
		

	
	local_pad_3 = pm.group()

	
	chris = pm.parentConstraint(joint_3, local_pad_3)

	
	pm.delete(chris)

	
	pm.orientConstraint(control_icon_3, root_joint_3)


	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

def renaming_tool():
	'''
	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tools.renaming_tool()
	'''

	'''
	root joint - 'ct_head_00_bind'
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

def joint_renamer():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tools.hierarchy_tool()
	'''

	print 'joint renamer'
	import pymel.core as pm
	'''
	'lt_arm_01_bind' -> 'lt_arm_03_waste'
	'ct_tail_01_bind' -> 'ct_tail_06_waste'
	'''
	ori = raw_input[]
	system_name = raw_input[]
	count = 1
	suffix = 'bind'

	

	for current_joint in joint_chain:
		count = count + 1
		new_name ='{0}_{1}_0{2}_{3}' .format(ori, system_name, count, suffix)
		print 'new name:' , new_name

		current_joint.rename[new_name]
		
		

	new_name ='{0}_{1}_0{2}_{3}' .format(ori, system_name, count, 'waste')
	current_joint.rename[new_name]

def padding_tool():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tools.padding_tool()
	'''

	selected = pm.ls(selection=True)
	
	root_joint = selected[0]

	
	pad = pm.group(empty=True)


	
	temp_constraint = pm.pointConstraint(root_joint, pad)
	
	pm.delete(temp_constraint)


	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	
	pm.parent(root_joint, pad)


	pad_name = root_joint.replace('01_bind', '00_pad')
	
	pad.rename(pad_name)

	print 'padding group created.'

def priming_tool():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tools.priming_tool()
	'''
	
	selected = pm.ls(selection=True)
	

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')
		
		
		control_icon = pm.circle(normal=[1,0,0], radius=1.8,
			name = control_icon_name)[0]
		
		local_pad = pm.group(name=local_pad_name)

		print 'control icon:', control_icon
		print 'pad created:', local_pad

		
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		
		pm.orientConstraint(control_icon, target_joint)


	print ' local oriented controls created'

def lock_and_hide_trans():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tool.locking_tool()
	'''
	import pymel.core as pm

	selected_control = pm.ls(selection=True)

	control_icons=selected[0]
	
	control_icons.tx.set(lock=True, keyable=False)
	control_icons.ty.set(lock=True, keyable=False)
	control_icons.tz.set(lock=True, keyable=False)
	control_icons.sx.set(lock=True, keyable=False)
	control_icons.sy.set(lock=True, keyable=False)
	control_icons.sz.set(lock=True, keyable=False)
	control_icons.v.set(lock=True, keyable=False)

	print 'selected_control:', selected

def lock_and_hide_rotate():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tool.locking_tool()
	'''
	import pymel.core as pm

	selected_control = pm.ls(selection=True)

	control_icons=selected[0]


	control_icons.rx.set(lock=True, keyable=False)
	control_icons.ry.set(lock=True, keyable=False)
	control_icons.rz.set(lock=True, keyable=False)
	control_icons.sx.set(lock=True, keyable=False)
	control_icons.sy.set(lock=True, keyable=False)
	control_icons.sz.set(lock=True, keyable=False)
	control_icons.v.set(lock=True, keyable=False)

	print 'selected_control:', selected

def unlock_and_show_trans():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tool.locking_tool()
	'''
	import pymel.core as pm

	selected_control = pm.ls(selection=True)

	control_icons=selected[0]



	control_icons.tx.set(lock=False, keyable=True)
	control_icons.ty.set(lock=False, keyable=True)
	control_icons.tz.set(lock=False, keyable=True)
	control_icons.rx.set(lock=False, keyable=True)
	control_icons.ry.set(lock=False, keyable=True)
	control_icons.rz.set(lock=False, keyable=True)
	control_icons.sx.set(lock=False, keyable=True)
	control_icons.sy.set(lock=False, keyable=True)
	control_icons.sz.set(lock=False, keyable=True)
	control_icons.v.set(lock=False, keyable=True)

	print 'selected_control:', selected

def unlock_and_show_rotates():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tool.locking_tool()
	'''
	
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

def separator_attribute():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tool.locking_tool()
	'''



	selected =pm.ls(selection=True)
	first_selected =selected[0]

	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum' en="-----------:" , keyable=True )

	attribute = first first_selected.attr(attribute_name)
	attribute.set(lock=true)

def setting_pivot():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tool.locking_tool()
	'''
	import pymel.core as pm

	selected_control = pm.ls(selection=True)

	control_icons=selected[0]

	selection = pm.ls(selection=True)

	driver_pivot = selection[0]
	driven_pivot = selection[1]
	print 'driver pivot{0} - Driven pivot{1}' . format(driver_pivot, driven_pivot)

	'''
	getting a pivot pointe
	world space or object space
	'''

	driver_translation = pm.xform(drivor_pivot, query=True, ws=True, t=True)




	pm.xform(driven_pivot, ws=True, pivots=driver_translation)

def transforming_xform():
	'''

	import batchelder_kailee
	reload(batchelder_kailee)
	batchelder_kailee_rigging_tool.locking_tool()
	'''
	pm.xform([t=[0,1,0], ro=[0,0,0], s=[1,1,1])

	pm.xform(a=True,t=[0,3,0])

	pm.xform(r=True,t=[0,3,0])


	pm.xform(os=True, t=[5,0,0])



	pm.circle(normal=[1,0,0], radius=2, s=16)
	pm.xform(Ct_control_icon.cv[::2], r=True, scale=[.5,.5,.5])



