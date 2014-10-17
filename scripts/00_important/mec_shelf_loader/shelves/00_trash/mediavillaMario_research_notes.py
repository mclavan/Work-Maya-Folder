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

	# Mel Code:
		makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

	# This command freezes the object selected and makes all the channels into there default points and makes the position your in into a default
	# I found this by doing it in maya and reading it in the script editor

	# Mel to Python Code:
		pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)



	#----Flags----
	# t = Transforms that would freeze where they are
	# r = Rotate
	# s = Scale
	# n = normals

# Delete History

	# Mel code:
		DeleteHistory -ch

	# What this does is delete all the histroy an object has
	# I found this by doing it in maya and reading it in the script editor

	# Mel to Python code:
		pm.delete(ch=True)


	#----Flags----
	# ch = Contruction History - Removes the construction history on the objects specified or selected.

# Center Pivot
	
	# Mel code:
		xform -cp

	# What this does is it grabs the pivot of the object selected and center it on the origin object
	# I found this by doing it in maya and reading it in the script editor

	# Mel to Python code:
		pm.xform(cp=True)

	#----Flag----
	# cp = Center Pivot - Set pivot points to the center of the object's bounding box.

# Single Chain and Rotate Plan IKs

	# Mel: Rotate Plan
	ikHandle -sol ikRPsolver

	# Mel: Single Chain
	ikHandle -sol ikSCsolver # The Single Chain is default so it dosen't need to be called but since i don't trust maya i added it anyways.

	# The Rotate Plan is used when there is something like a shoulder or knee but basicly something that has a 3 middle joint that it can bend from
	# The Single Chain is used for going from joint to joint and it not needing a bend but still needing an IK.
	# I found both of them by using them on maya and looking at the script editor but also the python commands page that autodesk provides.

	# Mel to Python code: Rotate Plan
	pm.ikHandle(sol='ikRPsolver')

	# Mel to Python code: Single Chain
	pm.ikHandle(sol='ikSCsolver')
	# I found this by doing it in maya and reading it in the script editor

	#----Flag----
	# sol = Solver - Specifies the solver needed for the handle could be RP or SC

# Cluster

	# Mel code:
		newCluster " -envelope 1";

	# This sets a weight to the selected curve so it can move corretly and independently
	# I found it by using them on maya and looking at the script editor but also the python commands page that autodesk provides.

	# Mel to Python
		pm.cluster()
	
	#----Flag----
	# envelope - Set the envelope value for the deformer.

	'''
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	for current_cv in first_selected.cv:

		pm.cluster(current_cv)
	'''

# Grouping (Does not need to be included on Shelf!)
	
	# Mel code:
		doGroup

	# Mel to Python:
		pm.group()

	# This groups selected objects together, it also creates a hierchy between these objects that could make things work as one
	# I found it by using them on maya and looking at the script editor but also the python commands page that autodesk provides.

	#----Flags----
	name(n) - 	names the group
	empty()	-	Creates an empty group
	
	# Grouping by default parents selected objects in the scene.
	# In this example the son would be the top node 
	pm.group(name='grandFather')
	pm.group(name='father')
	pm.group(name='son')

	# Empty groups can be created too.
	pm.group(name='grandFather', empty=True)
	pm.group(name='father', empty=True)
	pm.group(name='son', empty=True)

# Parenting (Does not need to be included on Shelf!)

	# Mel code:
		parent

	# This makes it so there is a parent to child relationship between the obejcts and it allows for if something happens to one it dosen't need to other object to do it.
	# I found it by using them on maya and looking at the script editor but also the python commands page that autodesk provides.

	# Mel to Python:
		pm.parent()

	#----Flags----
	# selected(obj) - you can make it so it takes on object first or force someone to group with something in the scene with this added.

# Duplicating (Does not need to be included on Shelf!)

	# Mel code:
		duplicate -rr;

	# This is used to make another object with the same numbers in the channels
	# I found this by clicking duplicate in maya and looking at it in the script editor

	# Mel to Python code:
		pm.duplicate(rr=True)

	#----Flag----
	# rr = returnRootsonly - return only the root nodes of the new hierarchy.

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle

	# Mel code:
		circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;

	# This creates a NURB circle
	# Selecting it on the create menu and looking at it in the script editor

	# Mel to Python code:
		pm.circle()

	# Control is facing the y-axis. Good for FK back controls, World oriented.
	pm.circle(normal=[0,1,0])

	# Control is faicng the x-axis. Good for local oriented controls.
	pm.circle(normal=[1,0,0])

	#-----flags-----
	# normal - direction of the control
	# radius - size of the control
	# sections - How many sections the control has

