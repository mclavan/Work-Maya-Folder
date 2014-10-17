###RIGGING TOOLS########
# Shane King Cri1 1405
# Helpful  scripts for rigging.


import pymel.core as pm

# Extra 

def control_renamer():
	#Control Renamer Tool
	# Shane King
	#######INSTRUCTIONS
	# Select control at the top of the hierarchy


	# This script will open two dialog boxes that ask for specific info
	# It will rename all the children of the control you select
	# you must put information for the orientation and system of the control

	import pymel.core as pm

	# get selected
	sel_controls = pm.ls(selection=True, dag=True)

	#create Prompt dialogs for input


	oriName = pm.promptDialog(title = 'Rename Control', message = 'Enter Orientation', button = ['OK', 'Cancel'], defaultButton = 'OK', cancelButton = 'Cancel',)

	if oriName == 'OK':
		oriText = pm.promptDialog(q = True, text = True)

		


	


	systemName = pm.promptDialog(title = 'Rename Control', message = 'Enter System', button = ['OK', 'Cancel'], defaultButton = 'OK', cancelButton = 'Cancel', dismissString = 'Cancel')

	if systemName == 'OK':
			systemText = pm.promptDialog(q = True, text = True)
	    
	   

	# naming convention


	ori = oriText
	system_name = systemText
	count = 1

	suffix = 'icon'



	# loop through the Chain

	for current_controls in sel_controls:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)

		# Create If statements for the prompt Dialog windows,


		# rename

		current_controls.rename(new_name)

		count = count + 1

	print 'Controls Have Been Renamed.'

def ECC():
	# Easy Control Colors Tool
	# Shane King
	# Changes the colors of your Icons based on orientation naming convention
	#### ASSUMPTIONS
	#### 1. The suffix of your controls end with _icon
	##### 2. Your prefix is your orientation


	#### Instructions:
	# Select ONE color at a time by clicking the checkbox.
	### It will not work with more than one color selected at once.

	## next, Enter the naming convention for your orientation
	# Example : "lt", "cnt", "rt"
	# Press the Go! button

	# to close the window , simply press the red x at the upper left corner.



	# import EasyColorControls as ECC
	# reload(ECC)
	#ECC.UI()




	import EasyColorControls as ECC
	reload(ECC)
	ECC.UI()

def defaultControlIcons():

	# default Control Icon Tool
	#Shane King
	# Resets all the translations and rotations for a control icon

	### INSTRUCTIONS
	# you do not need to select anything for this script
	# simply run, and the controls will be reset based apon naming convention
	## Assumptions: suffix is "_icon"

	### If you have translate or rotate locked, it will give you a warning
	# saying that you can not change those attributes
	# this will only change the unlocked attributes

	# select all controls with the naming convention "icon"

	# import RiggingTools as rt
	# reload(rt)
	#rt.defaultControlIcons()

	import pymel.core as pm
	




	controlIcons = pm.ls("*_icon")

	# create a for loop to set attributes for translate, rotate, to zero

	for currentIcons in controlIcons:
		pm.setAttr(currentIcons + '.rx', 0)
		pm.setAttr(currentIcons + '.ry', 0)
		pm.setAttr(currentIcons + '.rz', 0)
		pm.setAttr(currentIcons + '.tx', 0)
		pm.setAttr(currentIcons + '.ty', 0)
		pm.setAttr(currentIcons + '.tz', 0)

def ikfkSystem_Tool():
	##IK FK System Tool
	#Shane King
	## Select root joint of the drive system, and this tool will
		#duplicate the system into two new joints and rename them.

	import ikfkSystem as ifs
	reload(ifs)

def HSL():
	# Hide Show Lock Attributes
	#Shane King
	# This tool Will Hide Show And Lock The Checked Attributes
	# Select the attribute that you want to hide, show, or lock, then press the associated button
	# show button , will show and unlock your attributes.


	import HSL
	reload(HSL)

def hideShowPoly():

	# Hide And Show Poly Tool
	#Shane King


	##INSTRUCTIONS

	#click shelf button and will hide or show poly based apon the current state.



	import pymel.core as pm



	polyhidden = pm.modelEditor('modelPanel4', q = True, pm = True)


	if polyhidden:
		pm.modelEditor('modelPanel4', e = True, pm = False)

	else:
		pm.modelEditor('modelPanel4', e = True, pm = True)

def renamerTool():
	#### Renamer Tool ######
	# Shane King
	#### Renames all of your selection and more!#######
	#Instructions

	# Make your selection
	##Do one part at a time
	## example : Do the prefix, than press accept, than do the suffix , accept, then search and replace, accept
	## doing it in an order of operation will prevent problems.


	import RenamerToolUI as rt
	reload(rt)
	rt.UI()

