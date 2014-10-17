'''
Research Notes

Name:  Nadia Hipolita

# How to add buttons from pull-down menus:
#	Tools can be selected from the pull-down menu, and while they are active, you can middle-mouse the icon on the left bar to the shelf
# 	You can also shift+control+click on the pull-down menu is also another way to add tools.

Current Shelf Tools: A list of tools
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 

# To get double click buttons, right click any button, select open and go to the double click command
# Enter the desired code for the double-click in the box,be sure to select either MEL or python 

Drop Down Menus: 

# To get the drop down buttons, right click any button, select the Popup Menu Items tab
# In the box on the left enter the name of the menu Items
# With the menu item selected enter the code for the function in the box on the right, be sure to select either MEL or Python

'''

'''
Each tool you will need document:
	1) MEL Commmand
	2) What type of command is it and how did you find it?
	3) Convert MEL to Python.
	4) Important Flags
		-explain Flags
'''

'''
General Research and Command Information


# ---------------Researching Code---------------------------
# How to:  
# Go to History - Echo All (this displays all the code Maya uses to run a Command)
# Run the task normally, copy the MEL script
# Use "whatIs" command to find out with script is the command (Do not use Run Time Command)
# Undo is another way to find script
# Make sure to turn of Echo All when done
# Double click any command highlighted in blue to Command Documentation

# ---------------Command Types-------------------------------
# Run time Command:  functions, runs the command after it
# --Only runs on selected objects
# --Good for shelf (one button tasks)
# Command (Maya Command):  the one actually completes the task
# --Will always be lowercase
# --use these the majority of the time
# Mel Procedure: a function performed by a script 
# --Maya shows where this function is located and how it works
# --This is where you would edit the core functions of Maya (this is advanced programming, don't mess with!)

# ---------------MEL to Python--------------------------------
# Always begin with import pymel.core as pm
# Every command in Python begins with pm. 
# pm. command (flag = value OR [list])
# Toggle flags:  No values in Maya but need values in Python, like True 
# --commandName -flag
# Objects are typically listed at the end of the script in Maya, but in Python they come first
# Special Conversions:
# --Python cannot use the same flag twice, so you must create a grouped list
# --Mel commands can also be used in Python with pm.mel.eval, the command would need to be defined first as mel_line = xxxx
# Runtime Commands in Python:  pm.mel.Command()
# Mel Procedures in Python:
# --pm.mel.command like pm.mel.jdsWin()

# ------------Variables-------------------------------------
# Contain data, can only hold one point of information, be descriptive
# name = object
# print name
# joint_1 (name) = 'lt_arm_01_bind' (variable)
# print joint_1 

# -----------Flags------------------------------------------
# Provides information about the attributes/objects of a command
# Order not important

# ------------Selection-------------------------------------
# Use the pm.ls to select all the objects in a scene.  To get a the specific number of objects in a scene use len(pm.ls()).  Make sure to use print function to see info.
# to get a hierarchy of joints within a scene use selected_objects = pm.ls(selection=True); variable_name_low(lower heirarchy) = selected_objects[0]; variable_name(upper heirarchy) = pm.ls(varible_name_low, dag=True)
# print 'System Name:', selected
# Getting specific objects in a scene use binding_joints = pm.ls('*_bind'); print 'Binding Joints:' binding_joint (Can be used with other suffix names, which is why naming is SO IMPORTANT)
# Use the naming convention to retreive root_systems = pm.ls('*_01_bind'); print 'Joint Systems:', root_systems

# ------------Functions------------------------------------
# Breaks code into pieces so individual segments can be retrieved
# To make a function use def code_name(): and press enter (make sure text under it is tabbed in)
# use help(code_name) to find information about code

# ------------Loops----------------------------------------
# loops are used to expand code to how many objects need to be affected by it.  So instead of being limited to a 3 joint system, the code can affect 2 to 200 joints.
# How to use Loops
# for variable(1) in list: (hit enter, needs to be tabbed under)
# Can be used to generally rename objects


'''

# Freeze Transforms
# Appears with FreezeTransformations (0), run time command, and peformFreezeTransformations (0), MEL procedure.
# I used Command Documentation to find the definitions.
# Maya Code:
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1
# Python Code:
pm.makeIdentity (apply = True, t=1, r=1, s=1, n=0, pn=1)

