'''
Research Notes

sorensonBrandon

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: parentConstraint double click mountains offset

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

	# makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

		pm.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1)

		# t=translate, r=rotate, s=scale, n=normal, pn=preserveNormals

# Delete History

	# delete -ch;

		pm.delete(ch=True)

		# ch is constructionHistory

# Center Pivot

	# xform -cp

		pm.xform(cp=True)

		# cp is centerPivot which sets the pivot to the objects bounding box.

# Single Chain and Rotate Plan IKs

	# Single Chain and Rotate Plan IKs
	# ikHandle, ikHandle -sol ikRPsolver

	pm.ikHandle(sol= 'ikSCsolver')

	pm.ikHandle(sol= 'ikRPsolver')

	# ------Flags------

	# startjoint(sj)- where the ik will start from
	# endEffector(ee)- you got it it's where the endeffector will go.
	# solver(sol)- indicates the the solver "ie" ikRPsolerver, ikSCsolver, ikSplineSolver


# Cluster

	# cluster

	#pm.cluster()

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	#pm.select(first_selected.cv[:], r=True)

	for current_cv in first_selected.cv:
		pm.custer(current_cv)

	# ------Flags------

	# weightedNode(wn)- Transform node in the DAG above the cluster to which all percents are applied. The second DAGobject specifies the descendent of the first DAGobject from where the transformation matrix is evaluated. Default is the cluster handle.
	# bindState(bs)- When turned on, this flag adds in a compensation to ensure the clustered objects preserve their spatial position when clustered. This is required to prevent the geometry from jumping at the time the cluster is created in situations when the cluster transforms at cluster time are not identity.

# Grouping (Does not need to be included on Shelf!)
	
	pm.group()
	
	# ------Flags------
	name(n) - names the group
	empty() - creates a empty group

	# grouping by default parents 

		# in this example the groups form inside the previous group

		pm.group(name='grandfather')
		pm.group(name='father')
		pm.group(name='son')

		# empty groups can be created too
		
		pm.group(name='grandfather', empty=True)
		pm.group(name='father', empty=True)
		pm.group(name='son', empty=True)
		
# Parenting (Does not need to be included on Shelf!)

	# parentConstraint -mo -weight 1;

	pm.parent()

# Duplicating (Does not need to be included on Shelf!)

	# duplicate

	pm.duplicate()

	# ------Flags------
	#returnRootsOnly(rr)- returns the root nodes of the created hierarchy, controls only what is in the output string[]. 

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	# nurbs circle 
	# circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;

	pm.circle(c=[0,0,0], nr=[0,1,0], sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1)
	pm.circle(normal=[0,1,0])
		# control is facing in the y-axis good for back controls

	pm.circle(normal=[1,0,0])
		# control is facing in the x-axis good for local oriented controls
			# -----Flags-----
			noraml - direction of the control
			radius - size of the control
			sections - number of section of control


# Square

	#pm.nurbsSquare(c=[0,0,0], nr=[0,1,0], sl1=1, sl2=1, sps=1, d=3, ch=1)
	# this creates a nurbs square that is composed of four seperate sides

	# curve -d 1 -p 0 0 0 -p 0 0 5 -p 5 0 5 -p 5 0 0 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;

	pm.curve(d=1,p=[[0,0,0],[0,0,5],[5,0,5],[5,0,0],[0,0,0]], k=[0,1,2,3,4])

# Cube

	# Nurbs cube
	# curve -d 1 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;

	pm.curve(d=1, p=[[0.5,0.5,0.5],[0.5,-0.5,0.5],[0.5,-0.5,-0.5],[0.5,0.5,-0.5],[0.5,0.5,0.5],[-0.5,0.5,0.5],[-0.5,-0.5,0.5],[0.5,-0.5,0.5],[0.5,-0.5,-0.5],[-0.5,-0.5,-0.5],[-0.5,-0.5,0.5],[-0.5,0.5,0.5],[-0.5,0.5,-0.5],[-0.5,-0.5,-0.5],[0.5,-0.5,-0.5],[0.5,0.5,-0.5],[-0.5,0.5,-0.5]], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

# Arrow
	# Nurbs arrow
	# curve -d 1 -p 2 0 1 -p 2 0 -1 -p 0 0 -1 -p 0 0 -2 -p -2 0 0 -p 0 0 2 -p 0 0 1 -p 2 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

	pm.curve(d=1, p=[[2,0,1],[2,0,-1],[0,0,-1],[0,0,-2],[-2,0,0],[0,0,2],[0,0,1],[2,0,1]], k=[0,1,2,3,4,5,6,7])

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint

	# parentConstraint -mo -weight 1;

	pm.parentConstraint('Driver','Driven')

	# -----Flags-----
	# maintainOffset(mo)= (boolean) If used the postion and rotation of the constained object will be kept.

# Orient Constraint

	# orientConstraint

	pm.orientConstraint(control_icon_1,root_joint, mo=True)

	# Driver is the contro icon 
	# Driven is the taget joint 
	# mo = maintain offset

# Point Constraint

	# pointConstraint

	pm.pointConstraint()

	# mo = maintain offset

# Pole Vector Constraint
	# How does this constraint differ from the previous three.

	# poleVectorConstraint

	pm.poleVectorConstraint()
	# it doesn't have a maintain offset.
	# This constraint differs becuase it only constrains the poleVector of an ikRPsolve handle to point at a target object or at the average position of a number of targets
'''
Attributes (Convered in Podcast)
'''
# Create float attribute

	import pymel.core as pm

	#getting the selected object
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	first_selected.addAttr(raw_input(), keyable=True)

		# you can use t to afect the translation attribute r for rotation s for scale
		# and v for visiblity 
		# to lock and hide attribute(s) you would use lock=True"or"False and keyable=True"or"False


# Create Separator Attribute

	import pymel.core as pm

	#getting the selected object
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	name = raw_input()

	first_selected.addAttr(name, keyable=True, at='enum', en="-----------:")
	first_selected.setAttr(name, lock=True)

		# the second part of the above code will lock the attribute from manipulation.
		# if you don't add the "keyable=True" the attribute that you make will not appear in the attribute list like the others
		# at = what type of attribut that you are makeing 


# Template Attributes 
# Create a group of attributes at one time.

	import pymel.core as pm

	#getting the selected object
	selected = pm.ls(selection=True)
	first_selected = selected[0]

	first_selected.addAttr('FINGERS', keyable=True, at= 'enum', en='----------:')
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('CURL', keyable=True, at= 'enum', en='----------:')
	first_selected.CURL.set(lock=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)
	first_selected.addAttr('SPREAD', keyable=True, at= 'enum', en='----------:')
	first_selected.SPREAD.set(lock=True)
	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)
	first_selected.addAttr('THUMB', keyable=True, at= 'enum', en='----------:')
	first_selected.THUMB.set(lock=True)
	first_selected.addAttr('thumb_curl', keyable=True)
	first_selected.addAttr('thumb_drop', keyable=True)
	
	# if you don't add the "keyable=True" the attribute that you make will not appear in the attribute list like the others
	# at = what type of attribut that you are makeing 
		# default is a float attribute 


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


