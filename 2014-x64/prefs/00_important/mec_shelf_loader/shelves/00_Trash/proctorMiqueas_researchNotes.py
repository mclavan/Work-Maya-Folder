'''
Research Notes

Miqueas Proctor

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: ??
SC/RP solver
Parent Constraint
Point Constraint

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
1. makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
2. Freeze Transforms, Maya Command
3. pm.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
4. apply = boolean, t(translations), r(roations), s(scale), n(normals)

# Delete History
1. DeleteHistory;
2. Delete History, Maya Command
3. pm.delete (ch=True)
4. ch(constructionHistory)

# Center Pivot
1. CenterPivot;
2. center pivot, Maya Command
3. pm.xform (cp=True)
4. cp(centerPivots)

# Single Chain and Rotate Plan IKs
# MEL
1. RP solver code = ikHandle -sol ikRPsolver;
2. SC solver code = ikHandle;
# python
3. import pymel.core as pm
   pm.ikHandle(sol="ikSCsolver")

   import pymel.core as pm
5. pm.ikHandle(sol="ikRPsolver")
6. sol(solver) = string; set what type of ik to make


# Cluster
1. newCluster " -envelope 1";
2. Cluster, Maya Command
3. import pymel.core as pm
   pm.cluster(en=True)
4. en(envelope default is 1.0)

# Grouping (Does not need to be included on Shelf!)
1. doGroup 0 1 1;
2. Grouping, Maya Command
3. import pymel.core as pm
  pm.group(empty=True)
4. em(empty)
# Parenting (Does not need to be included on Shelf!)
1. parent;
2. Parenting, Maya Command
3. import pymel.core as pm
    pm.parent()
# Duplicating (Does not need to be included on Shelf!)
1. duplicate -rr;
2. Duplicating, Maya Command
3. import pymel.core as pm
   pm.duplicate()
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
1. circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
2. Nurbs Circle, Maya Command
3. import pymel.core as pm
   pm.circle( nr=(0, 1, 0), c=(0, 0, 0) )
4. nr(normal), c(center)
# Square
1. curve -d 1 -p -0.494149 0 -0.498337 -p 0.494149 0 -0.498337 -p 0.494149 0 0.515088 -p -0.494149 0 0.515088 -p -0.494149 0 -0.498337 -k 0 -k 1 -k 2 -k 3 -k 4 ;
2. CV curve, Maya Command
3. Mel_line = 'curve -d 1 -p -0.494149 0 -0.498337 -p 0.494149 0 -0.498337 -p 0.494149 0 0.515088 -p -0.494149 0 0.515088 -p -0.494149 0 -0.498337 -k 0 -k 1 -k 2 -k 3 -k 4;'
pm.mel.eval(Mel_line)
4. d(degree), p(pivot)
# Cube
1. curve -d 1 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;
2. CV curve, Maya Command
3. Mel_line = 'curve -d 1 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24;'
   pm.mel.eval(Mel_line)
4. d(degree), p(pivot)
# Arrow
1. curve -d 1 -p 0 0 5 -p -5 0 0 -p -2 0 0 -p -2 0 -5 -p 2 0 -5 -p 2 0 0 -p 5 0 0 -p 0 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
2. CV curve, Maya
3. Mel_line = 'curve -d 1 -p 0 0 5 -p -5 0 0 -p -2 0 0 -p -2 0 -5 -p 2 0 -5 -p 2 0 0 -p 5 0 0 -p 0 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7;'
pm.mel.eval(Mel_line)
4. d(degree), p(pivot)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
1. parentConstraint -mo -weight 1;,parentConstraint -weight 1
2. Constraint, Maya Command
3. import pymel.core as pm
   pm.parentConstraint(mo=True, weight=True), pm.parentConstraint(mo=False, weight=True)
4. mo(maintainOffset), w(weight)
# Orient Constraint
1. orientConstraint -mo -weight 1;, orientConstraint -offset 0 0 0 -weight 1;
2. Constraint, Maya Command
3. import pymel.core as pm
   pm.orientConstraint(mo=True, weight=True), pm.orientConstraint(mo=False)
4. mo(maintainOffset), w(weight) o(offset)
# Point Constraint
1. pointConstraint -mo -weight 1;, pointConstraint -offset 0 0 0 -weight 1;
2. Constraint, Maya Command
3. import pymel.core as pm
   pm.pointConstraint(mo=True, weight=True), pm.pointConstraint(mo=False, weight=True)
4. mo(maintainOffset), w(weight), o(offset)
# Pole Vector Constraint
1. poleVectorConstraint -weight 1;
2. Constraint, Maya Command
3. import pymel.core as pm
3. pm.poleVectorConstraint(weight=True)
4. w(weight)
# How does this constraint differ from the previous three.
# The pole vector constraint only has the weight slide in it's option box.
'''
Attributes (Convered in Podcast)
'''
import pymel.core as pm
# Getting the selected object
selected = pm.ls(selecteion=True)
first_selected = selected[0]
print 'first selected object:', first_selected
# Create float attribute

first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

# Create Separator Attribute

addAttr -ln "FINGERS"  -at "enum" -en "--------:"  |nurbsCircle1;
setAttr -e-keyable true |nurbsCircle1.FINGERS;

first_selected.addAttr('FINGERS', at='enum', keyable=True,
	en= "--------:")
first_selected.FINGERS.set(lock=True)

#quick qttribute
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)

attribute_name = raw_input()
first_selected.addAttr(attribute_name, at='enum', keyable=True,
	en= "--------:")
first_selected.FINGERS.set(lock=True)
# Template Attributes
'''
FINGERS
CURL
index_curl
middle_curl
pinky_curl
'''
# Create a group of attributes at one time. 

first_selected.addAttr('FINGERS', at='enum', keyable=True,
	en= "--------:")
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('CURL', at='enum', keyable=True,
	en= "--------:")
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('SPREAD', at='enum', keyable=True,
	en= "--------:")
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB', at='enum', keyable=True,
	en= "--------:")
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True)
first_selected.addAttr('thumb_drop', keyable=True)

 
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