# -------------Flags-----------------------
apply (a) - default is False, when true the transformations are applied to the shape after transformations are made identity
translate (t) - if true, then only translation is applied to shape and it will be 0,0,0.
rotate (r) - if true, then only rotation will be applied to the shape and it will be 0,0,0.
scale (s) - if true, only scale is applied to shape and it will be 0,0,0.
normal (n) - default is to set to not freeze normals.
preserveNormals - if true normals will be reverese if object is negatively scaled.


# Delete History
# Appears with DeleteHistory, run time command
# I used pm.mel.whatIs to find the command and the Command Documentation
# Maya Command:
delete -all -constructionHistory
# Python Command:
pm.delete(all=True, constructionHistory=True)

# --------------Flags-------------------------------
all(all) - Remove all objects of specified kind, used in conjunction with the following flags.
constructionHistory (ch) - remove the construction history on a objects specified or selected
attribute (at) - list of attributes to selected
hierarchy (hi) - hierarchy expansion options
controlPoints (cp) - explicity specifies whether or not to include the control points of a shape
staticChannels (sc) - remove static animation channels from the scene

# Center Pivot
# Appears as (with Echo All) CenterPivot (Run time Command); xform -cp (command)
# Maya command: 
xform -cp
# Python command:
pm.xform(centerPivots=True) 

# ----------Flags------------------------------------
centerPivots (cp) - centers the pivot of selected object 

# Single Chain and Rotate Plan IKs
# Single Chain IK 
# Appears as ikHandle 
# To create a complete code you will need to define variables and set list

# Single Chain (SC) IK:
# Maya Command:
ikHandle(startJoint='joint1', endEffector='joint5')
# Python Command:
pm.ikHandle(startJoint='joint1', endEffector='joint5')

# Rotate Plane (RP) IK:
# Maya Command:
ikHandle(sol=ikRPsolver, startJoint='joint1', endEffector='joint5')

# Python Command:
pm.ikHandle(sol=ikRPsolver, startJoint='joint1', endEffector='joint5')


# When you use selected:

# Single Chain (SC) IK:
# Maya Command:
ikHandle
# Python Command:
pm.ikHandle()

# Rotate Plane (RP) IK:
# Maya Code:
ikHandle -sol -ikRPsolver
# Python Code:
pm.ikHandle (sol='ikRPsolver')

# -----------------Flags------------------
startJoint (sj) - the joint beginning the IK
endEffector (ee) - the joint at the end of the IK
solver(sol) - sets that a particular type of IK will be used, like ikRPsolver, ikSCsolver, ikSplineSolver



# Cluster
# Appears as (with Echo all) cluster(command)
# Maya Code:
cluster 
# Python Code:
pm.cluster 

# ---------------Notes----------------------
# cluster is used with a string
# You can name the clusters and use a flag to identity specific joints on which to put he cluster


# Grouping (Does not need to be included on Shelf!)
pm.group()

# Grouping by default parents selected objects in the scene.
# In this example the son would be the top node.
pm.group(name='son')
pm.group(name='father')
pm.group(name='grandFather')


# Empty groups can be created too.
pm.group(name='son',empty=True)
pm.group(name='grandFather', empty=True)
pm.group(name='father', empty=True)

# ---------Flags-----------------
name(n) - names the group.
empty(em) - creates an empty group.



# Parenting (Does not need to be included on Shelf!)
# Maya Code:
parent (child, parent)
# Python Code:
pm.parent(child, parent)

# -------Notes-------------------
# This code will have to be run twice to parent multiple objects to each other
# 'child' and 'parent' are variables, you can define them with selected or specificed names


# Duplicating (Does not need to be included on Shelf!)
# Appears as Duplicate (run time command); performDuplicate false (MEL procedure); duplicate -rr (command);
# Maya Code:
duplicate
# Python Code:
pm.duplicate()

# ------Flags----------------------------
returnRootsOnly (rr) - returns only the root nodes of heirarchy
# How to duplicate a group:
pm.duplicate('group1')
smartTransform (st) - remembers the transformations and duplicates in along those lines



'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
pm.circle()
#Control is facing the y-axis.  Good for FK back controls.  World oriented.
pm.circle(normal=[0,1,0])

# Control is facing the x-axis.  Good for local oriented controls.
pm.circle(normal=[1,0,0])

