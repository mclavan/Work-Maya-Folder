'''
Steffan Lones
rigging_tools.py 

Description:
4 functions:
	Padding tool - add pads to joints 
	Renaming tool - renames joints and controls
	priming tool - creates locally oriented icons for each joint
	heiarchy
Intended to be used to set up a joint system

how to run:
import rigging_tools.py
reload(rigging_tools.py)
'''
import pymel.core as pm 


def joint_rename():
	'''
	#create a function called jointrename
	#select the root joint and loop through all joint in the chain
	# ori_name_count_suffix
	# ct_back_01_bind
	'''
	#build new name
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	#get all joints in chain
	joint_chain = pm.ls(selection = True, dag = True)

	for current_joint in joint_chain:
		new_name = '{0}_{01}_0{02}_{03}'.format(ori, name, count, suffix)
		count = count + 1
		current_joint.rename(new_name)
		print new_name
	new_name = '{0}_{01}_0{02}_{03}'.format(ori, name, count-1, 'waste')
	current_joint.rename(new_name)

def priming_tool():
	'''
	the user is going to select a target joint.
	The tool will then create a control located on the target joint

	how to run:
	import rigging_tools.py
	reload(rigging_tools.py)
	rigging_tools.priming_tool()
	'''

	# Get selected

	selected = pm.ls(selection = True, dag=True)
	#root_joint = selected[0]

	last_control = ''

	# create control
	for joint in selected:
		#rename
		control_name = joint.replace('bind', 'icon')
		pad_name = joint.replace('bind','local')

		#create icon
		control = pm.circle(normal = [1,0,0], radius = 1.8, name = control_name)[0]

		#group icon
		local_pad = pm.group(name = pad_name)

		# move and orient control
		# use a parent constraint to move control to joint
		temp = pm.parentConstraint(joint,local_pad)
		# constraint is no longer needed	
		# delete constraint
		pm.delete(temp)

		# orient constrain that stuff
		pm.orientConstraint(control,joint)

		#parent pads to controls
		if last_control != '':
			pm.parent(local_pad,last_control)
		last_control = control

