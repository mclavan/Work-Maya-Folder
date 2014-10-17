'''
Research Notes

Christian Ward

Current Shelf Tools: 20
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 0

Drop Down Menus: 0

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

	FreezeTransformations
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1

	# Maya shelf editor lists as Mel command

	makeIdentity( apply=True )

	# -apply(-a)	boolean	create
		# If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.
	# -translate(-t)	boolean	create
		# If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied. (Note: the translate flag is not meaningful when applied to joints, since joints are made to preserve their world space position. This flag will have no effect on joints.)
	# -rotate(-r)	boolean	create
		# If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
	# -scale(-s)	boolean	create
		# If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
	# -jointOrient(-jo)		create
		# If this flag is set, the joint orient on joints will be reset to align with worldspace.
	# -normal(-n)	uint	create
		# If this flag is set to 1, the normals on polygonal objects will be frozen. This flag is valid only when the -apply flag is on. If this flag is set to 2, the normals on polygonal objects will be frozen only if its a non-rigid transformation matrix. ie, a transformation that does not contain shear, skew or non-proportional scaling. The default behaviour is not to freeze normals.
	# -preserveNormals(-pn)	boolean	create
		# If this flag is true, the normals on polygonal objects will be reversed if the objects are negatively scaled (reflection). This flag is valid only when the -apply flag is on.

# Delete History

	DeleteHistory

	# Maya shelf editor lists as Mel command

	delete(history=True)

	# -attribute(-at)	string	createmultiuse
		# List of attributes to select
		# In query mode, this flag needs a value.
	# -hierarchy(-hi)	string	create
		# Hierarchy expansion options. Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.)
		# In query mode, this flag needs a value.
	# -shape(-s)	boolean	create
		# Consider attributes of shapes below transforms as well, except "controlPoints". Default: true. (Not valid for "pasteKey" cmd.)
		# In query mode, this flag needs a value.
	# -controlPoints(-cp)	boolean	create
		# This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false. (Not valid for "pasteKey" cmd.)
		# In query mode, this flag needs a value.
	# -all(-all)		create
		# Remove all objects of specified kind, in the scene. This flag is to be used in conjunction with the following flags.
	# -inputConnectionsAndNodes(-icn)		create
		# Break input connection to specified attribute and delete all unconnected nodes that are left behind. The graph will be traversed until a node that cannot be deleted is encountered.
	# -constructionHistory(-ch)		create
		# Remove the construction history on the objects specified or selected.
	# -staticChannels(-sc)		create
		# Remove static animation channels in the scene. Either all static channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
	# -channels(-c)		create
		# Remove animation channels in the scene. Either all channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
	# -unitlessAnimationCurves(-uac)	boolean	create
		# Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to unitless-input animation curves (for instance, those created by 'setDrivenKeyframe' will be deleted. When false, no unitless-input animation curves will be deleted. Default: true.
	# -timeAnimationCurves(-tac)	boolean	create
		# Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to time-input animation curves (for instance, those created by 'setKeyframe' will be deleted. When false, no time-input animation curves will be deleted. Default: true.
	# -expressions(-e)		create
		# Remove expressions in the scene. Either all expressions can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
	# -constraints(-cn)		create
		# Remove selected constraints and constraints attached to the selected nodes, or remove all constraints in the scene.

# Center Pivot

	CenterPivot

	# Maya shelf editor lists as Mel command

	xform(cp=True)

	# 	-centerPivots(-cp)		create
		# Set pivot points to the center of the object's bounding box. (see -p flag)

# Single Chain and Rotate Plan IKs

	IKHandleTool

	# Maya shelf editor lists as Mel command

	ikHandle(sj='joint1', ee='joint2', p=2, w=.5)
		# Will create a handle from Joint-1 to an end-effector at
		# the location of Joint-5 with a priority of 2 and a
		# weight of 0.5

	# -name(-n)	string	createqueryedit
		# Specifies the name of the handle.
	# -startJoint(-sj)	string	createqueryedit
		# Specifies the start joint of the handle's joint chain.
	# -endEffector(-ee)	string	createqueryedit
		# Specifies the end-effector of the handle's joint chain. The end effector may be specified with a joint or an end-effector. If a joint is specified, an end-effector will be created at the same position as the joint and this new end-effector will be used as the end-effector.
	# -priority(-p)	int	createqueryedit
		# Sets the priority of the handle. Logically, all handles with a lower number priority are solved before any handles with a higher numbered priority. (All handles of priority 1 are solved before any handles of priority 2 and so on.) Handle priorities must be ] 0.
	# -autoPriority(-ap)		edit
		# Specifies that this handle's priority is assigned automatically. The assigned priority will be based on the hierarchy distance from the root of the skeletal chain to the start joint of the handle.
	# -weight(-w)	float	createqueryedit
		# Specifies the handles weight in error calculations. The weight only applies when handle goals are in conflict and cannot be solved simultaneously. When this happens, a solution is computed that weights the "distance" from each goal to the solution by the handle's weight and attempts to minimize this value. The weight must be ]= 0.
	# -positionWeight(-pw)	float	createqueryedit
		# Specifies the position/orientation weight of a handle. This is used to compute the "distance" between the goal position and the end-effector position. A positionWeight of 1.0 computes the distance as the distance between positions only and ignores the orientations. A positionWeight of 0.0 computes the distance as the distance between the orientations only and ignores the positions. A positionWeight of 0.5 attempts to weight the distances equally but cannot actually compute this due to unit differences. Because there is no way to add linear units and angular units.
	# -solver(-sol)	string	createqueryedit
		# Specifies the solver. The complete list of available solvers may not be known until run-time because some of the solvers may be implemented as plug-ins. Currently the only valid solver are ikRPsolver, ikSCsolver and ikSplineSolver.
	# -forceSolver(-fs)	boolean	createqueryedit
		# Forces the solver to be used everytime. It could also be known as animSticky. So, after you set the first key the handle is sticky.
	# -snapHandleFlagToggle(-shf)	boolean	createqueryedit
		# Specifies that the handle position should be snapped to the end-effector position if the end-effector is moved by the user. Setting this flag on allows you to use forward kinematics to pose or adjust your skeleton and then to animate it with inverse kinematics.
	# -snapHandleToEffector(-see)		edit
		# All handles are immediately moved so that the handle position and orientation matches the end-effector position and orientation.
	# -sticky(-s)	string	createqueryedit
		# Specifies that this handle is "sticky". Valid values are "off", "sticky", "superSticky". Sticky handles are solved when the skeleton is being manipulated interactively. If a character has sticky feet, the solver will attempt to keep them in the same position as the user moves the character's root. If they were not sticky, they would move along with the root.
	# -connectEffector(-ce)	boolean	createedit
		# This option is set to true as default, meaning that end-effector translate is connected with the endJoint translate.
	# -jointList(-jl)		edit
		# Returns the list of joints that the handle is manipulating.
	# -exists(-ex)	string	edit
		# Indicates if the specified handle exists or not.
	# -setupForRPsolver(-srp)	boolean	edit
		# If the flag is set and ikSolver is ikRPsolver, call RPRotateSetup for the new ikHandle. It is for ikRPsolver only.
	# -enableHandles(-eh)		edit
		# set given handles to full ik (ikBlend attribute = 1.0)
	# -disableHandles(-dh)		edit
		# set given handles to full fk (ikBlend attribute = 0.0)
	# -curve(-c)	name	createqueryedit
		# Specifies the curve to be used by the ikSplineHandle. Joints will be moved to align with this curve. This flag is mandatory if you use the -freezeJoints option.
	# -createCurve(-ccv)	boolean	create
		# Specifies if a curve should automatically be created for the ikSplineHandle.
	# -freezeJoints(-fj)	boolean	createedit
		# Forces the curve, specfied by -curve option, to align itself along the existing joint chain. When false, or unspecified, the joints will be moved to positions along the specified curve.
	# -simplifyCurve(-scv)	boolean	create
		# Specifies if the ikSplineHandle curve should be simplified.
	# -rootOnCurve(-roc)	boolean	createqueryedit
		# Specifies if the root is locked onto the curve of the ikSplineHandle.
	# -twistType(-tws)	string	createqueryedit
		# Specifies the type of interpolation to be used by the ikSplineHandle. The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".
	# -createRootAxis(-cra)	boolean	create
		# Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.
	# -parentCurve(-pcv)	boolean	create
		# Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.
	# -snapCurve(-snc)	boolean	create
		# Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.
	# -numSpans(-ns)	int	create
		# Specifies the number of spans in the automatically generated curve of the ikSplineHandle.
	# -rootTwistMode(-rtm)	boolean	createqueryedit
		# Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types.

# Cluster

	CreateCluster;
	
	# Maya shelf editor lists as Mel command

	cluster( rel=True )
		# Create a relative cluster with its own cluster handle. The
		# cluster handle is drawn as the letter "C".

	# 	-name(-n)	string	create
		# Used to specify the name of the node being created
	# -geometry(-g)	string	queryeditmultiuse
		# The specified object will be added to the list of objects being deformed by this deformer object, unless the -rm flag is also specified. When queried, this flag returns string string string ...
	# -geometryIndices(-gi)		query
		# Complements the -geometry flag in query mode. Returns the multi index of each geometry.
	# -remove(-rm)		editmultiuse
		# Specifies that objects listed after the -g flag should be removed from this deformer.
	# -before(-bf)		createedit
		# If the default behavior for insertion/appending into/onto the existing chain is not what you want then you can use this flag to force the command to stick the deformer node before the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
	# -after(-af)		createedit
		# If the default behavior for insertion/appending into/onto the existing chain is not what you want then you can use this flag to force the command to stick the deformer node after the selected node in the chain even if a new geometry shape has to be created in order to do so. Works in create mode (and edit mode if the deformer has no geometry added yet).
	# -afterReference(-ar)		createedit
		# The -afterReference flag is used to specify deformer ordering in a hybrid way that choses between -before and -after automatically. If the geometry being deformed is referenced then -after mode is used in adding the new deformer otherwise -before mode is used. The net effect when using -afterReference to build deformer chains is that internal shape nodes in the deformer chain will only appear at reference file boundaries, leading to lightweight deformer networks that may be more amicable to reference swapping.
	# -split(-sp)		createedit
		# Branches off a new chain in the dependency graph instead of inserting/appending the deformer into/onto an existing chain. Works in create mode (and edit mode if the deformer has no geometry added yet).
	# -frontOfChain(-foc)		createedit
		# This command is used to specify that the new deformer node should be placed ahead (upstream) of existing deformer and skin nodes in the shape's history (but not ahead of existing tweak nodes). The input to the deformer will be the upstream shape rather than the visible downstream shape, so the behavior of this flag is the most intuitive if the downstream deformers are in their reset (hasNoEffect) position when the new deformer is added. Works in create mode (and edit mode if the deformer has no geometry added yet).
	# -parallel(-par)		createedit
		# Inserts the new deformer in a parallel chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. Works in create mode (and edit mode if the deformer has no geometry added yet).
	# -ignoreSelected(-is)		create
		# Tells the command to not deform objects on the current selection list
	# -deformerTools(-dt)		query
		# Returns the name of the deformer tool objects (if any) as string string ...
	# -prune(-pr)		edit
		# Removes any points not being deformed by the deformer in its current configuration from the deformer set.
	# -exclusive(-ex)	string	createquery
		# Puts the deformation set in a deform partition.
	# -weightedNode(-wn)	string string	createqueryedit
		# Transform node in the DAG above the cluster to which all percents are applied. The second DAGobject specifies the descendent of the first DAGobject from where the transformation matrix is evaluated. Default is the cluster handle.
	# -bindState(-bs)	boolean	create
		# When turned on, this flag adds in a compensation to ensure the clustered objects preserve their spatial position when clustered. This is required to prevent the geometry from jumping at the time the cluster is created in situations when the cluster transforms at cluster time are not identity.
	# -envelope(-en)	float	createqueryedit
		# Set the envelope value for the deformer. Default is 1.0
	# -relative(-rel)		create
		# Enable relative mode for the cluster. In relative mode, Only the transformations directly above the cluster are used by the cluster. Default is off.
	# -resetGeometry(-rg)		edit
		# Reset the geometry matrices for the objects being deformed by the cluster. This flag is used to get rid of undesirable effects that happen if you scale an object that is deformed by a cluster.

# Grouping (Does not need to be included on Shelf!)
	
	doGroup 0 1 1;

	# Listed as Mel when made into button

	group(empty=True)
		# create an empty group node with no children

	# 	name(n)	string	create
		# Assign given name to new group node.
	# world(w)	boolean	create
		# put the new group under the world
	# parent(p)	string	create
		# put the new group under the given parent
	# empty(em)	boolean	create
		# create an empty group (with no objects in it)
	# relative(r)	boolean	create
		# preserve existing local object transformations (relative to the new group node)
	# absolute(a)	boolean	create
		# preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
	# useAsGroup(uag)	string	create
		# Use the specified node as the group node. The specified node must be derived from the transform node and must not have any existing parents or children.

# Parenting (Does not need to be included on Shelf!)
	
	parentPreset(0,1)

	# Listed as Mel when made into button

	parent('object1', 'object2')

	# 	world(w)	boolean	create
		# unparent given object(s) (parent to world)
	# relative(r)	boolean	create
		# preserve existing local object transformations (relative to the parent node)
	# absolute(a)	boolean	create
		# preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]
	# addObject(add)	boolean	create
		# preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.
	# removeObject(rm)	boolean	create
		# Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the scene. Use -world to remove the world as a parent of the given object.
	# shape(s)	boolean	create
		# The parent command usually only operates on transforms. Using this flags allows a shape that is specified to be directly parented under the given transform. This is used to instance a shape node. (ie. "parent -add -shape" is equivalent to the "instance" command). This flag is primarily used by the file format.
	# noConnections(nc)	boolean	create
		# The parent command will normally generate new instanced set connections when adding instances. (ie. make a connection to the shading engine for new instances) This flag supresses this behaviour and is primarily used by the file format.

# Duplicating (Does not need to be included on Shelf!)
	
	duplicatePreset(1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1)

	# Listed as Mel when made into button

	duplicate('object')

	# 	name(n)	string	create
		# name to give duplicated object(s)
	# smartTransform(st)	boolean	create
		# remembers last transformation and applies it to duplicated object(s)
	# upstreamNodes(un)	boolean	create
		# the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.
	# inputConnections(ic)	boolean	create
		# Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the nodes at the input side are not duplicated (unlike the -un option).
	# returnRootsOnly(rr)	boolean	create
		# return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted in the result. This flag controls only what is returned in the output string[], and it does NOT change the behaviour of the duplicate command.
	# renameChildren(rc)	boolean	create
		# rename the child nodes of the hierarchy, to make them unique.
	# instanceLeaf(ilf)	boolean	create
		# instead of duplicating leaf DAG nodes, instance them.
	# parentOnly(po)	boolean	create
		# Duplicate only the specified DAG node and not any of its children.
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	
	circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand

	# Maya shelf editor lists as Mel command

	circle( nr=(0, 0, 1), c=(0, 0, 0) )
		# create full circle at origin on the x-y plane

	# first(fp)	[linear, linear, linear]	createqueryedit
		# The start point of the circle if fixCenter is false. Determines the orientation of the circle if fixCenter is true.
	# firstPointX(fpx)	linear	createqueryedit
		# X of the first point. 
		# Default: 1
	# firstPointY(fpy)	linear	createqueryedit
		# Y of the first point. 
		# Default: 0
	# firstPointZ(fpz)	linear	createqueryedit
		# Z of the first point. 
		# Default: 0
	# normal(nr)	[linear, linear, linear]	createqueryedit
		# The normal of the plane in which the circle will lie.
	# normalX(nrx)	linear	createqueryedit
		# X of the normal direction. 
		# Default: 0
	# normalY(nry)	linear	createqueryedit
		# Y of the normal direction. 
		# Default: 0
	# normalZ(nrz)	linear	createqueryedit
		# Z of the normal direction. 
		# Default: 1
	# center(c)	[linear, linear, linear]	createqueryedit
		# The center point of the circle.
	# centerX(cx)	linear	createqueryedit
		# X of the center point. 
		# Default: 0
	# centerY(cy)	linear	createqueryedit
		# Y of the center point. 
		# Default: 0
	# centerZ(cz)	linear	createqueryedit
		# Z of the center point. 
		# Default: 0
	# radius(r)	linear	createqueryedit
		# The radius of the circle. 
		# Default: 1.0
	# sweep(sw)	angle	createqueryedit
		# The sweep angle determines the completeness of the circle. A full circle is 2Pi radians, or 360 degrees. 
		# Default: 6.2831853
	# useTolerance(ut)	boolean	createqueryedit
		# Use the specified tolerance to determine resolution. Otherwise number of sections will be used. 
		# Default: false
	# degree(d)	int	createqueryedit
		# The degree of the resulting circle: 1 - linear, 3 - cubic 
		# Default: 3
	# sections(s)	int	createqueryedit
		# The number of sections determines the resolution of the circle. Used only if useTolerance is false. 
		# Default: 8
	# tolerance(tol)	linear	createqueryedit
		# The tolerance with which to build a circle. Used only if useTolerance is true 
		# Default: 0.01
	# fixCenter(fc)	boolean	createqueryedit
		# Fix the center of the circle to the specified center point. Otherwise the circle will start at the specified first point. 
		# Default: true
	# Advanced flags
	# caching(cch)	boolean	createqueryedit
		# Modifies the node caching mode. See the node documentation for more information. 
		# Note: For advanced users only.
	# nodeState(nds)	int	createqueryedit
		# Modifies the node state. See the node documentation for more information. 
		# Note: For advanced users only.
	# Common flags
	# name(n)	string	create
		# Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace does not exist, it will be created.
	# constructionHistory(ch)	boolean	create
		# Turn the construction history on or off
	# object(o)	boolean	create
		# Create the result, or just the dependency node

# Square
	
	curve -d 1 -p -0.0656168 0 0 -p -0.0656168 0 0.0328084 -p -0.0656168 0 0.0656168 -p -0.0328084 0 0.0656168 -p 0 0 0.0656168 -p 0.0328084 0 0.0656168 -p 0.0656168 0 0.0656168 -p 0.0656168 0 0.0328084 -p 0.0656168 0 0 -p 0.0656168 0 -0.0328084 -p 0.0656168 0 -0.0656168 -p 0.0328084 0 -0.0656168 -p 0 0 -0.0656168 -p -0.0328084 0 -0.0656168 -p -0.0656168 0 -0.0656168 -p -0.0656168 0 -0.0328084 -p -0.0656168 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;

	# Maya shelf editor lists as Mel command

	# bezier(bez)	boolean	create
		# The created curve will be a bezier curve.
	# degree(d)	float	create
		# The degree of the new curve. Default is 3. Note that you need (degree+1) curve points to create a visible curve span. eg. you must place 4 points for a degree 3 curve.
	# replace(r)	boolean	create
		# Replaces an entire existing curve. If you use this flag, you must specify the name of the curve to replace, at the end of the command. (See examples below.)
	# append(a)	boolean	create
		# Appends point(s) to the end of an existing curve. If you use this flag, you must specify the name of the curve to append to, at the end of the command. (See examples below.)
	# point(p)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of a point. "linear" means that this flag can take values with units.
	# pointWeight(pw)	[linear, linear, linear, float]	createmultiuse
		# The x,y,z and w values of a point, where the w is a weight value. A rational curve will be created if this flag is used. "linear" means that this flag can take values with units.
	# editPoint(ep)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of an edit point. "linear" means that this flag can take values with units. This flag can not be used with the -point or the -pointWeight flags.
	# knot(k)	float	createmultiuse
		# A knot value in a knot vector. One flag per knot value. There must be (numberOfPoints + degree - 1) knots and the knot vector must be non-decreasing.
	# periodic(per)	boolean	create
		# If on, creates a curve that is periodic. Default is off.
	# objectSpace(os)	boolean	create
		# Points are in object, or "local" space. This is the default. You cannot specify both "-os" and "-ws" in the same command.
	# worldSpace(ws)	boolean	create
		# Points are in world space. The default is "-os". You cannot specify both "-os" and "-ws" in the same command.
		
# Cube
	
	curve -d 1 -p -0.0502104 0.0502104 0.0502104 -p -0.0502104 -0.0502104 0.0502104 -p -0.0502104 -0.0502104 -0.0502104 -p -0.0502104 0.0502104 -0.0502104 -p -0.0502104 0.0502104 0.0502104 -p 0.0502104 0.0502104 0.0502104 -p 0.0502104 -0.0502104 0.0502104 -p -0.0502104 -0.0502104 0.0502104 -p 0.0502104 -0.0502104 0.0502104 -p 0.0502104 -0.0502104 -0.0502104 -p 0.0502104 0.0502104 -0.0502104 -p 0.0502104 0.0502104 0.0502104 -p 0.0502104 0.0502104 -0.0502104 -p -0.0502104 0.0502104 -0.0502104 -p -0.0502104 -0.0502104 -0.0502104 -p 0.0502104 -0.0502104 -0.0502104 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;

	# Maya shelf editor lists as Mel command

	# bezier(bez)	boolean	create
		# The created curve will be a bezier curve.
	# degree(d)	float	create
		# The degree of the new curve. Default is 3. Note that you need (degree+1) curve points to create a visible curve span. eg. you must place 4 points for a degree 3 curve.
	# replace(r)	boolean	create
		# Replaces an entire existing curve. If you use this flag, you must specify the name of the curve to replace, at the end of the command. (See examples below.)
	# append(a)	boolean	create
		# Appends point(s) to the end of an existing curve. If you use this flag, you must specify the name of the curve to append to, at the end of the command. (See examples below.)
	# point(p)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of a point. "linear" means that this flag can take values with units.
	# pointWeight(pw)	[linear, linear, linear, float]	createmultiuse
		# The x,y,z and w values of a point, where the w is a weight value. A rational curve will be created if this flag is used. "linear" means that this flag can take values with units.
	# editPoint(ep)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of an edit point. "linear" means that this flag can take values with units. This flag can not be used with the -point or the -pointWeight flags.
	# knot(k)	float	createmultiuse
		# A knot value in a knot vector. One flag per knot value. There must be (numberOfPoints + degree - 1) knots and the knot vector must be non-decreasing.
	# periodic(per)	boolean	create
		# If on, creates a curve that is periodic. Default is off.
	# objectSpace(os)	boolean	create
		# Points are in object, or "local" space. This is the default. You cannot specify both "-os" and "-ws" in the same command.
	# worldSpace(ws)	boolean	create
		# Points are in world space. The default is "-os". You cannot specify both "-os" and "-ws" in the same command.

# Arrow
	
	curve -d 1 -p -0.0502104 0.0502104 0.0502104 -p -0.0502104 -0.0502104 0.0502104 -p -0.0502104 -0.0502104 -0.0502104 -p -0.0502104 0.0502104 -0.0502104 -p -0.0502104 0.0502104 0.0502104 -p 0.0502104 0.0502104 0.0502104 -p 0.0502104 -0.0502104 0.0502104 -p -0.0502104 -0.0502104 0.0502104 -p 0.0502104 -0.0502104 0.0502104 -p 0.0502104 -0.0502104 -0.0502104 -p 0.0502104 0.0502104 -0.0502104 -p 0.0502104 0.0502104 0.0502104 -p 0.0502104 0.0502104 -0.0502104 -p -0.0502104 0.0502104 -0.0502104 -p -0.0502104 -0.0502104 -0.0502104 -p 0.0502104 -0.0502104 -0.0502104 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;

	# Maya shelf editor lists as Mel command

	# bezier(bez)	boolean	create
		# The created curve will be a bezier curve.
	# degree(d)	float	create
		# The degree of the new curve. Default is 3. Note that you need (degree+1) curve points to create a visible curve span. eg. you must place 4 points for a degree 3 curve.
	# replace(r)	boolean	create
		# Replaces an entire existing curve. If you use this flag, you must specify the name of the curve to replace, at the end of the command. (See examples below.)
	# append(a)	boolean	create
		# Appends point(s) to the end of an existing curve. If you use this flag, you must specify the name of the curve to append to, at the end of the command. (See examples below.)
	# point(p)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of a point. "linear" means that this flag can take values with units.
	# pointWeight(pw)	[linear, linear, linear, float]	createmultiuse
		# The x,y,z and w values of a point, where the w is a weight value. A rational curve will be created if this flag is used. "linear" means that this flag can take values with units.
	# editPoint(ep)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of an edit point. "linear" means that this flag can take values with units. This flag can not be used with the -point or the -pointWeight flags.
	# knot(k)	float	createmultiuse
		# A knot value in a knot vector. One flag per knot value. There must be (numberOfPoints + degree - 1) knots and the knot vector must be non-decreasing.
	# periodic(per)	boolean	create
		# If on, creates a curve that is periodic. Default is off.
	# objectSpace(os)	boolean	create
		# Points are in object, or "local" space. This is the default. You cannot specify both "-os" and "-ws" in the same command.
	# worldSpace(ws)	boolean	create
		# Points are in world space. The default is "-os". You cannot specify both "-os" and "-ws" in the same command.

# Pyramid
	
	curve -d 1 -p -0.000383286 -0.0443104 -0.0546086 -p -0.0549919 -0.0443104 -4.77403e-09 -p -0.000383296 -0.0443104 0.0546086 -p 0.0542253 -0.0443104 0 -p -0.000383286 -0.0443104 -0.0546086 -p -0.000383294 0.0443104 0 -p 0.0542253 -0.0443104 0 -p -0.000383296 -0.0443104 0.0546086 -p -0.000383294 0.0443104 0 -p -0.0549919 -0.0443104 -4.77403e-09 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;

	# Maya shelf editor lists as Mel command

	# bezier(bez)	boolean	create
		# The created curve will be a bezier curve.
	# degree(d)	float	create
		# The degree of the new curve. Default is 3. Note that you need (degree+1) curve points to create a visible curve span. eg. you must place 4 points for a degree 3 curve.
	# replace(r)	boolean	create
		# Replaces an entire existing curve. If you use this flag, you must specify the name of the curve to replace, at the end of the command. (See examples below.)
	# append(a)	boolean	create
		# Appends point(s) to the end of an existing curve. If you use this flag, you must specify the name of the curve to append to, at the end of the command. (See examples below.)
	# point(p)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of a point. "linear" means that this flag can take values with units.
	# pointWeight(pw)	[linear, linear, linear, float]	createmultiuse
		# The x,y,z and w values of a point, where the w is a weight value. A rational curve will be created if this flag is used. "linear" means that this flag can take values with units.
	# editPoint(ep)	[linear, linear, linear]	createmultiuse
		# The x, y, z position of an edit point. "linear" means that this flag can take values with units. This flag can not be used with the -point or the -pointWeight flags.
	# knot(k)	float	createmultiuse
		# A knot value in a knot vector. One flag per knot value. There must be (numberOfPoints + degree - 1) knots and the knot vector must be non-decreasing.
	# periodic(per)	boolean	create
		# If on, creates a curve that is periodic. Default is off.
	# objectSpace(os)	boolean	create
		# Points are in object, or "local" space. This is the default. You cannot specify both "-os" and "-ws" in the same command.
	# worldSpace(ws)	boolean	create
		# Points are in world space. The default is "-os". You cannot specify both "-os" and "-ws" in the same command.

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint

	doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };

	# Maya shelf editor lists as Mel command

	parentConstraint( 'object1', 'object2' )

	# name(n)	string	createqueryedit
		# Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType
	# weight(w)	float	createqueryedit
		# Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
	# remove(rm)	boolean	edit
		# removes the listed target(s) from the constraint.
	# targetList(tl)	boolean	query
		# Return the list of target objects.
	# weightAliasList(wal)	boolean	query
		# Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
	# layer(l)	string	createedit
		# Specify the name of the animation layer where the constraint should be added.
	# skipTranslate(st)	string	createmultiuse
		# Causes the axis specified not to be considered when constraining translation. Valid arguments are "x", "y", "z" and "none".
	# skipRotate(sr)	string	createmultiuse
		# Causes the axis specified not to be considered when constraining rotation. Valid arguments are "x", "y", "z" and "none".
	# maintainOffset(mo)	boolean	create
		# If this flag is specified the position and rotation of the constrained object will be maintained.
	# createCache(cc)	[float, float]	edit
		# This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames. 
		# The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
	# deleteCache(dc)	boolean	edit
		# Delete an existing interpolation cache.

# Orient Constraint

	doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };

	# Maya shelf editor lists as Mel command

	orientConstraint( 'object1', 'object2' )

	# name(n)	string	createqueryedit
		# Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType
	# weight(w)	float	createqueryedit
		# Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
	# remove(rm)	boolean	edit
		# removes the listed target(s) from the constraint.
	# targetList(tl)	boolean	query
		# Return the list of target objects.
	# weightAliasList(wal)	boolean	query
		# Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
	# layer(l)	string	createedit
		# Specify the name of the animation layer where the constraint should be added.
	# offset(o)	[float, float, float]	createqueryedit
		# Sets or queries the value of the offset. Default is 0,0,0.
	# maintainOffset(mo)	boolean	create
		# The offset necessary to preserve the constrained object's initial orientation will be calculated and used as the offset.
	# skip(sk)	string	createeditmultiuse
		# Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". The default value in create mode is "none". This flag is multi-use.
	# createCache(cc)	[float, float]	edit
		# This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames. 
		# The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
	# deleteCache(dc)	boolean	edit
		# Delete an existing interpolation cache.

# Point Constraint

	doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };

	# Maya shelf editor lists as Mel command

	pointConstraint( 'object1', 'object2' )

	# name(n)	string	createqueryedit
		# Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType
	# weight(w)	float	createqueryedit
		# Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
	# remove(rm)	boolean	edit
		# removes the listed target(s) from the constraint.
	# targetList(tl)	boolean	query
		# Return the list of target objects.
	# weightAliasList(wal)	boolean	query
		 Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
	# layer(l)	string	createedit
		# Specify the name of the animation layer where the constraint should be added.
	# offset(o)	[float, float, float]	createqueryedit
		# Sets or queries the value of the offset. Default is 0,0,0.
	# maintainOffset(mo)	boolean	create
		# The offset necessary to preserve the constrained object's initial position will be calculated and used as the offset.
	# skip(sk)	string	createeditmultiuse
		# Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.

# Pole Vector Constraint
	# How does this constraint differ from the previous three.
	# Pole vector differs by requiring you to have to use it when using a revolving-plane ik handle

	poleVectorConstraint -weight 1

	# Maya shelf editor lists as Mel command

	poleVectorConstraint( 'object1', 'icon1' )

	# name(n)	string	createqueryedit
		# Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType
	# weight(w)	float	createqueryedit
		# Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
	# remove(rm)	boolean	edit
		# removes the listed target(s) from the constraint.
	# targetList(tl)	boolean	query
		# Return the list of target objects.
	# weightAliasList(wal)	boolean	query
		# Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag
	# layer(l)	string	createedit
		# Specify the name of the animation layer where the constraint should be added.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

	addAttr -ln "float"  -at double  |pCube1;
	setAttr -e-keyable true |pCube1.float;

	# Maya shelf editor lists as Mel command

	addAttr( longName='float', attributeType='Scaler', min=0.001, max=10000 )

	# 	longName(ln)	string	createquery
		# Sets the long name of the attribute.
	# shortName(sn)	string	createquery
		# Sets the short name of the attribute.
	# niceName(nn)	string	createqueryedit
		# Sets the nice name of the attribute for display in the UI. Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog. (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
	# binaryTag(bt)	string	createquery
		# This flag is obsolete and does not do anything any more
	# attributeType(at)	string	createquery
		# Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
	# dataType(dt)	string	createquerymultiuse
		# Specifies the data type. See "setAttr" for more information on data type names.
	# defaultValue(dv)	float	createqueryedit
		# Specifies the default value for the attribute (can only be used for numeric attributes).
	# multi(m)	boolean	createquery
		# Makes the new attribute a multi-attribute.
	# indexMatters(im)	boolean	createquery
		# Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
	# minValue(min)	float	createqueryedit
		# Specifies the minimum value for the attribute (can only be used for numeric attributes).
	# hasMinValue(hnv)	boolean	createqueryedit
		# Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
	# maxValue(max)	float	createqueryedit
		# Specifies the maximum value for the attribute (can only be used for numeric attributes).
	# hasMaxValue(hxv)	boolean	createqueryedit
		# Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
	# cachedInternally(ci)	boolean	createquery
		# Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.
	# internalSet(internalSet)	boolean	createquery
		# Whether or not the internal cached value is set when this attribute value is changed. This is an internal flag used for updating UI elements.
	# parent(p)	string	createquery
		# Attribute that is to be the new attribute's parent.
	# numberOfChildren(nc)	uint	createquery
		# How many children will the new attribute have?
	# usedAsColor(uac)	boolean	createquery
		# Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag. The attribute type "-at" should be "double3" or "float3" as appropriate. It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative. The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
	# usedAsFilename(uaf)	boolean	createquery
		# Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
	# hidden(h)	boolean	createquery
		# Will this attribute be hidden from the UI?
	# readable(r)	boolean	createquery
		# Can outgoing connections be made from this attribute?
	# writable(w)	boolean	createquery
		# Can incoming connections be made to this attribute?
	# storable(s)	boolean	createquery
		# Can the attribute be stored out to a file?
	# keyable(k)	boolean	createquery
		# Is the attribute keyable by default?
	# fromPlugin(fp)	boolean	createquery
		# Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
	# softMinValue(smn)	float	createqueryedit
		# Soft minimum, valid for numeric attributes only. Specifies the upper default limit used in sliders for this attribute.
	# hasSoftMinValue(hsn)	boolean	createquery
		# Flag indicating whether a numeric attribute has a soft minimum.
	# softMaxValue(smx)	float	createqueryedit
		# Soft maximum, valid for numeric attributes only. Specifies the upper default limit used in sliders for this attribute.
	# hasSoftMaxValue(hsx)	boolean	createquery
		# Flag indicating whether a numeric attribute has a soft maximum.
	# category(ct)	string	createqueryeditmultiuse
		# An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.
	# enumName(en)	string	createqueryedit
		# Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5. (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu. Extra menu items can appear that represent the numbers inbetween non-sequential option values. To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box. For example: "solo=1:triplet=2:quintet=3".)
	# exists(ex)	boolean	createquery
		# Returns true if the attribute queried is a user-added, dynamic attribute; false if not.

# Create Separator Attribute

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.

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


