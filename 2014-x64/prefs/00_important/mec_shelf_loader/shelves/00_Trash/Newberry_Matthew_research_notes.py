'''
Research Notes

Name

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons:FK, PRNT, ORI, PNT, PV

Drop Down Menus:SHPS

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
Maya Command-makeIdentity
Runtime Command-Freeze Transformtions
Flags:
t(translate)
r(rotate)
s(scale)
n(normals)
pn(preserveNormals)

Found with echo all
Navigation:
Modify > Freeze Transformations

Mel:
makeIdentity -apply true, t=1, r=1, s=1, n=1, pn=1

Python:
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=1, pn=1)
# Delete History
Maya Command- delete
Runtime Command- DeleteHistory
Flags:
ch(construction history)

Found with echo all
Navigation:
Edit > Delete by Type > History
Mel:
delete -ch
Python:
pm.delete(ch=True)
# Center Pivot
Maya Command- xform
Runtime Command- CenterPivot
Flags:
cp(centerPivots)

Found with echo all
Navigation:
Modify > Center Pivots

Mel:
xform -cp
Python:
pm.xform(cp=True)


# Single Chain and Rotate Plan IKs
Maya Command- ikhandle
Runtime Command- NA
Flags:
s (sticky)
sol (solver)
Found with echo all
Navigation:
Skeleton > IK Handle Tool 
Mel:
ikHandle -sol ikRPsolver -s 0;
ikHandle -sol ikSCsolver -s 0;
Python:
pm.ikHandle(sol='ikRPsolver' s=0)
pm.ikHandle(sol='ikSCsolver' s=0)

# Cluster
Maya Command- cluster
Runtime Command- NA
Flags:
NA

Found by entering 'cluster' into script editor
Navigation:
Create Deformers > Cluster
Mel:
cluster
Python:
pm.cluster()
# Grouping (Does not need to be included on Shelf!)
Maya Command-  group
Runtime Command- NA
Flags: 
NA

Found by entering 'group' into script editor
Navigation:
'Command G'
Mel:
group
Python:
pm.group()
# Parenting (Does not need to be included on Shelf!)
Maya Command-parent
Runtime Command- Parent
Flags:
NA
Found with echo all
Navigation:
Hotkey P
Mel:
parent
Python:
pm.parent
# Duplicating (Does not need to be included on Shelf!)
Maya Command- duplicate
Runtime Command- Duplicate
Flags:
rr(returnRootsOnly)
Found with echo all
Navigation:
"Command D"
Mel:
duplicate
Python:
pm.duplicate()
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
Maya Command- circle
Runtime Command- CreateNURBSCircle
Flags:
c(center)
nr(normal)
sw(sweep)
r(radius)
d(degree)
ut(useTolerence)
tol(tolerence)
s(selections)
ch(constructionHistory)
Found with echo all
Navigation:
Create > Nurbs Primitives > Circle
Mel:
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
Python:
pm.circle(c =(0,0,0), nr= (0,1,0), sw=, 360, r=1, d= 3, ut= 0, tol= 0, s= 8, ch= 1)

# Square
Maya Command- curve
Runtime Command- NA
Flags:
d(degree)
p(point)
k(knot)
Navigation:
Create > CV Curve Tolls
Mel:
curve -d 1 -p -1 0 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
Python:
mel_code = "curve -d 1 -p -1 0 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;"
pm.mel.eval(mel_code)

# Cube
Maya Command- curve
Runtime Command- NA
Flags:
d(degree)
p(point)
k(knot)
Found with echo all
Navigation:
Create > CV Curve Tool
Mel:
 curve
Python:

# Arrow
Maya Command- curve
Runtime Command- NA
Flags:
d(degree)
p(point)
k(knot)

Navigation:
Create > CV Curve Tool
Mel:
curve -d 1 -p -5 0 5 -p 5 0 2 -p 4 0 3 -p -2 0 1 -p -1 0 2 -p -3 0 4 -p -2 0 5 p -5 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ; 
Python:
mel_code = 'curve -d 1 -p -5 0 5 -p 5 0 2 -p 4 0 3 -p -2 0 1 -p -1 0 2 -p -3 0 4 -p -2 0 5 p -5 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_code)
'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
Maya Command- parentConstraint
Runtime Command- ParentConstraint
Flags:
NA

Navigation:
Constraint > ParentConstraint
Mel:
parentConstraint
Python:
selected = pm.ls(selection=True)
pm.parentConstraint(selected, maintainOffset=True)

selected = pm.ls(selection=True)
pm.parentConstraint(selected, maintainOffset=False)
# Orient Constraint
Maya Command-orientConstraint
Runtime Command- OrientConstraint
Flags:NA


Navigation:
Constraint > OrientConstraint
Mel:
OrientConstraint
Python:
selected = pm.ls(selection=True)
pm.oreintConstraint(selected, maintainOffset=True)

selected = pm.ls(selection=True)
pm.orientConstraint(selected, maintainOffset=False)
# Point Constraint
Maya Command- pointConstraint
Runtime Command- PointConstraint
Flags:
NA

Navigation:
Constraint > PointConstraint
Mel:
pointConstraint
Python:
selected = pm.ls(selection=True)
pm.pointConstraint(selected, maintainOffset=True)

selected = pm.ls(selection=True)
pm.pointConstraint(selected, maintainOffset=False)
# Pole Vector Constraint
Maya Command- poleVectorConstraint
Runtime Command- PoleVectorConstraint
Flags:
NA

Navigation:
Constraint > Pole Vector

Mel:
poleVectorConstraint
Python:
selected = pm.ls(selection=True)
pm.poleVectorConstraint(selected)
# How does this constraint differ from the previous three.
This constraint lacks the maintain offset option that the other three do.
'''
Attributes (Convered in Podcast)
'''
# Create float attribute
Maya Command- addAttr
Runtime Command- NA
Flags:
ln(longname)
at(attributeType)
h(hidden)

Mel:
addAttr
Python:
first_selected.addAttr('finger_curl', keyable =True
# Create Separator Attribute
Maya Command- addAttr
Runtime Command- NA
Flags:
ln(longname)
at(attributeType)
en(enumName)


Mel:
addAttr -ln "FINGERS" -at "enum" -en "Green:Blue" |group1:
setAttr -e keyable true |group1.FINGERS;
addAttr -ln "CURL" -at "enum" -en "---------------" |group1:
setAttr -e keyable true |group1.CURL;

Python:
first_selected.addAttr('FINGERS', at='enum', en='------------', keyable=True)
first_selected.FINGERS.set(lock=True)
# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
Maya Command- addAttr
Runtime Command- NA
Flags:
ln(longname)
at(attributeType)
en(enumName)


Mel:
addAttr -ln "FINGERS" -at "enum" -en "Green:Blue" |group1:
setAttr -e keyable true |group1.FINGERS;
addAttr -ln "CURL" -at "enum" -en "---------------" |group1:
setAttr -e keyable true |group1.CURL;

Python:
selected = pm.ls(selection=True)
print 'Current Selection:', selected

first_selected = selected[0]
first_selected.addAttr('FINGERS', at='enum', en='------------', keyable=True)
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected = selected[0]
first_selected.addAttr('SPREAD', at='enum', en='------------', keyable=True)
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.

Research:
Detach Component
- DetachComponent
Separate
- SeperatePolygon
Extract
- ExtractFace
Combind
- CombinePolygons
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
-FreezeTransformations
-DeleteHistory
-CenterPivot
'''


