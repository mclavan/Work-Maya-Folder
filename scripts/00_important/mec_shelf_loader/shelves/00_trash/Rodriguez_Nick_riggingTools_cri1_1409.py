'''
Rodriguez Nick
Rodriguez_Nick_riggingTools_cri1_1409.py

Description:
	A group of rigging related tools 

How to Run:

import Rodriguez_Nick_riggingTools_cri1_1409
reload (Rodriguez_Nick_riggingTools_cri1_1409)

'''

print 'hi'

import pymel.core as pm 

def hierarchy():
	'''
	create a hierarchy based on a giving system 
	select root join chain and function 

	import Rodriguez_Nick_riggingTools_cri1_1409
	reload (Rodriguez_Nick_riggingTools_cri1_1409)
	Rodriguez_Nick_riggingTools_cri1_1409.hierarchy()

	'''


	'''
	input 
	root joints

	'''
	joint_system = pm.ls(selection=True, dag=True)
	#print 'joint system:', joint_system

	root_joint=joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	'''	
	padding the root_joint

	'''
	#create a empty group
	
	new_name_pad = root_joint.replace('01_bind','00_pad')
	root_pad = pm.group(empty=True, name=new_name_pad)

	#move group to target joint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)
	#freeze transgforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)
	#parent joint back to the group
	pm.parent(root_joint, root_pad)
	'''
	create local cotrols

	'''
	'''
	#control one - root joint
	'''
	#create contorl 
	#Renaming by using replace()
	new_name_icon_1 = root_joint.replace('01_bind', '01_icon')
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2, name=new_name_icon_1)[0]
	#created a group
	#grouping the control in the process
	

	#Renaming by using replace()

	new_name_local_pad_1 = root_joint.replace('01_bind', '01_pad')
	local_pad_1 = pm.group(name=new_name_local_pad_1)
	print 'control 1 created: ', control_icon_1
	print 'control pad 1 created: ', local_pad_1
	#move group over to target
	#delete constrain
	#driver ; joint
	#driven : group

	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)
	#orient constrain the joint tothe control
	#driver -> driven
	#control-> joint
	pm.orientConstraint(control_icon_1, root_joint)

	
	



	'''
	#control two
	'''
	#create contorl 
	#Renaming by using replace()
	new_name_icon_2 = joint_2.replace('02_bind', '02_icon')
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2, name=new_name_icon_2)[0]
	#created a group
	#grouping the control in the process


	#Renaming by using replace()
	new_name_local_pad_2 = joint_2.replace('02_bind', '02_pad')
	local_pad_2 = pm.group(name=new_name_local_pad_2)
	print 'control 2 created: ', control_icon_2
	print 'control pad 2 created: ', local_pad_2
	#move group over to target
	#delete constrain
	#driver ; joint
	#driven : group

	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)
	#orient constrain the joint tothe control
	#driver -> driven
	#control-> joint
	pm.orientConstraint(control_icon_2, joint_2)

	'''
	#control three
	'''

	#create contorl 
	#Renaming by using replace()
	new_name_icon_3 = joint_3.replace('03_bind', '03_icon')
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2, name=new_name_icon_3)[0]
	#created a group
	#grouping the control in the process

	#Renaming by using replace()
	new_name_local_pad_3 = joint_3.replace('03_bind', '03_pad')
	local_pad_3 = pm.group(name=new_name_local_pad_3)
	print 'control 3 created: ', control_icon_3
	print 'control pad 3 created: ', local_pad_3
	#move group over to target
	#delete constrain
	#driver ; joint
	#driven : group

	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)
	#orient constrain the joint tothe control
	#driver -> driven
	#control-> joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent contorls selected
	'''
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	#lock and hide




	print 'hierarchy created'

def padding_tool():
	'''
		import Rodriguez_Nick_riggingTools_cri1_1409
		reload (Rodriguez_Nick_riggingTools_cri1_1409)
		Rodriguez_Nick_riggingTools_cri1_1409.padding_tool()

	Select the joint and run the tool in order to do the following:

	'''
	selected = pm.ls(selection=True)
	#print 'current selected: ', selected
	root_joint = selected[0]

	#create empty group
	pad = pm.group(empty=True)

	#move group to joint
	# and deleted contrains
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)


	#freeze transforms
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#parent
	pm.parent(root_joint, pad)

	#renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'padding tool created'

def priming_tool():
	'''


	import Rodriguez_Nick_riggingTools_cri1_1409
	reload (Rodriguez_Nick_riggingTools_cri1_1409)
	Rodriguez_Nick_riggingTools_cri1_1409.priming_tool()

	'''
	selected = pm.ls(selection= True)
	#print' joints selected: ', selected
	#target_joint = selected[0] 

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		#create a control
		# normal set to x and radius is 2
		control_icon = pm.circle(normal=[1, 0, 0], radius = 2, name= control_icon_name)[0]
		# group controls(not empty group)
		local_pad = pm.group(name= local_pad_name)

		print 'control icon: ', control_icon
		print 'pad created:', local_pad
		#snapgroup to target joint

		#and delete constraint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		#orient constraint joint ot control
		pm.orientConstraint(control_icon, target_joint)


	print 'local Oriented controls created'

def joint_renamer():
	'''
		this tool renaming a selected joint chain

		slected a root joint and run the fucntion
			-	the script will prompt you first for the orientation(lt, rt, ct) and the name 
			of the system (arm, back, leg)

		import Rodriguez_Nick_riggingTools_cri1_1409
		reload(Rodriguez_Nick_riggingTools_cri1_1409)
		Rodriguez_Nick_riggingTools_cri1_1409.joint_renamer()
	'''
	joint_chain = pm.ls(selection=True, dag=True)

	# first pop up is the orientation ( lt, rt, ct)
	# second pop up is for the name of it (back, leg, head...)


	#don't worry about the waste
	#ori_name_count_suffiz
	#lt_arm_01_bind

	ori= raw_input()
	name= raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
	    new_name= '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'current joint: {0} - new name {1}'.format(current, new_name)

	    
	    
	    #rename command
	    
	    current.rename(new_name)
	    
	    count= count + 1
	    
	new_name= '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'current joint: {0} - new name {1}'.format(current, new_name)
	    
	current.rename(new_name)

def snapping_tool():
	'''
	This tool moves the first slected object to the second 
		-Translates and Rotates the target object

		import Rodriguez_Nick_riggingTools_cri1_1409
		reload (Rodriguez_Nick_riggingTools_cri1_1409)
		Rodriguez_Nick_riggingTools_cri1_1409.snapping_tool()
	'''
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	kenny = pm.parentConstraint(selected[0],selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second'

def unlock_and_show():
	'''
		import Rodriguez_Nick_riggingTools_cri1_1409
		reload (Rodriguez_Nick_riggingTools_cri1_1409)
		Rodriguez_Nick_riggingTools_cri1_1409.unlock_and_show()

		This will unlock the Translations, rotations and scales that are locked 
		and will also show them back

	'''

	selected = pm.ls(selection=True)
	print 'Currently selected: ', selected

	first_selected = selected[0]
	
	first_selected.tx.set(lock=False, keyable = True)
	first_selected.ty.set(lock=False, keyable = True)
	first_selected.tz.set(lock=False, keyable = True)
	first_selected.rx.set(lock=False, keyable = True)
	first_selected.ry.set(lock=False, keyable = True)
	first_selected.rz.set(lock=False, keyable = True)
	first_selected.sx.set(lock=False, keyable = True)
	first_selected.sy.set(lock=False, keyable = True)
	first_selected.sz.set(lock=False, keyable = True)
	first_selected.v.set(lock=False, keyable = True)