def ikForLegSystem():


	###### IK System for Leg Tool
	###### Shane King
	###### Creates all the iks needed for the ideal leg system.
	###### Instructions::: Select root joint, then run script.

	import pymel.core as pm

	#Get selected
	selected_joints = pm.ls(selection=True)


	#Get the Root Joint
	root_joint = selected_joints[0]

	#Get the hierarchy
	leg_system = pm.ls(root_joint, dag=True)
	print leg_system

	#Assign variables to Leg System Joints
	ankle_joint = leg_system[2]
	ball_joint = leg_system[3]
	toe_joint = leg_system[4]

	#Create Rotate ikSolver for Root and Ankle

	pm.ikHandle(sj=root_joint, ee=ankle_joint, sol='ikRPsolver')

	#Create SCsolver for Ankle and Ball

	pm.ikHandle(sj=ankle_joint, ee=ball_joint)

	#Create SCsolver for Ball and Toe
	pm.ikHandle(sj=ball_joint, ee=toe_joint)

	#Clear selection
	pm.select(cl=True)




# Four Required Tools
def hierarchy():
	
	#Shane King


	#hierarchy.py

	#Description:

	#How to run:
	#import hierarchy
	#reload(hierarchy)
	
	import pymel.core as pm 
	print 'Hierarchy Generated'

	# The user will select the root joint and the tool will apply the systems.
	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	#    create and empty group
	pad = pm.group(empty=True , name = 'lt_middle_01_pad')
	print 'Root Pad Created:' , pad

	# move group to root joint
	# 	point constrain group to root joint
	temp = pm.pointConstraint(root_joint , pad)
	# 	offset needs to be off (snapping)
	# 	delete constraint
	pm.delete(temp)
	# 	freeze transforms
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	#Delete History
	pm.delete(ch=True)
	# Parent root joint to group
	pm.parent(root_joint , pad)


	# Create a local oriented control for each joint and will pad root joint
	  # lt_middle_01_bind, lt_middle_02_bind , lt_middle_03_bind
	   # Create control
	root_icon = pm.circle(name='lt_middle_01_icon', normal=[1,0,0])[0]
	#   delete history
	pm.delete(ch=True)
	# create group (NOT EMPTY)
	root_local = pm.group(name = 'lt_middle_01_local')
	# create parent constraint to move to joint
	#driver is joint driven is group
	#	    offset is off
	temp = pm.parentConstraint(root_joint, root_local)
	# delete constraint
	pm.delete(temp)
	# orient constraint circle to joint
	pm.orientConstraint(root_icon , root_joint)

	second_icon = pm.circle(name= 'lt_middle_02_icon' , normal=[1,0,0])[0]
	pm.delete(ch=True)
	second_local = pm.group(name= 'lt_middle_02_local')
	temp = pm.parentConstraint(second_joint , second_local)
	pm.delete(temp)
	pm.orientConstraint(second_icon , second_joint)
	pm.parent(second_local , root_icon)

	third_icon = pm.circle(name= 'lt_middle_03_icon' , normal=[1,0,0])[0]
	pm.delete(ch=True)
	third_local = pm.group(name = 'lt_middle_03_local')
	temp = pm.parentConstraint(third_joint,third_local)
	pm.delete(temp)
	pm.orientConstraint(third_icon,third_joint)
	pm.parent(third_local,second_icon)
	pm.select(clear = True)

	middle_group = pm.group(name='lt_middleFinger')
	pm.parent(pad , middle_group)
	pm.parent(root_local , middle_group)

def padding_tool():
	
	#import RiggingTools
	#reload(RiggingTools)
	#RiggingTools.padding_tool
	import pymel.core as pm


	
	selection = pm.ls(selection=True)
	#print "Current Selected: " selection
	root_joint = selection[0]

	#create empty group

	# parent to joint


	# delete contraint

	pad = pm.group(empty = True)

	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# freeze transforms

	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	# parent
	pm.parent(root_joint, pad)

	# renaming

	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created....'

def joint_renamer():
	#Joint Renamer Tool
	#Shane King

	# Practical use of loops.
	#Renaming joint based upon a naming convention.


	# How to Run:

	#import RiggingTools as rt
	#reload(rt)
	#rt.joint_renamer()


	import pymel.core as pm

	# get selected
	joint_chain = pm.ls(selection=True, dag=True)

	# naming convention


	ori = raw_input()
	system_name = raw_input()
	count = 1
	suffix = 'bind'

	

	# loop through the Chain

	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)

		# rename

		current_joint.rename(new_name)

		count = count + 1

	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count-1, 'waste')
	current_joint.rename(new_name)
	print 'Joints Have Been Renamed.'

def priming_tool():
	import pymel.core as pm
	#Local Oriented Control Tool

	#Shane King

	# Select joints, and will automatically create a local pad and control on the selected joints

	#import RiggingTools as rt
	#reload(rt)
	#rt.priming_tool()

	#get selected
	selection = pm.ls(selection=True)

	#target_joint = selected[0]

	for target_joint in selection:

		control_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local')

		#Create control
		#set radious and normal
		control_icon = pm.circle(normal=[1 , 0 , 0], r=1.8, 
			name=control_name)[0]

		#group control
		local_pad = pm.group(name=local_pad_name)


		# move group to target joint
		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		#delete constraint
		pm.delete(temp_constraint)

		#orient constraint joint to control
		pm.orientConstraint(control_icon, target_joint)



#######!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!########

## Drop Down Controls 
# the only drop down is the CTRL ICONS button, custom icon

## I have custom icons that i loaded into my maya icons folder in the directory. 


#### DOUBLE CLICK BUTTONS

#ALL THE CONSTRAINTS, 
# If you double click Maintain offest will be off
# one click maintain offset is on













