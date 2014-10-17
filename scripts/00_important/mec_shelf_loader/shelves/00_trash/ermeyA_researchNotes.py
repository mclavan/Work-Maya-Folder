'''
Research Notes

Name
Ariel Ermey

Current Shelf Tools: 21
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 0

Drop Down Menus: 0

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

	# Mel Command:
		makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	# Python Command:
		pm.makeIdentity(apply=True, t=1, r=1, n=0)
	#			-----------Flags-----------
			rotate(r) 
			scale(s)
			translate(t)
			normal(n)
			jointOrient(jo)
			preserveNormals(pn)
# Delete History

	# Mel Command:
		DeleteHistory;
	# Python Command:
		pm.delete(ch=True)
	#			-----------Flags-----------
			contructionHistory(ch)

# Center Pivot
	# Mel Command:
	CenterPivot;

	# Python Command:
	xform(cp)
	#----------Flag----------
	centerPivots(cp)
	rotatePivot(rp)
	scalePivot(sp)

# Single Chain and Rotate Plan IKs
# Single Chain
	# Mel Command:
	ikHandle;

	# Python Command:
	pm.ikHandle(sol='ikScsolver')

# Rotate Plain
	# Mel Command:
	ikHandle -sol ikRPsolver;

# Cluster
	# Mel Command:
	ClusterCurve;

import pymel.core as pm

selected = pm.ls(selection=True)
first_selected = selected[0]

# pm.cluster()

# Grouping (Does not need to be included on Shelf!)
	# Mel Command: 
	doGroup 0 1 1;

# Parenting (Does not need to be included on Shelf!)
	# Mel Command:
	parent;

# Duplicating (Does not need to be included on Shelf!)
	# Mel Command:
	duplicate -rr;
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	# Mel Command:
	circle -ch on -o on -nr 0 1 0 -r 1.178146 ;

	# Python Command:
	pm.circle()
	#	---------Flags---------------
		name(n)
		constructionHistory(ch)
		object(o)

# Square
	# Mel Command:
	curve -d 1 -p -6.018917 0 1.021753 -p -3.946304 0 1.011708 -p -3.964546 0 3.022193 -p -5.970381 0 3.007124 -p -6.036268 0 1.025252 -k 0 -k 1 -k 2 -k 3 -k 4 ;

	# Python Command:

# Cube
	# Mel Command:
	curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;

# Arrow
	# Mel Command:
	curve -d 1 -p -0.965969 0 4.048459 -p 1.009226 0 4.003205 -p 1.045404 0 6.993132 -p 2.032963 0 7.020764 -p -0.012523 0 9.015782 -p -2.007876 0 7.03083 -p -0.975245 0 7.010264 -p -0.990367 0 4.048374 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	# Driver -> Driven.
	# Mel Command:
	doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };

	# Python Command:
	pm.parentConstraint()
	#------------Flags-------------
	name(n)
	remove(rm): removes the listed target(s) from the constraint. 

# Orient Constraint
	# Mel Command:
	doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };

	# Python Command:
	pm.orientConstraint()
	#-------------Flags---------------
	name(n)
	remove(rm):removes the listed target(s) from the constraint. 

# Point Constraint
	# Mel Command:
	doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };

# Pole Vector Constraint
	# Mel Command:
	poleVectorConstraint -weight 1
# How does this constraint differ from the previous three.
# It selects one or more targets followed by the Rotate Plane ikHandle to constrain.
	# It is made just for the RP Solver ik handle

'''
Attributes (Convered in Podcast)
'''
import pymel.core as pm
# Getting the selected object.
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Objects:', first_selected

# Create float attribute
first_selected.addAttr('index_curl', keyable=True)

# Create Separator Attribute
addAttr -ln "Separator"  -at "enum" -en "----------------:"  |nurbsCircle1;
setAttr -e-keyable true |nurbsCircle1.Seperater;

first_selected.addAttr('FINGERS', keyable=True,
	 at='enum', en="----------------:")


# Template Attributes 
FINGERS
CURL
Pinky

first_selected.addAttr('FINGERS', keyable=True,
	 at='enum', en="----------------:")
first_selected.addAttr('CURL', keyable=True,
	 at='enum', en="----------------:")
first_selected.addAttr('Pinky', keyable=True,
	 at='enum', en="----------------:")

# Create a group of attributes at one time.  
# The finger attributes are an example.
# Code to create a shelf button for this.
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)

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


