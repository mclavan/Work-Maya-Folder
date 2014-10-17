'''
Research Notes

Name: Huston Petty

Current Shelf Tools: 
	- Nuke Button 
	- Delete History
	- Freeze Transforms 
	- Center Pivot
	- Square Icon
	- Circle Icon
	- Triangle Icon 
	- Arrow Icon 
	- Cube Icon
	- Pyramid Icon 
	- Joint Tool (not python)
	- Single Chain IK creator; selection based
	- Rotate Plane IK creator; selection based
	- Spline IK creator; selection based
	- Cluster: all selected CVs on a curve
	- Local Orientation; parentConstraint(mo=False) 
	- Parent Contraint
	- Orient Contraint
	- Point Constraint
	- Pole Vector Constraint
	- Unlock and Show
	- Prime
	- Custom Float Attribute Name
	- Custom Separator Attribute Name
	- Custom Boolean Attribute Name
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
	# Makes transformation attributes set to clean values
	pm.makeIdentity(bat_grp, apply=True, t=1, r=1, s=1, n=0)

	#-----------------------FLAGS------------------------
		# apply - (a) 'True' means transforms are frozen; 'False' means transforms are NOT frozen
		# translate - (t) 'True' = translations are frozen; 'False' = translations are NOT frozen
		# rotate - (r) 'True' = rotations are frozen; 'False' = rotations are NOT frozen
		# scale - (s) 'True' = scale is frozen; 'False' = scale is NOT frozen
		# normal - (n) 'True' = normals are frozen; 'False' = normals are NOT frozen



# Delete History
	# Deleting history on an object is another form of cleaning it up for its intended use
	pm.delete(constructionHistory=True)

	# To delete the history of one or more specific objects simply specify its name/variable before the constructionHistory flag
	pm.delete('cube', ch=True)
	pm.delete('cube', 'cube1', 'cube2', ch=True)

	#-----------------------FLAGS------------------------
		# all - (all) Remove all objects of specified kind, in the scene; Used in conjunction with other flags
		# constructionHistory - (ch) Deletes any history made in process of making or editing objects/systems
		# constraints - (cn) Deletes specified constraints



# Center Pivot
	# Places objects pivot point at the center of its bounding box
	pm.xform(centerPivots=True) 

	# To center pivots of one or more specific objects simply specify its name/variable before the centerPivots flag
	pm.xform('cube', 'cube1', 'cube2', cp=True)

	#-----------------------FLAGS------------------------
		# centerPivots - (cp) 'True' = pivots are centered in bounding box



# Single Chain and Rotate Plan IKs
	# Single Chain - used for systems with no bending point (ex. clavicle); one bind and one waste joint
	pm.ikHandle(name='ikHandle', startJoint='joint1', endEffector='joint2', solver='ikSCsolver')

		#To create an IK handle from selection
		import pymel.core as pm 
		selected_joints = pm.ls(selection=True)
		pm.ikHandle(sj=selected_joints[0], ee=selected_joints[1], sol= 'ikSCsolver')

	# Rotate Plane - used for systems with bending point (ex. elbow, knee, etc.)
	pm.ikHandle(n='ikHandle', startJoint='joint1', endEffector='joint3', solver='ikRPsolver')

		# To create an IK handle from selection
		import pymel.core as pm 
		selected_joints = pm.ls(selection=True)
		pm.ikHandle(sj=selected_joints[0], ee=selected_joints[1], sol= 'ikRPsolver')

	# Spline Handle - uses control vertices of a nurbs curve to control joint movement
	pm.ikHandle(n='ikHandle', sj='joint1', ee='joint5', curve='curve1', createCurve=False, parentCurve=False, solver='ikSplineSolver')

		#To create an IK handle from selection
		import pymel.core as pm 
		selected_objects = pm.ls(selection=True)
		pm.ikHandle(sj=selected_objects[0], ee=selected_objects[1], curve=selected_objects[2], createCurve=False, parentCurve=False, solver='ikSplineSolver')

	# ALL OF THE IK TOOLS can be used in conjunction with a list command with its selection flag set to true in order to make an easy to use button the works based on selection order.
	selected_joints = pm.ls(selection=True)
	pm.ikHandle(sj=selected_joints[0], ee=selected_joints[1], sol= 'ikRPsolver')



	#---------------------FLAGS--------------------
		# name - (n) Specify name for new IK handle
		# startJoint - (sj) Specify the name of the starting join in IK handle
		# endEffector - (ee) Specify the name of the ending join in IK handle
		# solver - (sol) Specify the type of IK solver is being created (ex. ikRPsolver, ikSCsolver, and ikSplineSolver)
		# ASK ABOUT setupForRPsolver - (srp)

	# -----------SPLINE SOLVER ONLY FLAGS----------
		# curve - (c) Specify the curve that IK system will follow; only used on ikSplineSolver
		# parentCurve - (pcv) 'False' = curve does not get parented to root joint of chain
		# createCurve - (ccv) 'False' = curve will NOT automatically be created for the ikSplineHandle; create custom curve instead



# Cluster
	# Clustering is the process of putting transform nodes onto a single or multiple vertices. This enables them to be controlled by icons and animated.
	pm.cluster()

	# Clustering multpile vertices at once can be done through a list with its flatten flag set to true and a for loop
	selected_verts = pm.ls(sl=True, fl=True)
	for indiv_cv in selected_verts:
    	pm.cluster(indiv_cv)

	


# Grouping (Does not need to be included on Shelf!)
	# Grouping will create a group of any objects selected
	pm.group()

	# To group in proper order the last group will need to be created first
	pm.group(n= 'son')
	pm.group(n= 'father')
	pm.group(n= 'grandFather')

	# Empty groups can be created in any order but a special 'empty' flag must be applied
	pm.group(em=True, n= 'grandFather')
	pm.group(em=True, n= 'son')
	pm.group(em=True, n= 'father')

	#---------------------FLAGS--------------------
		# name - (n) Sets the name seen in the outliner
		# empty - (em) When set to 'True' or 'False' an empty group can be created
	


# Parenting (Does not need to be included on Shelf!)
	# Parenting takes two selected objects and creaters a hierarchy based on selection order.
	pm.parent()

	# Parenting works differently than normal grouping, select the DRIVEN FIRST and DRIVER LAST. Only works on two objects per command line
	pm.parent('son', 'father')
	pm.parent('father', 'grandFather')

	
		
# Duplicating (Does not need to be included on Shelf!)
	# Makes a copy of specific object(s) 
	pm.duplicate()
	pm.duplicate('curve1')



'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	# Creates nurbs circle for contol icons; mainly used in FK systems
	pm.circle()

	# Creates a nurbs circle control icon facing up on the Y axis
	pm.circle(normal=[0, 1, 0])
	
	# Creates a nurbs circle control icon facing up on the X axis
	pm.circle(normal=[1, 0, 0])

	#--------------------FLAGS------------------
		# normal - (nr) Changes the direction object faces
		# radius - (r) Size of circle
		# sections - (s) Amount of control points
		# degree - (d) type of curve created 
	


# Square
	#Creates a nurbs square, deletes its history, and freezes its transforms.
	pm.curve(d=1, p=[[-1, 0, -1], [1, 0, -1], [1, 0, 1], [-1, 0, 1], [-1, 0, -1]], k=[0, 1, 2, 3, 4])

		#OR

	square_icon = pm.circle(r=1.415, s=4, d=1, nr=[0, 1, 0], n='square_icon')
	pm.rotate(0, 0, '45deg')
	pm.makeIdentity(square_icon, apply=True, t=1, r=1, s=1, n=0)
	pm.delete(square_icon, constructionHistory=True)



# Cube
	# Creates a cube shaped control icon; usually for head, hands, hips, etc.
	icon = pm.curve(degree=1, p=[[1, 2, 1], [-1, 2, 1], [-1, 2, -1], [1, 2, -1], [1, 2, 1], [1, 0, 1], [1, 0, -1], [1, 2, -1], [1, 0, -1], [-1, 0, -1], [-1, 2, -1], [-1, 0, -1], [-1, 0, 1], [-1, 2, 1], [-1, 0, 1], [1, 0, 1], [1, 2, 1]], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
	pm.xform(icon, centerPivots=True)


# Arrow
	# Creates a typical arrow shaped control icon
	pm.curve(d=1, p=[[-0.5, 0, 2], [0.5, 0, 2], [0.5, 0, 0], [1, 0, 0], [0, 0, -2], [-1, 0, 0], [-0.5, 0, 0], [-0.5, 0, 2]], k=[0, 1, 2, 3, 4, 5, 6, 7])



'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	# Parent Contraints are a way of parenting objects to one another without being confined to a hierarchy; They are selected DRIVER FIRST and then DRIVEN LAST; 
	pm.parentConstraint(mo=True)

	# Parent constraints can also be used with maintainOffset OFF which will cause one object to snap to the orientation and position of another object.
	pm.parentConstraint(mo=False)

	# This constraint can be used in conjunction to a list command with its selection flag set to true in order to make an easy to use button the works based on selection order.
	selected_objects = pm.ls(selection=True)
	pm.parentConstraint(selected_objects[0], selected_objects[1], mo=True)
	

	#---------------------FLAGS--------------------
	# maintainOffset - (mo) 'True' = offset orientation maintained; 'False' = second object selected will be oriented and placed same as first object selected



# Orient Constraint
	# Orient constraint is a form of constraining one object to another only through the objects rotation.
	pm.orientConstraint(mo=True)

	# This constraint can be used in conjunction to a list command with its selection flag set to true in order to make an easy to use button the works based on selection order.
	selected_objects = pm.ls(selection=True)
	pm.orientConstraint(selected_objects[0], selected_objects[1], mo=True)

	#---------------------FLAGS--------------------
	# maintainOffset - (mo) 'True' = offset orientation maintained; 'False' = second object selected will be oriented and placed same as first object selected



# Point Constraint
	# Point constraint is a way of constraining one object to another only through the objects translations.
	pm.pointConstraint(mo=True)

	# This constraint can be used in conjunction to a list command with its selection flag set to true in order to make an easy to use button the works based on selection order.
	selected_objects = pm.ls(selection=True)
	pm.pointConstraint(selected_objects[0], selected_objects[1], mo=True)

	#---------------------FLAGS--------------------
	# maintainOffset - (mo) 'True' = offset orientation maintained; 'False' = second object selected will be oriented and placed same as first object selected



# Pole Vector Constraint
	# Pole Vectors are constraints used to assign a control to aim the elbow of an IK system at
	pm.poleVectorConstraint()

		# This constraint is different from the rest of the constraints in that it it does not require a maintainOffset flag to be specified, it only requires the two objects used to be specified.

	# This constraint can be used in conjunction to a list command with its selection flag set to true in order to make an easy to use button the works based on selection order.
	selected_objects = pm.ls(selection=True)
	pm.poleVectorConstraint(selected_objects[0], selected_objects[1])



'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	# When creating a float attribute one needs to name the attribute and make it keyable for it to be visible in Channel Box
	first_selected.addAttr('attributeName', keyable=True)

# Create Separator Attribute
	# When creating a separator attribute it is important to name it properly, make it keyable,  
	# specify that it is an 'enum' attribute, and then name the name(s) of the item(s) in the enum list.
	first_selected.addAttr('SEPARATOR', keyable=True, attributeType='enum', enumName='---------:')

	# Then it is important to lock the attribute in the next line 
	first_selected.SEPARATOR.set(lock=True)


# Template Attributes 
	#To create a template of attributes one must type all code for each desired attribute.
	first_selected.addAttr('FINGERS', keyable=True, at='enum', en= '-----------:')
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('CURL', keyable=True, at='enum', en= '-----------:')
	first_selected.CURL.set(lock=True)

	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('ring_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', keyable=True, at='enum', en= '-----------:')
	first_selected.SPREAD.set(lock=True)

	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('ring_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	first_selected.addAttr('THUMB', keyable=True, at='enum', en= '-----------:')
	first_selected.THUMB.set(lock=True)	

	first_selected.addAttr('thumb_curl', keyable=True)
	first_selected.addAttr('thumb_spread', keyable=True)
	first_selected.addAttr('thumb_drop', keyable=True)

	first_selected.addAttr('VISIBILITY', keyable=True, at='enum', en= '-----------:')
	first_selected.VISIBILITY.set(lock=True)	

	first_selected.addAttr('icons_vis', keyable=True, at='bool')

	#---------------------FLAGS--------------------
	# keyable - (k) True enables the object to be visible in channel box and be keyed
	# maxValue - (max) Maximum value for attribute
	# minValue - (min) Minimum value for attribute
	# lock - (l) locks or unlocks an attribute
	# hidden - (h) hides the attribute 
	# attributeType - (at) specify the type of attribute you are creating
	# enumName - (en) specify the name of created attrinute


'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.
'''

Research:
# Detach Component - Runtime command that Detaches selected components(edges or vertices) from mesh 
# A 'Separate' command needs to follow this command to split a mesh into two pieces.
	pm.mel.DetachComponent()

# Separate - Splits any objects with detached or separate components into separate parts.
	pm.mel.SeparatePolygon()
	
# Extract - Detaches AND Separates any selected faces from a mesh into a separate object.
	pm.mel.ExtractFace()

# Combind - Takes two or more separate objects and combines them under a single Tranform Node
# They can be Separated unless components are merged
	pm.mel.CombinePolygons()

# Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
	selected = pm.ls(selection=True)

	for indiv in selected:

		pm.makeIdentity(indiv, a=True, t=1, r=1, s=1, n=0)

		pm.delete(indiv, constructionHistory=True)

		pm.xform(indiv, centerPivots=True)




