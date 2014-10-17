'''

Gabriel Hernandez

Hernandez_Gabriel_riggingTools_cri1_1405

Description:
tools to help in the rigging prosses 


how to run

import Hernandez_Gabriel_riggingTools_cri1_1405
reload (Hernandez_Gabriel_riggingTools_cri1_1405)


'''
import pymel.core as pm
def hierarchy():
	'''
	Gabriel Hernandez

	Hernandez_Gabriel_riggingTools_cri1_1405

	Description:


	how to run

	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.hierarchy()


	'''
	

	

	# User will select the start/root of the chain

	root_joint = 'lt_middle_01_bind'
	second_joint ='lt_middle_02_bind'
	third_joint ='lt_middle_03_bind'

	# pad's the mentioned joint.
		# creates empty group.

	pad = pm.group (name = 'lt_middle_00_pad',empty = True)
	print 'pad created',pad


		# move grouop to to root joint.
			# parent constrain. 

	sam = pm.pointConstraint(root_joint, pad) 
	print "sam created",sam

		# then delet it.
	pm.delete(sam)
	print 'sam killed'

		# freeze transforms.
	pm.makeIdentity(pad, apply=True , t=1, r=1, s=1, n=0)
	print 'freeze transforms'

		# deleted history
	pm.delete(pad,ch=True)
	print 'deleted history'

		# parent root joint to group.
	pm.parent(root_joint, pad)
	print 'pad created'


	# Create local orientated control for each joint
		
		# lt_middle_01_bind,
		#created control
	control_icon_1 = pm.circle(name ='lt_middle_01_icon',normal =[1,0,0])[0]
	print'crtl 1 created'

		#create group for control
	local = pm.group(name='lt_middle_01_local')
	print 'group1 created', local
		#move it to place 
	sam = pm.parentConstraint (root_joint,local)
	print 'sam created'
		#killed the constrain
	pm.delete(sam)
	print "sam killed"
		# freeze transforms.
	pm.makeIdentity(control_icon_1, apply=True , t=1, r=1, s=1, n=0)
	print 'freeze transforms'
		#delte history
	pm.delete(control_icon_1,ch=True)
	print "hist delete"
		#Orient constrain the group ()
	pm.orientConstraint(control_icon_1,root_joint)
	print 'group orientated'

		#lt_middle_02_bind  second_joint
			#created control
	control_icon_2 = pm.circle(name ='lt_middle_02_icon', normal =[1,0,0] )[0]
	print'crtl 2 created'

		#create group for control
	local2 = pm.group(name='lt_middle_02_local')
	print 'group2 created', local
		#move it to place 
	sam = pm.parentConstraint (second_joint,local2)
	print 'sam created'
		#killed the constrain
	pm.delete(sam)
	print "sam killed"
		# freeze transforms.
	pm.makeIdentity(control_icon_2, apply=True , t=1, r=1, s=1, n=0)
	print 'freeze transforms'
		#delte history
	pm.delete(control_icon_2,ch=True)
	print "hist delete"
		#Orient constrain the group ()
	pm.orientConstraint(control_icon_2,second_joint)
	print 'group orientated'



		#lt_middle_03_bind third_joint
			#created control
	control_icon_3 = pm.circle(name ='lt_middle_03_icon' ,normal =[1,0,0])[0]
	print'crtl 1 created'

		#create group for control
	local3 = pm.group(name='lt_middle_03_local')
	print 'group1 created', local
		#move it to place 
	sam = pm.parentConstraint (third_joint,local3)
	print 'sam created'
		#killed the constrain
	pm.delete(sam)
	print "sam killed"
		# freeze transforms.
	pm.makeIdentity(control_icon_3, apply=True , t=1, r=1, s=1, n=0)
	print 'freeze transforms'
		#delte history
	pm.delete(control_icon_3,ch=True)
	print "hist delete"
		#Orient constrain the group ()
	pm.orientConstraint(control_icon_3,third_joint)
	print 'group orientated'


	#parent group 3 to 2
	pm.parent(local3,control_icon_2)
	print '3-2 parent'
	#parent group 2 to 1 
	pm.parent(local2,control_icon_1)
	print '2-1 parent'
	pm.select("*_icon")
	Icon_selected = pm.ls(selection=True)

	for icon in Icon_selected:

		#lock and hide transforms
		icon.tx.set(lock= True,keyable=False)
		icon.ty.set(lock= True,keyable=False)
		icon.tz.set(lock= True,keyable=False)
		icon.sx.set(lock= True,keyable=False)
		icon.sy.set(lock= True,keyable=False)
		icon.sz.set(lock= True,keyable=False)
		icon.v.set(lock= True,keyable=False)
		print "icont  t,s,v lock and hiden",icon


