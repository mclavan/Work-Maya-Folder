'''
Research Notes

Name

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: ??

Drop Down Menus: ??

'''

'''
Each tool you will need document:
	1) MEL Commmand
	2) What type of command is it and how did you find it?
	3) Convert MEL to Python.
	4) Important Flags
'''

'''
General Tools Research
'''

# Extra comand I like to use is select comand
pm.select()

# ---Flags---
	clear (-cl)= clear selection
	all (-all)= select all
	visible (-vis)= selects all visible

'''
THis comand selects a certain item depending on the flag. The one I use most is flag -cl.
This clears the selection.
'''

# Freeze Transforms
makeIdentity 

# ---Flags---
	apply (a)= 'True/False command. True freezes transforms acording to world orientation.'
	translations, rotations, scale (-t, -r, -s)= 'freezes the translations, rotations, and scale'
	normals (-n)= 'freezes the normals. The default is 1.'

pm.makeIdentity (apply=True, t=1, r=1, s=1, n=1)


# Delete History
DeleteHistory;

''' 
DeleteHistory is a special funtion to delete command. it deletes the histroy of the object.
DeleteHistory is a runtime command that is preset to delete all history. If I want to only delete
specific history, I would have to use the (-ch) flag on the delete command.
'''
pm.delete(ch=True)


# Center Pivot
CenterPivot

xform -cp;

pm.xform(cp=True)



'''
Center Pivot is also a runtime command. The command is xform, with the flag being -cp.
'''

# Single Chain and Rotate Plan IKs

# This is for mel

'''
After testing both the sc and rp hadle tool, I found there to be only one minor difference in the code.
First the single chain code is:
'''
IKHandleTool;
select -d ikHandle1 ;
select -r joint5.rotatePivot ;
select -add joint5|joint2.rotatePivot ;
ikHandle;

'''
The extra code for it to be a rotate plane ik handle is the below code replacing the last line for the sc code.
'''
ikHandle -sol ikRPsolver;

#---Flags---
	startJoint (-sj)= THe start joint
	endEffector (-ee)= the end effector, which can be a joint.
	priority (-p)= The priority of the ik handle.
	weight (-w)= The weight of the ik handle.

# for the python command, it is 
pm.ikHandle() 'with same flags'

# Cluster
pm.cluster()

# This will create the clusters for a selected curve.
for current_cv in first_selected.cv:
    
   #Apply cluster to current cv
   pm.cluster(current_cv)


'''
I am having troubles explaining this one.
'''

# Grouping (Does not need to be included on Shelf!)
pm.group()

	#Grouping by default parents selected objects in the scene
	# parenting like this example does child-parent order
	pm.group(name='Grandfather')
	pm.group(name='Father')
	pm.group(name='son')

	# grouping with the flag empty being true makes each group seperate
	pm.group(name='Grandfather', empty=True)
	pm.group(name='Father', empty=True)
	pm.group(name='son', empty=True)



# Parenting (Does not need to be included on Shelf!)
pm.parent()
# Quick key is p
parent (-w)
# This unparents the selected object
# Quick key is shift+p

# Duplicating (Does not need to be included on Shelf!)
pm.duplicate()

# Quick key is cmd+d

# ---Flags---
	returnRootsOnly (-rr)= 'This is the default flag. It returns the nodes the the heirarchy'
	name (-n)= '(string) This names the duplicated object(s)'
	remaneChildren (-rc)= 'This renames the children of the dupicated object to make them unique'

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
pm.circle()
# creating a circle with the y axis being the normal
pm.circle(normal=[0, 1, 0])

# ---Flags----
	normal = Direction of the control.
	radius = Sizze of the control
	sections = How many sections of the control line


# Square
pm.circle(degree=1, sections=4)

# ---Flags---
	degree = 'Two main values, linear=1 and cubic=3'
	sections = 'Four points makes a square'
	normal = 'Direction of the control.'


# Cube and Arrow icons.

'''
you create a cube icon by using the cv curve tool. When creating the cube and arrow, I use the eval command.
this allows us to write a mel code as a string in pymel, and then pymel reads it as a mel code. Sometimes this makes 
the job easier. Note:  because both the cube and the arrow are created by using the same command, curve,
the flags are the same.
'''
# ---Flags---
	degree (-d)= 'weather or not the curve will be linear= 1, or curved= 3, default is 3'
	'Note, to see the curve = -d+1. To see a linear curve, you need 2 points.'
	point (-p)= 'x,y,z position'
	knot (-k)= 'The knot vector for each point value'

