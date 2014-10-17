'''
Research Notes

Tristan Hall

Current Shelf Tools:
* Includes double click and drop down menu buttons.

Double Click Buttons:

Drop Down Menus:

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
# MEL Command
makeIdentity (-a boolean, -jo, -n unit, -r boolean, -s boolean, -t boolean)

#makeIdentity is a Maya Command; found by using Maya script editor and Autodesk Python Library

# MEL to Python
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

# ---- Flags ----
	apply (a), translate (t), rotate (r), scale (s), jointOrient (jo), normal(n)

# --------------------------------------------------------------------

# Delete History
# Be sure to activate "Echo All" in the Script Editor to see this code
# Runtime Command; found through Script Editor in Maya
deleteHistory;
import pymel.core as pm 
mel_life = 'deleteHistory'
pm.mel.eval(mel_line)

# Python Code;  ch = Construction History
pm.delete(ch=True)

# ---- Flags ----
	controlPoints (cp), all (all), inputConnectionsAndNodes (icn), 
	constructionHistory (ch), staticChannels (sc), channels (sc), 
	unitlessAnimationCurves (uac), timeAnimationCurves (tac)
	expressions (e), constraints (cn)

# --------------------------------------------------------------------

# Center Pivot
# Echo All;  MEL Command; found through Maya Python Library
# MEL Command
CenterPivot;
xform -cp;

# Python Command
pm.xform(cp=True)

# ---- Flags ----
	centerPivots (cp)

# --------------------------------------------------------------------

# Single Chain IK
pm.ikHandle(solver='ikSolver')

# Rotating Plane IK
# MEL Command
ikHandle -sol ikRPsolver;

# Python Command
pm.ikHandle(sol='ikRPsolver')

# Cluster
pm.cluster()

# Grouping (Does not need to be included on Shelf!)
# Command will group selected objects in Maya
pm.group(name='Group Name')

# For empty groups, use flag "empty=True"
pm.group(name='Group Name', empty=True)

# ---- Flags ----
	name (n), empty (em)

# Parenting (Does not need to be included on Shelf!)
# When selecting objects for parent constraints, remember...
#  Driver, THEN Driven
# The example below is of selecting four objects, with the last object being the parent
pm.parent('child', 'child', 'child')

# Duplicating (Does not need to be included on Shelf!)
	
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
# MEL Command
# Maya Command Type; found through Maya tool output code
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 3.53146e-07 -s 8 -ch 1; objectMoveCommand

# Python Command
pm.circle(name='Ct_Circle_01_Icon', normal=[1, 0, 0], radius=2)[0]

# ---- Flags ----
	name (n), radius (r)

# --------------------------------------------------------------------

# Square
# MEL Commant
# Maya Command Type; found through Maya tool output code
curve -d -1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4

# Python Command
pm.square(name=Ct_Square_01_Icon)[0]

# --------------------------------------------------------------------

# Cube
# MEL Command ...  It's a long one; Maya Command Type; found through Maya tool output code from CV curves
curve -d 1 -p 2.584201 6.08012 2.567347 -p 2.584201 6.08012 -2.601056 -p -2.584201 6.08012 -2.601056 -p -2.584201 6.08012 2.567347 -p 2.584201 6.08012 2.567347 -p 2.584201 0.911717 2.567347 -p 2.584201 0.911717 -2.601056 -p 2.584201 6.08012 -2.601056 -p 2.584201 0.911717 -2.601056 -p -2.584201 0.911717 -2.601056 -p -2.584201 6.08012 -2.601056 -p -2.584201 0.911717 -2.601056 -p -2.584201 0.911717 2.567347 -p -2.584201 6.08012 2.567347 -p -2.584201 0.911717 2.567347 -p 2.584201 0.911717 2.567347 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;

# Python Command
pm.curve (d=1, p=[2.584201, 6.08012, 2.567347], p=[2.584201, 6.08012, -2.601056], p=[-2.584201, 6.08012, -2.601056], p=[-2.584201, 6.08012, 2.567347], p=[2.584201, 6.08012, 2.567347], p=[2.584201, 0.911717, 2.567347], p=[2.584201, 0.911717, -2.601056], p=[2.584201, 6.08012, -2.601056], p=[2.584201, 0.911717, -2.601056], p=[-2.584201, 0.911717, -2.601056], p=[-2.584201, 6.08012, -2.601056], p=[-2.584201, 0.911717, -2.601056], p=[-2.584201, 0.911717, 2.567347], p=[-2.584201, 6.08012, 2.567347], p=[-2.584201, 0.911717, 2.567347], p=[2.584201, 0.911717, 2.567347], k=0, k=1, k=2, k=3, k=4, k=5, k=6, k=7, k=8, k=9, k=10, k=11, k=12, k=13, k=14, k=15)

# --------------------------------------------------------------------

# Arrow
# MEL Command ...  Also fairly lengthy; Maya Command Type; found through Maya tool output code from CV curves
curve -d 1 -p 0.940182 0.501604 -0.312278 -p 0.5 0.5025 -0.31487 -p 0.5 0.5025 1.351845 -p -0.5 0.5025 1.351845 -p -0.5 0.5025 -0.31487 -p -0.940182 0.501604 -0.312278 -p 0 0.501604 -1.978424 -p 0.940182 0.501604 -0.312278 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

# Python Command
pm.curve (d=1, p=[0.940182, 0.501604, -0.312278], p=[0.5, 0.5025, -0.31487], p=[0.5, 0.5025, 1.351845], p=[-0.5, 0.5025, 1.351845], p=[-0.5, 0.5025, -0.31487], p=[-0.940182, 0.501604, -0.312278], p=[0, 0.501604, -1.978424], p=[0.940182, 0.501604, -0.312278], k=0, k=1, k=2, k=3, k=4, k=5, k=6, k=7)

# --------------------------------------------------------------------

'''
Constraints
- Remember to test offset on and off with these commands.
'''

# Parent Constraint
# Parent Constraint defaults to maintain offset by default (Snapping)
# MEL Command w/o Offset;  Discovered through Script Editor and by applying various constraints to objects in Maya
doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
parentConstraint -weight 1;

# MEL Command w/ Offset
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

# Python Command
pm.parentCosntraint('driver', 'driven')
pm.parentCosntraint('driver', 'driven', maintainOffset=False)

# Maintain Offset
# MEL
parentCosntraint -mo -weight 1;

# Python
pm.parentCosntraint('driver', 'driven', mo=True)

# ----  Flags ----
	maintainOffset (mo) - Snapping or no Snapping
	weight (w) - How much influence a contrainst has over its target

# --------------------------------------------------------------------
	
# Orient Constraint
# MEL Command w/o Offset; Discovered through Script Editor and by applying various constraints to objects in Maya
doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
orientConstraint -offset 0 0 0 -weight 1;

# MEL Command w/ Offset
doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
orientConstraint -mo -weight 1;

# Python Command w/o Offset
pm.orientConstraint('driver', 'driven')

# Python Command w/ Offset
pm.orientCosntraint('driver', 'driven', maintainOffset=False)

# ---- Flags ----
	maintainOffset (mo) - Snapping or no Snapping
	weight (w) - How much influence a contrainst has over its target

# --------------------------------------------------------------------

# Point Constraint
# MEL Command w/o Offset
doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;

# MEL Commant w/ Offset
doCreatePointConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
pointConstraint -mo -weight 1;

# Python Commant w/o Offset
pm.pointConstraint('driver', 'driven')

# Python Command w/ Offset
pm.pointConstraint('driver', 'driven', maintainOffset=False)

# --------------------------------------------------------------------

# Pole Vector Constraint
# MEL Command
poleVectorConstraint -weight 1;

# Pole Vector Constraints are different as they can only be made between control icons and IK handles
# Python Command
pm.poleVectorConstraint('control_icon', 'ik_handle')

# Pole Vector Constraints don't have any offset functions, and can only be used when the driven is an IK handle

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

# --------------------------------------------------------------------

# Create Separator Attribute
first_selected.addAttr('FINGERS',  keyable=True,
	at='enum', en="-------------------:")
first_selected.FINGERS.set(lock=True)

'''
Tool - Quick Attribute Creator
'''
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)

attribute_name = raw_input()
first_selected.addAttr('FINGERS',  keyable=True,
	at='enum', en="-------------------:")

# --------------------------------------------------------------------

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.

first_selected.addAttr('FINGERS',  keyable=True,
	at='enum', en="-------------------:")
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('CURL',  keyable=True,
	at='enum', en="-------------------:")
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('SPREAD',  keyable=True,
	at='enum', en="-------------------:")
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB',  keyable=True,
	at='enum', en="-------------------:")
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True)
first_selected.addAttr('thumb_drop', keyable=True)

# --------------------------------------------------------------------

'''
Research:
Detach Component
Separate
Extract
Combind
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
'''


