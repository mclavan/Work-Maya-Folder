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

	# Mel: makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1; Python: pm.makeIdentity(apply=True, t=1, s=1, r=1) 

	# This command resets transforms, scale, rotations, and normals  back to either 0 or 1

	# -Translate -Rotate -Scale -jointOrient -lockNormals

	# (t)=Transform (r)=Rotate (s)=Scale (n)=Normal 

# Delete History

	# Mel: DeleteHistory; Python: pm.DeleteHistoty()

	# Deletes History

	# -constructionHistory, -staticChannels, -channels

	# constructionHistory(ch), staticChannels(sc), channels(c)

# Center Pivot

	# Mel: CenterPivot; Python: pm.CenterPivot()

	# This command takes the current pivot and moves it to the center of the geometry.

	# no important flags

	# no important flags


# Single Chain and Rotate Plan IKs

	# Mel: ikHandle; Python: pm.ikHandle()

	# The handle command is used to create, edit, and query a handle within Maya. The standard edit (-e) and query (-q) flags are used for edit and query functions.

	# startJoint, endEffector, priority,

	# startJoint(sj), endEffector(ee), priority(p)

	# 	import maya.cmds as cmds

		# Will create a handle from Joint-1 to an end-effector at
		# the location of Joint-5 with a priority of 2 and a
		# weight of 0.5
		#
		cmds.ikHandle( sj='joint1', ee='joint5', p=2, w=.5 )

# Cluster

	# Mel: newCluster " -envelope 1"; Python: pm.cluster()

	# The cluster command creates a cluster or edits the membership of an existing cluster.

	# name, geometry, remove, before, after

	# name(n), geometry(g), remove(rm), before(bf), after(af)

	#	cmds.sphere()
		cmds.cluster( wn=('elbow1', 'elbow1') )

# Grouping (Does not need to be included on Shelf!)
	
	# Mel: doGroup; Python: pm.group()

	# This command groups the specified objects under a new group and returns the name of the new group.

	# name, world, parent, empty, relative

	# name(n), world(d), parent(p), empty(em), relative(r)

	#	# create an empty group node with no children
		cmds.group( em=True, name='null1' )

# Parenting (Does not need to be included on Shelf!)
	
	# Mel: parent; Python: pm.parent()

	# This command parents (moves) objects under a new group, removes objects from an existing group, or adds/removes parents.

	# world, relative, absolute

	# world(d), relative(r), absolute(a)

	# 	# Let's try that again with the -relative flag. This time
		# the circle will move.
		cmds.undo()
		cmds.parent( 'circle1', 'group2', relative=True )

# Duplicating (Does not need to be included on Shelf!)
	
	# Mel: duplicate name_of_object; Python: pm.duplicate (n='name_of_object')

	# This command duplicates the given objects. If no objects are given, then the selected list is duplicated

	# name, 

	# name(n)

	# 	# Create a duplicate of the group
		cmds.duplicate( 'group1' )
		# Result: group2 sphere1 sphere2 #

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	# Mel: circle -ch on -o on -nr -r ; pm.circle(ch, o, nr, r)

	# The circle command creates a circle or partial circle (arc)

	# name, constructionHistory, object

	# name(n), constructionHistroy(ch), object (o)

	# 	# create full circle at origin on the x-y plane
		cmds.circle( nr=(0, 0, 1), c=(0, 0, 0) )

# Square
	# Mel: nurbsSquare -ch -o -n ; Python: pm.nurbsSquare(ch, o, n)

	# The nurbsSquare command creates a square

	# constructionHistory, object, name

	# constructionHistory(ch), object(o), name(n)

	# 	# create degree 1 square with side length 2, center (0,0,0) on the
		# x-y plane
		cmds.nurbsSquare( nr=(0, 0, 1), d=1, c=(0, 0, 0), sl1=2, sl2=2 )
# Cube
	# Mel: nurbsCube -ch on -o on -po -ax -w -lr -hr ; Python: pm.nurbsCube(ch, o, po, ax, w, lr, hr)

	# The nurbsCube command creates a new NURBS Cube made up of six planes.

	# constructionHistory, object, polygon, name

	# constructionHistory(ch), object(o), polygon(po), name(n)

	# 	cmds.nurbsCube( w=3, hr=5 )
		cmds.nurbsCube( w=10, p=(0, 0, 1) )
		cmds.nurbsCube( d=1, u=3, v=5, w=5 )

# Arrow
	#

	#

	#

	#

	#


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	# Mel: parentConstraint -n -w -rm; Python: pm.parentConstraint(n, w, rm)

	# Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s).

	# name, weight, remove

	# name(n), weight(w), remove(rm)

# Orient Constraint
	# Mel: orientConstraint -n -w -rm -l -o -sk -cc -dc; Python: pm.orientConstraint(n, w, rm, l, o, sk, cc, dc)

	# Constrain an object's orientation to match the orientation of the target or the average of a number of targets.

	# name, weight, remove, layer, offset, skip, createCache, deleteCache

	# name(n), weight(w), remove(rm), layer(l), offset(o), skip(sk), createCache(cc), deleteCache(dc)

# Point Constraint
	# Mel: pointConstraint -n -w -rm -l -o -sk; Python: pm.pointConstraint(n, w, rm, l, o, sk)

	# Constrain an object's position to the position of the target object or to the average position of a number of targets.

	# name, weight, remove, layer, offset, skip

	# name(n), weight(w), remove(rm),layer(l), offset(o), skip(sk)

# Pole Vector Constraint
	# Mel: poleVectorConstraint -n -w -rm -l; pm.poleVectorConstraint(n, w, rm, l)

	# Constrains the poleVector of an ikRPsolve handle to point at a target object or at the average position of a number of targets.

	# name, weight, remove, layer

	# name(n), weight(w), remove(rm),layer(l)

# How does this constraint differ from the previous three.
	# This constraint does not maintain the offset

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
Mel:	addAttr -ln "Create"  -at double  |nurbsCircle2;
setAttr -e-keyable true |nurbsCircle2.Create;
addAttr -ln "Create"  -at double  |nurbsCircle1;
setAttr -e-keyable true |nurbsCircle1.Create;

Python: pm.addAttr(ln "Create", at='double', nurbsCircle2)
setAttr(e, keyable=True, nurbsCircle2.Create)
addAttr(ln "Create", at=double, nurbsCircle1)
setAttr(e, keyable=True, nurbsCircle1.Create)

Flags: e, ln

# Create Separator Attribute

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
pm.addAttr(ln = 'FINGERS', at ='enum', en='---------------', keyable=True)
pm.addAttr(ln = 'CURLS', at ='enum', en='---------------', keyable=True)
pm.addAttr(ln = 'pinky_curl', at = 'double', keyable=True)
pm.addAttr(ln = 'middle_curl', at = 'double', keyable=True)
pm.addAttr(ln = 'ring_curl', at = 'double', keyable=True)
pm.addAttr(ln = 'index_curl', at = 'double', keyable=True)

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


