'''
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
	1)makeIdentity -apply	true -t 1 -r 1 -s 1 -n 
	2)CMD, Modify> Freeze Transforms
	3)pm.makeIdentity()
	4)apply, t,s,n
	'''

# Delete History
	'''
	1)DeleteHistory
	2)CMD,Edit> DeleteAllbyType
	3)delete()
	4)(ch)
	'''

# Center Pivot
	'''
	1)CenterPivot
	2)CMD, Modify> Center Pivot
	3)pm.mel.CenterPivot
	4)none
	'''

# Single Chain and Rotate Plan IKs
	'''
	1)ikHandle
	2)Runtime CMD, skeleton> IK_Handle_Tool
	3)pm.mel.IK_Handle_Tool()
	4)none
	'''

# Cluster
	'''
 	1)cmds.cluster( rel=True )
 	2)
 	3)
 	4)
	'''

# Grouping (Does not need to be included on Shelf!)

# Parenting (Does not need to be included on Shelf!)

# Duplicating (Does not need to be included on Shelf!)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	'''
	1)circle
	2)CMD, Create> Nurbs_Primitives> Circle
	3)pm.circle()
	4)c, nr, sw, r, d, ut, tol, s, ch
	# use values for mel and command flags for Python
	''' 

# Square
	'''
	1)curve
	2)CMD, Create> Nurbs_Primitives> Square
	3)pm.mel.eval()
	4)mel_line (Use the flags from the mel commands then insert them into the python commands)
	'''

# Cube
	'''
	1)curve
	2)CMD, Create> Nurds_Primitives> Cube
	3)pm.mel.eval()
	4)mel_line (Use the flags from the mel commands then insert them into the python commands)
	'''

# Arrow
	'''
	1)curve
	2)CMD, Create> CV_Curve_Tool
	3)pm.mel.eval()
	4)mel_line (Use the flags from the mel commands then insert them into the python commands)
	'''


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	'''
	1)parentConstraint
	2)CMD,Constraint> Parent
	3)pm.parentConstraint()
	4)mo
	'''

# Orient Constraint
	'''	
	1)orientConstraint
	2)CMD, Constraint>Orient
	3)pm.orientConstraint()
	4)mo
	'''

# Point Constraint
	'''
	1)pointConstraint
	2)CMD, Constraint>Point
	3)pm.pointConstraint()
	4)mo
	'''

# Pole Vector Constraint
	'''
	# How does this constraint differ from the previous three.
	
	The pole vector controls the rotation of both the icon control and the ik handle. 
	The constraint is usually placed infront of the knee.

	1)poleVectorConstraint
	2)CMD, Constraint> Pole Vector
	3)pm.poleVectorConstraint()
	4)none

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