# ----------Flags-----------
normal - Direction of the control.
radius - Size of the control.
sections - How many sectiosn the control has. 

# Square
pm.circle(degree=1, sections=4)

# -------Flags---------------
degree(d) = Two main values, linear=1 and cubic=3
sections(s) = Four points make a square
normal(n) = Normal flag works just like the normal circle command.

# Cube
# The curve command creates cv curves.  A curve was used in Linear to create the cube shape.
# Maya Code
curve -d 1 -p -1.049712 0.748059 -1.019445 -p -1.049712 0.748059 1.019445 -p -1.049712 -0.748059 1.019445 -p -1.049712 -0.748059 -1.019445 -p -1.049712 0.748059 -1.019445 -p 1.049712 0.748059 -1.019445 -p 1.049712 -0.748059 -1.019445 -p -1.049712 -0.748059 -1.019445 -p -1.049712 0.748059 -1.019445 -p 1.049712 0.748059 -1.019445 -p 1.049712 0.748059 1.019445 -p 1.049712 -0.748059 1.019445 -p 1.049712 -0.748059 -1.019445 -p 1.049712 0.748059 -1.019445 -p 1.049712 0.748059 1.019445 -p -1.049712 0.748059 1.019445 -p -1.049712 -0.748059 1.019445 -p 1.049712 -0.748059 1.019445 -p 1.049712 0.748059 1.019445 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 ;

# Python Code
mel_line='curve -d 1 -p -1.049712 0.748059 -1.019445 -p -1.049712 0.748059 1.019445 -p -1.049712 -0.748059 1.019445 -p -1.049712 -0.748059 -1.019445 -p -1.049712 0.748059 -1.019445 -p 1.049712 0.748059 -1.019445 -p 1.049712 -0.748059 -1.019445 -p -1.049712 -0.748059 -1.019445 -p -1.049712 0.748059 -1.019445 -p 1.049712 0.748059 -1.019445 -p 1.049712 0.748059 1.019445 -p 1.049712 -0.748059 1.019445 -p 1.049712 -0.748059 -1.019445 -p 1.049712 0.748059 -1.019445 -p 1.049712 0.748059 1.019445 -p -1.049712 0.748059 1.019445 -p -1.049712 -0.748059 1.019445 -p 1.049712 -0.748059 1.019445 -p 1.049712 0.748059 1.019445 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 ;'
pm.mel.eval(mel_line)
# The curve command creates cv curves.  The curve command below will create an arrow.
# Maya code:
curve -d 1 -p -0.540481 0 -3.044861 -p 0.424182 0 -3.046763 -p 0.428595 0 -0.809008 -p 1.180086 0 -1.125873 -p -0.0310796 0 1.05049 -p -1.242245 0 -1.125873 -p -0.536068 0 -0.807105 -p -0.540481 0 -3.044861 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

#Python Code
mel_line='curve -d 1 -p -0.540481 0 -3.044861 -p 0.424182 0 -3.046763 -p 0.428595 0 -0.809008 -p 1.180086 0 -1.125873 -p -0.0310796 0 1.05049 -p -1.242245 0 -1.125873 -p -0.536068 0 -0.807105 -p -0.540481 0 -3.044861 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)

# Arrow
# Maya Command
curve -d 1 -p -0.540481 0 -3.044861 -p 0.424182 0 -3.046763 -p 0.428595 0 -0.809008 -p 1.180086 0 -1.125873 -p -0.0310796 0 1.05049 -p -1.242245 0 -1.125873 -p -0.536068 0 -0.807105 -p -0.540481 0 -3.044861 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7

# Python Command
mel_line='curve -d 1 -p -0.540481 0 -3.044861 -p 0.424182 0 -3.046763 -p 0.428595 0 -0.809008 -p 1.180086 0 -1.125873 -p -0.0310796 0 1.05049 -p -1.242245 0 -1.125873 -p -0.536068 0 -0.807105 -p -0.540481 0 -3.044861 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7' ;
pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint 
# Appears as parentConstraint -mo -weight 1 (command, w/offset); parentConstraint -weight 1 (command, w/o offset)
# Parent Constraint by default is maintain offset is OFF (snaps by default)
# Maya Code:
parentConstraint(driver, driven) 
# Could also put a long version, parentConstraint (driver, driven, maintainOffset=False)
# Python Code:
pm.parentConstraint (driver, driven)

