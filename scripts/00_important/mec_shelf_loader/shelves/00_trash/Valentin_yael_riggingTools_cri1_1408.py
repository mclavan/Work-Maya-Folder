'''
Yael Valentin

Valentin_yael.py

import Valentin_yael
reload (Valentin_yael)



Description:
	test scrips for selection and verification of selecetion

intructions:

rename Valentin_yael before funning any commands
'''
print 'hello Michael'
print 'How are you?'
print 'I hope I got this right'
print 'Valentin_yael tools active.'

import pymel.core as pm

print 'pymel active'


'''	
Description:
		Project 4 script and tools for FK system

'''

'''
first pad joints
Valentin_yael.pading_tool

then run hierarchy()
Valentin_yael.hierarchy()
'''
def pading_tool():

	joint_system = pm.ls(selection = True, dag = True)

	#print 'Joint Sytem:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	pading_tool

	how to run;

	import Valentin_yael
	reload (Valentin_yael)
	Valentin_yael.pading_tool
	'''

	#create an empty group

	root_pad=pm.group(empty=True,name='lt_middle_1_pad')

	print'group created'

	#move group over tp target joint

	temp_constraint= pm.parentConstraint(root_joint,root_pad)
	pm.delete(temp_constraint)

	print 'group moved'

	#freeze transform on group
	pm.makeIdentity(root_pad,apply = True, t=1, r=1, s=1, n=0)

	print 'transforms frozen'

	#parent group to joint

	pm.parent(root_joint,root_pad)

	print 'joint parented to group '


def hierarchy():
	'''
	create hierchy based on given system
	-select root joint chain and execute the following functions.

	import Valentin_yael
	Valentin_yael.hierarchy()
	'''

	print 'def hierarchy active.'

	'''
	what are we working on:
	#Hierchy for the
	#finger FK system 
	root joints
	'''

	'''
	#selection
	'''

	joint_system = pm.ls(selection = True, dag = True)

	#print 'Joint Sytem:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	padding root joint
	'''

	#create empty group (when you create a none empty group will automaticly parent co0ntrol icon)

	root_pad = pm.group(empty= True, name='lt_middleFinger_grp')
 

	#move by parent contraint group to joint (check off maintAIN OFFSET) then delete the temp. 

	temp_constraint = pm.pointConstraint(root_joint, root_pad)

	pm.delete(temp_constraint)

	#(This will allow the group to take the values of the join for correect orientation and move the group dirrectly to joing)

	#freeze transform group

	pm.makeIdentity(root_pad, apply = True, t=1, r=1, s=1, n=0)

	#parentroot joint to pad

	pm.parent(root_joint, root_pad)



	'''
	local controls
	'''

	'''
	#control 1-root_joint
	'''
	#create circle
	#(creates Icon for the FK system with pm. commands with a radious of 2 and 8 sections)
	#normals=[1.0.0] raious = 2
	control_1_icon = pm.circle(name='lt middle_1_icon', r=2,sections=8,normal=[1,0,0])[0]

	#create group and groupd controls during process
 	local_1_pad = pm.group(control_1_icon, name='lt middle_1_pad')
 	
 	#(name='lt_middle_01_pad')[0] #or local_pad_1 = pm.group()

 	print 'local_1_pad created', local_1_pad
 	print 'control 1 created', control_1_icon

	#move control to correspondimng joint

	#delete constraint after snap
	#driver: joint
	#driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_1_pad)
	pm.delete(temp_constraint)

	#orient constraint joit to control 
	#(driver--> driven or control_icon to joint)
	pm.parentConstraint(control_1_icon,root_joint)

	print 'grandpa' 
	'''

	#control 2
	'''
	#create circle
	#(creates Icon for the FK system with pm. commands with a radious of 2 and 8 sections)
	#normals=[1.0.0] raious = 2
	control_2_icon = pm.circle(name='lt middle_2_icon', r=2,sections=8,normal=[1,0,0])[0]

	#create group and groupd controls during process
 	local_2_pad = pm.group(control_2_icon, name='lt middle_2_pad')
 	
 	
 	#(name='lt_middle_02_pad')[0] #or local_pad_1 = pm.group()

 	print 'local_2_pad created', local_2_pad
 	print 'control 2 created', control_2_icon

	#move control to correspondimng joint

	#delete constraint after snap
	#driver: joint
	#driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_2_pad)
	pm.delete(temp_constraint)

	#orient constraint joit to control 
	#(driver--> driven or control_icon to joint)
	pm.parentConstraint(control_2_icon,joint_2)


	print 'daddy' 


	'''
	#control 3
	'''
		#create circle
	#(creates Icon for the FK system with pm. commands with a radious of 2 and 8 sections)
	#normals=[1.0.0] raious = 2
	control_3_icon = pm.circle(name='lt middle_3_icon', r=2,sections=8,normal=[1,0,0])[0]

	#create group and groupd controls during process
 	local_3_pad = pm.group(control_3_icon, name='lt middle_3_pad')
 	

 	#local_3_pad(name='local_3_pad',normal=[1,0,0])[0]
 	#(name='lt_middle_03_pad')[0]  #or local_pad_1 = pm.group()

 	print 'local_3_pad created', local_3_pad
 	print 'control 3 created', control_3_icon

	#move control to correspondimng joint

	#delete constraint after snap
	#driver: joint
	#driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_3_pad)
	pm.delete(temp_constraint)

	#orient constraint joit to control 
	#(driver--> driven or control_icon to joint)
	pm.parentConstraint(control_3_icon,joint_3)

	print 'son' 

	'''
	parent control together
	'''
	pm.parent(local_1_pad,root_pad)
	pm.parent(local_2_pad, control_1_icon)
	pm.parent(local_3_pad, control_2_icon)

	print 'control icon created'

	print 'hierarchy created.'

	#create circle
	#(creates Icon for the FK system with pm. commands with a radious of 2 and 8 sections)

	#control_icon_1 = pm.circle(name='lt middle_icon_1', r=2,sections=8,normal=[1,0,0])[0]




	#parent circle to empty group
	#pm.group(control_icon_1, name = 'lt_middle_1_local')

	#print 'control_icon_1'
	#(this will move Icon to joint)

	#freeze transforms on circle


