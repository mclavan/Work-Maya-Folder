'''
Research Notes

Michelle Brake

How to run:
import brakeMichelle_researchNotes
reload(brakeMichelle_researchNotes)

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
#1)
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
#2)
#I ran freeze transforms in Maya and copied it out of the script editor.
#3)
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
#4)
#apply (a)
#transtlate (t)
#rotate (r)
#scale (s)
#normal (n)

# Delete History
#1)
DeleteHistory;
delete -ch;
#2)
#Turned on Echo All Commands to have delete history show up then copied out of script editor.
#3)
pm.delete(ch=True)
#4)
#constructionHistory (-ch)

# Center Pivot
#1)
CenterPivot;
xform -cp;
editMenuUpdate MayaWindow|mainEditMenu;
#2)
#Turned on Echo All Commands to have center pivot show up then copied out of script editor.
#3)
pm.xform(cp=True)
#4)
#centerPivots (-cp)

# Single Chain IK
#1)
ikHandle -sol ikSCsolver;
#2)
#I created a single-chian IK in Maya and copied it out of the script editor.
#3)
pm.ikHandle(sol='ikSCsolver')
#4)
#-solver (-sol)

# Rotate Plane IK
#1)
ikHandle -sol ikRPsolver;
#2)
#I created a rotate-plane IK in Maya and copied it out of the script editor.
#3)
pm.ikHandle(sol='ikRPsolver')
#4)
#-solver (-sol)

# Cluster
#1)
newCluster " -envelope 1";
#2)
#I created a cluster in Maya and copied it out of the script editor.
#3)
pm.cluster(en=1)
#4)
#-envelope (-en)

# Grouping (Does not need to be included on Shelf!)
#1)
doGroup 0 1 1;
#2)
#I created a group in Maya and copied it out of the script editor.
#3)
pm.group()
#4)
#N/A

# Parenting (Does not need to be included on Shelf!)
#1)
parent;
#2)
#I created a parent in Maya and copied it out of the script editor.
#3)
pm.parent()
#4)
#N/A

# Duplicating (Does not need to be included on Shelf!)
#1)
duplicate -rr;
#2)
#I created a duplicate in Maya and copied it out of the script editor.
#3)
pm.duplicate(rr=True)
#4)
#-returnRootsOnly (-rr)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''

# Circle
#1)
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;
#2)
#I created a circle in Maya and copied it out of the script editor.
#3)
pm.circle()[0]
#4)
#-center (-c)
#-normal (-nr)
#-sweep (-sw)
#-radius (-r)
#-degree (-d)
#-useTolerance (-ut)
#-tolerance (-tol)
#-sections (-s)
#-constructionHistory (-ch)

# Square
#1)
curve -d 1 -p 12 0 -2 -p 12 0 -3 -p 11 0 -3 -p 11 0 -2 -p 12 0 -2 -k 0 -k 1 -k 2 -k 3 -k 4 ;
#2)
#I created a CV curve in Maya and copied it out of the script editor.
#3)
mel_line = 'curve -d 1 -p 12 0 -2 -p 12 0 -3 -p 11 0 -3 -p 11 0 -2 -p 12 0 -2 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)
#4)
#-degree (-d)
#-point (-p)
#-knot (-k)

# Cube
#1)
curve -d 1 -p 5.486977 0.5 -4.26194 -p 4.486977 0.5 -4.26194 -p 4.486977 0.5 -3.26194 -p 5.486977 0.5 -3.26194 -p 5.486977 0.5 -4.26194 -p 5.486977 -0.5 -4.26194 -p 4.486977 -0.5 -4.26194 -p 4.486977 0.5 -4.26194 -p 4.486977 0.5 -3.26194 -p 4.486977 -0.5 -3.26194 -p 4.486977 -0.5 -4.26194 -p 5.486977 -0.5 -4.26194 -p 5.486977 -0.5 -3.26194 -p 4.486977 -0.5 -3.26194 -p 4.486977 0.5 -3.26194 -p 5.486977 0.5 -3.26194 -p 5.486977 -0.5 -3.26194 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;
#2)
#I created a CV curve in Maya and copied it out of the script editor.
#3)
mel_line = 'curve -d 1 -p 5.486977 0.5 -4.26194 -p 4.486977 0.5 -4.26194 -p 4.486977 0.5 -3.26194 -p 5.486977 0.5 -3.26194 -p 5.486977 0.5 -4.26194 -p 5.486977 -0.5 -4.26194 -p 4.486977 -0.5 -4.26194 -p 4.486977 0.5 -4.26194 -p 4.486977 0.5 -3.26194 -p 4.486977 -0.5 -3.26194 -p 4.486977 -0.5 -4.26194 -p 5.486977 -0.5 -4.26194 -p 5.486977 -0.5 -3.26194 -p 4.486977 -0.5 -3.26194 -p 4.486977 0.5 -3.26194 -p 5.486977 0.5 -3.26194 -p 5.486977 -0.5 -3.26194 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;'
pm.mel.eval(mel_line)
#4)
#-degree (-d)
#-point (-p)
#-knot (-k)

# Arrow
#1)
curve -d 1 -p 12 0 -7 -p 10 0 -5 -p 8 0 -7 -p 9 0 -7 -p 9 0 -9 -p 11 0 -9 -p 11 0 -7 -p 12 0 -7 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
#2)
#I created a CV curve in Maya and copied it out of the script editor.
#3)
mel_line = 'curve -d 1 -p 12 0 -7 -p 10 0 -5 -p 8 0 -7 -p 9 0 -7 -p 9 0 -9 -p 11 0 -9 -p 11 0 -7 -p 12 0 -7 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)
#4)
#-degree (-d)
#-point (-p)
#-knot (-k)

'''
Constraints
- Remember to test offset on and off with these commands.
'''

# Parent Constraint
#1)
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;
#2)
#I created a parent constraint in Maya and copied it out of the script editor.
#3)
pm.parentConstraint()
#4)
#-maintainOffset (-mo)
#-weight (-w)

# Orient Constraint
#1)
doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
orientConstraint -mo -weight 1;
#2)
#I created a orient constraint in Maya and copied it out of the script editor.
#3)
pm.orientConstraint()
#4)
#-maintainOffset (-mo)
#-weight (-w)

# Point Constraint
#1)
doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;
#2)
#I created a point constraint in Maya and copied it out of the script editor.
#3)
pm.pointConstraint()
#4)
#-offset (-o)
#-weight (-w)

# Pole Vector Constraint
#1)
poleVectorConstraint -weight 1;
#2)
#I created a pole vector constraint in Maya and copied it out of the script editor.
#3)
pm.poleVectorConstraint()
#4)
#-weight (-w)
# How does this constraint differ from the previous three.
#You need to have a icon and a rotate-plane IK as opposed to just 2+ object(s).

'''
Attributes (Covered in Podcast)
'''

# Create float attribute
#1)
addAttr -ln "Float"  -at double;
setAttr -e-keyable true;
#2)
#I created an attribute in Maya and copied it out of the script editor.
#3)
addAttr('Float', keyable=True)
#4)
#-longName (-ln)
#-attributeType (-at)
#-enumerated (-e)
#-keyable (-k)

# Create Separator Attribute
#1)
addAttr -ln "Separator"  -at "enum" -en "----------:";
setAttr -e-keyable true;
setAttr -lock true;
#2)
#I created a locked attribute in Maya and copied it out of the script editor.
#3)
addAttr('Separator', at='enum', en='----------', keyable=True)
Separator.set(lock=True)
#4)
#-longName (-ln)
#-attributeType (-at)
#-enumName (-en)
#-enumerated (-e)
#-keyable (-k)

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
#1)
addAttr -ln "index_curl"  -at double;
setAttr -e-keyable true;
addAttr -ln "middle_curl"  -at double;
setAttr -e-keyable true;
addAttr -ln "pinky_curl"  -at double;
setAttr -e-keyable true;
#2)
#I created a group of attributes in Maya and copied it out of the script editor.
#3)
addAttr('index_curl', keyable=True)
addAttr('middle_curl', keyable=True)
addAttr('pinky_curl', keyable=True)
#4)
#-longName (-ln)
#-attributeType (-at)
#-enumerated (-e)

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