# When you use selected:

# Maya Code w/o offset:
parentConstraint -mo -weight 1 
# Python Code w/o offset:
pm.parentConstraint(maintainOffset=True, weight=1)

# Maya Code w/offset:
parentConstraint -weight 1
# Python Code w/offset:
pm.parentConstraint(maintainOffset=False, weight=1)

# -----Flags---------------
# This code has a toggle flag
maintainOffset (mo) - this sets the offset on and off (use mo=True/False)
weight (w) - sets the weight of the constraint
# This command can also constrain rotation of the axis

# Orient Constraint
# Appears as orientConstraint -offset 0 0 0 -weight 1 (command, w/o offset);
# This command also works if you specifiy the joints to be constrained by selecting them
# Creating variables is a good way to get desired joints 
# Maya Command:
orientConstraint(driver, driven)
#Python Command:
pm.orientConstraint(driver, driven)

# When you use selected:

# Maya Code w/o offset:
orientContstraint -offset 0 0 0 -weight 1
# Python Code w/o offset:
pm.orientContstraint(offset = [0,0,0], weight =1)

# Maya code w/offset:
orientConstraint -mo -weight 1
# Python code w/offset:
pm.orientConstraint(maintainOffset=True, weight=1)


# -----------------Flags-------------------------------------------
offset (o) = sets or queries the value of the offs et
weight (w) = sets the weight fo the value for the specified target
maintainOffset (mo) = the offset necessary to preserve the constrained object initial position, snapping
name (n) = the name of the constraint


# Point Constraint
# Appears as doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" } (MEL Procedure); pointConstraint -offset 0 0 0 -weight 1;
# I used pm.mel.whatIs to find the define the commands after makeing a point constraint.
# The default of the command is offset ON
# Maya Command:
pointConstraint(driver, driven)
#Python Command:
pm.pointConstraint(driver, driven)

# When you use selected:

# Maya command w/offset:
pointconstraint -mo -weight 1
# Python command w/offset:
pm.pointconstraint (maintainOffset=True, weight=1)

# Maya Command w/o offset
pointConstraint -offset 0 0 0 -weight
# Python command w/o offset:
pm.pointConstraint (offset=[0,0,0], weight=1)

# -----------------Flags-------------------------------------------
offset (o) = sets or queries the value of the offs et
weight (w) = sets the weight fo the value for the specified target
maintainOffset (mo) = the offset necessary to preserve the constrained object initial position, snapping
name (n) = the name of the constraint

# Pole Vector Constraint
# Maya Command:
poleVectorConstraint(driver[control], driven[ikHandle])
# Python Command:
pm.poleVectorConstraint(driver, driven)

# When you use selected:

# Maya Command:
poleVectorConstraint -weight 1
# Python Command:
poleVectorConstraint(weight=1)

# --------------Flags--------------------------------------------
weight(w) = how much the control affects the IK Handle

# How does this constraint differ from the previous three: 
# A Pole Vector Constraint works with IK Rotate Plane Handles.  It directs the point direction of the bend in the IK Rotate Plane and also how much it bends as well.  

'''
Attributes 
'''


# Float Attributes
# Appears as addAttr -ln "stuff"  -at double  -min 20 -max 38 |pCube1; setAttr -e-keyable true |pCube1.stuff;
# The default is a float attribute with no max or min
# Maya Command:
addAttr -ln "attribute_name" -at double -min 20 -max 38
setAttr -e-keyable
# Create float attribute
selected=pm.ls(selection=True)
first_selected=selected[0]

# A name can also hard coded into the command.
attribute_name=raw_input()
first_selected.addAttr(attribute_name, keyable=True, min=360, max=360)

# Create Separator Attribute
# Python Command:
attribute_name=raw_input()
first_selected.addAttr(attribute_name, at='enum', en='---------------:', keyable=True)
# Locking the Attribute
attribute=first_selected.attr(attribute_name)
attribute.set(lock=True)


# Template Attributes 
# To create a group of attributes it is necessary to create several variable and define them.
# Get Selection:
selected = pm.ls(selection=True)
first_selected = selected[0]

# Create a group of attributes at one time.


