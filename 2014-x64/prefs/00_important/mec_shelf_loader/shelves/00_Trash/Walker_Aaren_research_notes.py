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

# Freeze Transforms
'''
1.FreezeTransformations;
 	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

2. This will freeze any tranforms on selected objects in the scene. 
	This was found under modify, freeze Transforms.

3. pm.makeIdentity( apply=True, t = 1, r = 1, s = 1, n = 0)

4. t = translate, r = rotate, s = scale, n = normals.'''

# Delete History
'''
1. DeleteHistory;
	delete -ch;
2. This command will delete history on any objects selected in the scene.
	This can be found under edit, delete by type, history. 

3. pm.delete(ch=True)
4. ch = construction History.'''

# Center Pivot
'''
1.CenterPivot;
	xform -cp;
2. This command will take the pivot point and center in on what ever is selected. 
	This can be found in modify, center pivot.
3. pm.xform(cp=True)
4. cp = center pivot.
'''

# Single Chain and Rotate Plan IKs
'''SCS
1. ikHandle;
2. This command will make a Single chain ik solver on what ever joints are selected. 
	This command can be found under 

3. pm.ikHandle()
4. ----



'''
'''RPS
1. ikHandle -sol ikRPsolver

2. This command will create a rotate plane ik solver on a selected joint chain. 
	This can be found under skeleton, ikHandle, rotate plane. 

3. pm.ikHandle(sol='ikRPsolver')

4. sol = solver.



'''
# Cluster
'''
1. CreateCluster;
	newCluster"-envelope 1";

2. This will create a cluster on seleced joints. 

3. pm.cluster(envelope=1)

4. ----------

'''
# Grouping (Does not need to be included on Shelf!)
'''
1. group -empty;

2. this will group what is selected together. 
	The hot key is command G. 

3. pm.group(empty=True)

4. empty= will create a group with nothing in it. 
'''
# Parenting (Does not need to be included on Shelf!)
'''
1. parent;

2. This will parent to objects together. 
	The hot key for this is command P

3. pm.parent()

4. ----------
'''

# Duplicating (Does not need to be included on Shelf!)
'''
1. duplicate -rr;

2. This will create a copy of what is selected.
	The hot key is command D. 

3. pm.duplicate(rr=True)

4. rr = returnRootsonly 
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
1. circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 32 -ch 1;

2. This will create a nurbs circle on the orgin. 
	This can be found under create, nurbs primitives, circle.

3. pm.Circle

4. t = Transforms, s = scale, r = rotate, sw = sweep, ch = constructionHistory
'''
# Square
'''
1. nurbsSquarePreset(0,0,0,0,0,1,0,1,1,1,3,1);
	nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ; objectMoveCommand;

2. This will create a nurbs Square on the orgin. 
	This can be found under create, nurbs primitives, square.

3. mel_line= nurbsSquarePreset(0,0,0,0,0,1,0,1,1,1,3,1);
	nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ; objectMoveCommand;
	pm.mel.eval(mel_line)
4.------
'''