'''
Description:
		project 4 Lock and hide

'''
def lock_and_hide():
	'''
	run command:
	Valentin_yael.lock_and_hide()
	'''
	#Valentin_yael.Lock_and_hide
	#get_selected

	selected_controls= pm.ls(selection = True)

	control_1_icon= Selected_control[0]
 	control_3_icon= selected_control[2]
 	control_2_icon= selected_control[1]
	

	print 'selected_controls:', control_1_icon
	#repeate process per control
	'''
	control_1_con
	'''


	control_1_icon.tx.set(lock= True, keyable = False)
	control_1_icon.tx.set(lock= True, keyable = False)
	control_1_icon.tx.set(lock= True, keyable = False)
	control_1_icon.sx.set(lock= True, keyable = False)
	control_1_icon.sx.set(lock= True, keyable = False)
	control_1_icon.sx.set(lock= True, keyable = False)
	control_1_icon.rx.set(lock= True, keyable = False)
	control_1_icon.rx.set(lock= True, keyable = False)
	control_1_icon.rx.set(lock= True, keyable = False)
	control_1_icon.v.set(lock= True, keyable = False)

	'''
	control_2_con
	'''


	control_2_icon.tx.set(lock= True, keyable = False)
	control_2_icon.tx.set(lock= True, keyable = False)
	control_2_icon.tx.set(lock= True, keyable = False)
	control_2_icon.sx.set(lock= True, keyable = False)
	control_2_icon.sx.set(lock= True, keyable = False)
	control_2_icon.sx.set(lock= True, keyable = False)
	control_2_icon.rx.set(lock= True, keyable = False)
	control_2_icon.rx.set(lock= True, keyable = False)
	control_2_icon.rx.set(lock= True, keyable = False)
	control_2_icon.v.set(lock= True, keyable = False)

	'''
	control_3_con
	'''


	control_3_icon.tx.set(lock= True, keyable = False)
	control_3_icon.tx.set(lock= True, keyable = False)
	control_3_icon.tx.set(lock= True, keyable = False)
	control_3_icon.sx.set(lock= True, keyable = False)
	control_3_icon.sx.set(lock= True, keyable = False)
	control_3_icon.sx.set(lock= True, keyable = False)
	control_3_icon.rx.set(lock= True, keyable = False)
	control_3_icon.rx.set(lock= True, keyable = False)
	control_3_icon.rx.set(lock= True, keyable = False)
	control_3_icon.v.set(lock= True, keyable = False)
	
	print 'controls are locked and stored away, far, far away!'