# The finger attributes are an example.
# Finger Attribute Command
attribute_name_02 = 'CURL'
first_selected.addAttr(attribute_name_02, at='enum', en='---------------:', keyable=True)
# Lock the Attribute
attribute_02=first_selected.attr(attribute_name_02)
attribute_02.set(lock=True)

# Create float attributes under the enum attribute
attribute_name_03 = 'index_curl'
first_selected.addAttr(attribute_name_03, keyable=True, min=-360, max=360)

attribute_name_04 = 'middle_curl'
first_selected.addAttr(attribute_name_04, keyable=True, min=-360, max=360)

attribute_name_05 = 'pinkie_curl'
first_selected.addAttr(attribute_name_05, keyable=True, min=-360, max=360)

# Color Change Attribute
# Appears as setAttr "curveShape1.overrideEnabled" 1
# Maya Command:
setAttr -overrideEnabled 1

# Making the color change requires the number for the color, to find the number go to: Window, Attribute Spreadsheet, and OverrideColor
# In my process, I created the icon first and then changed it color but color changes can also run off selected objects in a scene
# Python Commands
# Create the icon:
pm.circle(normal=[0,1,0], radius=2)

# Get Selected
selected = pm.ls(selection=True)
icon = selected[0]

# Change the Color
icon.overrideEnabled.set(1)
blue = 6
icon.overrideColor.set(blue)

# Other colors: Red = 4 and Yellow = 16

#--------------Flags-------------------------------------
long name (ln) = long name of the attribute
attribute type (at) = the type of the attribute created, like 'float'
minValue (min) = the minimum value of an attribute
maxValue (max) = the maximum value of an attribute
hidden(h) = hides the attribute
keyable (k) = makes the attribute keyable or not
enum (en) =  the name of the enum
# overrideEnabled and overrideColor are not flags but pymel attributes, to access them you must put the object.pymelattribute
# set and get are used to determine how the command will be applied, set to apply the command and get to retreive a command


'''
Lock, Hide, Unlock and Show Attributes

'''
# Lock and Hide run off of pymel attributes so it is necessary to use a defined variable based on selection.
# Lock and Hide ALL

# Translations
control_icon.tx.set(lock=True, keyable=False)
control_icon.ty.set(lock=True, keyable=False)
control_icon.tz.set(lock=True, keyable=False)

# Rotations
control_icon.rx.set(lock=True, keyable=False)
control_icon.ry.set(lock=True, keyable=False)
control_icon.rz.set(lock=True, keyable=False)

# Scale
control_icon.sx.set(lock=True, keyable=False)
control_icon.sy.set(lock=True, keyable=False)
control_icon.sz.set(lock=True, keyable=False)

# Visibility
control_icon.v.set(lock=True, keyable=False)



# Unlock and Show ALL

# Translations
control_icon.tx.set(lock=False, keyable=True)
control_icon.ty.set(lock=False, keyable=True)
control_icon.tz.set(lock=False, keyable=True)

# Rotations
control_icon.rx.set(lock=False, keyable=True)
control_icon.ry.set(lock=False, keyable=True)
control_icon.rz.set(lock=False, keyable=True)

# Scale
control_icon.sx.set(lock=False, keyable=True)
control_icon.sy.set(lock=False, keyable=True)
control_icon.sz.set(lock=False, keyable=True)

# Visibility
control_icon.v.set(lock=False, keyable=True)


'''
Proxy
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.
'''
# Detach Component
# Appears with Echo All as DetachComponent (Run Time Command) and performDetachComponents (MEL Procedure)
# Maya Command:
DetachComponent
# Python Command:
pm.mel.DetachComponent

# Extract
# Appears with Echo All as ExtractFace (Run time Command) and performPolyChipOff (MEL procedure)
# Maya Command
ExtractFace
# Python Command
pm.mel.ExtractFace()

# Combine
# Appears with Echo All and as polyUnite (command) and CombinePolygons (Run time Commands) 
# Maya command
CombinePolygons
# Python Command
pm.mel.CombinePolygon()

# Separate
# Appears with Echo All as SeparatePolygon (Run time Command), performPolyShellSeparate(MEL Procedure), and polySeparate (command)
# Maya command:
SeparatePolygon
#Python Command
pm.mel.SeparatePolygon()

# NUKE
pm.delete(all=True, constructionHistory=True)
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
pm.xform(centerPivots=True) 