# Square

	# Python code:
		pm.circle(degree=1, sections=4)

	# This places down a NURB square
	# The circle can add more sections to itself and with that you create a square

	#----Flags----
	# degree(d) = two main values, linear=1 and cubic=3
	# sections(s) = Four points makes a square
	# nomal(nr) = Normal flags works just like the normal circle command

# Cube
	
	# Python using Mel code: 
	#It is trieng to extimate where the points are so .eval can be used on curves so it won't freak out
	pm.mel.eval('curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')

	# This creates a NURB cube in the scene
	# This was created using a poly cube and then drawing with the CV curve tool and then catching the values in the script editor.

	#----Flag----
	# eval = evaluate - it evaluates where the point is in 3D space.

# Arrow

	# Mel code:
		# Didn't see that we needed to give back a mel code and forgot to save the MEL code i got for this

	# This creates a arrow in the scene
	# This was created using a poly cube and then drawing with the CV curve tool and then catching the values in the script editor.

	# Mel to Python code:
		pm.curve(d=1,p=[(0,0,-1.093365),(-0.443179,0,-0.0143405),(-0.202705,0,-0.267664),(-0.202705,0,1.018291),(0.202705,0,1.018291),(0.202705,0,-0.267664),(0.443179,0,-0.0143405),(0,0,-1.093365)],k=[0,1,2,3,4,5,6,7])

	#----Flags----
	# d = degree - This gets the degree of a new curve
	# p = position - This keeps the position of the item and where it's points are
	# k = Knot - A knot value in a knot vector

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint

	# Mel code:
		# Offset ON
		parentConstraint -mo -weight 1;
		# Offset OFF
		parentConstraint -weight 1;

	# Parent constraint is used to pair up object but for them to keep there independence as seperate objects
	# I used maya and then i looked at the script editor

	# Mel to Python code:
		# Parent constriant default to maiuntain offset is off by default (snapping)
		# Offset ON
		pm.parentConstraint('driver', 'driven', mo=True)
		# Offset OFF
		pm.parentConstraint('driver', 'driven', mo = False)


	#----Flags----
	# maintainOffset (mo) - Snapping or no Snapping
	# weight(w) - How much influence a contraint has over its target

# Orient Constraint

	# Mel code:
		# Offset ON
		orientConstraint -mo -weight 1;
		# Offset OFF
		orientConstraint -weight 1;

	# Constrain an object's orientation to match the orientation of the target or the average of a number of targets by using it's orientation.
	# I used maya and then i looked at the script editor

	# Mel to Python code:
		# Parent constriant default to maiuntain offset is off by default (snapping)
		# Offset ON
		pm.orientConstraint('driver', 'driven', mo=True)
		# Offset OFF
		pm.orientConstraint('driver', 'driven', mo = False)

	#----Flags----
	# maintainOffset (mo) - Snapping or no Snapping
	# weight(w) - How much influence a contraint has over its target

# Point Constraint

	# Mel code:
		# Offset ON
		pointConstraint -mo -weight 1;
		# Offset OFF
		pointConstraint -weight 1;

	# Constrain an object's orientation to match the orientation of the target or the average of a number of targets by using it's points.
	# I used maya and then i looked at the script editor

	# Mel to Python code:
		# Parent constriant default to maiuntain offset is off by default (snapping)
		# Offset ON
		pm.pointConstraint('driver', 'driven', mo=True)
		# Offset OFF
		pm.pointConstraint('driver', 'driven', mo = False)

	#----Flags----
	# maintainOffset (mo) - Snapping or no Snapping
	# weight(w) - How much influence a contraint has over its target

# Pole Vector Constraint

	# Mel code:
		poleVectorConstraint -weight 1;

	# This is mainly used for shoulders and knees of what you are making so the joints and geometry follow and point at the correct orientation and position.
	# I used maya and then i looked at the script editor

	# Mel to Python code:
		pm.poleVectorConstraint('driver', 'driven')

	#----Flag----
	# weight(w) - How much influence a contraint has over its target

