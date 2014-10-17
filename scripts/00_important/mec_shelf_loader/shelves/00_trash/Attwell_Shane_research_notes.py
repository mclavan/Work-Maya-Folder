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

import pymel.core as pm

# Freeze Transforms
# MEL Command:
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

# Comand Method
Modify -> Freeze Transforms

# Python Command
pm.makeIdentity(a=True, t=1, r=1, s=1, n=0)

# --- Flags ---
apply(a) - If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.
translate(t) - If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied. (Note: the translate flag is not meaningful when applied to joints, since joints are made to preserve their world space position. This flag will have no effect on joints.)
rotate(r) - If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
scale(s) - If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.

# Delete History
# MEL Command:
delete -ch;

pm.mel.DeleteHistory

# Comand Method
Edit -> Delete by Type -> History

# Python Command
pm.delete(['object1', 'object2'], ch=True)

# --- Flags ---
constructionHistory(ch) - Remove the construction history on the objects specified or selected.

# Center Pivot
# MEL Command:
xform -cp;

# Comand Method
Modify -> Center Pivot

# Python Command
pm.xform(['object1', 'object2'], cp=True)

# --- Flags ---
centerPivots(cp) - Set pivot points to the center of the bounding box of the object.

# Single Chain and Rotate Plan IKs
# MEL Command:
# Rotate Plain: 

ikHandle -sol ikRPsolver;

# Single Chain:

ikHandle;

# Comand Method
Skeleton -> IKHandle Tool

# Python Command
pm.ikHandle()
	(sol='ikSCsolver')
	(sol='ikRPsolver')

# --- Flags ---
name(n) - Specifies the name of the handle.
startJoint(sj) - Specifies the start joint of the handle joint chain.
endEffector(ee) - Specifies the end-effector of the handle joint chain. The end effector may be specified with a joint or an end-effector. If a joint is specified, an end-effector will be created at the same position as the joint and this new end-effector will be used as the end-effector.

# Cluster
# MEL Command:
newCluster " -envelope 1";

# Comand Method
Create Deformer -> Cluster

# Python Command
pm.cluster()

# --- Flags ---
name(n) - names cluster nodes
envelope(en) - set envelope value of deformer

# Grouping (Does not need to be included on Shelf!)
# MEL Command:
doGroup 0 1 1;

# Comand Method
Hotkeys: Command + G

# Python Command
pm.group()

pm.group(name='grandfather')
pm.group(name='father')
pm.group(name='son')

pm.group(name='grandfather', empty=True)
pm.group(name='father', empty=True)
pm.group(name='son', empty=True)

# --- Flags ---
name(n) - names new group node
empty() - names empty group
parent(p) - put the new group under the given parent
world(w) - put the new group under the world

# Parenting (Does not need to be included on Shelf!)
# MEL Command:
select -r 'object1' ;
select -tgl 'object2' ;
parent;

# Comand Method
Hotkeys: select 'object1' -> shift select 'object2' -> P

Constrain -> Parent

# Python Command
pm.parent()

# --- Flags ---
world(w) - unparent given object(s) (parent to world)
relative(r) - preserve existing local object transformations (relative to the parent node)
absolute(a)	- preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]
addObject(add) - preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.
removeObject(rm) - Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the scene. Use -world to remove the world as a parent of the given object.
shape(s) - The parent command usually only operates on transforms. Using this flags allows a shape that is specified to be directly parented under the given transform. This is used to instance a shape node. 

# Duplicating (Does not need to be included on Shelf!)
# MEL Command:
duplicate -rr;

# Comand Method
Hotkeys: Command + D

# Python Command
pm.duplicate()

# --- Flags ---
name(n)	- name to give duplicated object(s)
smartTransform(st) - remembers last transformation and applies it to duplicated object(s)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
# MEL Command:
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;

# Comand Method
Create -> Nurbs Primitives -> Circle Option Box -> Degree = cubic, Sections = 8

# Python Command
pm.circle()
pm.circle(normal=[1,0,0])
pm.circle(normal=[0,1,0])

# --- Flags ---
normal - direction of control
radius - size
sections - number of sections

# Square
# MEL Command:
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 1 -ut 0 -tol 0 -s 4 -ch 1; objectMoveCommand;

# Comand Method
Create -> Nurbs Primitives -> Circle Option Box -> Degree = linear, Sections = 4

# Python Command
pm.circle(degree=1, sections=4)

# --- Flags ---
degree(d) - the degree of the resulting circle
sections(s) - four points make square
normal(nr) - normal Flags work like normal circle


# Cube
# MEL Command:
curve -d 1 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;

# Comand Method
Create -> CV Curve Tool Option Box -> linear

