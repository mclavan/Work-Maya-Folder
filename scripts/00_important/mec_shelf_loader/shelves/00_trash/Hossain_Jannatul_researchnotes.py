'''
Research Notes

Name (Hossain_Jannatul)

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

# Freeze Transforms
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

#-Flags--
	normal(n) - Set to 0 by default. Do not freeze normals.

# Delete History
# Dekete commad can delete any node in maya.
pm.delete()
pm.delete(ch=True)
pm.delete(constructionHistory=True)

#--Flags--
	constructionHistory(ch)
	staticChannels(sc)		-Delete keys that are not used.
	channels(c)				-Delete animation on selevted.

# Center Pivot
pm.xform(cp=True)
pm,xform(centerPiovts=True)

#----Flags---
	centerpivots(cp)			
								
# Single Chain and Rotate Plan IKs
# Rotate plan
ikHandle -sol ikRPsolver;
pm.ikHandle(sol='ikRPsolver')
# solver falg is default to ikSCsolver
pm.ikhandle()
pm.ikhandle(solver='ikSCsolver')

# Cluster
pm.Cluster()

import pymel.core as pm

selected= pm.ls(selection=True)
first_selected = selected [0]

#pm.cluster()
#Phython list range(slice)
#pm.select(first_selected.cv[:],r=True)
#---flag----
	name

# Grouping (Does not need to be included on Shelf!)
pm.group()

#_____Flags _______
name(n) - names the group.
empty() - Creates an empty group. 

# Grouping by default paretns selected objects in the scene.
# In this example 

# Parenting (Does not need to be included on Shelf!)
# Multiple childern and then the parent.
pm.parent('child','child', 'parent')

# Duplicating (Does not need to be included on Shelf!)
pm.duplicate()
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
pm.circle()
# Control is facing the y-axis. Good for FK back controls. World oriented.
pm.circle(normal=[1,0,0])

# Control is facing the x-axis. Good for local oriented controls.

# ______ Flags _______
pm.circle(normal=[1,0,0])
'''
normal = Direction of control. 
radius = How many sections the controls has.
section = How many sections does the control has.
'''
# Square
pm.circle(normal= [1, 0, 0],degree=1, sections=4)
#_____ Flags ______
degree (d) = Two main values, linear=1 and cubic=3
sections(s) = Four points makes a suare 
normal(nr) = Normal flags work just like the normal circle command.

# Cube
import pymel.core as pm 
mel_line = 'curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 ;'
pm.mel.eval(mel_line)

# Arrow
# The curve command creates cv curves. The curve command below will create an an arrow .
import pymel.core as pm 
mel_line = 'curve -d 1 -p 1 0 5 -p 3 0 5 -p 3 0 2 -p 5 0 2 -p 2 0 0 -p -1 0 2 -p 1 0 2 -p 1 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)
'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
#pm.parentConstraint ('parent','parent', 'child')
#pm.parentConstraint ('ikChain', 'fkChain','bindChain')

# parentConstraint with Mainttain offset
parentConstraint -mo -weight 1;
# parentConstraint without Maintainoffset
parentConstraint -weight 1;

# Orient Constraint
orientConstraint -offset 0 0 0 -weight 1;
# Point Constraint
pm.pointConstraint()
pm.pointConstraint(maintainOffset=True)

# Pole Vector Constraint
# How does this constraint differ from the previous three.
# Don't have a maintainOffset, otherwise will work exactly the same.
pm.poleVectorConstraint()
pm.poleVectorConstraint('control_icon','ik_handle')

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

attribute_name = raw_input ()
first_selected.addAttr(attribute_name, keyable=True)

# Create Separator Attribute
selected = pm.ls(selection=True)
	first_selected = selected[0]

	attribute_name= raw_input()
	first_selected.addAttr(attribute_name, at='enum', en='.......',keyable=True)
	attribute = first_selected.attr(attribute_name)
	attribute.set(lock=True)

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.

'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.

Research:
Detach Component
Separate
Extract
Combind
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
'''


