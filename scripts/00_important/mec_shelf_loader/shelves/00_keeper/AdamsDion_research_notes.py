'''
Research Notes

Dion Adams


Current Shelf Tools:
'''
# Icons
	# Arrow
	# Square
	# Circle
	# Cube
# Tools
	# Center pivot
*	# IK handle (single click SC, double click RP)
	# Freeze Ttansformations
	# Delete history
*	# Lock and Hide (Drop down to choose translations or rotations )
*	# Unlock and Show (Drop down to choose translations or rotations )
# Constraints
*	# Point Constraint (Single click no offset, Double click to maintain offset)
*	# Parent Constraint (Single click no offset, Double click to maintain offset)
*	# Orient Constraint (Single click no offset, Double click to maintain offset)
*	# Pole Vector Constraint (Single click No offset, Double click to maintain offset)
	# Cluster


	'''
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: Above ^^^

Drop Down Menus: Above ^^^

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
	# 1.makeIdentity -apply true, -t 1, -r 1, -s 1, -n 0;
	# 2.Resets the selected transform and all of its children down to the shape level by the identity transformation.
	#   Selected a sphere and selected freeze transforms in menu bar the got the command from the script editor.
	# 3. pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0) 
	# 4. (a) -apply - If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false. 
# Delete History
	# 1. delete -ch;
	# 2. This command is used to delete selected objects, or all objects, or objects specified along with the command. 
	#    Created a sphere and used the echo all button to get the code from the script editor after selecting delete history in the drop down menu.
	# 3. pm.mel.DeleteHistory()
	# 4. (ch) -constructionHistory - Remove the construction history on the objects specified or selected.

# Center Pivot
	# 1. xform -cp
	# 2. This command can be used query/set any element in a transformation node. It can also be used to query some values that cannot be set directly such as the transformation matrix or the bounding box.
	#    Used the echo all button to get the code from the script editor after selesting center pivot in the drop down menu.
	# 3. pm.xform()
	# 4. (cp) -centerPivot - Set pivot points to the center of the object's bounding box.

# Single Chain and Rotate Plan IKs
	# 1. ikHandle -s 0; ikHandle -sol ikRPsolver -s 0; 
	# 2. The handle command is used to create, edit, and query a handle within Maya. The standard edit (-e) and query (-q) flags are used for edit and query functions.
	# 3. pm.ikhandle()
	# 4.
# Cluster
	# 1. cluster -em
	# 2. The cluster command creates a cluster or edits the membership of an existing cluster. The command returns the name of the cluster node upon creation of a new cluster.
	# 3. pm.cluster(em=1)
# Grouping (Does not need to be included on Shelf!)
	# 1. doGroup 0 1 1;
	# 2. This command groups the specified objects under a new group and returns the name of the new group.
	# 3. pm.group()
# Parenting (Does not need to be included on Shelf!)
	# 1. parent;
	# 2. This command parents (moves) objects under a new group, removes objects from an existing group, or adds/removes parents.
	# 3. pm.parent()
# Duplicating (Does not need to be included on Shelf!)
	# 1. duplicate -rr;
	# 2. This command duplicates the given objects. If no objects are given, then the selected list is duplicated.
	# 3. pm.duplicate(rr=1)
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	# Creates a circle icon.
	# circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; 
	# pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1;
	# (-n) -name - s the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.
	# (-ch) -constructionHistory - Turn the construction history on or off
	# (-o) -object - Create the result, or just the dependency node
# Square
	# Creates a square icon.
	# curve -d 1 -p -5 0 -5 -p 5 0 -5 -p 5 0 5 -p -5 0 5 -p -5 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 ;
	# mel_line = 'curve -d 1 -p -5 0 -5 -p 5 0 -5 -p 5 0 5 -p -5 0 5 -p -5 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
	# pm.mel.eval(mel_line)
	# (-bez) -bezier - The created curve will be a bezier curve.
	# (-d) -degree - The degree of the new curve. Default is 3. Note that you need (degree+1) curve points to create a visible curve span. eg. you must place 4 points for a degree 3 curve.
	# (-r) -replace - Replaces an entire existing curve. If you use this flag, you must specify the name of the curve to replace, at the end of the command.
# Cube
	# Creates a cube icon.
	# curve -d 1 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;
	# mel_line = 'curve -d 1 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
	# pm.mel.eval(mel_line)
# Arrow
	# Create an arrow icon.
	# curve -d 1 -p -5 0 5 -p -10 0 5 -p 0 0 -5 -p 10 0 5 -p 5 0 5 -p 5 0 15 -p -5 0 15 -p -5 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
	# mel_line = 'curve -d 1 -p -5 0 5 -p -10 0 5 -p 0 0 -5 -p 10 0 5 -p 5 0 5 -p 5 0 15 -p -5 0 15 -p -5 0 5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	# pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	# 1. parentConstraint -mo -weight 1;
	# 2. Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s).
	# 3. pm.parentConstraint()
	# 4. (-mo) -maintainOffset - The offset necessary to preserve the constrained object's initial orientation will be calculated and used as the offset.
	#    (-w) -weight - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
# Orient Constraint
	# 1. orientConstraint -offset 0 0 0 -weight 1;
	# 2. Constrain an object's orientation to match the orientation of the target or the average of a number of targets.
	# 3. pm.orientConstraint()
	# 4. (-w) -weight - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
	#	 (-mo) -maintainOffset - The offset necessary to preserve the constrained object's initial orientation will be calculated and used as the offset.
	#	 (-n) -name - Sets the name of the constraint node to the specified name.
# Point Constraint
	# 1. pointConstraint -offset 0 0 0 -weight 1;
	# 2. Constrain an object's position to the position of the target object or to the average position of a number of targets.
	# 3. pm.orientConstraint()
	# 4. (-o) -offset - Sets or queries the value of the offset. Default is 0,0,0.
	#    (-w) -weight - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
# Pole Vector Constraint
	# 1. poleVectorConstraint -weight 1;
	# 2. Constrains the poleVector of an ikRPsolve handle to point at a target object or at the average position of a number of targets.
	# 3. poleVectorConstraint()
	# 4.(-w) -weight - Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
# attribute_name = raw_input()
# first_selected.addAttr(attribute_name, keyable=True)
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


