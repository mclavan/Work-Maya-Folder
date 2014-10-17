'''
JohnsonKevin
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
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

	# Did not require echo.
	'''

	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	'''
	# Flags
	# apply
	'''


# Delete History
	'''
	DeleteHistory;
	delete -ch;

	# Requires echo to be turned on.
	'''

	pm.delete(ch=True)

	'''
	# Flags
	# ch
	'''


# Center Pivot
	'''
	CenterPivot;
	xform -cp;

	# Requires echo to be turned on.
	'''

	pm.xform(cp=True)

	'''
	# Flags
	# cp
	'''



# Single Chain and Rotate Plane IKs
	'''
	# Single Chain
	select -r joint1.rotatePivot ;
	select -add joint2.rotatePivot ;
	ikHandle;

	# Does not require echo
	'''

	import pymel.core as pm 

	selected = pm.ls(selection=True)
	print 'current selected', selected

	pm.ikHandle(sol='ikSCsolver')

	'''
	# Flags
	# sol
	'''

	'''
	# Rotate Plane
	select -r joint5.rotatePivot ;
	select -tgl joint3.rotatePivot ;
	ikHandle -sol ikRPsolver;

	# Does not Require echo
	'''

	import pymel.core as pm 

	selected = pm.ls(selection=True)
	print 'current selected', selected

	pm.ikHandle(sol='ikRPsolver')

	'''
	# Flags
	# sol
	'''



# Cluster
	'''
	ClusterCurve;

	# Requires echo to be turned on.
	'''

	pm.Cluster()

# Grouping (Does not need to be included on Shelf!)
	'''
	doGroup 0 1 1;

	# Echo not required
	'''

	pm.group()

# Parenting (Does not need to be included on Shelf!)
	'''
	parent;

	# Echo not required
	'''

	pm.parent()

# Duplicating (Does not need to be included on Shelf!)
	'''
	duplicate -rr:

	# Echo not required
	'''

	pm. duplicate()



'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	'''
	circle -normal 1 0 0;

	'''

	pm.circle( nr = (0, 1, 0))

	'''
	# Flags
	# nr
	'''

# Square
	'''
	mel_line = 'curve -d 1 -p 5 0 5 -p 5 0 0 -p 10 0 0 -p 10 0 5 -p 5 0 5 -k 0 -k 1 -k 2 -k 3 -k 4;'

	# Create a primitive polygon cube, and traced one face.
	'''

	pm.mel.eval(mel_line)


# Cube
	'''
	mel_line = 'curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;'

	# Create a primitive polygon cube, and traced the edges
	'''

	pm.mel.eval(mel_line)

# Arrow
	'''
	mel_line = 'curve -d 1 -p 9.068954 0 7.988272 -p 9.103088 0 6.93281 -p 8.008158 0 6.964105 -p 8.042444 0 5.985507 -p 6.055032 0 7.440648 -p 8.090532 0 8.959941 -p 8.124827 0 7.981345 -p 9.144465 0 7.95112 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	
	# Used CV Curve tool, and draw an arrow on the grid.
	'''

	pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	'''
	# doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
	# parentConstraint -mo -weight 1;

	# Echo not required
	'''

	pm.parentConstraint

# Orient Constraint
	'''
	# doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
	# orientConstraint -offset 0 0 0 -weight 1;

	# Echo not required
	'''

	pm.orientConstraint

# Point Constraint
	'''
	# doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
	# pointConstraint -offset 0 0 0 -weight 1;

	# Echo not required
	'''

	pm.pointConstraint

# Pole Vector Constraint
	'''
	# poleVectorConstraint -weight 1;

	# Echo not required
	'''

	pm.poleVectorConstraint

# How does this constraint differ from the previous three.
	'''
	# The pole vector does not have a list attatched to its MEL command.
	'''

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

# Create Separator Attribute
	
	'''
	addAttr -ln "FINGERS" -at "enum" -en "Green:Blue:" |group1;
	setattr -e-keyable true |group1.FINGERS;

	addAttr -ln "CURL" -at "enum" -en "-----------:"
	setAttr -e-keyable true |group1.CURL;
	'''

	first_selected.addAttr('FINGERS', keyable=True
		at='enum', en="-----------:"
	first_selected.FINGERS.set(lock=True)

# Template Attributes 
	
	'''
	FINGERS
	CURL
	index_curl
	middle_curl
	pinky_curl
	'''

	first_selected.addAttr('FINGERS', keyable=True,
		at='enum', en="-----------:")
	first_selected.FINGERS.set(lock=True)
	first_selected.add('CURL', keyable=True,
		at='enum', en="-----------:")
	first_selected.CURL.set(lack=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', keyable=True,
		at='enum', en="-----------:")
	first_selected.SPREAD.set(lack=True)
	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	first_selected.addAttr('THUMB', keyable=True,
		at='enum', en="-----------:")
	first_selected.THUMB.set(lack=True)
	first_selected.addAttr('thumb_drop', keyable=True)
	first_selected.addAttr('thumb_spread', keyable=True)


# Create a group of attributes at one time.  
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


