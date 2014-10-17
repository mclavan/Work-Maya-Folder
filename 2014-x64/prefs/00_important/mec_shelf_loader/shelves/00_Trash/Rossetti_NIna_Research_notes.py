'''
Research Notes

Nina Rossetti

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: none

Drop Down Menus: none

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
makeIdentity -apply true -t 1 -r 1 -s 1 n 0 -pn 0;
Command, whatIs
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
Apply,t=translate,r=rotate,s=scale,n=normal, pn=preserveNormals

# Delete History
delete -ch;
Command, whatIs
pm.delete(ch=True)
ch=constructionHistory

# Center Pivot
xform -cp;
Command, whatIs
pm.xform(cp=True)
cp=centerPivots

# Single Chain and Rotate Plan IKs
ikHandle;
Command, whatIs
pm.ikHandle(solver='ikSCsolver')
Solver=ikSCsolver

ikHandle -sol ikRPsolver;
Command, whatIs
pm.ikHandle()
sol=solver

# Cluster
Clustercurve;
Run Time Command, whatIs
pm.cluster()
envelope

# Grouping (Does not need to be included on Shelf!)
Group 0 0 1;
Run Time Command, whatIs
pm.group(empty=True)

# Parenting (Does not need to be included on Shelf!)
parent;
Command, whatIs
pm.parent()
w=parent to world, r=preserve exisiting local object transformation

# Duplicating (Does not need to be included on Shelf!)
duplicate;
Command, whatIs
pm.duplicate()
st=smartTransform

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
Command, whatIs
pm.circle()
c=center, r=radius

# Square
curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
Command, whatIs
mel_line = 'curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;;'
pm.mel.eval(mel_line)

# Cube
curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;
Command, whatIs
mel_line='curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;'
pm.mel.eval(mel_line)

# Arrow
curve -d 1 -p 1 0 0 -p 2 0 0 -p 0 0 2 -p -2 0 0 -p -1 0 0 -p -1 0 -2 -p 1 0 -2 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
Command, whatIs
mel_line='curve -d 1 -p 1 0 0 -p 2 0 0 -p 0 0 2 -p -2 0 0 -p -1 0 0 -p -1 0 -2 -p 1 0 -2 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
parentConstraint -mo -weight 1;
Command, whatIs
pm.parentConstraint()
mo=maintainOffeset, w=weight

# Orient Constraint
orientConstraint -mo -weight 1;
Command, whatIs
pm.orientConstraint()
mo=maintainOffeset, w=weight

# Point Constraint
pointConstraint -offset 0 0 0 -weight 1;
Command, whatIs
pm.pointConstraint()
o=offeset, w=weight
# Pole Vector Constraint
poleVectorConstraint -weight 1;
Command, whatIs
pm.poleVectorConstraint()
w=weight
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

# Create Separator Attribute
first_selected.addAttr('FINGERS', keyable=True)
at='enum', en='-----------------:')
first_selected.FINGERS.set(lock=True)



# Template Attributes 
first_selected.addAttr('FINGERS', keyable=True)
at='enum', en='-----------------:')
first_selected.FINGERS.set(lock=True)

first_selected.addAttr('CURL', keyable=True)
at='enum', en='-----------------:')
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('SPREAD', keyable=True)
at='enum', en='-----------------:')
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB', keyable=True)
at='enum', en='-----------------:')
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True)
first_selected.addAttr('thumb_drop', keyable=True)

# Create a group of attributes at one time.  
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)

attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)
at='enum', en='-----------------:')
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


