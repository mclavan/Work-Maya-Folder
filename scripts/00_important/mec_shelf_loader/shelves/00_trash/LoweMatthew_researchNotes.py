'''
Research Notes

LoweMatthew

Current Shelf Tools: 





General Tools Research


# Freeze Transforms

1) makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

2) "command" The makeIdentity command is a quick way to reset the selected transform and all its
children down to the shape level by the identity transforms.
It is an undoable command but not queryable or editable. 

3) pm.makeIdentity(apply=true, t=1,r=1,s=1,n=0,pn=1)

4) -apply, -translate(-t) , -rotate(-r) , -scale(-s) , -jointOrient(-jo) , -normal(-n) 
-preserveNormals(-pn)

# Delete History

1)DeleteHistory;
delete -ch;

2) "runtime-command" The "DeleteHistory:" command is a pymel language command but the delete; command is
used to delete selected objects, or objects specified along with the command such as the 
history of an object like in this case. 

3) pm.delete=(True)

4)-attribute, -channels, -constraints, -constructionHistory, -controlPanel, -expressions, -hierarchy,
-inputConnectionsAndNodes, -shapes, -staticChannels, -timeAnimationCurves, -unitlessAnimationCurves

# Center Pivot

1) CenterPivot; 
	delete -cp;

2) This is a is a runtime command. xform command can be used query/set element in a transfomation node. It 
can also be used to query some values that cannot be set directly such as the transformation matrix or bounding box.
it can also set the pivot points value's. 

3) pm.xform(cp=True) 

4) -absolute, -boundingBox. -boundingBoxInvisble, -centerPivots, -deletePriorHistory, -euler, -matrix,
-objectSpace, -pivots, -preserve, -preserveUV, -reflection, -reflectionAboutBBox, -reflectionAboutOrigin,
-reflectAboutX, -reflectionAboutY, -reflectionAboutZ, -reflectionTolerance, -relative, -rotateOrder, 
-rotateTranslation, -rotation, -scale, -scalePivot, -scaleTranslation, -shear, -translation, -worldSpace,
-worldSapceDistance, -zeroTransformPivots

# Single Chain and Rotate Plan IKs

1)# IK handle tool

IKHandleTool;
setToolTo ikHandleContext;
editMenuUpdate MayaWindow|mainEditMenu;
changeToolIcon;
dR_contextChanged;
currentCtx;

# single chain ik

select -r joint1.rotatePivot ;
select -add joint2.rotatePivot ;
ikHandle -p 0 -s 0;

# Multi-chain ik

select -r joint1.rotatePivot ;
select -add joint2.rotatePivot ;
ikHandle -p 0 -sol ikRPsolver -s 0;

2) The handle command is used to create, edit, and query a hanlde within Maya. The standard edit (-e) and
query (-q) flags are used for edit and query functions. If there are two joints selected and neither
-startJoint nor -endEffector flags are not specifiec, the the handle will be created from the selected joints.
If the joint is selected and neither -startJoint nor -endEffector flags are specified, then the handle will 
be created with th selected joint as tge ebd-effector and the start joint will be the top of the joint chain
containing the end effector. 

3) # single chain ik
	pm.select (r=True, joint1.rotatePivot)
	pm.select (add=True, joint2.rotatePivot)
	pm.ikHandle (p=0, s=0)

   # multi-chain ik
	pm.select (r=True, joint1.rotatePivot)
	pm.select (add=True, joint2.rotatePivot)
	pm.ikHandle (p=0, sol=True, ikRPsolver=True, s=0)

4) -name, -startJoint, -endEffector, -priority, -autoPriority, -weight, -positionWeight, -solver, -forceSolver,
-snapHandleToEffector, -anapHandleFlagToggle, -sticky, -connectEffector, -jointList, -exists, -setupForRPsolver,
-enableHandles, -disableHandles, -curve, -createCurve, -freezeJoints, -simplifyCurve, -rootOnCurve, -twistType,
-createRootAxis, -parentCurve, -snapCurve, -numSpace, -rootTwistMode

# Cluster

1) newCluster " -envelope 1";

2) The cluster command creates a cluster or edits the membership of an existing cluster. The commancd returns 
the name of the cluster node upon creation of a new cluster. After creating a cluster, the cluster's weights 
can be modified using the percent command or the set editor window. 

3) pm.cluster (envelope=1)

4) -after, -afterReference, -before, -bindTools, -envelope, -exclusive, -frontOfChain, -geometry, -geometryIndices,
-ignoreSelected, -includeHiddenDelections, -name, -parallel, -prune, -relative, -remove, -resetGeometry, -split, weightedNode

# Grouping (Does not need to be included on Shelf!)

1) create an empty group node with no children (group -em -name null1;)
   create some objects and group them (sphere -n sphere1; circle -n circle1; group -n group1 circle1 sphere1;)
   create a group node under another node and move the sphere under the new group node. (group -parent null1 sphere1;)

2)This command groups the specified objects under a new group and returns the name of the new group. If the -em flag is 
specified, then an empty group (with no objects) is created. If the -w flag is specified then the new group is placed 
under the world, otherwise if -p is specified it is placed under the specified node. If neither -w or -p is specified 
the new group is placed under the lowest common group they have in common. (or the world if no such group exists)
If an object is grouped with another object that has the same name then one of the objects will be renamed by this command.

3) # create an empty group node with no children (pm.group( em=True, name='null1' ))
   # create some objects and group them ( pm.sphere( n='sphere1' ) pm.circle( n='circle1' ) pm.group( 'circle1', 'sphere1', n='group1' ))
   # create a group node under another node and move the sphere under the new group node. (pm.group( 'sphere1', parent='null1' ))

4) -name, -world, -parent, -empty, -relative, -absolute, -useAsGroup

# Parenting (Does not need to be included on Shelf!)

1) creating objects ( circle and empty group ) and moving the circle1 under group1 (MEL)

circle -name circle1; 
group -n group1;
parent circle1 group1;

2) This command parents (moves) objects under a new group, removes objects from an existing group, or adds/removes parents.
If the -w flag is specified all the selected or specified objects are parented to the world (unparented first).
If the -rm flag is specified then all the selected or specified instances are removed.
If there are more than two objects specified all the objects are parented to the last object specified.
If the -add flag is specified, the objects are not reparented but also become children of the last object specified.
If there is only a single object specified then the selected objects are parented to that object.
If an object is parented under a different group and there is an object in that group with the same name then this 
command will rename the parented object.

3) creating objects ( circle and empty group ) and moving the circle1 under group1 (Python)

pm.circle ( name ='circle1' )
pm.group ( name = 'group1' )
pm.parent ( 'circle' , 'group1' )

4) -absolute, -addObject, -noConnections, -relative, -removeObject, -shape, -world

# Duplicating (Does not need to be included on Shelf!)

1) duplicate -rr; 

2) This command duplicates the given objects. If no objects are given, then the selected list is duplicated. The upstream 
Nodes option forces duplication of all upstream nodes leading upto the selected objects.. Upstream nodes are defined as 
all nodes feeding into selected nodes. During traversal of Dependency graph, if another dagObject is encountered, then 
that node and all it's parent transforms are also duplicated.

3) pm.duplicate (rr=True)

4) -inputConnections, -instanceLeaf, -name, -parentOnly, -renameChildren, -returnRootsOnly, -smartTransform, -upstreamNodes

Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.

# Circle

1) CreateNURBSCircle;
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;

2) The circle command creates a circle or partial circle (arc) and can also place that object in the scene.

3) pm.circle (c = [0, 0 ,0] nr = [0, 1, 0] sw = 360, r = 1, d = 3, ut = 0, tol = 0, s = 8, ch = 1)

4) -caching, -center, -centerX, -centerY, -centerZ, -constructionHistory, -degree, -first, -firstPointX, -firstPointY, 
-firstPointZ, -fixCenter, -name, -nodeState, -normal, -normalX, -normalY, -normalZ, -object, -radius, -sections, -sweep, 
-tolerance, -useTolerance

# Square

1) CreateNURBSSquare;
nurbsSquarePreset(0,0,0,0,0,1,0,1,1,1,3,1);
nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ;

2) The nurbsSquare command creates a square and can also place that object in the scene.

3) pm.nurbsSquare (c = [ 0, 0, 0] nr = [ 0, 1, 0] sl1 = 1, sl2 = 1, sps = 1, d = 3, ch = 1)

4) -caching, -center, -centerX, -centerY, -centerZ, -constructionHistory, -degree, -name, -nodeState, 
-normal, -normalX, -normalY, -normalZ, -object, -sideLength1, -sideLength2, -spansPerSide

# Cube

1) nurbsCube -p 0 0 0 -ax 0 1 0 -w 1 -lr 1 -hr 1 -d 3 -u 1 -v 1 -ch 1;

2) The nurbsCube command creates a new NURBS Cube made up of six planes. It creates an unit cube with center at 
origin by default.

3) pm.nurbsCube ( p = [ 0, 0, 0] ax = [ 0, 1, 0] w = 1, lr = 1, hr = 1, d = 3, u = 1, v = 1, ch = 1)

4) -axis, -caching, -constructionHistory, -degree, -heightRatio, -lengthRatio, -name, -nodeState, -object, 
-patchesU, -patchesV, -pivot, -polygon, -width

# Arrow

1) curve -d 1 -p -6 4 0 -p -4 2 0 -p -5 2 0 -p -5 -1 0 -p -7 -1 0 -p -7 2 0 -p -8 2 0 -p -6 4 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

2) This command creates a curve in a specific shape resembling an arrow.

3) pm.curve ( d = 1, p = [-6, 4, 0] p = [-4, 2, 0] p = [-5, 2, 0] 
p = [-5, -1, 0] p = [-7, -1, 0] p = [-7, 2, 0] p = [8, 2, 0] p = [-6, 4, 0] 
k = 0, k = 1, k = 2, k = 3, k = 4, k = 5, k = 6, k = 7)

4) -append, -bezier, -degree, -editPoint, -knot, -objectSpace, -periodic, -point, -pointWeight, -replace, -worldSpace

Constraints
- Remember to test offset on and off with these commands.

# Parent Constraint

1) parentConstraint;

2) Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s). 
In the case of multiple targets, the overall position and rotation of the constrained object is the weighted average 
of each target's contribution to the position and rotation of the object. A parentConstraint takes as input one or 
more "target" DAG transform nodes at which to position and rotate the single "constraint object" DAG transform node. 
The parentConstraint positions and rotates the constrained object at the weighted average of the world space position, 
rotation and scale target objects.

3) pm.parentConstraint()

4) -createCache, -deleteCache, -layer, -maintainOffset, -name, -remove, -skipRotate, -skipTranslate, -targetList, -weight, 
-weightAliasList

# Orient Constraint

1) orientConstraint;

2) Constrain an object's orientation to match the orientation of the target or the average of a number of targets.
An orientConstraint takes as input one or more "target" DAG transform nodes to control the orientation of the single 
"constraint object" DAG transform The orientConstraint orients the constrained object to match the weighted average 
of the target world space orientations.

3) pm.orientConstraint()

4) -createCache, -deleteCache, -layer, -maintainOffset, -name, -offset, -remove, -skip, -targetList, -weight, -weightAliasList

# Point Constraint

1) pointConstraint;

2) Constrain an object's position to the position of the target object or to the average position of a number of targets.
A pointConstraint takes as input one or more "target" DAG transform nodes at which to position the single "constraint object"
DAG transform node. The pointConstraint positions the constrained object at the weighted average of the world space position
target objects.

3) pm.pointConstraint()

4) -layer, -maintainOffset, -name, -offset, -remove, -skip, -targetList, -weight, -weightAliasList

# Pole Vector Constraint

1) poleVectorConstraint;

2) Constrains the poleVector of an ikRPsolve handle to point at a target object or at the average position of a number 
of targets. An poleVectorConstraint takes as input one or more "target" DAG transform nodes at which to aim pole vector 
for an IK handle using the rotate plane solver. The pole vector is adjust such that the in weighted average of the world 
space position target objects lies is the "rotate plane" of the handle.

3) pm.poleVectorConstraint()

4) -layer, -name, -remove, -targetList, -weight, -weightAliasList

# How does this constraint differ from the previous three.

This type of constraint directly references the current rotate plane solver to determine the pole vector orientation.

Attributes (Convered in Podcast)

# Create float attribute

addAttr -ln "name of object" -at double -keyable true;

pm.addAttr (ln = 'name of object', at = 'double', keyable = True)

# Create Separator Attribute

addAttr (ln = 'name_of_object', at = 'enum', en = '-----------', channelBox = True) 

# Template Attributes 

attribute_name = raw_input()
pm.addAttr(ln=attribute_name, at='enum', en='---------', keyable=True)
print attribute_name

# Create a group of attributes at one time.

pm.addAttr (ln = 'index_curl', at = 'double', keyable = True)
pm.addAttr (ln = 'middle_curl', at = 'double', keyable = True)
pm.addAttr (ln = 'ring_curl', at = 'double', keyable = True)
pm.addAttr (ln = 'pinky_curl', at = 'double', keyable = True)
pm.addAttr (ln = 'thumb_curl', at = 'double', keyable = True)

#Proxy (Extra)
 Modeling commands can be difficult to use.  In creating a proxy toolset, 
 I typically use the Run Time Commands in this case.

 Research:

 #Detach Component

 DetachEdgeComponent;
 performDetachEdges;

 #Separate

 polySeparate -ch 1 pSphereShape1;

 #Extract

 hilite pSphere1 ;
 selectMode -component ;
 select -r pSphere1.f[0:399] ;
 polyChipOff -ch 1 -kft 1 -dup 0 -off 0 pSphere1.f[0:399];
 polyPerformAction ("polySeparate -rs 1", "o", 0);
 polySeparate -rs 1 -ch 1 pSphereShape1;

 #Combine

 polyUnite -ch 1 -mergeUVSets 0 -name pSphere1 pSphere1;

 #Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot

 makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
 DeleteHistory;
 delete -ch;
 CenterPivot;
 delete -cp;

'''