def padding_tool():
	'''
	How to run:
		import rigging_tools.py
		reload(rigging_tools.py)
		rigging_tools.padding_tool()

	Description:
		To add a pad to the root joint and rename appropriately

	'''
	#get selection
	selected = pm.ls(selection=True)

	root_joint = selected[0]

	# create empty group
	pad = pm.group(empty=True)

	# move the group over to joint
	temp = pm.pointConstraint(root_joint,pad)

	#delete constraint
	pm.delete(temp)

	#freeze transforms on group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#parent joint to group
	pm.parent(root_joint,pad)

	#renaming 
	pad_name = root_joint.replace('01_bind','00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def hierarchy():
	'''
	how to run: 
		import rigging_tools
		reload(rigging_tools)
		rigging_tools.hierarchy()
	'''

	import pymel.core as pm 
	print 'Hierarchy Generated'

	# The user will select the root joint and the tool will apply the systems
	root_joint = 'lt_middle_01_bind'
	second_joint = 'lt_middle_02_bind'
	third_joint = 'lt_middle_03_bind'

	# create and empty group
	pad = pm.group(empty=True , name = 'lt_middle_01_pad')
	print 'Root Pad Created:' , pad

	# 	move group to root joint
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
	# delete history
	pm.delete(ch=True)
	# create group (NOT EMPTY)
	root_local = pm.group(name = 'lt_middle_01_local')
	# create parent constraint to move to joint
	#	driver is joint driven is group
	#	offset is off
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

####################################################################################################

'''
Steffan Lones

Icon Color
Iconcolor.py 

Description:
	To change color of icons and controls in Maya.

How to run:
	import rigging_tools
	repload(rigging_tools)
	rigging_tools.iconColor()

'''

def iconColor():
	'''
	Description:
	To change color of icons and controls in Maya.

	How to run:
	import rigging_tools
	repload(rigging_tools)
	rigging_tools.iconColor()
	'''

	# get selection
	selection = pm.ls(selection = True , dag = True)

	#get input
	window = pm.window(title = 'icon color:' , mxb = False , mnb = False , sizeable = False)
	pm.columnLayout( columnAttach=('both', 5), rowSpacing=5, columnWidth=100 )
	pm.text(label = 'Is the Icon:')
	centerB = pm.button(label = 'center' , bgc = [1,1,0] , command = center)
	rightB = pm.button(label = 'right' , bgc = [1,0,0] , command = right)
	leftB = pm.button(label = 'left' , bgc = [0,0,1] , command  = left)
	pm.showWindow(window)

def center(*args):
	selection = selection = pm.ls(selection = True , dag = True)
	for icon in selection:
		icon.overrideEnabled.set(1)
		icon.overrideColor.set(17)

def right(*args):
	selection = pm.ls(selection = True , dag = True)
	for icon in selection:
		icon.overrideEnabled.set(1)
		icon.overrideColor.set(13)

def left(*args):
	selection = pm.ls(selection = True , dag = True)
	for icon in selection:
		icon.overrideEnabled.set(1)
		icon.overrideColor.set(6)

		



###
'''
Steffan Lones
attributeShower.py 

Description: 
	To show hidden attributes and to unlock them:
	To hide and lock attributes based on user input.

how to run:
	import rigging_tools
	reload(rigging_tools)
	rigging_tools.UI()
'''

def UI():

	#get selection

	selection = pm.ls(selection = True , dag = True)

	#make window/UI

	#make buttons have commands

	window = pm.window(title = 'Show or Hide Attributes', w = 275 , h = 65, mxb = False , mnb = False , sizeable = False)

	layout = pm.formLayout()

	transCB = pm.checkBox( 'transCB' , label='Translate')
	rotCB = pm.checkBox( 'rotCB' , label='Rotate' )
	scaleCB = pm.checkBox( 'scaleCB' , label='Scale' )
	vCB = pm.checkBox( 'vCB' ,  label='Visibility' )
	show = pm.button (label = 'Show' , command = showing , w = 80)
	hide = pm.button (label = 'Hide', command = hiding , w = 80)
	close = pm.button (label = 'Close', command =('pm.deleteUI(\"' + window + '\", window=True)') , w = 80)

	# lay out the buttons and checkboxes

	pm.formLayout(layout, edit = True, af = [(transCB, "left" , 10) , (transCB, "top" , 10 )])
	pm.formLayout(layout, edit = True, af = [(rotCB, "left" , 85) , (rotCB, "top" , 10 )])
	pm.formLayout(layout, edit = True, af = [(scaleCB, "right" , 77) , (scaleCB, "top" , 10 )])
	pm.formLayout(layout, edit = True, af = [(vCB, "right" , 5) , (vCB, "top" , 10 )])
	pm.formLayout(layout, edit = True, af = [(show, "left" , 10) , (show, "top" , 35 )])
	pm.formLayout(layout, edit = True, af = [(hide, "left" , 100) , (hide, "top" , 35 )])
	pm.formLayout(layout, edit = True, af = [(close, "right" , 5) , (close, "top" , 35 )])

	pm.showWindow( window )


def hiding(*args):

	#what happens if they click hide?

	transCB = pm.checkBox('transCB' , q = True , v = True)
	rotCB = pm.checkBox('rotCB' , q = True , v = True)
	scaleCB = pm.checkBox('scaleCB' , q = True , v = True)
	vCB = pm.checkBox('vCB' , q = True , v = True)
	selection = pm.ls(selection = True , dag = True)

	#hide translate
	if transCB == True:

		for item in selection:
			pm.setAttr(".tx" , lock=True , keyable=False)
			pm.setAttr(".ty" , lock=True , keyable=False)
			pm.setAttr(".tz" , lock=True , keyable=False)

	#hide rotate

	if rotCB == True:

		for item in selection:
			pm.setAttr(".rx" , lock=True , keyable=False)
			pm.setAttr(".ry" , lock=True , keyable=False)
			pm.setAttr(".rz" , lock=True , keyable=False)

	#hide scale

	if scaleCB == True:

		for item in selection:
			pm.setAttr(".sx" , lock=True , keyable=False)
			pm.setAttr(".sy" , lock=True , keyable=False)
			pm.setAttr(".sz" , lock=True , keyable=False)

	#hide visibility

	if vCB == True:

		for item in selection:
			pm.setAttr(".v" , lock = True , keyable = False)
 		
def showing(*args):

	#what if they click show?

	transCB = pm.checkBox('transCB' , q = True , v = True)
	rotCB = pm.checkBox('rotCB' , q = True , v = True)
	scaleCB = pm.checkBox('scaleCB' , q = True , v = True)
	vCB = pm.checkBox('vCB' , q = True , v = True)
	selection = pm.ls(selection = True , dag = True)

	#show translate

	if transCB == True:

		for item in selection:
			pm.setAttr(".tx" , lock=False , keyable=True)
			pm.setAttr(".ty" , lock=False , keyable=True)
			pm.setAttr(".tz" , lock=False , keyable=True)

	#show rotation
	if rotCB == True:

		for item in selection:
			pm.setAttr(".rx" , lock=False , keyable=True)
			pm.setAttr(".ry" , lock=False , keyable=True)
			pm.setAttr(".rz" , lock=False , keyable=True)

	#show scale

	if scaleCB == True:

		for item in selection:
			pm.setAttr(".sx" , lock=False , keyable=True)
			pm.setAttr(".sy" , lock=False , keyable=True)
			pm.setAttr(".sz" , lock=False , keyable=True)

	#show visibility
	if vCB == True:

		for item in selection:
			pm.setAttr(".v" , lock = False , keyable = True)

def renameTool():
	"loads renaming tool with prefix, suffix, and find and replace"
	import renameTool
	reload(renameTool)
	renameTool.UI()
