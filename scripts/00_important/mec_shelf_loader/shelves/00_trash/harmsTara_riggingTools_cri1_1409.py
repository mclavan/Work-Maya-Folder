'''
Tara Harms
harmsTara_riggingTools_cri1_1409.py

Description: 
	A group of rigging related rigging tools.

How to Run:
	import harmsTara_riggingTools_cri1_1409
	reload(harmsTara_riggingTools_cri1_1409)

'''

print 'Rigging Tools Active'

import pymel.core as pm 

'''
BASIC TOOLS 
	These tools will make common rigging trials easier 
	and quicker to set-up.
'''

def snapping_tool():
	'''
	Description:
		This tool moves the first selected object to the second.
		It translates and rotates the target object.

	How to use:
		Select first object (ex: joint_01), 
		then shift select next object (ex: control_icon_01).
		Next run tool in script editor.



	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.snapping_tool()

	'''


 	selected = pm.ls(selection=True)
 	print 'Selected: {0}'.format(selected)


 	#By Default commands work on selected.
 	Peach = pm.parentConstraint(selected [0], selected[1])
	pm.delete(Peach)

 	print 'The first selected object was moved to the second.'

def point_snapping_tool():
	'''
	Description:
		This tool moves the first selected object to the second.
		It translates the target object.

	How to use:
		

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.point_snapping_tool


	'''


	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)


	#By Default commands work on selected.
	Peach = pm.parentConstraint(selected [0], selected[1])
	pm.delete(Peach)

	print 'The first selected object was moved to the second.'

def world_icon():
	'''
	Description:
		This tool creates a world-oriented control (no pad above it) 
		and moves it to a selected joint.

	How to use:
		select a joint and run the tool.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload (harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.world_icon()
		
	'''
	#Get selected

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	first_joint = selected[0]

	#Create a control icon.
	control_icon_1 = pm.circle(normal=[0, 1, 0], radius=2) [0]

	#Move the control to the target joint.
	#Delete the constraint.

	Bowser = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(Bowser)

	print 'Icons Created.'

def lock_and_hide():

	'''
	Description:
		This tool locks and hides all channels except the rotate channel.

	How to use:
		First select control icon and then run command.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload (harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.lock_and_hide()
	'''
	selected = pm.ls(selection=True)
	first_selected = selected [0]

	first_selected.tx.set(lock=True, keyable=False)
	first_selected.ty.set(lock=True, keyable=False)
	first_selected.tz.set(lock=True, keyable=False)
	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)
	first_selected.v.set(lock=True, keyable=False)

	print 'First selected object has all channels locked and hidden.'

def unlock_and_show():
	'''
	Description:
		Makes all the channels of the selected unlocked and keyable.

	How to use:
		To unlock desired channels, first select the object 
		whose channels have been locked and hidden. Next run the tool.
		All channels should now be visible again. 

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.unlock_and_show()

	'''

	selected = pm.ls(selection=True)
	first_selected = selected [0]

	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)

	print 'First selected object has all channels shown.'

def hierarchy():
	'''
	Description:
		Create a hierarchy based upon a given system.

	How to use:
		Select the root joint chain and execute function

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.hierarchy()

	'''
	#Input
	#We are working on the root joint.

	joint_system = pm.ls(selection=True, dag=True)

	#print 'Joint System:', joint_system

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]

	'''
	Padding Root Joint
	'''

	# Create an empty group
	root_pad = pm.group(empty=True)

	# Move the group over to the target joint.
	temp_constraint = pm.pointConstraint(root_joint, root_pad)
	pm.delete(temp_constraint)

	# Freeze transforms on group.
	pm.makeIdentity(root_pad, apply=True, t=1, r=1, s=1, n=0)

	# Parent root joint to the group.
	pm.parent(root_joint, root_pad)

	'''
	Local Controls
	'''

	'''
	Control 1 - root_joint
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_1 = pm.circle(normal=[1, 0, 0], radius=2)[0]
	# Create a group.
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad.
	print 'Control 1 created:', control_icon_1
	print 'Local Pad 1 created:', local_pad_1



	# Move group over to the target joint.
	# Delete Constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(root_joint, local_pad_1)
	pm.delete(temp_constraint)
	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_1, root_joint)
	# Driver -> Driven
	# Control -> Joint

	'''
	Control 2
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]
	# Create a group.
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad.
	print 'Control 2 created:', control_icon_2
	print 'Local Pad 2 created:', local_pad_2



	# Move group over to the target joint.
	# Delete Constraint after snapping.
	# Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_2, local_pad_2)
	pm.delete(temp_constraint)
	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_2, joint_2)
	# Driver -> Driven
	# Control -> Joint

	'''
	Control 3
	'''
	# Create a control
	# normal=[1,0,0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]
	# Create a group.
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad.
	print 'Control 3 created:', control_icon_3
	print 'Local Pad 3 created:', local_pad_3



	#Move group over to the target joint.
	#Delete Constraint after snapping.
	#Driver: joint
	# Driven: group
	temp_constraint = pm.parentConstraint(joint_3, local_pad_3)
	pm.delete(temp_constraint)
	# Orient Constrain the joint to the control.
	pm.orientConstraint(control_icon_3, joint_3)
	# Driver -> Driven
	#Control -> Joint

	'''
	Parent controls together
	'''
	# Pad 3 (last) -> control 2
	pm.parent(local_pad_3, control_icon_2)
	pm.parent(local_pad_2, control_icon_1)

	hierarchy_group1 = local_pad_1
	hierarchy_group2 = local_pad_2


	print 'hierarchy created'

