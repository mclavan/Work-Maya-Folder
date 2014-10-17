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
1. makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
2. Used to 0 out all the transforms on an object.
3. pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
4. t = transform, s = scale, r = rotate
'''
# Delete History
'''
1. DeleteHistory;
   delete -ch;
2. Deletes all the history on a selected object.
3. pm.delete(ch=True)
4. ch = constructionHistory
'''
# Center Pivot
'''
1. CenterPivot;
   xform -cp;
2. Centers the pivot on a selected object.
3. pm.xform(cp=True)
4. cp = centerPivot
'''
# Single Chain and Rotate Plan IKs
'''
#RPS
1. ikHandle -sol ikRPsolver;
2. Creates a rotate plane solver ikhandle with two joints.
3. pm.ikHandle(sol='ikRPsolver')
4. sol = solver which determines what kind of solver the tool creates.
#SCS
1. ikHandle;
2. Creates a single chain solver ikhandle with two joints.
3. pm.ikHandle()
4. -
'''
# Cluster
'''
1. CreateCluster;
   newCluster " -envelope 1";
2. Creates a cluster at the selected point.
3. pm.cluster(envelope=1)
4. envelope = Sets the envelope value for the deformer.
'''
# Grouping (Does not need to be included on Shelf!)
'''
1. group -empty;
2. Creates an empty group at the origin of the scene.
3. pm.group(empty=True)
4. empty = Makes the group contrain no objects.
'''
# Parenting (Does not need to be included on Shelf!)
'''
1. parent;
2. Moves multiple objects into a group on a driver driven basis.
3. pm.parent()
4. -
'''
# Duplicating (Does not need to be included on Shelf!)
'''
1. dpuplicate -rr;
2. Duplicates selected objects.
3. pm.duplicate(rr=True)
4. rr = returnRootsonly returns only the roots of the new Hierarchy.
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
2. Creates a nurbs circle at the origin of the scene.
3. pm.circle()
4. t = transform, s = scale, r = rotate, sw = sweep, ch = constructionHistory
'''
# Square
'''
1. curve -d 1 -p -32.169597 0 0.235259 -p -32.230538 0 16.084858 -p -16.112057 0 16.03634 -p -16.113514 0 0.171695 -p -32.032999 0 0.356013 -k 0 -k 1 -k 2 -k 3 -k 4 ;
2. Ultimately creates a square with the given coords.
3. mel_line = 'curve -d 1 -p -32.169597 0 0.235259 -p -32.230538 0 16.084858 -p -16.112057 0 16.03634 -p -16.113514 0 0.171695 -p -32.032999 0 0.356013 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
   pm.mel.eval(mel_line)
4. t = transform, s = scale, r = rotate, d = degree, p = point
'''
# Cube
'''
1. curve -d 1 -p 6.70437 6.70437 6.70437 -p 6.70437 6.70437 -6.70437 -p -6.70437 6.70437 -6.70437 -p -6.70437 6.70437 6.70437 -p 6.70437 6.70437 6.70437 -p 6.70437 -6.70437 6.70437 -p -6.70437 -6.70437 6.70437 -p -6.70437 6.70437 6.70437 -p -6.70437 -6.70437 6.70437 -p -6.70437 -6.70437 -6.70437 -p -6.70437 6.70437 -6.70437 -p -6.70437 -6.70437 -6.70437 -p 6.70437 -6.70437 -6.70437 -p 6.70437 6.70437 -6.70437 -p 6.70437 -6.70437 -6.70437 -p 6.70437 -6.70437 6.70437 -p 6.70437 6.70437 6.70437 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;
2. Ultimately creates a cube with the given coords.
3. mel_line = 'curve -d 1 -p 6.70437 6.70437 6.70437 -p 6.70437 6.70437 -6.70437 -p -6.70437 6.70437 -6.70437 -p -6.70437 6.70437 6.70437 -p 6.70437 6.70437 6.70437 -p 6.70437 -6.70437 6.70437 -p -6.70437 -6.70437 6.70437 -p -6.70437 6.70437 6.70437 -p -6.70437 -6.70437 6.70437 -p -6.70437 -6.70437 -6.70437 -p -6.70437 6.70437 -6.70437 -p -6.70437 -6.70437 -6.70437 -p 6.70437 -6.70437 -6.70437 -p 6.70437 6.70437 -6.70437 -p 6.70437 -6.70437 -6.70437 -p 6.70437 -6.70437 6.70437 -p 6.70437 6.70437 6.70437 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;'
   pm.mel.eval(mel_line)
4. t = transform, s = scale, r = rotate, d = degree, p = point
'''
# Arrow
'''
1. curve -d 1 -p 0 0 0 -p -32 0 32 -p -16 0 32 -p -16 0 64 -p 16 0 64 -p 16 0 32 -p 32 0 32 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
2. Ultimately creates an arrow shape with the given coords.
3. mel_line = 'curve -d 1 -p 0 0 0 -p -32 0 32 -p -16 0 32 -p -16 0 64 -p 16 0 64 -p 16 0 32 -p 32 0 32 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
   pm.mel.eval(mel_line)
4. t = transform, s = scale, r = rotate, d = degree, p = point
'''


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
'''
1. parentConstraint -mo -weight 1;
2. Parent constrains objects together.
3. pm.parentConstraint()
4. mo = maintainOffset, weight = determines the weight value for selected objects.
'''
# Orient Constraint
'''
1. orientConstraint -offset 0 0 0 -weight 1;
2. Creates an orient constraint between multiple objects.
3. pm.orientConstraint()
4. offset = (t)ranslate (s)cale (r)otate, weight = determines the weight value for selected objects.
'''
# Point Constraint
'''
1. pointConstraint -mo -weight 1;
2. Point constrains objects together.
3. pm.pointConstraint()
4. mo = maintainOffset, weight = determines the weight value for selected objects.
'''
# Pole Vector Constraint
# How does this constraint differ from the previous three.
'''
1. poleVectorConstraint -weight 1;
2. Craetes a pole vector constraint between an ikhandle and another object.
3. pm.poleVectorConstraint()
4. weight = determines the weight value for selected objects.
'''


'''
Attributes (Convered in Podcast)
'''
import pymel.core as pm
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object:', first_selected

# Create float attribute
'''
1. addAttr -ln "floaty" -e-keyable true
2. Creates a floating attribute that is limited by a number range.
3. first_selected.addAttr('floaty', keyable=True)
4. ln = longName
'''
# Create Separator Attribute
'''
1. addAttr -ln "Doopy"  -at "enum" -en "Green:Blue:"  |nurbsCircle1;
   setAttr -e-keyable true |nurbsCircle1.Doopy;
2. Creates a separator that isn't limited by a number range.
3. first_selected.addAttr('Doopy', at='enum', keyable=True, en="Green:Blue")
4. ln = longName, at = attributeType, -en = enumerators
'''
# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
'''
1. addAttr -ln "Doopy"  -at "enum" -en "Green:Blue:"  |nurbsCircle1;
   setAttr -e-keyable true |nurbsCircle1.Doopy;
   addAttr -ln "Floaty" -e-keyable true
2. Creates several template attributes quickly.
3. first_selected.addAttr('Doopy', at='enum', keyable=True, en="Green:Blue")
   first_selected.addAttr('Floaty', keyable=True)
4. -
'''


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


