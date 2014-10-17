# '''
# kayode omololu
# KayodeOmololu_riggingTools_CRI1_1409.py

# description:
#      a group of rigging related tools

# how to run :

# import KayodeOmololu_riggingTools_CRI1_1409
# reload(KayodeOmololu_riggingTools_CRI1_1409)     
# '''

# print 'riggin tools arctive'

# import pymel.core as pm

# def tool() :
#      print 'tool active'

# def snapping_tool() :

# 	'''
# 	this tool moves the first selecte object to the second.
# 	-translates and rotates the target object.

# 	import KayodeOmololu_riggingTools_CRI1_1409
# 	KayodeOmololu_riggingTools_CRI1_1409.snapping_tool()
# 	'''    

# 	print 'the first selected object was moved to the second.'

# 	selected = pm.ls(selection = True)
# 	print 'selected:{0}'. format(selected)

# 	target_joint = selected[0]
# 	control_icon = selected[1]

# 	#by default commmans work on selected
# 	kenny = pm.parentConstraint(selected[0],selected[1])pm.delete(kenny)

# 	print 'the first selected object was moved to the second.'





# 	 def point_snapping_tool() :

# 	 '''
# 	 this tool moves the first selecte object to the second.
# 	 -translates and rotates the target object.

# 	 import rigging_tools
# 	 rigging_tools.snapping_tool()
# 	 '''    

# 	 selected = pm.ls(selection = True)
# 	 print 'selected:{0}'.format(selected)

# 	 target_joint = selected[0]
# 	 control_icon = selected[1]

# 	 #by default commmans work on selected
# 	 kenny = pm.pointConstraint(selected[0],selected[1])pm.delete(kenny)

# 	 print 'the first selected object was moved to the second.'

# def world_icon():
# 	#get selected
# 	selected = pm.ls(selection = True)
# 	print 'selected:{0}'.format(selected)

# 	first_joint = selected[0]

# 	# create a control icon.
# 	control_icon_1 = pm.circle(normal = [0, 1, 0], radius = 2)[0]

# 	# move the control to the target joint.
# 	# delete the constraint.

# 	print 'icons created'	


print 'rigging tools active'
import pymel.core as pm




