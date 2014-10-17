'''
Research Notes

Ethan Holbert

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
makeIdentity -apply True -t 1 -r 1 -s 1 -n 0 -pn 1;
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

# Delete History
delete -ch "targetName";
pm.mel.DeleteHistory()

# Center Pivot
CenterPivot;
pm.centerPivot()

# Single Chain and Rotate Plan IKs

# Cluster

# Grouping (Does not need to be included on Shelf!)
pm.group()

# Parenting (Does not need to be included on Shelf!)
parentConstraint "lt_armFK_bind" "lt_armFK_icon";

# Duplicating (Does not need to be included on Shelf!)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
circle -sections 16 -radius 3.5 -normal 1 0 0;
pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3)

# Square
pm.square(name=Ct_name_icon, normal=[1, 0, 0])

# Cube
pm.cube(name=Ct_name_icon, normal=[1, 0, 0])

# Arrow
pm.arrow(name=Ct_name_icon, normal=[1, 0, 0])


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
pm.parentConstraint()

# Orient Constraint
pm.orientConstraint()

# Point Constraint
pm.pointConstraint(mo=True)

# Pole Vector Constraint
pm.poleVector()

# How does this constraint differ from the previous three.

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


