'''
Research Notes

Danny Restrepo

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
	# MEL Command:
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	// General Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=2)
	# Important Flags:
	-apply(-a), -translate(-t), -rotate(-r), -scale(-s), -preserveNormals(-pn)

# Delete History
	# MEL Command:
	delete -ch;
	// General Command (command help category)
	#Python Command
	import pymel.core as pm
	pm.delete(ch=True)
	# Important Flags:
	-constructionHistory(-ch)

# Center Pivot
	# MEL Command:
	xform -cp;
	// General Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.xform(cp=True)
	# Important Flags:
	-centerPivots(-cp)

# Single Chain and Rotate Plan IKs
	# MEL Command:
	ikHandle;
	ikHandle -sol ikRPsolver;
	// Animation Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.ikHandle
		or
	pm.ikHandle(sol=ikRPsolver)
	# Important Flags:
	-startJoint(-sj), -endEffector(-ee), -solver(-sol)

# Cluster
	# MEL Command:
	cluster;
	// Animation, Deformation Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.cluster
	# Important flags:
	-envelope(-en)

# Grouping (Does not need to be included on Shelf!)
	# MEL Command:
	group;
	// General Command (command help category)
	# Python Command
	import pymel.core as pm
	pm.group
	# Important Flags
	-empty(-em)

# Parenting (Does not need to be included on Shelf!)
	# MEL Command:
	parent;
	// General Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.parent
	# Important Flags:
	-world(-w)

# Duplicating (Does not need to be included on Shelf!)
	# MEL Command:
	duplicate;
	// General Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.duplicate
	# Important Flags:
	-returnRootsOnly(-rr)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	# MEL Command:
	circle -ch on -o on -nr 0 1 0 -r 5.164829;
	// Modeling, Curves Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.circle(ch=True, object=True, nr=(0,1,0), r=5
	# Important Flags:
	-constructionHistory(-ch), -object(-o), -normal(-nr), -radius(-r)

# Square
	# MEL Command:
	curve -d 1 -p 1.666667 0 1.666667 -p -1.666667 0 1.666667 -p -1.666667 0 -1.666667 -p 1.666667 0 -1.666667 -p 1.666667 0 1.666667 -k 0 -k 1 -k 2 -k 3 -k 4 ;
	// Modeling, Curves Command (command help category)
	# Python Command:
	import pymel.core as pm
	pm.curve(d=1, p=[(1, 0, 1), (-1, 0, 1), (-1, 0, -1), (1, 0, -1), (1, 0, 1)], k=[0,1,2,3,4])
	# Important Flags:
	-point(-p), -knot(-k), -degree(-d)

# Cube
	# MEL Command:
	curve -d 1 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;
	// Modeling, Curves Command (Command help category)
	#Python:
	import pymel.core as pm
	pm.curve(d=1, p=[(0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)(-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5)(-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
	# Important Flags:
	-degree(-d), -point(-p), -knot(-k)

# Arrow
	# MEL Command:
	curve -d 1 -p 3.333333 0 0 -p 0 0 3.333333 -p 0 0 1.666667 -p -3.333333 0 1.666667 -p -3.333333 0 -1.666667 -p 0 0 -1.666667 -p 0 0 -3.333333 -p 3.333333 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
	// Modeling, Curves Command (Command help category)
	# Python:
	import pymel.core as pm
	pm.curve(d=1, p=[(3.333333, 0, 0), (0, 0, 3.333333), (0, 0, 1.666667), (-3.333333, 0, 1.666667), (-3.333333, 0, -1.666667), (0, 0, -1.666667), (0, 0, -3.333333), (3.333333, 0, 0)], k=[0,1,2,3,4,5,6,7])
	# Important Flags:
	-degree(-d), -point(-p), -knot(-k)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	# MEL Command:
	parentConstraint -mo -weight 1;
	parentConstraint -weight 1;
	// Animation, Constraints Command (Command help category)
	# Python:
	import pymel.core as pm
	pm.parentConstraint(mo=True,weight=1)
	pm.parentConstraint(mo=False,weight=1)
	# Important Flags:
	-maintainOffset(-mo), -weight(-w)

# Orient Constraint
	# MEL Command:
	orientConstraint -mo -weight 1;
	orientConstraint -offset 0 0 0 -weight 1;
	// Animation, Constraints Command (Command help category)
	# Python:
	import pymel.core as pm
	pm.orientConstraint(mo=True,weight=1)
	pm.orientConstraint(offset=[0,0,0],weight=1)
	# Important Flags:
	-offset(-o), -maintainOffset(-mo), -weight(-w)

# Point Constraint
	# MEL Command:
	pointConstraint -mo -weight 1;
	pointConstraint -offset 0 0 0 -weight 1;
	// Animation, Constraints Command (Command help category)
	# Python:
	import pymel.core as pm
	pm.pointConstraint(mo=True,weight=1)
	pm.pointConstraint(offset=[0,0,0],weight=1)
	# Important Flags
	-offset(-o), -maintainOffset(-mo), -weight(-w)

# Pole Vector Constraint
# How does this constraint differ from the previous three.
	# Doesn't Have an offset
	# MEL Command:
	poleVectorConstraint -weight 1;
	// Animation, IK Command (Command help category)
	# Python:
	import pymel.core as pm
	pm.poleVectorConstraint(weight=1)
	# Important Flags:
	-weight(-w)

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

# Create Separator Attribute

# Template Attributes 
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