def padding_tool():

	'''
	Description:
		Creates a group that is snapped to root joint, has transforms frozen, joints parented under 
		the pad and is renamed to match joint system.

	How to use:
		Click on root joint and run command.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload (harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.padding_tool()

	'''

	selected = pm.ls(selection=True)
	# print 'Current Selected:' selected
	root_joint = selected[0]

	#Create empty group
	#empty=True will create an empty group.
	pad = pm.group(empty=True)
	#Move group to joint
	#Delete Constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)
	#Freeze Transforms on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s =1, n=0)
	#Parent joint to group
	pm.parent(root_joint, pad)

	#Renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def finger_attributes():
	
	'''
	Description:
		This tool will create attributes for the fingers without needing 
		to tediously add them manually through the 'Add Attribute' window. 

	How to use: 
		Select the control you are wanting to add attributes to. 
		Run the tool and then you will see new attributes added to the channel box.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.finger_attributes()

	'''

	import pymel.core as pm
	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	#addAttr
	# attribute_name = raw_input()
	# first_selected.addAttr(attribute_name,keyable=True)


	#Creating Separator Attributes

	import pymel.core as pm

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected

	first_selected = selected[0]

	#addAttr
	# attribute_name = raw_input()
	# first_selected.addAttr(attribute_name, at='enum', en='---------', keyable=True)

	first_selected.addAttr('FINGERS', at='enum', en='---------', keyable=True)
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', at='enum', en='---------', keyable=True)
	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	print 'finger attributes created.'

def joint_renamer():

	'''
	Description:
		This tool renames a selected joint chain.

	How to use. 
			Select a root joint and run the function.
			The script will prompt you first to change the orientation and the name of 
			the system ('arm', 'back', 'leg')

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.joint_renamer()

	'''
	#lists
	import pymel.core as pm

	#Select the root joints and Ii will get its children.
	joint_chain = pm.ls(selection=True, dag=True)

	#Do not worry about the waste suffix.
	#ori_name_count_suffix
	#lt_arm_01_bind

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current in joint_chain:
	    new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)
	    
	    # Rename Command
	    #Variable.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1
    

    
    
	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)

	# Rename Command
	#Variable.rename(new_name)
	current.rename(new_name)

	print 'joints renamed.'

def priming_tool():

	'''
	Description:
		This tool creates an icon on top of a selected joint. 
		Icon is renamed, parented to joint, grouped in a local pad, and renamed.

	How to use:
		Select joint first the run command.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload (harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.priming_tool()

	'''

	# Get selected.
	selected = pm.ls(selection=True)
	# target_joint = selected[0]
	
	for target_joint in selected:
		control_icon_name = target_joint.replace('_bind', '_icon')
		local_pad_name = target_joint.replace('_bind', '_local ')

		# Create a control
		# normal set to x and radius is 2
		control_icon = pm.circle(normal=[1, 0, 0], radius=2,
				name=control_icon_name)[0]
		
		# Group control (not and empty group)
		local_pad = pm.group(name=local_pad_name)

		print 'Control Icon:', control_icon
		print 'Pad Created:', local_pad

		# Move group to target joint.
		# Delete Constraint.

		temp_constraint = pm.parentConstraint(target_joint, local_pad)
		pm.delete(temp_constraint)

		#Orient Constraint joint to the control.
		pm.orientConstraint(control_icon, target_joint)


	print 'Local oriented controls created.'   

def hide_polygons():
	
	'''
	Description:
		This is a double-click function.
		This tool hides all geometry in the scene for the perspective window only.
		Once you double-click the the button for this tool the geometry will reappear.

	How to use:
		simply run the command and all polygons will be hidden. 
		OR
		click the 'Hide Polygons' button on the shelf.
		Double click 'Hide Polygons' button to show items again.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.hide_polygons()

	'''


	mel_line = 'modelEditor -e -polymeshes false modelPanel4;'
	pm.mel.eval(mel_line)

	#mel_line = 'modelEditor -e -polymeshes true modelPanel4;'
	#pm.mel.eval(mel_line)

	print 'polygons are now hidden'

def freeze_transforms():

	'''
	Description:
		This tool freezes transforms on a selected object.

	How to use:
		Select and object and run command.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.freeze_transforms()

	'''

	pm.makeIdentity(apply=True, t=1, r=1, s =1, n=0)

	print 'transforms have been frozen.'
    
