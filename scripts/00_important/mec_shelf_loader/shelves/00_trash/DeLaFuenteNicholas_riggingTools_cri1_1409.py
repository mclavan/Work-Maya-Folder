'''

Nicholas De La Fuente

Descriptin- Rigging tools

How to Run:

import DeLaFuenteNicholas_riggingTools_cri1_1409
reload(DeLaFuenteNicholas_riggingTools_cri1_1409)


'''



print 'rigging Tools Active'

import pymel.core as pm 

def tool():
	print 'Tool Active'

def parent_snap_tool():
	'''
	This tool moves the first selected object to the second
	-Translates and roatates the targer object.

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	DeLaFuenteNicholas_riggingTools_cri1_1409.parent_snap_tool()
	'''
	
	selected = pm.ls(selection = True)
	print ' selected: {0}'.format(selected)

	kenny = pm.parentConstraint(selected[0],selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second.'



def point_snapping_tool():
	'''
	This tool moves the first selected object to the second
	-Translates the targer object.

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	DeLaFuenteNicholas_riggingTools_cri1_1409.point_snapping_tool()
	'''
	
	selected = pm.ls(selection = True)
	print ' selected: {0}'.format(selected)

	kenny = pm.pointConstraint(selected[0],selected[1])
	pm.delete(kenny)


	print 'The first selected object was moved to the second.'


def world_icon():
	'''
	Nicholas De La Fuente

	Descriptin: Creates a world oriented object and snap it to a joint.

	How to Run:

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.world_icon()

	'''

	#get selected
	selected = pm.ls(selection = True)
	print ' selected: {0}'.format(selected)

	first_joint = selected[0]

	#create a control icon
	control_icon_1 = pm.circle(normal = [0, 1, 0], radius = 2)[0]
	#move control icon to the target joint
	
	#delete the constraint
	kenny = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(kenny)



	print 'Icons Created.'

def hierachy():
	'''
	Nicholas De La Fuente

	Description

	create a hierachy based upon a given system

	select root joint chain and execute function.
	
	How to Run:

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.hierachy()
	'''
	'''
	Input
	What are we working on?
	The root joint
	# '''
	joint_system = pm.ls(selection = True, dag= True)
	# print'Joint System', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding root joint
	'''

	#create empty group
	root_pad = pm.group(empty = True)

	#move the group over to the target joint
	kenny = pm.pointConstraint(root_joint, root_pad)
	pm.delete(kenny)


	#freeze transforms on group
	pm.makeIdentity(apply = True, t=1, r=1, s=1, n=0)
	
	# parent joint back to the group
	pm.parent(root_joint, root_pad)
	'''
	Local Controls

	'''
	'''
	Control 1 - root_joint
	'''
	#create control.
	#normal=[1,0,0], radius= 2
	control_icon_1 = pm.circle(normal=[1,0,0], radius=2, name= 'lt_middle_01_icon')[0]


	#create group
	#grouping control durign the process
	local_pad_1 = pm.group(name = 'lt_middle_01_pad')
	
	#output control and pad
	print 'Control 1 created:', control_icon_1
	print 'Local Pad 1 created:',local_pad_1	
	#move group over to the target joint

	#Driver:Joint:
	#Driven: Group

	kenny = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(kenny)

	#delete constraint after snapping.
	pm.orientConstraint(control_icon_1, root_joint)

	#orient constrain the joint to the conrtol
	# driver > drive
	#control > joint

	'''
	Control 2
	'''
	#create control.
	#normal=[1,0,0], radius= 2
	control_icon_2 = pm.circle(normal=[1,0,0], radius=2, name= 'lt_middle_02_icon')[0]


	#create group
	#grouping control durign the process
	local_pad_2 = pm.group(name= 'lt_middle_02_pad')
	
	#output control and pad
	print 'Control 2 created:', control_icon_2
	print 'Local Pad 2 created:',local_pad_2	
	#move group over to the target joint

	#Driver:Joint:
	#Driven: Group

	kenny = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(kenny)

	#delete constraint after snapping.
	pm.orientConstraint(control_icon_2, joint_2)

	#orient constrain the joint to the conrtol
	# driver > drive
	#control > joint
 
	'''
	Conrol 3
	'''
	#create control.
	#normal=[1,0,0], radius= 2
	control_icon_3 = pm.circle(normal=[1,0,0], radius=2, name= 'lt_middle_03_icon')[0]


	#create group
	#grouping control durign the process
	local_pad_3 = pm.group(name= 'lt_middle_03_pad')
	
	#output control and pad
	print 'Control 3 created:', control_icon_3
	print 'Local Pad 3 created:',local_pad_3	
	#move group over to the target joint

	#Driver:Joint:
	#Driven: Group
	kenny = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(kenny)

	#delete constraint after snapping.
	

	#orient constrain the joint to the conrtol
	# driver > drive
	#control > joint
	pm.orientConstraint(control_icon_3, joint_3)

	'''
	Parent Controls together
	'''

	#pad 3 (last) > control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)


	

	print 'hierachy created.'


def renamer():
	
	'''
	Nicholas De La Fuente

	Description: Renaming template tool 

	How to run 

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.renamer()


	'''


	#Naming Conventions

	RootJoint = 'ct_back_01_bind'
	RootPad = 'ct_back_01_pad'
	ProxyGeo ='ct_back_01_proxy'
	LocalPad ='ct_back_01_local'
	ControlIcon ='ct_back_01_icon'



	root_joint = 'ct_back_01_bind'

	proxy_name = root_joint.replace('_bind', '_proxy')
	icon_name = root_joint.replace('_bind', '_icon')
	root_pad_name = root_joint.replace('01_bind', '00_pad')


	print 'Old Name:', root_joint
	print 'Proxy Name:', proxy_name
	print 'Control Name:', icon_name
	print 'Root Pad name:', root_pad_name



	#Get selected

	selected = pm.ls(selection=True)
	first_selected = selected[0]
	second_selected = selected[1]

	new_proxy_name = first_selected.replace('_bind', '_proxy')

	second_selected.rename(new_proxy_name)
	print 'New Proxy Name:', second_selected

	selected = pm.ls(selection=True)
	root_joint = selected[0]


	new_pad_name = root_joint.replace('01_bind', '00_pad')
	print 'Pad Name:', new_pad_name
	pad = pm.group(empty=True, name = new_pad_name)



def joint_renamer():

	'''
	This joint renames selected joints chains

	Select first joint in chain and run function.
	- Script will come up with two prompts first 
		(1: What is the Orientation?) (2:What is the Name?)

	How to run

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.joint_renamer()

	'''

	#select the root joint and Ill get its children.
	joint_chain = pm.ls(selection = True, dag = True)

	#Dont worry about the waste suffix
	#ori_name_count_suffix
	#lt_arm_01_bind

	ori = raw_input('What Orientation?')
	name = raw_input('What Name?')
	count = 1
	suffix = 'bind'

	for current in joint_chain:
	    new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	    #rename command
	    
	    #vairable.rename (new_name)
	    current.rename(new_name)
	    
	    count = count + 1
	    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count -1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)

	current.rename(new_name)


def seperator_attribute():

	'''
	Nicholas De La Fuente

	Description: Creates seperator attributes and lets you name it before you do it.

	How to run:
	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.seperator_attribute():
	

	'''

	#Creating Seperator Attributes

	'''
	Seperator Attributes

	Description:Creates a Seperator attribute and lets you name it before.
	'''

	selected = pm.ls(selection = True)
	print ' Currently selected;', selected
	
	first_selected = selected[0]

	#addAttr
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at = 'enum', en= "-------------:", keyable=True)


def quick_attribute():
	
	'''

	Nicholas De La Fuente	

	Description: Creates a quick attribute and lets you name it before you
	it is created.

	How to run

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.quick_attribute()
	'''

	#Creating quick Attributes
	'''
	Raw Input attributes

	Description: Creates a quick attribute and lets you name it before you
	it is created.

	'''


	selected = pm.ls(selection = True)
	print ' Currently selected;', selected

	first_selected = selected[0]

	#addAttr
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, keyable=True)



def template_attributes():

	#Creating Attributes
	'''
	Nicholas De La Fuente

	How to run

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.template_attributese()


	Template attributes 

	Description: Creates a series of attributes right after to each other 	
	'''
	selected = pm.ls(selection = True)
	print ' Currently selected;', selected

	first_selected = selected[0]

	#addAttr
	first_selected.addAttr('index_curl',keyable=True)
	first_selected.addAttr('pinky_curl',keyable=True)

	first_selected.addAttr('index_spread',keyable=True)
	first_selected.addAttr('middle_spread',keyable=True)
	first_selected.addAttr('pinky_spread',keyable=True)



def icon_color_blue():
	'''
	Description: Turns icon slected blue

	How to run: 
	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.icon_color_blue()

	'''

	selected = pm.ls(selection = True)
	print ' Currently selected;', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	blue = 6
	first_selected.overrideColor.set(blue)


def icon_color_red():

	'''
	How to run: 
	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.icon_color_red()

	'''
	selected = pm.ls(selection = True)
	print ' Currently selected;', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	red = 13
	first_selected.overrideColor.set(red)



def icon_color_yellow():
	'''
	How to run: 
	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.icon_color_yellow()

	'''


	
	selected = pm.ls(selection = True)
	print ' Currently selected;', selected

	first_selected = selected[0]

	first_selected.overrideEnabled.set(1)
	yellow = 17
	first_selected.overrideColor.set(yellow)


def unlock_and_show():
	'''
	unlock_and_show

	Description: Unlocks an attribute and shows hidden attributs

	How to run: 
	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.unlock_and_show()

	'''

	selected = pm.ls(selection = True)
	print ' Currently selected;', selected

	first_selected = selected[0]
	#lock and hide
	first_selected.tx.set(lock=False, keyable =True)
	first_selected.ty.set(lock=False, keyable =True)
	first_selected.tz.set(lock=False, keyable =True)
	first_selected.rx.set(lock=False, keyable =True)
	first_selected.ry.set(lock=False, keyable =True)
	first_selected.rz.set(lock=False, keyable =True)
	first_selected.sx.set(lock=False, keyable =True)
	first_selected.sy.set(lock=False, keyable =True)
	first_selected.sz.set(lock=False, keyable =True)
	first_selected.v.set(lock=False, keyable =True)

	'''
	For a hide and lock tool reverse the true and False

	'''



def padding_tool():
	
	'''
	Nicholas De La Fuente

	Description: Creates a pad for the selected objects.

	How to run:
	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)

	DeLaFuenteNicholas_riggingTools_cri1_1409.padding_tool()

	'''
	selected = pm.ls(selection= True)
	# print 'Current selected:', selected

	root_joint = selected[0]
	
	#create empty group
	#empty set to true will create an empty group
	pad = pm.group(empty = True)
	#move group to joint
	# delete constraint
	kenny = pm.pointConstraint(root_joint, pad)
	pm.delete(kenny)

	# freexe transforms on the group
	pm.makeIdentity(pad, apply = True, t=1, r=1, s=1, n=0)
	# Parent joint to group
	pm.parent(root_joint, pad)

	#renaming
	#change 01_bind to 00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)


	print 'Padding Group created'


def priming_tool():
	

	'''

	Nicholas De La Fuente

	Description: creates a local oriented control on joints.

	How to run:

	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.priming_tool
	'''

	# Get selected

	selected = pm.ls(selection = True)
	# print ' Joints Selected:', selected

	# target_joint = selected[0]

	for target_joint in selected:


		#Create control
		#normal set to x and radius set to 2

		control_icon = pm.circle(normal = [1, 0, 0], radius = 2)[0]


		#group control (not empty group)
		local_pad = pm.group()

		print 'Control Icon:', control_icon
		print 'Pad created:', local_pad

		#move group to target joint.
		# and delete constraint

		kenny = pm.parentConstraint(target_joint, local_pad)
		pm.delete(kenny)

		#orient constraint joint to control
		pm.orientConstraint(control_icon, target_joint)




	print 'Local Oriented Controls Created.'

def cluster_tool():
	'''
	Nicholas De La Fuente

	Description: Creates clusters on a curve.

	How to run 


	import DeLaFuenteNicholas_riggingTools_cri1_1409
	reload(DeLaFuenteNicholas_riggingTools_cri1_1409)
	DeLaFuenteNicholas_riggingTools_cri1_1409.cluster_tool():

	'''

	#Given to us by the user.

	selected = pm.ls(selection = True)

	selected_curve = selected[0]

	for current_cv in selected_curve.cv:
		print current_cv
		pm.cluster(current_cv)



'''
To create a double command switch SC, RP IK button.

Nicholas De La Fuente

Description: Click on start joint and end effector joint, if you want a rotate place ik click once. 
If you want a single chain ik click twice.

#Given to us by the user.


pm.ls(selection = True)
	
pm.ikHandle(sol = 'ikRPsolver')

print 'RP ik created'


# When button is created right click on it go to edit and click tab double click commands. Copy this lower code into that window. 
pm.ls(selection = True)
	
pm.ikHandle(sol = 'ikSCsolver')
print 'SC ik created'

'''










	    

    
