def priming():
	'''
	Gabriel Hernandez
	Description:
	priming tool, by selecting a target joint this tool will create a icon  that will have a pad and will control the joint.
	reload(Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.priming()
	'''
	#allow section possible
	selected = pm.ls(selection= True)
	print "selected",selected

	for joint in selected:
		#create icon 
		icon=pm.circle(radius=2.2, normal=[1,0,0])[0]
		print 'icon created'
		#create pad for icon
		pad=pm.group(empty=True)
		print 'pad created',pad

		#place icon in to pad
		pm.parent(icon,pad)
		print "icon in pad"

		#snap group to selected
		sam= pm.parentConstraint(joint,pad)
		print 'sam created',sam

		#delte constrain
		pm.delete(sam)
		print 'sam killed'

		#fr transforms for icon 
		pm.makeIdentity(icon,apply=True , t=1, r=1, s=1, n=0)
		print "fr trnasformation icon"

		#rename pad
		name_pad= joint.replace('bind','void')
		pad.rename(name_pad)

		#rename icon
		name_icon= joint.replace('bind','icon')
		icon.rename(name_icon)

		#delete history for icon
		pm.delete(icon,ch=True)
		print 'history deleted icon'
		#orientconstraint icon to joint
		final=pm.orientConstraint(icon,joint)
		print 'control created'
	
def padding():
	'''
	Gabriel Hernandez
	Hernandez_Gabriel_riggingTools_cri1_1405

	Description:
	Padding tool, by selecting a target this tool will create a pad for it.


	How to run:
	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.padding()

	'''
	#make selection possible

	selection= pm.ls(selection=True)
	#first selcted s the rootjoint
	root= selection[0]
	print "selected", root

	#create group
	pad=pm.group(empty=True)
	print 'pad created',pad
	#snap group to root
	sam= pm.parentConstraint(root,pad)
	print 'sam created',sam
	#delte constrain
	pm.delete(sam)
	print 'sam killed'
	#fr transforms
	pm.makeIdentity(pad,apply=True , t=1, r=1, s=1, n=0)
	print "fr trnasformation"
	#rename pad
	name= root.replace('bind','pad')
	pad.rename(name)
	#delete history
	pm.delete(pad,ch=True)
	print 'history deleted'
	#place root in to pad
	pm.parent(root,pad)
	print "pad created"

def joint_rename():
	'''

	Gabriel Hernandez

	Hernandez_Gabriel_riggingTools_cri1_1405

	Description:
	Rename joint tool, by selecting the root of a joint chaint the tool will rename the whole chain based on the given  orientation and  name.

	how to run

	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.joint_rename()


	'''

	#makes selection possible

	selection=pm.ls(selection=True,dag=True)
	print 'item selected', selection

	# define name imputs "ori_name_count_sufix"

	ori=raw_input()
	name= raw_input()
	count= 1
	sufix= 'bind'

	#for loop  
	for joint in selection:
		
		#rename, given the past  possible imputs 

		new_name = '{0}_{1}_0{2}_{3}'.format(ori,name,count,sufix)
		count=count + 1

		joint.rename(new_name)


		
	new_name = '{0}_{1}_0{2}_{3}'.format(ori,name,count-1,'end')
	print 'joint name', new_name
	joint.rename(new_name)

	print 'joint chain renamed'