# Cube
'''
1. nurbsCube -p 0 0 0 -ax 0 1 0 -w 1 -lr 1 -hr 1 -d 3 -u 1 -v 1 -ch 1; objectMoveCommand;
2. This will create a nurbs cube on the orgin. 
	This can be found under create, nurbs primitives, cube.

3. pm.mel.eval(mel_line)
'''
# Arrow
'''
1.SnapToGrid; dR_enterForSnap;
	// Undo: doDelete // 
	SelectToolOptionsMarkingMenu;
	curve -d 1 -p 0 0 2 -p -1 0 1 -p 0 0 1 -p 0 0 0 -p 0 0 -1 -p 1 0 -1 -p 1 0 0 -p 1 0 1 -p 2 0 1 -p 1 0 2 -p 1 0 2 -p 1 0 3 -p 0 0 2 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;
	MarkingMenuPopDown;
	select -r curve1 ;
	select -r curve1.cv[11] ;
	TranslateToolWithSnapMarkingMenu;
	MarkingMenuPopDown;
	move -r -os -wd -0.430742 0 0 ;
	move -r -os -wd 0 0 -0.308809 ;
	// Undo: move -r -os -wd 0 0 -0.308809  // 
	// Undo: move -r -os -wd -0.430742 0 0  // 
	move -r -os -wd 0 0 0 ;
	SnapToGrid; dR_enterForSnap;
	move -r -os -wd -0.378444 0 0 ;
	move -r -os -wd 0 0 -0.390297 ;
	move -r -os -wd -0.0193595 0 0 ;
	select -cl  ;

2.


3.mel_line =  SnapToGrid; dR_enterForSnap;
// Undo: doDelete // 
SelectToolOptionsMarkingMenu;
curve -d 1 -p 0 0 2 -p -1 0 1 -p 0 0 1 -p 0 0 0 -p 0 0 -1 -p 1 0 -1 -p 1 0 0 -p 1 0 1 -p 2 0 1 -p 1 0 2 -p 1 0 2 -p 1 0 3 -p 0 0 2 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;
MarkingMenuPopDown;
select -r curve1 ;
select -r curve1.cv[11] ;
TranslateToolWithSnapMarkingMenu;
MarkingMenuPopDown;
move -r -os -wd -0.430742 0 0 ;
move -r -os -wd 0 0 -0.308809 ;
// Undo: move -r -os -wd 0 0 -0.308809  // 
// Undo: move -r -os -wd -0.430742 0 0  // 
move -r -os -wd 0 0 0 ;
SnapToGrid; dR_enterForSnap;
move -r -os -wd -0.378444 0 0 ;
move -r -os -wd 0 0 -0.390297 ;
move -r -os -wd -0.0193595 0 0 ;
select -cl  ;
pm.mel.eval(mel_line)

4. -------------
'''

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
'''
1. parentConstraint -mo -weight 1;
2. This will create an parentConstraint on the selected objects 
	This is found under constrain, parentConstraint.
3. pm.parentConstraint()

4. weight= how much weight an object has in a scene. 


'''

# Orient Constraint
'''
1. orientConstraint -offset 0 0 0 -weight 1;

2. This will create an orientConstraint on the selected objects 
	This is found under constrain, orientConstraint.

3. pm.orientConstraint()

4. weight= how much weight an object has in a scene. 
'''
# Point Constraint
'''
1. pointConstraint -mo -weight 1; 

2. This will create an pointConstraint on the selected objects 
	This is found under constrain, pointConstraint.

3. pm.pointConstraint()

4. mo=maintainOffset,  weight= how much weight an object has in a scene. 
'''
# Pole Vector Constraint
'''
1. poleVectorConstraint -wieght 1;

2.  This will create an poleVectorConstraint on the selected objects 
	This is found under constrain, orientConstraint.

3. pm.poleVectorConstraint()

4. weight= how much weight an object has in a scene. 
'''
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
import pymel.core as pm

selected = pm.ls(selection=True)
print 'currently selected:', selected 


selected[0].addAttr('index_curl', keyable=True)
selected[0].addAttr('middle_curl', keyable=True)
selected[0].addAttr('ring_curl', keyable=True)
selected[0].addAttr('pinky_curl', keyable=True)
selected[0].addAttr('index_spread', keyable=True)
# Create Separator Attribute
selected.addAttr('FINGERS', keyable=True, at='enum', en='------------')
selected.FINGERS.set(lock=True)
# Template Attributes 
selected.addAttr('FINGERS', keyable=True, at='enum', en='------------')
selected.FINGERS.set(lock=True)

selected.addAttr('CURL', keyable=True, at='enum', en='------------')
selected.CURL.set(lock=True)

selected[0].addAttr('index_curl', keyable=True)
selected[0].addAttr('middle_curl', keyable=True)
selected[0].addAttr('ring_curl', keyable=True)
selected[0].addAttr('pinky_curl', keyable=True)

selected.addAttr('SPREAD', keyable=True, at='enum', en='------------')
selected.SPREAD.set(lock=True)

selected[0].addAttr('index_spread', keyable=True)
selected[0].addAttr('middle_spread', keyable=True)
selected[0].addAttr('ring_spread', keyable=True)
selected[0].addAttr('pinky_spread', keyable=True)


selected.addAttr('THUMB', keyable=True, at='enum', en='------------')
selected.THUMB.set(lock=True)

selected[0].addAttr('thumb_curl', keyable=True)
selected[0].addAttr('thumb_drop', keyable=True)


# Create a group of attributes at one time.  
# The finger attributes are an example.
attribute_name=raw_input()
selected[0].addAttr(attribute_name, keyable=True)
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


