'''
Research Notes

Mei Li Ham

Current Shelf Tools: 20
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: --

Drop Down Menus: --

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

# Selected object

# Froze transforms

# MEL: 

'''
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

'''
# Python:

pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

# Important Flags:

'''
-apply
'''

# Delete History

# Selected object

# Turned on echo

# Deleted history

# MEL:

'''
DeleteAllHistory;
delete -ch;

'''

# Python:
pm.delete('object A', ch=True)

# Important flags:
'''
-ch
''' 

# Center Pivot

# Selected object

# Turned one echo

# Centered Pivot

# MEL:

'''
CenterPivot;
xform -cp;
'''

# Python:

pm.xform(cp=True)

# Important Flags
'''
-cp
'''

# Single Chain and Rotate Plan IKs

# Selected joint tool

# Created IKs

# MEL:

#Single Chain
'''
select -r joint1.rotatePivot ;
select -add joint2.rotatePivot ;
ikHandle;
'''

# Python: 

import pymel.core as pm 

selected = pm.ls(selection=True)
print 'current selected', selected

pm.ikHandle(sol='ikSCsolver')



# Rotate Plane
'''
select -r joint5.rotatePivot ;
select -tgl joint3.rotatePivot ;
ikHandle -sol ikRPsolver;

'''

# Python:
import pymel.core as pm 

selected = pm.ls(selection=True)
print 'current selected', selected

pm.ikHandle(sol='ikRPsolver')


# Cluster

# Create Curve

# Select each vertex point on curve

# Create Clusters under Surfaces/Edit Curves/Selection

# MEL:

'''
ClusterCurve;
'''

# Python:
pm.Cluster()

# Grouping (Does not need to be included on Shelf!)

# Selected object

# Pressed G

# MEL: 
'''
doGroup 0 1 1;

'''

# Python:
pm.group()

# Parenting (Does not need to be included on Shelf!)

# Selected two different objects

# Press P

# MEL: 

'''
parent;
'''

# Python:
pm.parent()

# Duplicating (Does not need to be included on Shelf!)

# Select an object

# Press CMD + D

# MEL: 

'''
duplicate -rr;
'''

# Python:
pm.duplicate()

# Important Flags

'''

-rr

'''

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle


'''
circle -normal 1 0 0;

'''

# Python:
pm.circle((nr=0, 1, 0))


# Square

# Created primitive cube

# Selected CV curve tool.

# Outlined one side of cube 


# Python: 

mel_line = 'curve -d 1 -p -0.5 0.0448471 -0.5 -p -0.5 0.0448471 0.5 -p 0.5 0.0448471 0.5 -p 0.5 0.0448471 -0.5 -p -0.5 0.0448471 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)



# Cube

# Created Polygon primitive Cube.

# Selected CV curve tool.

# Created curve outlining cube.

# Selected the curve.


# Python: 

mel_line = 'curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;'
pm.mel.eval(mel_line)



# Arrow

# Selected CV curve tool.

# Created arrow on grid.

# Selected curve.


# Python: 

mel_line = 'curve -d 1 -p -1.193544 0 -0.249049 -p -1.195521 0 0.317346 -p -0.0194022 0 0.347562 -p -0.00778073 0 0.902027 -p 0.837515 0 0.0112026 -p -0.0291822 0 -0.734218 -p -0.0309758 0 -0.22039 -p -1.207121 0 -0.222098 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)




'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint

# MEL
'''
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

'''

# Python:
import pymel.core as pm 

selected = pm.ls(selection=True)
print 'current selected', selected

pm.parentConstraint(selected, mo=True)


# Orient Constraint

'''

doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
orientConstraint -offset 0 0 0 -weight 1;

'''

# Python:
import pymel.core as pm 

selected = pm.ls(selection=True)
print 'current selected', selected

pm.orientConstraint(selected, mo=True)


# Point Constraint

'''

doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;

'''

# Python:
import pymel.core as pm 

selected = pm.ls(selection=True)
print 'current selected', selected

pm.pointConstraint(selected, mo=True)

# Pole Vector Constraint

'''

poleVectorConstraint -weight 1;

#Python:
import pymel.core as pm 

selected = pm.ls(selection=True)
print 'current selected', selected

pm.poleVectorConstraint(selected)

'''
# How does this constraint differ from the previous three.

'''
# It uses one line of text, not two. It also does not consist of a lot of numbers.
'''

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

# Create Separator Attribute
'''
addAttr -ln "FINGERS"  -at "enum" -en "Green:Blue:"  |group1;
setAttr -e-keyable true |group1.FINGERS;

addAttr -ln "CURL"  -at "enum" -en "------------------:"  |group1;
setAttr -e-keyable true |group1.CURL;
'''

first_selected.addAttr('FINGERS', keyable=True, 
	at='enum', en= "------------------:")
first_selected.FINGERS.set(lock=True)
'''
# Template Attributes
FINGERS
CURL
index_curl
middle_curl
pinky_curl 
'''
import pymel.core as pm

selected=pm.ls(selection=True)
first_selected = selected[0]
print 'current selected', selected

first_selected.addAttr('FINGERS', keyable=True, 
	at='enum', en= "------------------:")
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('CURL', keyable=True, 
	at='enum', en= "------------------:")
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('SPREAD', keyable=True, 
	at='enum', en= "------------------:")
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB', keyable=True, 
	at='enum', en= "------------------:")
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True)
first_selected.addAttr('thumb_drop', keyable=True)

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