def color_icons():
	'''
	Gabriel Hernandez
	Hernandez_Gabriel_riggingTools_cri1_1405
	Description:
	upont given a orientation of the icon it willcolor it a specific color


	IMPORTANT: 
		icons must have their name "_icon"
		left icons must have "lt" in their name
		right icons must have "rt_" in their name
		cetered icons  must have "ct_" in their name


	How to run:
	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.color_icons()

	'''

	pm.select("*_icon")
	Icon_selected = pm.ls(selection=True)

	for icon in Icon_selected:
	    pm.setAttr(icon+".overrideEnabled",1)
	    if icon.find("lt_")  !=-1 :
	        pm.setAttr(icon+".overrideColor",6)
	    elif icon.find('rt_') !=-1:
	        pm.setAttr(icon+".overrideColor",13)
	    elif icon.find('ct_') !=-1:
	        pm.setAttr(icon+".overrideColor",22)      
	    else: 
	        print "nope"
	    print "Icon colored",icon    

def Lock_hide_tsv():
	'''
	Gabriel Hernandez
	Hernandez_Gabriel_riggingTools_cri1_1405

	Description:
	tool will lock and hide the transforms, scales and v of the selection

	How to run:
	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.Lock_hide_tsv()

	'''
	#allow section possible
	selected = pm.ls(selection= True)
	print "selected",selected

	#forloop
	for icon in selected:

		#lock and hide transforms
		icon.tx.set(lock= True,keyable=False)
		icon.ty.set(lock= True,keyable=False)
		icon.tz.set(lock= True,keyable=False)
		icon.sx.set(lock= True,keyable=False)
		icon.sy.set(lock= True,keyable=False)
		icon.sz.set(lock= True,keyable=False)
		icon.v.set(lock= True,keyable=False)
		print "icont  t,s,v lock and hiden",icon

def Lock_hide_rsv():
	'''
	Gabriel Hernandez
	Hernandez_Gabriel_riggingTools_cri1_1405

	Description:
	tool will lock and hide the rotations, scales and v of the selection

	How to run:
	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.Lock_hide_rsv()

	'''
	#allow section possible
	selected = pm.ls(selection= True)
	print "selected",selected

	#forloop
	for icon in selected:

		#lock and hide transforms
		icon.rx.set(lock= True,keyable=False)
		icon.ry.set(lock= True,keyable=False)
		icon.rz.set(lock= True,keyable=False)
		icon.sx.set(lock= True,keyable=False)
		icon.sy.set(lock= True,keyable=False)
		icon.sz.set(lock= True,keyable=False)
		icon.v.set(lock= True,keyable=False)
		print "icont  r,s,v lock and hiden",icon

def Lock_hide_sv():
	'''
	Gabriel Hernandez
	Hernandez_Gabriel_riggingTools_cri1_1405

	Description:
	tool will lock and hide the scales and v of the selection

	How to run:
	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.Lock_hide_sv()

	'''
	#allow section possible
	selected = pm.ls(selection= True)
	print "selected",selected

	#forloop
	for icon in selected:
		icon.sx.set(lock= True,keyable=False)
		icon.sy.set(lock= True,keyable=False)
		icon.sz.set(lock= True,keyable=False)
		icon.v.set(lock= True,keyable=False)
		print "icont  s,v lock and hiden",icon

def Unlock_show_trsv():
	'''
	Gabriel Hernandez
	Hernandez_Gabriel_riggingTools_cri1_1405
	Description:
	tool will unlock and show the scales and v of the selection

	How to run:
	import Hernandez_Gabriel_riggingTools_cri1_1405
	reload (Hernandez_Gabriel_riggingTools_cri1_1405)
	Hernandez_Gabriel_riggingTools_cri1_1405.Unlock_show_trsv()

	'''
	#allow section possible
	selected = pm.ls(selection= True)
	print "selected",selected

	#forloop
	for icon in selected:
		icon.tx.set(lock= False,keyable=True)
		icon.ty.set(lock= False,keyable=True)
		icon.tz.set(lock= False,keyable=True)
		icon.rx.set(lock= False,keyable=True)
		icon.ry.set(lock= False,keyable=True)
		icon.rz.set(lock= False,keyable=True)
		icon.sx.set(lock= False,keyable=True)
		icon.sy.set(lock= False,keyable=True)
		icon.sz.set(lock= False,keyable=True)
		icon.v.set(lock= False,keyable=True)
		print "icont t,r,s,v unlock and reveal",icon


print 'Tools loaded'