# How does this constraint differ from the previous three.
	
	# The pole vector makes it so things like your shoulder and knee are looking the correct way the others make it so when you
	#  parent something there are hierchies that need to be followed so the rig can work



'''
Attributes (Convered in Podcast)
'''
# Create float attribute

	selected = pm.ls(selection=True)
	root_joint = selected[0]

	print 'Root Joint: ', root_joint

	# What this does is create the attribute and then you add the name
	root_joint.addAttr('index_curl', keyable=True)
	root_joint.addAttr('middle_curl', keyable=True)
	root_joint.addAttr('pinky_curl', keyable=True)

	#----Flags----
	# keyable - it makes it so you can change the attribute with a user made number

# Create Separator Attribute

	# This creates the needed space for specifieng a part of the attribute that
	# makes the fingers since we have them doing multiple things these things
	# have to be named properly and places where they need to be.

	root_joint.addAttr('FINGERS', keyable=True,
		at='enum', en="--------------:")
	root_joint.FINGERS.set(lock=True)



	# This makes a Attribute quickly
	# The first one creates the name and see if it's keyable
	# The second one creates the seperators needed when making multiple attributes
	attr_name = raw_input()
	root_joint.addAttr(attr_name, keyable=True)

	attr_name = raw_input()
	root_joint.addAttr(attr_name, keyable=True,
		at='enum', en="--------------:")


# Template Attributes 

	'''
	FINGERS
	CURL
	index_curl
	middle_curl
	pinky_curl
	'''
	
	selected = pm.ls(selection=True)
	root_joint = selected[0]sf
	# Finger Attributes
	root_joint.addAttr('FINGERS', keyable=True,
		at='enum', en="--------------:")
	root_joint.FINGERS.set(lock=True)
	# Curl Attributes
	root_joint.addAttr('CURL', keyable=True,
		at='enum', en="--------------:")
	root_joint.CURL.set(lock=True)
	root_joint.addAttr('index_curl', keyable=True)
	root_joint.addAttr('middle_curl', keyable=True)
	root_joint.addAttr('pinky_curl', keyable=True)
	# Spread Attributes
	root_joint.addAttr('SPREAD', keyable=True,
		at='enum', en="--------------:")
	root_joint.SPREAD.set(lock=True)
	root_joint.addAttr('index_spread', keyable=True)
	root_joint.addAttr('middle_spread', keyable=True)
	root_joint.addAttr('pinky_spread', keyable=True)
	# Thumb Attributes
	root_joint.addAttr('THUMB', keyable=True,
		at='enum', en="--------------:")
	root_joint.THUMB.set(lock=True)
	root_joint.addAttr('thumb_curl', keyable=True)
	root_joint.addAttr('thumb_drop', keyable=True)


# Create a group of attributes at one time.
	'''
	FINGERS
	CURL
	index_curl
	middle_curl
	pinky_curl
	'''
	
	selected = pm.ls(selection=True)
	root_joint = selected[0]sf
	# Finger Attributes
	root_joint.addAttr('FINGERS', keyable=True,
		at='enum', en="--------------:")
	root_joint.FINGERS.set(lock=True)
	# Curl Attributes
	root_joint.addAttr('CURL', keyable=True,
		at='enum', en="--------------:")
	root_joint.CURL.set(lock=True)
	root_joint.addAttr('index_curl', keyable=True)
	root_joint.addAttr('middle_curl', keyable=True)
	root_joint.addAttr('pinky_curl', keyable=True)
	# Spread Attributes
	root_joint.addAttr('SPREAD', keyable=True,
		at='enum', en="--------------:")
	root_joint.SPREAD.set(lock=True)
	root_joint.addAttr('index_spread', keyable=True)
	root_joint.addAttr('middle_spread', keyable=True)
	root_joint.addAttr('pinky_spread', keyable=True)
	# Thumb Attributes
	root_joint.addAttr('THUMB', keyable=True,
		at='enum', en="--------------:")
	root_joint.THUMB.set(lock=True)
	root_joint.addAttr('thumb_curl', keyable=True)
	root_joint.addAttr('thumb_drop', keyable=True)

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


