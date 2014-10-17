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
	# Python
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	# Mel
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

		#----Flags----
		apply(a) - applies to the object
		translate(t) - (x,y,z)
		rotate(r) - (x,y,z)
		scale(s) - (x,y,z) = 1
		jointOrient(jo) - changing the orientation to world space
		normal(n) - freeze normals

# Delete History
	pm.delete(ch=True)

		#---Flags----
		all (all) - delets all objects selected fromt he list bellow
		attribute (at) - listing the attributes 
		channels (c) - 
		constraints (cn) -
		constructionHistory (ch) -
		controlPoints (cp) -
		expressions (e) -
		hierarchy (hi) -


# Center Pivot
	pm.xform(cp=True)

# Single Chain and Rotate Plan IKs
	# Single
	pm.ikHandle()
	pm.ikhandle(sol='ikSCsolver')
	# Rotate
	pm.ikHandle()
	pm.ikHandle (sol = 'ikRPsolver')


# Cluster
	pm.cluster()

# Grouping (Does not need to be included on Shelf!)
	pm.group()

		#----Flags----
		name(n) - names the group
		empty() - creates an empty group.
	# Grouping by default parents selected objects in the scene
	# In this example the son would be the top node
	pm.group(name='grandfather')
	pm.group(name='father')
	pm.group(name='son')

	#empty groups can be created too.
	pm.group(name='grandfather', empty=True)
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
	pm.circle(normal=()
	# Control is facing the y-axis. Good for FK back controls. World oriented
	pm.circle(normal=[0, 1, 0])

	#Control is facing the x-axis. Good for local oriented controls
	pm.circle(normal=[1, 0, 0])

	#--- Flags ---
	normal - Direction of the control 
	radius - Size of the controls
	section - How many sections does the controls has
# Square
	

 pm.circle(normal=[1, 0, 0], degree=1, sections=4)
 #--- Flags ---
 degree (d) = Two main values, linear=1 and cubic=3
 sections(s) = Four points make
 normal(nr) = Normals flags work just like the normal circle command.

# Cube
	import pymel.core as pm
	mel_line = 'curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
	pm.mel.eval(mel_line)

# Arrow
	import pymel.core as pm
	mel_line = 'curve -d 1 -p -7.5 0 -2.5 -p 0 0 -2.5 -p 0 0 -5 -p 7.5 0 0 -p 0 0 5 -p 0 0 2.5 -p -7.5 0 2.5 -p -7.5 0 -2.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	pm.mel.eval(mel_line)


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	import pymel.core as pm
	pm.parentConstraint()
	# Parent contraint defaults to maintain offset is off by default (snapping)
	pm.parentConstraint('driver', 'driven')
	pm.parentConstraint('driver', 'driven', maintainOffset=True)

	#maintain offset
	parentConstraint -mo -weight 1;
	pm.parentConstraint('driver', 'driven', maintainOffset=True)

	#----Flags----
	maintainOffset (mo) - Snapping or no Snapping
	weights(w) - How much influence a contraint has over its target.


# Orient Constraint
pm.orientConstraint()

# Point Constraint
pm.parentConstraint()

# Pole Vector Constraint
pm.poleVectorConstraint()
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	# index curl attribute
		import pymel.core as pm

		selected = pm.ls(selection=True)
		first_selected = selected[0]

		# Create a float attribute
		first_selected.addAttr('index_curl', keyable=True)


# Create Separator Attribute
	import pymel.core as pm

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# Create a float attribute
	attribute_name = raw_input()
	first_selected.addAttr(attribute_name, at='enum', en="--------------:", keyable=True)
	attribute = first_selected.attr(attribute_name)
	attribute.set(lock=True)


# Template Attributes 

# Create a group of attributes at one time.  
		import pymel.core as pm

		selected = pm.ls(selection=True)
		first_selected = selected[0]

		# Create a float attribute
		first_selected.addAttr('index_curl', keyable=True)
		first_selected.addAttr('middle_curl', keyable=True)
		first_selected.addAttr('pinky_curl', keyable=True)

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


