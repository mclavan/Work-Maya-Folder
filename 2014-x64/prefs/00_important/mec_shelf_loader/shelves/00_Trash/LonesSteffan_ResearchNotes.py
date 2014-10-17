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
	#Mel: makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	#Maya command, found using script editor
	#Python: pm.makeIdentity( apply=True, t=1, r=1, s=1, n=0 )
	#flags: -t freezes translate -r freezes rotate -s freezes scale -n freezes normals

# Delete History
	#Mel: deleteHistory;
	#Maya command , found using echo
	#python: pm.delete(ch = True)

# Center Pivot
	#Mel: CenterPivot;
	#Maya command, found using echo
	#python: pm.xform(cp = True)

# Single Chain and Rotate Plane IKs
	#single chain:
		#Mel: ikHandle;
		#Maya command, found using echo
		#python: pm.ikHandle()
		#Flags: sj= start joint  ee= end joint
	#RP:
		#mel: ikHandle -sol ikRPsolver;
		#Maya command, found using echo
		#python: pm.ikHandle(sol='ikRPsolver')
		#Flags: sol = solver to use  ikRPsolver = set up to use RP

# Cluster
	#mel: newCluster " -envelope 1";
	#maya command, found using script editor
	#python: pm.cluster()

# Grouping (Does not need to be included on Shelf!)
	#Mel: doGroup 0 1 1;
	#runtime command, runs when command G is hit, found using script editor
	#python: pm.group()

# Parenting (Does not need to be included on Shelf!)
	#Mel: parent;
	#runtime command , runs when p is hit , found using script editor
	#python: pm.parent()

# Duplicating (Does not need to be included on Shelf!)
	#Mel: duplicate -rr;
	#runtime command, found when pressed command D , found using script editor
	#python: pm.duplicate()

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	#Mel: Circle;
	#maya command; found using script editor
	#python: pm.circle()
	#flags r = radius  n = normal  

# Square
	#mel: curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
	#maya command, found using script editor
	#python: pm.curve( d=1 ,p=[(-1 ,0 ,-1) , (1 ,0 ,-1) , (1,0 ,1), (-1, 0 ,1),( -1, 0 ,-1)], k=[ 0,1,2,3,4])
	#flags: d= degree 1 = linear 3 = bezier  p = point coords  k = knots

# Cube
	#mel: curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;
	#maya command, found using script editor
	#python: pm.curve(d=1 , p = [(-0.5,0.5,0.5), (0.5 ,0.5 ,0.5) , (0.5 ,0.5 ,-0.5) , (-0.5,0.5,-0.5), (-0.5,0.5,0.5) ,(-0.5,-0.5,0.5) , (-0.5,-0.5,-0.5), (-0.5,0.5,-0.5) , (0.5,0.5,-0.5) , (0.5,-0.5,-0.5) , (-0.5,-0.5,-0.5) , (0.5,-0.5,-0.5) ,(0.5,-0.5,0.5), (0.5,0.5,0.5) ,(0.5,-0.5,0.5),(-0.5,-0.5,0.5)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

# Arrow
	#mel: curve -d 1 -p -2 0 0 -p 0 0 -2 -p 0 0 -1 -p 3 0 -1 -p 3 0 1 -p 0 0 1 -p 0 0 2 -p -2 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
	#maya command, found using script editor
	#python: pm.curve(d=1, p=[(-2,0,0),(0,0,-2),(0,0,-1),(3,0,-1),(3,0,1),(0,0,1),(0,0,2),(-2,0,0)], k=[0,1,2,3,4,5,6,7])


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	#mel: parentConstraint;
	#maya command found using script editor
	#python: pm.parentConstraint()
	#flags: mo= maintain offset

# Orient Constraint
	#mel: orientConstraint;
	#maya command found using script editor
	#python: pm.orientConstraint()
	#flas mo= maintain offset

# Point Constraint
	#mel: pointConstraint;
	#maya command found using script editor
	#python: pm.pointConstraint()
	#flags: mo = maintain offset

# Pole Vector Constraint
# How does this constraint differ from the previous three. No maintain offset
	#mel: poleVectorConstraint;
	#maya command found using script editor
	#python: pm.poleVectorConstraint()

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	#mel: addAttr -ln "name" -at "float";
	#maya command found using script editor
	#python: pm.addAttr(name = "name" , keyable = True, float=True)
	#flags: float = makes float attribute n= name

# Create Separator Attribute
	#mel: addAttr -ln "name -at enum;
	#maya command found using script editor
	#python: pm.addAttr(name = 'name' , keyable = true ,enum=True)
	#flags: enum = makes enum attribute

# Template Attributes 
# Create a group of attributes at one time. 
	#mel:  addAttr -ln "float1" -at "float";
		#  addAttr -ln "float2" -at "float";
		#  addAttr -ln "float3" -at "float";

	#python: pm.addAttr(name = "name" , keyable = True, float=True)
		#	 pm.addAttr(name = "name1" , keyable = True, float=True)
		# 	 pm.addAttr(name = "name2" , keyable = True, float=True)
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


