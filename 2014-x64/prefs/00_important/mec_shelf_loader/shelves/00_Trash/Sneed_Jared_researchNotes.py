'''
Research Notes

Jared Sneed

Current Shelf Tools: 
	NUKE: Freeze Transforms, Delete History, Center Pivot
	IK FK: Single Chain IK, Rotate Plane IK
	CLUS: Creates clusters
	CRVS: Different control curves
	PAR: Parent Constraint
	ORI: Orient Constraint
	PNT: Point Constraint
	POL: Pole Vector
	FING: Finger Attributes

* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: N/a

Drop Down Menus:
IK FK
CRVS
PAR
ORI
PNT
POL

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
	# Was no MEL command found, other than makeIdentity
	# comamnd was found in the script editor
	
	 makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	 pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	# FLAGS:
		# t=Translate, r=Rotate, s=Scale
	

# Delete History
	deleteHistory;, delete -ch;
	# command was NOT found in Script Editor
		# had to turn on Echo All

	pm.delete(ch=True)
	#FLAGS:
		# -ch=constructionHistory, -c=channels, -cn=constraints,
		# -all=All specified kinds of objects

# Center Pivot
	centerPivot; xform -cp;
		# command was NOT found in Script Editor
			 # had to Echo All

	pm.xform(cp=True)
	#FLAGS:
		# -a=Absolute, -p=Preserve, -cp=CenterPivots, -ztp=zeroTransformPivots

# Single Chain and Rotate Plan IKs
	ikHandle -sj;
	ikHandle -sol ikRPsolver;
		# command was in Script Editor
		# found info on about 


	pm.ikHandle(sj=*, ee=*)
	pm.ikHandle(sol="ikRPsolver")
	#FLAGS:
	# -sj=StartJoint, -ee=EndEffector, -sol=Solver, -n=Name

# Cluster
	cluster -rel;
	# found command from maya command list

	pm.cluster(rel=True)
	# FLAGS:
		# -rel=relative

# Grouping (Does not need to be included on Shelf!)
	group -em -name null1;
	# wasn't able to find the right mel command through Script Editor
	# found command through Maya command doc

	pm.group(em=True)
	#FLAGS:
		-em=True, -name=Name of new gorup node, -p=Parent group under given parent

# Parenting (Does not need to be included on Shelf!)
	parentConstraint -mo -weight 1;
	pointConstraint -offset 0 0 0 -weight 1;
	orientConstraint -offset 0 0 0 -weight 1;
	poleVectorConstraint -weight 1;
	# commands were all present in Script Editor after doing the action

	pm.paretnConstraint()
	pm.pointConstraint()
	pm.orientConstraint()
	pm.poleVectorConstraint()
	# FLAGS:
		#-name=Sets the name of the constraint node to the specified name -mo=maintainOffset, -o=Offset

# Duplicating (Does not need to be included on Shelf!)
	duplicate -rr;
	#command can be found in Script Editor

	pm.duplicate('')
	#FLAGS:
		# -name= name duplicated object

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
		# Simply makes a curve circle
		# MEL orients it to face up, Python orients it on its side.
	pm.circle()
		#FLAGS:
			# -c=center, -n=normal  -sw=sweep	-r=radius -d=degree

# Square
	curve -d 1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4;
	# Drew out square curve
	# command was then in Script Editor

	mel_line = 'curve -d 1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4;'
pm.mel.eval(mel_line)

# Cube
curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;
	# Brought in poly cube
	# snapped CV cuve to all points
	# found command points in Script editor

mel_line = 'curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;'
pm.mel.eval(mel_line)
#FLAGS:
	# -d=degree, -p=point, -k=knot

# Arrow
curve -d 1 -p 4 0 0 -p 2 0 -2 -p 2 0 -1 -p 0 0 -1 -p 0 0 1 -p 2 0 1 -p 2 0 2 -p 4 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7;
	# snapped points on grid to make shape
	#found command in Script Editor

mel_line = 'curve -d 1 -p 4 0 0 -p 2 0 -2 -p 2 0 -1 -p 0 0 -1 -p 0 0 1 -p 2 0 1 -p 2 0 2 -p 4 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7;'
pm.mel.eval(mel_line)
#FLAGS:
	# -d=degree, -p=point, -k=knot

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	parentConstraint -mo -weight 1;
		# # select the driver and driven
		# parent constriain, from menu
		# offset on
		# command in Script Editor
	parentConstraint -weight 1;
		# # select the driver and driven
		# orient constriain, from menu
		# offset off
		# command in Script Editor

	pm.parentConstraint('name', 'name', mo=True)
	pm.parentConstraint('name', 'name', mo=False)
	# FLAGS:
		# name=name of driver and driven, st=skipTranslate, sr=skipRotate 

# Orient Constraint
	orientConstraint -mo -weight 1;
		# # select the driver and driven
		# orient constriain, from menu
		# offset on
		# command in Script Editor
	orientConstraint -offset 0 0 0 -weight 1;
		# # select the driver and driven
		# orient constriain, from menu
		# offset off
		# command in Script Editor

		pm.orientConstraint('name', 'name', mo=True)
		pm.orientConstraint('name', 'name', mo=False)
	#FLAGS:
		# -name=name, o=offset

# Point Constraint
	pointConstraint -mo -weight 1;
		# select the driver and driven
		# point constriain, from menu
		# offset on
		# command in Script Editor 
	pointConstraint -offset 0 0 0 -weight 1;
		# select the driver and driven
		# point constriain, from menu
		# offset off
		# command in Script Editor
		pm.orientConstraint('name', 'name', mo=True)
		pm.orientConstraint('name', 'name', mo=False)
	#FLAGS:
		# -name=name, o=offset


# Pole Vector Constraint
# How does this constraint differ from the previous three.
	# pole vector HAS to be constrained to an IK handle.
	# it cannot be constrainted to just anything 
	poleVectorConstraint -weight 1;
		# Had to make IK handle and 2 control curves
		# Tested pole vector on IK Handle=Sucess
		# Tested ploe vector on control curve2=Faliure

	pm.poleVectorConstraint()

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	addAttr -ln "Curl"  -at double  |joint1;
	setAttr -e-keyable true |joint1.Curl;
	# made object
	# selected object, and attribute
	# Added attribute
	# command in Script Editor
	first_selected.addAttr('index_curl', keyable=True)
	#FLAGS:
		#-ln=longName, -at=attributeType

# Create Separator Attribute
first_selected.addAttr('FINGERS',
    at='enum', en='---------------:', keyable=True)
	# This was coverd in class

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.

import pymel.core as pm

selected = pm.ls(selection=True)
print 'Current Selection', selected

first_selected = selected[0]
first_selected.addAttr('FINGERS',
    at='enum', en='---------------:', keyable=True)
first_selceted.FINGERS.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)
first_selected = selected[0]
first_selected.addAttr('SPREAD',
    at='enum', en='---------------:', keyable=True)
first_selceted.FINGERS.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)
first_selected.addAttr('THUMB',
    at='enum', en='---------------:', keyable=True)
first_selceted.FINGERS.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True)
first_selected.addAttr('thumb_bend', keyable=True)

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


