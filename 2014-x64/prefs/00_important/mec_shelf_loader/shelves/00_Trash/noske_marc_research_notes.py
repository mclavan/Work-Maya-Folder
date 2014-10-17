'''
Research Notes

Name: Marc Dennis Noske

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
pm.makeIdentity(apply=True t=1, r=1, s=1, n=0)

#Flags
	# -a = Apply
	# -t = Translate
	# -r = Rotate
	# -s = Scale
	# -n = Normal
	# -pn = Preserve Normal

# Delete History
	#MEL Command
		DeleteHistory

	#Python  Command
		pm.delete(ch=True)

#Flag
	# -ch = Constrution History
...
- I had to turn on Echo in order to see it in the Script Editor

# Center Pivot
	#MEL Command
	-CenterPivot;

	#Python Command:
	import pymel.core as pm
	pm.xform(cp=1)

	#Flag
		# -cp = Center Pivots

# Single Chain and Rotate Plan IKs
	#MEL Command
	ikHandle -sol ikRPsolver
	ikHandle -sol ikSCsolver

	#Python Command
	-import pymel.core as pm
	pm.ikHandle(sol= 'ikRPsolver')
	-import pymel.core as pm
	pm.ikHandle(sol= 'ikSCsolver')

	#Flag
		# -sol = Solver

# Cluster
	#MEL Command
	newCluster "-envolope 1"

	#Python Command
	pm.cluster(en=1)

	#Flag
		# -en = envolope
	...
		- In order to find this command I had to turn on echo;

# Grouping (Does not need to be included on Shelf!)
	#MEL Command
	Group -w 1;

	#Python Command
	pm.group(w=1)

	#Flag
		# -w = world

# Parenting (Does not need to be included on Shelf!)
	#MEL Command
	parent;

	#Python Command
	pm.parent('ikHandle1', 'null1', add=True)

# Duplicating (Does not need to be included on Shelf!)
	#MEL Command

	#Python Command
	
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3, s=16, ch=1)

# Square
pm.curve(d=1, p[[-1.2, 0, -1.2], [1.2, 0, -1.2], [1.2, 0, 1.2], [-1.2, 0, 1.2], [-1.2, 0, -1.2]], k=[0, 1, 2, 3, 4,])

# Cube
pm.curve(d=1, p=[[-3.929348, 3.929348, 3.929348], [3.929348, 3.929348, 3.929348], [3.929348, -3.929348, 3.929348], [-3.929348, -3.929348, 3.929348], [-3.929348, 3.929348, 3.929348], [-3.929348, 3.929348, -3.929348], [-3.929348, -3.929348, -3.929348], [-3.929348, -3.929348, 3.929348], [-3.929348, -3.929348, -3.929348], [-3.929348, -3.929348, 3.929348], [-3.929348, 3.929348, 3.929348], [-3.929348, 3.929348, -3.929348], [-3.929348, -3.929348, -3.929348], [3.929348, -3.929348, -3.929348], [3.929348, 3.929348, -3.929348], [-3.929348, 3.929348, -3.929348], [3.929348, 3.929348, -3.929348], [3.929348, 3.929348, 3.929348], [3.929348, -3.929348, 3.929348], [3.929348, -3.929348, -3.929348], [3.929348, 3.929348, -3.929348], [3.929348, 3.929348, 3.929348], [-3.929348, 3.929348, 3.929348], [-3.929348, -3.929348, 3.929348], [3.929348, -3.929348, 3.929348], [3.929348, 3.929348, 3.929348]], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# Arrow
pm.curve(d=1, p[[0, 0, -1.8], [-1.8, 0, -3] [-0.6, 0, -3], [0, 0, -6], [0.6, 0, -3], [1.8, 0, -3], [0, 0, -1.8]], k=[0, 1, 2, 3, 4, 5, 6])

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	-offset on
		pm.parentConstraint(mo=True)
	-offset off
		pm.parentConstraint(mo=True)

# Orient Constraint
	-offset on
		pm.orientConstraint(mo=True)
	-offset offset
		pm.orientConstraint(mo=True)

# Point Constraint
	-offset on
		pm.pointConstraint(mo=True)
	-offset off
		pm.pointConstraint(mo=True) 

# Pole Vector Constraint
	-Weight on
		pm.poleVectorConstraint(w=1)
	-Weight off
		pm.poleVectorConstraint(w=0)

# How does this constraint differ from the previous three.
The poleVectorConstraint is different from the other three because it uses w or weight instead of mo which is maintain offset.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
first_selected.addAttr('indexCurl', keyable=True)

# Create Separator Attribute
first_selected.addAttr('Fingers', at='enum', en="--------------")
first_selected.addAttr('Fingers', keyable=False)

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