'''
COLORED ICON TOOLS
	These tools will make creating colored icons an easier task.
	In the tools listed we will be using 3 primary colors. but the set up
	instructions will explain how to create new color tools for the future.

	How to use Colored Icon Tools (blue_color, red_color, yellow_color):
	
		setting up colors:
			Make sure that you change this attr. under nurbsCircle1 tab 
			and not the shape tab.
			change icon color by going into 'object display' (inside of attribute editor) 
			going under 'drawing overrides' and checkin off 'enable overrides'.
			Now you can change to desired color.
			Inside of the Attribute Spreadsheet window put 'override' into search bar. 
			This will limit the search. Select the 'All' button to have the color box show up.
			The number of the color you have selected will show up in the color box. 
			That is the number you will use for the code. Each color needs it's own tool 
			for maya to run them.
	
		Switching Colors:
			To change the color of an icon select the icon and then run command for 
			desired color. 
'''

def blue_color():

	'''
	Description:
		Changes color of selected icon to blue.

	How to use:
		First select icon, then run command to change icon's color.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.blue_color()
	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected
	#first_selected.tx

	first_selected = selected[0]

	
	blue = 6
	first_selected.overrideEnabled.set(1)
	first_selected.overrideColor.set(blue)

	print'objects are now blue.'

def red_color():

	'''
		Description:
			Changes color of selected icon to red.

		How to use:
			First select icon, then run command to change icon's color.

		How to run:
			import harmsTara_riggingTools_cri1_1409
			reload(harmsTara_riggingTools_cri1_1409)
			harmsTara_riggingTools_cri1_1409.red_color()
	'''


	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected
	#first_selected.tx

	first_selected = selected[0]

	red = 13
	first_selected.overrideEnabled.set(1)
	first_selected.overrideColor.set(red)

	print'objects are now red.'

def yellow_color():

	'''
		Description:
			Changes color of selected icon to yellow.

		How to use:
			First select icon, then run command to change icon's color.

		How to run:
			import harmsTara_riggingTools_cri1_1409
			reload(harmsTara_riggingTools_cri1_1409)
			harmsTara_riggingTools_cri1_1409.yellow_color()
	'''
	

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected
	#first_selected.tx

	first_selected = selected[0]

	yellow = 17
	first_selected.overrideEnabled.set(1)
	first_selected.overrideColor.set(yellow)

	print'objects are now yellow.'

'''
CONTROL ICON TOOLS
	These are basic shape controls that we can use as different
	icons in the rigging system. Making tools is a simple process: 
	create a control with the 'create curve' tool. Copy and paste
	code generated from the control you created into a sublime document.
	Place '' both in front and behind text to yellow it out. 
	In front of code, write out: 

	mel_line = 'code goes here'
	pm.mel.eval(mel_line)

	This will allow the code to be read in python and now 
	you can run it using sublime or create buttons for the new control.
'''

def cube():

	'''
	Description:
		Creates a cube icon.

	How to use:
		Simply run command and icon will appear

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.cube()

	'''
	mel_line = 'curve -d 1 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'

	pm.mel.eval(mel_line)

	print 'cube icon created.'

def spur():

	'''
	Description:
		Creates a spur shaped icon.

	How to use:
		Simply run command and a spur icon will appear.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.spur()
	'''
	
	mel_line = 'circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand; select -r nurbsCircle1.cv[4] ; select -tgl nurbsCircle1.cv[2] ; select -tgl nurbsCircle1.cv[0] ; select -tgl nurbsCircle1.cv[6] ; scale -ws -r -p 0cm 0cm 0cm 0.0858578 0.0858578 0.0858578; select -cl  ;'

	pm.mel.eval(mel_line)

	print 'spur icon created.'

def arrow():

	'''
	Description:
		Creates an arrow icon.

	How to use:
		Simply run command and an arrow icon will appear.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.arrow()

	'''
	mel_line = 'curve -d 1 -p 0.0756077 0 0.966433 -p 4.092831 0 0.966433 -p 4.092831 0 -1.011989 -p 0.0992828 0 -1.011989 -p 0.0992828 0 -3.005243 -p -3.989385 0 -0.0207857 -p 0.0509349 0 2.996001 -p 0.0509349 0 0.933684 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'

	pm.mel.eval(mel_line)

	print 'arrow icon created.'

def pointer():

	'''
	Description:
		Creates a pointer icon

	How to use:
		Simply run command and pointer icon will appear.

	How to run:
		import harmsTara_riggingTools_cri1_1409
		reload(harmsTara_riggingTools_cri1_1409)
		harmsTara_riggingTools_cri1_1409.pointer()
	'''
	mel_line = 'circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;select -r nurbsCircle1.cv[7] ; move -r 4.075228 0 0 ; select -tgl nurbsCircle1.cv[0] nurbsCircle1.cv[6] ; select -d nurbsCircle1.cv[7] ; ScaleToolWithSnapMarkingMenu;MarkingMenuPopDown;scale -ws -r -p 0.783612cm 0cm 0cm 0.422747 0.422747 0.422747 ;select -cl  ;'

	pm.mel.eval(mel_line)

	print 'pointer icon created.'





























