'''
Research Notes

Name

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: ALL CONSTRAINTS, MO on and off

Drop Down Menus: CTRL ICON 

'''

'''
Each tool you will need document:
	1) MEL Commmand
	2) What type of command is it and how did you find it?
	3) Convert MEL to Python.
	4) Important Flags
'''
import pymel.core as pm
'''
General Tools Research
'''

# Freeze Transforms
	#MEL Command = makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	# I researched the help docs, and I did it in maya
	#/////Convert to python normal(n), preserveNormals(pn)

pm.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)



# Delete History
	# MEL COMMAND : DeleteHistory; not enough info
	# looked up python commaned ref
	#constructionHistory(ch)

pm.delete(ch = True)

# Center Pivot
	#MEL command = xform -cp;
	#research xform command in python command ref
	#xform( [objects...] , [absolute=boolean], [boundingBox=boolean], [boundingBoxInvisible=boolean], [centerPivots=boolean]

pm.xform(cp = True)


# Single Chain and Rotate Plan IKs
	#create and Ik and Sc solver looked up in python command ref
	  pm.ikHandle(sj=root_joint, ee=ankle_joint, sol='ikRPsolver')
	 pm.ikHandle(sj=ankle_joint, ee=ball_joint)
	# created a seperate script for these commands**

# Cluster
		#MEL Command
		## newCluster " -envelope 1";
		#// Result: cluster1 cluster1Handle // 

pm.cluster()





# Grouping (Does not need to be included on Shelf!)
	#MEL = doGroup 0 1 1;
	#group( [objects...] , [absolute=boolean], [empty=boolean], [name=string], [parent=string], [relative=boolean], [useAsGroup=string], [world=boolean]) 

pm.group()


# Parenting (Does not need to be included on Shelf!)
	#mel= parent;
	#parent( [dagObject...] [dagObject] , [absolute=boolean], [addObject=boolean], [noConnections=boolean], [relative=boolean], [removeObject=boolean], [shape=boolean], [world=boolean]) 
pm.parent()

# Duplicating (Does not need to be included on Shelf!)
# mel = duplicate -rr;
#duplicate( [objects...] , [inputConnections=boolean], [instanceLeaf=boolean], [name=string], [parentOnly=boolean], [renameChildren=boolean], [returnRootsOnly=boolean], [smartTransform=boolean], [upstreamNodes=boolean])
pm.duplicate(rr = True)
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
#mel = circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1
# created a circle in maya
#conversion
pm.circle(c = [0, 0, 0], nr = [0, 1 , 0], sw = 360, r = 1, d = 3, ut = 0, tol = 0.01, s = 8, ch = False)
selection = pm.ls(selection = True)
pm.rename(selection, "Circle_Icon1"))

# Square
#Created a cube, then used cv curve tool to snap to bottom face
# mel code = curve -d 1 -p 0.5 0 0.5 -p 0.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 0.5 -p 0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4
#
# These commands create curves with four control vertices.
# The first one is created without weights.  The third command
# shows how you can use units to specify position.
#cmds.curve( p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)] )


# conversion to python

pm.curve(d = 1, p = [(0.5, 0.0, 0.5), (0.5, 0.0, -0.5), (-0.5, 0.0, -0.5), (-0.5, 0.0, 0.5), (0.5, 0 , 0.5) ], k = [0, 1, 2, 3, 4] )
selection = pm.ls(selection = True)
pm.rename(selection, "Square_Icon1")

# Cube
#Created a poly cube then used the cv curve tool to snap to point
# mel code = curve -d 1 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 ;
# convert to python


