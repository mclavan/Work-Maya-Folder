'''
Research Notes

Name David Hobson

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
'''
#MEL
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

selected object
froze Transforms

#Python
pm.makeIdentity(selected, apply=True, t=1, r=1, s=1, n=0)
'''
# Delete History 
'''
#MEL
DeleteHistory;
delete -ch;

selected object
turned on echo
deleted history

#Python
pm.delete(ch=True)
'''
# Center Pivot
'''
#MEL
CenterPivot;
xform -cp;
editMenuUpdate MayaWindow|mainEditMenu;

selected object
turned on echo
centered pivot

#Python
pm.xform(cp=True)
'''
# Single Chain and Rotate Plan IKs
'''
Single Chain
#MEL
select -r joint1.rotatePivot ;
select -add joint2.rotatePivot ;
ikHandle;


#Python
pm.ikHandle(sol='ikSCsolver')


Rotate Plane
#MEL
select -r joint5.rotatePivot ;
select -tgl joint3.rotatePivot ;
ikHandle -sol ikRPsolver;

#Python
pm.ikHandle(sol='ikRPsolver')


Made joint Chain
Created Single chain/rotate plane IK
'''
# Cluster
'''
#MEL
ClusterCurve;

create curve 
selected all points
hit Cluster curve

#Python
pm.Cluster()
'''
# Grouping (Does not need to be included on Shelf!)
'''
#MEL
doGroup 0 1 1;

#Python
pm.group()

selected object
hit command G
'''
# Parenting (Does not need to be included on Shelf!)
'''
#MEL
parent;

#Python
pm.parent()

selected objects
hit P
'''
# Duplicating (Does not need to be included on Shelf!)
'''
#MEL
duplicate -rr;

#Python
pm.duplicate()

selected object
hit command D
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
#MEL
circle -normal 1 0 0;

#Python
pm.circle( nr = (0, 1, 0))
'''

# Square
'''
mel_line = 'curve -d 1 -p 5 0 5 -p 5 0 0 -p 10 0 0 -p 10 0 5 -p 5 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)

'''
# Cube
'''
mel_line = 'curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;'
'''
# Arrow
'''
mel_line = 'curve -d 1 -p 9.068954 0 7.988272 -p 9.103088 0 6.93281 -p 8.008158 0 6.964105 -p 8.042444 0 5.985507 -p 6.055032 0 7.440648 -p 8.090532 0 8.959941 -p 8.124827 0 7.981345 -p 9.144465 0 7.95112 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
'''

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
'''
#MEL
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

#Python
pm.parentConstraint
'''
# Orient Constraint

'''
#MEL
doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
orientConstraint -offset 0 0 0 -weight 1;

#Python
pm.orientConstraint
'''
# Point Constraint
'''
#MEL
doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;

#Python
pm.pointConstraint
'''
# Pole Vector Constraint
'''
#MEL
poleVectorConstraint -weight 1;

#Python
pm.poleVectorConstraint
'''
# How does this constraint differ from the previous three.
'''
One line of text instead of 2. Not a lot of numbers.
'''


'''
Attributes (Convered in Podcast)
'''
# Create float attribute

first_selected.addAttr('index curl', keyable=True)
first_selected.addAttr('middle curl', keyable=True)
first_selected.addAttr('pinky curl', keyable=True)

# Create Separator Attribute
'''
addAttr -ln "FINGERS" -at "enum" -en "Green:Blue:" |group1;
setAttr -e-keyable true |group1.FINGERS;

addAttr -ln "CURL" -at "enum" -en "----------------------:" |group1;
setAttr -e-keyable true |group1.CURL;
'''

first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------------------:")
first_selected.FINGERS.set(lock=True)

# Template Attributes 
'''
FINGERS
CURL
index_curl
middle_curl
pinky_curl
'''

first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------------------:")
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('CURL', keyable=True, at='enum', en="----------------------:")
first_selected.CURL.set(lock=True)
first_selected.addAttr('index curl', keyable=True)
first_selected.addAttr('middle curl', keyable=True)
first_selected.addAttr('pinky curl', keyable=True)

first_selected.addAttr('SPREAD', keyable=True, at='enum', en="----------------------:")
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index spread', keyable=True)
first_selected.addAttr('middle spread', keyable=True)
first_selected.addAttr('pinky spread', keyable=True)

first_selected.addAttr('THUMB', keyable=True, at='enum', en="----------------------:")
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb spread', keyable=True)
first_selected.addAttr('thumb curl', keyable=True)
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