'''
curl
'''

def Valentin_yael_curl():
	'''
	run command
	Valentin_yael.curl()
	'''
	selected= pm.ls(selection=True)

	first_selected= selected(0)

	first_selected.addattr('middle_curl',keyable=True)


'''
padding tools
'''
def pading_tool():

	joint_system = pm.ls(selection = True, dag = True)

	#print 'Joint Sytem:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	pading_tool

	how to run;

	import Valentin_yael
	reload (Valentin_yael)
	Valentin_yael.pading_tool
	'''

	#create an empty group

	root_pad=pm.group(empty=True, name='lt_middle_1_pad')

	print'group created'

	#move group over tp target joint

	temp_constraint= pm.parentConstraint(root_joint,root_pad)
	pm.delete(temp_constraint)

	print 'group moved'

	#freeze transform on group
	pm.makeIdentity(root_pad,apply = True, t=1, r=1, s=1, n=0)

	print 'transforms frozen'

	#parent group to joint

	pm.parent(root_joint,root_pad)

	print 'joint parented to group '

def prime_tool():
	

	'''
	how to run:
	import Valetin.Yael
	reload (Valentin_yael)
	Valentin_yael.prime_tool()
	'''
	selected= pm.ls(selection = True, dag = True)
	target_joint = selected[0]

	#name

	control_icon_name= target_joint.replace('_bind', '_icon')
	local_pad_name= target_joint.replace('_bind','_prime')

	print 'joints selected' 



	#create control
	#normals set to x and radious is 2
	control_icon=pm.circle(normals=[1,0,0], radius=2,
		name=control_icon_name)[0]

	print 'local icon created'

	#group control 
	local_pad =pm.group(name=local_pad_name)

	#move group to joint
	#delete temp constraint 

	temp_constraint= pm.parentConstraint(target_joint,local_pad)
	pm.delete(temp_constraint)

	#orient controls

	pm.orientConstraint(control_icon,target_joint)

	print 'local icon created'


def joint_renamer():


	'''
	run command:

	import Valetin.Yael
	reload (Valentin_yael)
	Valentin_yael.joint_renamer()
	'''


	#Get selected root_joint

	joint_system = pm.ls(selected=True, dag= True)

	#orientation_systemName_count_suffix

	#lt_arm_01_bind

	ori = 'lt'
	name = 'arm'
	count = 1
	suffix = 'bind'


	#loop Through the rest of joint chain
	
	for curent_joint in joint_system:
		#assembling new name
		new_name = '{0}_{1}_0{2}_{3}'.format(ori,name,count,suffix)

		#rename joint
		curent_joint.rename(new_name)
		
		print 'renaming:', current_joint,'new name', new_name

		#increasing the incriments of the count of each selected object
		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori,name,count,'waste')
	print 'renaming:', current_joint,'new name', new_name
	curent_joint.rename(new_name)



	print 'Ive changed the name master.'
