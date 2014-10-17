'''
Research Notes

Hannah Epling

Current Shelf Tools: FT, DH, CP, IK, Cluster, Controls, PaC, PVec, FLAttr, SpAttr, GrpAttr,
	Hierarchy, Padding, JRename, Priming, LockHide, Reset, AddAttr 
	
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: IK, PaC, OrC, PoC

Drop Down Menus: Controls

'''

'''
Each tool you will need document:
	1) MEL Commmand
	2) What type of command is it and how did you find it?
	3) Convert MEL to Python.
	4) Important Flags
'''

import pymel.core as pm

# KEY
	'''
	# Name
		Where the command was found.
		Important Flags.
		MEL
		Python
	'''

'''
General Tools Research
'''

# Freeze Transforms
	'''
	Found by Modify - Freeze Transforms. Echo All Commands was on for this. 
	Important Flags: Transforms, Rotate, Scale, Normals.
	'''
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)


# Delete History
	'''
	Found by Edit - Delete By Type - History. Echo All Commands was on for this.
	Important Flags: constructionHistory.
	'''
	DeleteHistory;
	delete -ch;

	pm.delete(ch=True)


# Center Pivot
	'''
	Found by Modify - Center Pivot. 
	Important Flags: centerPivots.
	'''
	CenterPivot;
	xform -cp;

	pm.xform(cp=True)


# Single Chain and Rotate Plan IKs
	'''
	Found by going under the Animation tab - Skeleton - IK Handle Tool Options
	Important Flags: Solver.
	'''
		# Rotate Plane
	ikHandle -sol ikRPsolver;

	pm.ikHandle(sol='ikRPsolver')

		# Single Chain
	ikHandle;

	pm.ikHandle()


# Cluster
	'''
	Found by going under the Surfaces Tab - Edit Curves - Selection - Cluster Curve
	Important Flags: none
	'''
	ClusterCurve;
	clusterCurve;

	pm.cluster()


# Grouping (Does not need to be included on Shelf!)
	'''
	Found by selecting an object and hitting Command + G
	Important Flags: none
	'''
	doGroup 0 1 1;

	pm.group ()


# Parenting (Does not need to be included on Shelf!)
	'''
	Found by selecting two objects and hitting P
	Important Flags: none
	'''
	parent;

	pm.paren
	t()

# Duplicating (Does not need to be included on Shelf!)
	'''
	Found by selecting an object and hitting Command + D
	Important Flags: returnRootsOnly
	'''
	duplicate -rr;

	pm.duplicate(rr=True)	


'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	'''
	Found by going under Create - NURBS Primatives - Circle.
	Important Flags: Normals, Radius
	'''
	circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;

	pm.circle()


# Square
	'''
	Found by Create - CV Curve tool (on liner) - Snapping to grid to create a square shape.
	Important Flags: Degree, Point, Knot 
	'''
	curve -d 1 -p -1 0 -1 -p -1 0 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;

	mel_line = 'curve -d 1 -p -1 0 -1 -p -1 0 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
	pm.mel.eval(mel_line)


# Cube
	'''
	Found by Create - CV Curve tool (on liner) - Snapping to cuve primative to create a cube shape.
	Important Flags: Degree, Point, Knot 
	'''
	curve -d 1 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;

	mel_line = 'curve -d 1 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;'
	pm.mel.eval(mel_line)


# Arrow
	'''
	Found by Create - CV Curve tool (on liner) - Snapping to grid to create an arrow shape.
	Important Flags: Degree, Point, Knot 
	'''
	curve -d 1 -p 1 0 -4 -p -1 0 -4 -p -1 0 1 -p -3 0 1 -p 0 0 5 -p 3 0 1 -p 1 0 1 -p 1 0 -4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

	mel_line = 'curve -d 1 -p 1 0 -4 -p -1 0 -4 -p -1 0 1 -p -3 0 1 -p 0 0 5 -p 3 0 1 -p 1 0 1 -p 1 0 -4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	pm.mel.eval(mel_line)



'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	'''
	Found under the Animation tab - Constrain - Parent.
	Important Flags: maintaintOffset, Weight.
	'''
		# With Offest On
	doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
	parentConstraint -mo -weight 1;

	pm.parentConstraint(mo=True, weight=1)
		
		# With Offest Off
	doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
	parentConstraint -weight 1;

	pm.parentConstraint(mo=False, weight=1)


# Orient Constraint
	'''
	Found under the Animation tab - Constrain - Orient.
	Important Flags: maintaintOffset, Weight.
	'''
		# With Offset On
	doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
	orientConstraint -mo -weight 1;

	pm.orientConstraint(mo=True, weight=1)

		# With Offset Off
	doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
	orientConstraint -offset 0 0 0 -weight 1;

	pm.orientConstraint(mo=False, weight=1)


# Point Constraint
	'''
	Found under the Animation tab - Constrain - Point.
	Important Flags: maintaintOffset, Weight.
	'''
		# With Offset On
	doCreatePointConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
	pointConstraint -mo -weight 1;

	pm.pointConstraint(mo=True, weight=1)

		# With Offset Off
	doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
	pointConstraint -offset 0 0 0 -weight 1;

	pm.pointConstraint(mo=False, weight=1)


# Pole Vector Constraint
# How does this constraint differ from the previous three.
	'''
	Found under the Animatio. tab - Constrain - Pole Vector.
	Important Flags: Weight.
	With this contraint, there are not as many values to deal with as the others.
	'''
	poleVectorConstraint -weight 1;

	pm.poleVectorConstraint(weight=1)



'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	'''
	Found by going into the Channel Box - Edit - Add Attribute - Select Float.
	Important Flags: Selection, Keyable
	'''
	selected = pm.ls(selection = True)
	print 'Current Selected:', selected

	first_selected = selected[0]
	first_selected.addAttr('attribute', keyable = True)

# Create Separator Attribute
	'''
	Found by going into the Channel Box - Edit - Add Attribute - Select Enum.
	Important Flags: Selection, Keyable, Lock, Attribute, Enum
	'''
	selected = pm.ls(selection = True)
	print 'Current Selected:', selected

	first_selected = selected[0]
	first_selected.addAttr('SEPARATOR', at= 'enum', en='------------:', keyable = True)
	first_selected.SEPARATOR.set(lock = True)


# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
	'''
	Found by creating a combination of Float and Enum attributes.
	Important Flags: Selection, Keyable, Lock, Attribute, Enum
	'''

	selected = pm.ls(selection = True)
	print 'Current Selected:', selected

	first_selected = selected[0]
	first_selected.addAttr('FINGERS', at= 'enum', en='------------:', keyable = True)
	first_selected.FINGERS.set(lock = True)
	first_selected.addAttr('CURL', at= 'enum', en='------------:', keyable = True)
	first_selected.CURL.set(lock = True)
	first_selected.addAttr('index_curl', keyable = True)
	first_selected.addAttr('middle_curl', keyable = True)
	first_selected.addAttr('pinky_curl', keyable = True)

	first_selected.addAttr('SPREAD', at= 'enum', en='------------:', keyable = True)
	first_selected.SPREAD.set(lock = True)
	first_selected.addAttr('index_spread', keyable = True)
	first_selected.addAttr('middle_spread', keyable = True)
	first_selected.addAttr('pinky_spread', keyable = True)

	first_selected.addAttr('THUMB', at= 'enum', en='------------:', keyable = True)
	first_selected.THUMB.set(lock = True)
	first_selected.addAttr('thumb_curl', keyable = True)
	first_selected.addAttr('thumb_drop', keyable = True)


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