pm.mel.eval ()

# Cube

pm.curve (flags)
pm.mel.eval ('curve -d 1 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17') ;

# Arrow

pm.curve (flags)
pm.mel.eval ('curve -d 1 -p 0 0 -5 -p 2 0 -2 -p 1 0 -2 -p 1 0 3 -p -1 0 3 -p -1 0 -2 -p -2 0 -2 -p 0 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7');

'''
Creating an arrow is the same as a cube, with less pionts located in different areas of space.
This uses the same flags, degree (-d), point (-p), and knot (-k).
'''
pm.mel.eval('curve -d 1 -p -1 0 -1 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 -1 -p 3 0 -1 -p 3 0 -2 -p 5 0 0 -p 3 0 2 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p 2 0 3 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 1 -p -3 0 1 -p -3 0 2 -p -5 0 0 -p -3 0 -2 -p -3 0 -1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24') ;

'''
As the arrow above, this creates another curve, which I use for the Center of Gravity icon, or COG

'''

'''
Constraints
- Remember to test offset on and off with these commands.

	All the constraints use the flag:
	-weight
	If you maintain offset, the flag used is 
	-mo
'''
# Parent Constraint
pm.parentConstraint()

# Orient Constraint
pm.orientConstraint()

# Point Constraint
pm.pointConstraint()

# Pole Vector Constraint
pm.poleVectorConstraint()

# How does this constraint differ from the previous three.
'''
Pole Vector Constraint does not have maintain offset flag (-mo)

'''

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=1)

#---Flags---
	longName (-ln) & shortName (-sn)= 'Sets the name of the attribute'
	attributeType (-at)= 'Sets the type of attribute. Float, Matrix and String must be in quotes.'
	minValue (-min) & maxValue (-max)= 'Sets the minum and maximum values for the attribute.'
	keyable (-k)= 'tells weather or not the attribute can be keyable.'
	enumName (-en)= 'eddits the string of a enum attribute'
	hidden (-h)= 'Weather or not the attribute is hidden from the ui.'


# raw input = name of attribute

# Create Separator Attribute
selected = pm.ls(selection=True)
first_selected = selected[0]

attribute_name = raw_input()
first_selected.addAttr(attribute_name, at='enum', en="----------------", keyable=1)

lockAtt = first_selected.attr(attribute_name)
lockAtt.set(lock=1)


'''
Template Attributes
FINGERS
CURL
index_curl
middle_curl
pinky_curl
SPREAD
index_spread
middle_spread
pinky_spread
THUMB
thumb_curl
thumb_drop

'''
# Create a group of attributes at one time.  
# The finger attributes are an example.

first_selected.addAttr('FINGERS', keyable=True, at='enum', en='----------------')
first_selected.FINGERS.set(lock=True)

first_selected.addAttr('CURL', keyable=True, at='enum', en='----------------')
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True, min=-10, max=10)
first_selected.addAttr('middle_curl', keyable=True, min=-10, max=10)
first_selected.addAttr('pinky_curl', keyable=True, min=-10, max=10)

first_selected.addAttr('SPREAD', keyable=True, at='enum', en'----------------')
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index_spread', keyable=True, min=-10, max=10)
first_selected.addAttr('middle_spread', keyable=True, min=-10, max=10)
first_selected.addAttr('pinky_spread', keyable=True, min=-10, max=10)

first_selected.addAttr('THUMB', keyable=True, en='------------------')
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True, min=-10, max=10)
first_selected.addAttr('thumb_drop', keyable=True, min=-10, max=10)


'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.

Research:
Detach Component
Separate
Extract
Combine
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
'''

# Selecting every cv on a curve
pm.select(first_selected.cv[:], r=1)

# Selecting every other cv on a curve
pm.select(first_selected.cv[::2], r=1)

'''
This section I will add my  own notes on commands I make
I will also explain which buttons on the shelf are special
example are buttons that have a single and double command.

'''

'''
'Main' key
This key I have set up to load pymel.core as pm,
Also to set the layout of my workspace to what I like.

'''

import pymel.core as pm
pm.mel.eval ('setNamedPanelLayout "Main_Layout"')

'''
All constraint keys will be single click= mo=False
	and double click= mo=True

'''











