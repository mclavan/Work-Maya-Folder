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
# straight forward, just freeze the transforms on a selceted target. 
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	
	#----- Flags ------
	apply(a) - implements the new values to t, r, s, & n.
	translate(t) - set to 1
	rotate(r) - set to 1
	scale(s) - set to 1
	normal(n) - set to 0 
	jointOrientation(jo) - set to world space. 


# Delete History
pm.delete(ch=True)

	#----- Flags -----
	attribute(at) - List of attributes to selecte
	hierarchy(hi) - Hierarchy expansion options. Valid values are "above," "below," "both," and "none."
	shape(s) - 	Consider attributes of shapes below transforms as well, except "controlPoints". Default: true.
	controlPoints(cp) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.

# Center Pivot
pm.xform(cp=True)

	#----- Flags -----
	absolute(a) - performs absolue transformation.
	relative(r) - perform relative tranformations.
	euler(eu) - modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
	 

# Single Chain and Rotate Plan IKs
pm.ikhandel()
pm.ikhandel (sol= 'ikRPsolver')

# Cluster
pm.cluster()

# Grouping (Does not need to be included on Shelf!)
	pm.group()

	#----- Flags ------
	name(n) - names the group.
	empty() - Creates an empty group.


	# Grouping by default parents selected objects in the scene
	#In theis example the son would be the top node
	pm.group(name='grandFather')
	pm.group(name='father')
	pm.group(name='son')

	#Empty groups can be created too.
	pm.group(name='grandFather', empty=True)
	pm.group(name='father', empty=True)
	pm.group(name='son', empty=True)



# Parenting (Does not need to be included on Shelf!)
pm.parent() 

# Duplicating (Does not need to be included on Shelf!)
pm.duplicate()

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	pm.circle()
	# Controls is facing the y-axis. Good for FK back controls. World orientation.
	pm.circle(normal=[0, 1, 0])

	#Control is facing the x-axis. Good for local oriented controls.
	pm.circle(normal=[1, 0, 0])

	#---- Flags -----
	normal - Direction of the control
	radius - Size of the control
	sections - How many sections the controls have.

# Square

	pm.circle(degree=1, sections=4)
	#---- Flags ------
	degree(d) = Two main values, linear=1 and cubic=3
	sections(s) = Four points makes a square
	normal(nr) = Normals flags work just like the normal circle command.

# Cube

# Arrow


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
pm.parentConstraint() 

# Orient Constraint
pm.orientConstraint()

# Point Constraint
pm.pointConstraint()

# Pole Vector Constraint
pm.poleVectorConstraint()

# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

selected = pm.ls(selection=True)
first_selected = selected[0]

attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)

# Create Separator Attribute
selected = pm.ls(selection=True)
first_selected = selected[0]

attribute_name = raw_input()
first_selected.addAttr(attribute_name, at='enum', en='.........', keyable=True)
attribute = first_selected.attr(attribute_name)
attribute.set(lock=True)

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