pm.curve(d = 1, p = [(0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5)], k = [0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
selection = pm.ls(selection = True)
pm.rename(selection, "Cube_Icon1")

# Arrow
#Created arrow with cv curve tool
# mel : curve -d 1 -p -4 0 8 -p 4 0 8 -p 4 0 0 -p 8 0 0 -p 0 0 -8 -p -8 0 0 -p -4 0 0 -p -4 0 8 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
#conversion to python
#scale object down then freeze transform
#scale -r 0.133317 0.133317 0.133317 ;


pm.curve(d = 1, p = [(-4, 0, 8), (4, 0, 8), (4, 0, 0), (8, 0, 0), (0, 0, -8), (-8, 0, 0), (-4, 0, 0), (-4, 0, 8)], k = (1, 2, 3, 4, 5, 6, 7, 8))
pm.scale(.13, .13, .13)
pm.rotate(0, 180, 0)
pm.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
selection = pm.ls(selection = True)
pm.rename(selection, "Arrow_Icon1")


'''
Constraints
- Remember to test offset on and off with these commands.
'''
'''

I CREATED TWO SHELF BUTTONS that have dropdowns for MO on and off
'''


# Parent Constraint
# I created a parent contraint in maya
#Mel: parentConstraint -mo -weight 1;
# parentConstraint( [target ...] [object] , [createCache=[float, float]], [deleteCache=boolean], [layer=string], [maintainOffset=boolean], [name=string], [remove=boolean], [skipRotate=string], [skipTranslate=string], [targetList=boolean], [weight=float], [weightAliasList=boolean]) 
pm.parentConstraint(target, object, mo = True, weight = 1)

# Orient Constraint
#same as parentConstraint
pm.orientConstraint(target, object, mo = True, weight = 1)
# Point Constraint
#same as parentConstraint
pm.pointConstraint(target, object, mo = True, weight = 1)

# Pole Vector Constraint
	#mel = poleVectorConstraint -weight 1; // Result: ikHandle1_poleVectorConstraint1 // 
# How does this constraint differ from the previous three.
#An poleVectorConstraint takes as input one or more "target" DAG transform nodes at which to aim pole vector for an IK handle using the rotate plane solver. The pole vector is adjust such that the in weighted average of the world space position target objects lies is the "rotate plane" of the handle.

# the polevector constraint is used on an Ik 
pm.poleVectorConstraint()
'''
Attributes (Convered in Podcast)
'''
# Create float attribute
#mel:	 addAttr -ln "float_attr"  -at double  |nurbsCircle1;
#		setAttr -e-keyable true |nurbsCircle1.float_attr;
#Create attr name "float attr"
# python conversion


pm.addAttr(ln = raw_input(), at = "double", keyable = True)



# Create Separator Attribute
#
#MEL:addAttr -ln "_____________"  -at "enum" -en "________________:"  |hierarchy_project_example|lt_index_01_local|lt_index_01_icon;
		#setAttr -e-keyable true |hierarchy_project_example|lt_index_01_local|lt_index_01_icon._____________;


pm.addAttr(ln = "_______", at = "enum", en = "_______", keyable = True)
# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.

pm.addAttr(ln = name, at = "double")
pm.setAttr(name, k = True)

pm.addAttr(ln = name2, at = "double")
pm.setAttr(name2, k = True)

pm.addAttr(ln = name3, at = "double")
pm.setAttr(name3, k = True)

# These are practical examples of python code. 




'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.

Research:
Detach Component
	Messed around and found polySplitEdge
	Researched command ref
	pm.polySplitEdge(operation=1)




Separate
did it in  may and got mel
mel:  polySeparate -ch 1 pCubeShape2;

did research on polySeparate on command ref

pm.polySeparate(ch = True)


Extract

did this in may and went through 3 commands
select -r polySurface1.f[1] ;
polyChipOff -ch 1 -kft 1 -dup 0 -off 0 polySurface1.f[1];
// Result: polyChipOff1 // 
polyPerformAction ("polySeparate -rs 1", "o", 0);
polySeparate -rs 1 -ch 1 polySurfaceShape1;
// Result: polySurface3 polySurface4 polySeparate2 // 
// Result: polySeparate -rs 1 -ch 1 polySurfaceShape1 // 

looked up each command in ref

pm.polyChipOff(ch = True, kft = True)

I could not figure this one out

Combind
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
'''