# Python Command
pm.curve(d=1, p=[[-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5]], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# --- Flags ---
width(w) - Width of the object Default: 1.0
lengthRatio(lr)	- Ratio of "length" to "width" Default: 1.0
heightRatio(hr)	- Ratio of "height" to "width" Default: 1.0
patchesU(u)	- Number of sections in U Default: 1
patchesV(v)	- Number of sections in V Default: 1
degree(d) - The degree of the resulting surface. 1 - linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic Default: 3
pivot(p) - The primitive's pivot point
axis(ax) - The primitive's axis

# Arrow
# MEL Command:
curve -d 1 -p 4.053876 0 7.001388 -p 4.030813 0 8.02597 -p 3.071233 0 8.031505 -p 4.554581 0 9.025369 -p 6.020382 0 8.072307 -p 5.049084 0 8.053041 -p 5.019561 0 6.998776 -p 4.122018 0 7.070391 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

# Comand Method
CV Curve Tool

# Python Command
pm.curve(d=1, p=[[4.053876, 0, 7.001388], [4.030813, 0, 8.02597], [3.071233, 0, 8.031505], [4.554581, 0, 9.025369], [6.020382, 0, 8.072307], [5.049084, 0, 8.053041], [5.019561, 0, 6.998776], [4.053876, 0, 7.001388]], k=[0, 1, 2, 3, 4, 5, 6, 7])


# --- Flags ---
degree(d) - valid values are 1, 2, 3, 5 or 7. Default is degree 3.
multEndKnots(me) - Default is true. False means that the curve will not pass through the end control vertices (CVs).
uniform(un) - Default is true, which means uniform parameterization will be used. False means chord length parameterization.

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
# Snapping
# MEL Command:
parentConstraint -weight 1;

# Comand Method
Constrain -> Parent Option Box -> maintainOffset off

# Python Command
pm.parentConstraint('driver', 'driven')

# Maintain Offset
# MEL Command:
parentConstraint -mo -weight 1;

# Comand Method
Constrain -> Parent Option Box -> maintainOffset off

# Python Command
pm.parentConstraint('driver', 'driven' mo=True)

# --- Flags ---
	maintainOffset (mo) - Snapping or no Snapping
	weight(w) - How much influence a constraint has over its target.

# Orient Constraint
# Snapping
# MEL Command:
orientConstraint -weight 1;

# Comand Method
Constrain -> Orient Option Box -> maintainOffset off

# Python Command
pm.orientConstraint('driver', 'driven')

# Maintain Offset
# MEL Command:
orientConstraint -mo -weight 1;

# Comand Method
Constrain -> Orient Option Box -> maintainOffset off

# Python Command
pm.orientConstraint('driver', 'driven' mo=True)

# --- Flags ---
	maintainOffset (mo) - Snapping or no Snapping
	weight(w) - How much influence a constraint has over its target.

# Point Constraint
# Snapping
# MEL Command:
pointConstraint -weight 1;

# Comand Method
Constrain -> Point Option Box -> maintainOffset off

# Python Command
pm.ppintConstraint('driver', 'driven')

# Maintain Offset
# MEL Command:
pointConstraint -mo -weight 1;

# Comand Method
Constrain -> Point Option Box -> maintainOffset off

# Python Command
pm.pointConstraint('driver', 'driven' mo=True)

# --- Flags ---
	maintainOffset (mo) - Snapping or no Snapping
	weight(w) - How much influence a constraint has over its target.

# Pole Vector Constraint
# Snapping
# MEL Command:
poleVectorConstraint -weight 1;

# Comand Method
Constrain -> Pole Vector Option Box -> maintainOffset off

# Python Command
pm.poleVectorConstraint('driver', 'driven')

# Maintain Offset
# MEL Command:
poleVectorConstraint -mo -weight 1;

# Comand Method
Constrain -> Pole Vector Option Box -> maintainOffset off

# Python Command
pm.pole_vectorConstraint('driver', 'driven' mo=True)

# --- Flags ---
	maintainOffset (mo) - Snapping or no Snapping
	weight(w) - How much influence a constraint has over its target.

# How does this constraint differ from the previous three.
	# - Pole Vectors only affects IKHandles, the other three affect all.
'''
Attributes (Convered in Podcast)
'''
# Create float attribute

selected = pm.ls(selection=True)
first_selected = selected[0]

attribute_name = raw_input()
first_selected.addAttr(attribute_name, at='enum', en='-------------:', keyable=True)


# Create Separator Attribute
selected = pm.ls(selection=True)
first_selected = selected[0]

attribute_name = raw_input()
first_selected.addAttr(attribute_name, at='enum', en='-------------:', keyable=True)
attribute = first_selected.attr(attribute_name)
attribute.set(lock=True)

# Template Attributes
selected_icon= pm.ls(selection=True)
control_icon = selected_icon[0]

control_icon.addAttr('Fingers', at='enum', en='-------------:', keyable=True)
control_icon.Fingers.set(lock=True)
control_icon.addAttr('Curl', at='enum', en='-------------:', keyable=True)
control_icon.Curl.set(lock=True)

control_icon.addAttr('index_curl', keyable=True)
control_icon.addAttr('middle_curl', keyable=True)
control_icon.addAttr('pinky_curl', keyable=True)


control_icon.addAttr('Spread', at='enum', en='-------------:', keyable=True)
control_icon.Spread.set(lock=True)
control_icon.addAttr('index_spread', keyable=True)
control_icon.addAttr('middle_spread', keyable=True)
control_icon.addAttr('pinky_spread', keyable=True)

control_icon.addAttr('Thumb', at='enum', en='-------------:', keyable=True)
control_icon.Thumb.set(lock=True)
control_icon.addAttr('index_spread', keyable=True)
control_icon.addAttr('middle_spread', keyable=True)
control_icon.addAttr('pinky_spread', keyable=True)

 
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