def hierarchy():
	'''
	create a hierarchy based on a given system

	select root joint chain and execute funtion.
	import rigging_tools
	rigging_tools.hierarchy()
	'''

	print 'hierarchy is made'



	'''
	input
	what are we working on ?
	the root first_joint.
	'''

	joint_system = pm.ls(selection=True, dag=True)
	# print 'joint system:', joint_system
	
	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	padding root joint 

	'''
	
	#create empty group
	root_pad = pm.group(empty=True, name = 'lt_ middle_00_pad')

	# move group over to the target joint
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# freeze transforms on group
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# parent root joint to the group
	pm.parent(root_joint, root_pad)

	'''
	local controls

	'''

	'''
	control 1 - root joint 
	'''
	# create a control

	# normal= (1, 0, 0), radius = 2
	control_icon_1 = pm.circle(normal= (1, 0, 0), radius = 2)[0]

	# create a group
	# grouping control during the process
	local_pad_1 = pm.group(name = 'local_pad_01_name')

	#output control and pad
	print 'control 1 created:', control_icon_1
	print 'local pad 1 created:', local_pad_1

	# move group over to the target joint
	# delete constrain after snapping
	# driver : joint
	# driven : group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm. delete(temp_constraint)

	# orient constrain the joint to the control
	# driver -> driven
	# control -> joint
	pm.orientConstraint(control_icon_1, root_joint)

	control_icon_1.tz.set(lock = True, keyable = False)
	control_icon_1.ty.set(lock = True, keyable = False)
	control_icon_1.tx.set(lock = True, keyable = False)
	control_icon_1.sz.set(lock = True, keyable = False)
	control_icon_1.sy.set(lock = True, keyable = False)
	control_icon_1.sx.set(lock = True, keyable = False)
	control_icon_1.v.set(lock = True, keyable = False)



	'''
	control 2
	'''
	# create a control

	# normal= (1, 0, 0), radius = 2
	control_icon_2 = pm.circle(normal= (1, 0, 0), radius = 2)[0]

	# create a group
	# grouping control during the process
	local_pad_2 = pm.group(name='local_pad_02_name')

	#output control and pad
	print 'control 3 created:', control_icon_2
	print 'local pad 3 created:', local_pad_2

	# move group pver to the target joint
	# delete constrain after snapping
	# driver : joint
	# driven : group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm. delete(temp_constraint)

	# orient constrain the joint to the control
	# driver -> driven
	# control -> joint
	pm.orientConstraint(control_icon_2, joint_2)

	control_icon_2.tz.set(lock = True, keyable = False)
	control_icon_2.ty.set(lock = True, keyable = False)
	control_icon_2.tx.set(lock = True, keyable = False)
	control_icon_2.sz.set(lock = True, keyable = False)
	control_icon_2.sy.set(lock = True, keyable = False)
	control_icon_2.sx.set(lock = True, keyable = False)
	control_icon_2.v.set(lock = True, keyable = False)


	'''
	control 3

	'''
	# create a control

	# normal= (1, 0, 0), radius = 2
	control_icon_3 = pm.circle(normal= (1, 0, 0), radius = 2)[0]

	# create a group
	# grouping control during the process
	local_pad_3 = pm.group(name='local_pad_03_name')

	#output control and pad
	print 'control 3 created:', control_icon_3
	print 'local pad 3 created:', local_pad_3

	# move group pver to the target joint
	# delete constrain after snapping
	# driver : joint
	# driven : group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm. delete(temp_constraint)

	# orient constrain the joint to the control
	# driver -> driven
	# control -> joint
	pm.orientConstraint(control_icon_3, joint_3)

	control_icon_3.tz.set(lock = True, keyable = False)
	control_icon_3.ty.set(lock = True, keyable = False)
	control_icon_3.tx.set(lock = True, keyable = False)
	control_icon_3.sz.set(lock = True, keyable = False)
	control_icon_3.sy.set(lock = True, keyable = False)
	control_icon_3.sx.set(lock = True, keyable = False)
	control_icon_3.v.set(lock = True, keyable = False)

	'''

	parent controls together.
	''' 
	# pad 3(last -> control 2)

	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)



	print 'hierarchy created'


def joint_renamer():
	'''
	this tool renames a selected joint chain

	select a root joint and run the function.
	- the script will prompt you first for the orientation ('lt', 'rt', 'ct') and the
	  name of the system ('arm','back','leg')

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.joint_renamer()  


	'''
	# select the root joint and i will get its children.

	joint_chain = pm.ls(selection = True, dag = True)

	# do not worry about the waste suffix
	# ori_name_count_suffix
	#lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)
		print 'current joint: {0} - new name:{1}'.format(current, new_name)

		# rename command
		# variable.rename(new_name)
		current.rename(new_name)

		count = count + 1


	new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, 'waste')
	print 'current joint: {0} - new name:{1}'.format(current, new_name)
	current.rename(new_name)


def padding_tool():

	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.padding_tool()

	'''

	selected = pm.ls(selection = True)
	# print 'current selected:', selected
	
	root_joint = selected[0]

	# create empty group
	# empty = True will create an empty group
	pm.group(empty = True)

	# move group to joint
	# and delete constraints
	temp_constraint.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	#freeze tarnsforms on group
	pm.makeIdentity(pad, apply = True, t =1, r =1, s = 1, n = 0)

	#parent the joint to group
	pm.parent(root_joint, pad)

	#renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


def priming_tool():
	'''
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.priming_tool()
	'''

	# get selected
	selected = pm.ls(selection = True)
	# print 'joints selected:', selected
	# target_joint = selected[0]

	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind','_local')

		print 'local oriented controls created.'

		# create control
		# normal set to x and radius is 1.8
		control_icon = pm.circle(normal = [1, 0, 0], radius = 1.8, name = control_icon_name)[0]

		# group control(NOT empty group)
		local_pad = pm.group(name = local_pad_name)

		print 'control icon:', control_icon
		print 'pad created:', local_pad

		#move group to target joint and delete constraints
		temp_constraint =  pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		# orient constraint joint to control
		pm.orientConstraint(control_icon, target_joint)



def unlock_and_show() :
	print 'whats up'
	selected = pm.ls(selection = True)
	print 'currently selected:', selected

	first_selected = selected[0]
	# lock and hide
	first_selected.tz.set(lock = True, keyable = False)
	first_selected.ty.set(lock = True, keyable = False)
	first_selected.tx.set(lock = True, keyable = False)
	first_selected.sz.set(lock = True, keyable = False)
	first_selected.sy.set(lock = True, keyable = False)
	first_selected.sx.set(lock = True, keyable = False)
	first_selected.v.set(lock = True, keyable = False)

	


# 	print 'padding group created.'















