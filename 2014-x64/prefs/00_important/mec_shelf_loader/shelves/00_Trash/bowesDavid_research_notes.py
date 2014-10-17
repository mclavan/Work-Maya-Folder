'''
Research Notes

David Bowes 

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
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
# It is a maya command and I found it by running the freeze transformations tool in maya on an icon I created
pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
t = Translate
r = Rotate
s = Scale 

# Delete History
DeleteHistory;
delete -ch;
# It is a maya command and I found it by turning on echo commands and running it. 
pm.delete(ch=True)
ch = Construction History

# Center Pivot
CenterPivot;
xform -cp;
# It is a maya command and I found it by turning on echo commands seeing as it would not 
# show otherwise. 
pm.xform(cp=True)
cp = Center Pivot

# Single Chain and Rotate Plan IKs
ikHandle;
ikHandle -sol ikRPsolver;
# It is a maya command and I just created a joint chain and ran the tool. 
pm.ikHandle(sol = 'ikSCsolver')
pm.ikRPsolver(sol = 'ikRPsolver')
sol = Solver

# Cluster
CreateCluster;
newCluster " -envelope 1";
# It is a maya command and I selected a circle and ran the tool. 
pm.cluster(en = 1)
en = envelope

# Grouping (Does not need to be included on Shelf!)
doGroup 0 1 1;
# It is a maya command and I came upon it by selecting two items and grouping them. 
pm.group(name = 'empty')
em = empty

# Parenting (Does not need to be included on Shelf!)
performParent false;
parent;
# It is a maya command and I selected child and parent and used the parent tool. 
pm.parent(empty)
em = empty 

# Duplicating (Does not need to be included on Shelf!)
duplicate -rr;
# It is a maya command and I selected and object and used the duplicate tool. 
pm.duplicate('empty')
rr = return roots only

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 4.56148e-09 -s 8 -ch 1; objectMoveCommand;
# It is a maya command and I just created a NURBS circle.
pm.circle(name = 'empty')
r = radius 
c = center 
nr = normal 
sw = sweep 
ut = use tolerance 
tol = tolerance
s = sections 
ch = construction history 
d = degree 

# Square
nurbsSquarePreset(0,0,0,0,0,1,0,1,1,1,3,1);
nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ; objectMoveCommand;
# It is a maya command and I just created a NURBS square. 
pm.square(name = 'empty')
c = center 
nr = normal 
sl1 = side length 1
sl2 = side length 2 
sps = spans per side 
d = degree 
ch = construction history

# Cube
nurbsCube -p 0 0 0 -ax 0 1 0 -w 1 -lr 1 -hr 1 -d 3 -u 1 -v 1 -ch 1; objectMoveCommand;
# It is a maya command and I just created a NURBS cube. 
pm.cube(name = 'empty')
p = pivot 
ax = axis 
w = width 
lr = length ratio
hr = height ratio 
d = degree 
u = patches U
v = patches V
ch = construction history 

# Arrow
curve -d 1 -p -1 0 -3 -p 1 0 -1 -p -1 0 -1 -p -1 0 3 -p -2 0 3 -p -2 0 -1 -p -4 0 -1 -p -2 0 -3 -p -1.584438 0 -3.465611 -p -1 0 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;
# It is a maya command and I created an arrow using the cv curve tool.
pm.curve(name = 'empty')
p = point 
k = knot 

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;
# It is a maya command and I just selected two objects and ran the tool. 
pm.parentConstraint(empty, maintainOffset = True)
mo = maintain offset

# Orient Constraint
doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
orientConstraint -offset 0 0 0 -weight 1;
# It is a maya command and I just selected two objects and ran the tool. 
pm.orientConstraint(empty, maintainOffset = True)
o = offset
w = weight

# Point Constraint
doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;
# It is a maya command and I just selected two objects and ran the tool. 
pm.pointConstraint(maintainOffset = True)
o = offset 
w = weight

# Pole Vector Constraint
poleVectorConstraint -weight 1;
# It is a maya command and I created an ikHandle and used the pole vector constraint on it. 
pm.poleVectorConstraint(w = 1)
w = weight 

# How does this constraint differ from the previous three.
# This constraint can only be used on a ikHandle instead of the others being able to be used 
# on controls and joints. 


'''
Attributes (Covered in Podcast)
'''
# Create float attribute
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)



# Create Separator Attribute
import pymel.core as pm 

selected = pm.ls(selection=True)
print 'Current Selected', selected 

first_selected = selected[0]
first_selected.addAttr('FINGERS', at='enum', en='--------------', keyable=True)
first_selected.FINGERS.set(lock=True)

# Template Attributes 
first_selected.addAttr('TOES', at='enum', en='--------------', keyable=True)
first_selected.TOES.set(lock=True)
first_selected.addAttr('CURL', at='enum', en='--------------', keyable=True)
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('CURL', at='enum', en='--------------', keyable=True)
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB', at='enum', en='--------------', keyable=True)
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True)
first_selected.addAttr('thumb_drop', keyable=True)

# Create a group of attributes at one time.  
# The finger attributes are an example.
import pymel.core as pm 

selected = pm.ls(selection=True)
print 'Current Selected', selected 

first_selected = selected[0]
first_selected.addAttr('TOES', at='enum', en='--------------', keyable=True)
first_selected.TOES.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)
first_selected.addAttr('THUMB', at='enum', en='--------------', keyable=True)
first_selected.THUMB.set(lock=True)
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
Separate
Extract
Combind
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
'''


