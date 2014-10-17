'''
Research Notes

Name
Ambe Elliott 

Current Shelf Tools: 
22 Total
*Double Click command

Nuke
Freeze transformations
Delete History
Center Pivot
IK Handle*
Cluster
Circle
Square
Cube
Arrow
Parent Constraint*
Orient Constraint*
Point Constraint*
Pole Vector Constraint
Float Attribute
Enum Attribute 
Template Attribute
Group Attribute
Finger Attribute
Color Change Blue
Color Change Red
Color Change Yellow
'''

'''
General Tools Research
'''

# Freeze Transforms
	
	#1) MEL Commmand

		makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
		

	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Modify>freeze transformations. 
		Created a polygon shape, moved, then opened script editor to view MEL command.
		'''
	#3) Convert MEL to Python.
		import pymel.core as pm  
		pm.makeIdentity(apply=True, t=1,r=1,s=1,n=0)

	#4) Important Flags
		'''
		t=translate
		r=rotate
		s=scale
		'''

# Delete History
	#1) MEL Commmand
		
		DeleteHistory;
		delete -ch;
		
	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Edit>delete by type> history.
		Created polygon shape, opened script editor, turned on echo all commands,
		viewed, then turned off echo all commands 
		'''
	#3) Convert MEL to Python.
		import pymel.core as pm 
		pm.delete(all=True,ch=True)
	#4) Important Flags
		'''
		ch= construction history
		'''

# Center Pivot
	#1) MEL Commmand
		
		xform -cp;
	
	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Modify>Center Pivot.
		Created polygon shape, displaced pivot, opened script editor, turned on echo all commands,
		viewed, then turned off echo all commands 
		'''
	#3) Convert MEL to Python.

		import pymel.core as pm 
		pm.xform(cp=True)

	#4) Important Flags
		'''
		cp=Center Pivot
		'''

# Single Chain and Rotate Plan IKs
	#1) MEL Commmand
		SC
		ikHandle;

		RP
		ikHandle -sol ikRPsolver;



	#2) What type of command is it and how did you find it?
		'''
		Drop down maya command. First click SC, second click, RP.Created joints. Selected first and last joint, skeleton>ik handle tool.
		Changed between SC and RP and reviewed MEL command in script editor. 
		'''
	#3) Convert MEL to Python.
		SC
		import pymel.core as pm 
		pm.ikHandle(sol='ikSCsolver')

		RP
		import pymel.core as pm 
		pm.ikHandle(sol='ikRPsolver')

	#4) Important Flags
		'''
		sol=solver
		'''


# Cluster
	#1) MEL Commmand

		newCluster " -envelope 1";
		cluster; 
		CreateCluster;

	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Modify>Center Pivot.
		Created curve icon, create deformers>cluster, opened script editor, turned on echo all commands,
		viewed MEL command, then turned off echo all commands
		'''
	#3) Convert MEL to Python.
		
		import pymel.core as pm 
		pm.cluster()

	#4) Important Flags
		'''
		en=envelope
		'''

# Grouping (Does not need to be included on Shelf!)
	#1) MEL Commmand
		Group;
		performGroup false;
		doGroup 0 1 1;
	#2) What type of command is it and how did you find it?
		'''
		No shelf command click. Edit>Group.
		Created curve icon, create deformers>cluster, opened script editor, turned on echo all commands,
		viewed MEL command, then turned off echo all commands
		'''
	#3) Convert MEL to Python.
		import pymel.core as pm 
		pm.group(empty=True)
	#4) Important Flags
		'''
		em=empty
		'''

# Parenting (Does not need to be included on Shelf!)
	#1) MEL Commmand

		parent;

	#2) What type of command is it and how did you find it?
		'''
		No shelf command click. Edit>parent.
		Created two joints, opened script editor and reviewed MEL command.
		'''
	#3) Convert MEL to Python.

		import pymel.core as pm 
		pm.parent()

	#4) Important Flags

# Duplicating (Does not need to be included on Shelf!)
	#1) MEL Commmand

		duplicate -rr;

	#2) What type of command is it and how did you find it?
		'''
		No shelf command click. Edit>Duplicate.
		Created polygon, opened script editor and reviewed MEL command.
		'''

	#3) Convert MEL to Python.

		import pymel.core as pm 
		pm.duplicate()

	#4) Important Flags
		'''
		rr=returnRootsOnly
		'''

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	#1) MEL Commmand

		circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1; objectMoveCommand;


	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Create>cv curve tool.
		Created shape, opened script editor and reviewed MEL command.
		'''
	#3) Convert MEL to Python.

		import pymel.core as pm
		mel_line='circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1;'
		pm.mel.eval(mel_line)

	#4) Important Flags
		'''
		eval=evaluate
		'''

# Square
	#1) MEL Commmand

		curve -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Create>cv curve tool.
		Created shape, opened script editor and reviewed MEL command.
		'''
	#3) Convert MEL to Python.

		import pymel.core as pm
		mel_line='curve -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4;'
		pm.mel.eval(mel_line)

	#4) Important Flags
		'''
		eval=evaluate
		'''

# Cube
	#1) MEL Commmand

		curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;

	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Create>cv curve tool.
		Created shape, opened script editor and reviewed MEL command.
		'''
		
	#3) Convert MEL to Python.

		import pymel.core as pm
		mel_line='curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15'
		pm.mel.eval(mel_line)
		
	#4) Important Flags
		'''
		eval=evaluate
		'''

# Arrow
	#1) MEL Commmand

		curve -d 1 -p -3 0 -11 -p 0 0 -7 -p -2 0 -7 -p -2 0 -4 -p -4 0 -4 -p -4 0 -7 -p -6 0 -7 -p -3 0 -11 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Create>cv curve tool.
		Created shape, opened script editor and reviewed MEL command.
		'''
	#3) Convert MEL to Python.

		import pymel.core as pm
		mel_line='curve -d 1 -p -3 0 -11 -p 0 0 -7 -p -2 0 -7 -p -2 0 -4 -p -4 0 -4 -p -4 0 -7 -p -6 0 -7 -p -3 0 -11 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7;'
		pm.mel.eval(mel_line)

	#4) Important Flags
		'''
		eval=evaluate
		'''


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	#1) MEL Commmand
	
		#Maintain Offset Checked
		doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
		parentConstraint -mo -weight 1;

		#Maintain Offset Unchecked
		doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
		parentConstraint -weight 1;

	#2) What type of command is it and how did you find it?
		'''
		Drop down maya command. First click maintain offset on, second click maintain offset off.
		Constrain>parent. Created two objects, opened script editor and reviewed MEL command.
		Repeat with maintain offset unchecked.
		'''

	#3) Convert MEL to Python.

		#Maintain Offset Checked
		import pymel.core as pm
		selected=pm.ls(selection=True) 
		'object1', selected[0]
		'object2', selected[1]
		pm.parentConstraint(selected [0],selected[1],mo=True)

		#Maintain Offset Unchecked

		import pymel.core as pm
		selected=pm.ls(selection=True) 
		'object1', selected[0]
		'object2', selected[1]
		pm.parentConstraint(selected [0],selected[1],mo=False)

	#4) Important Flags
		'''
		mo=maintain offset
		'''
	
# Orient Constraint
	#1) MEL Commmand
		#Maintain Offset Checked
		doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
		orientConstraint -mo -weight 1;

		#Maintain Offset Unchecked
		doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
		orientConstraint -offset 0 0 0 -weight 1;

	#2) What type of command is it and how did you find it?
		'''
		Drop down maya command. First click maintain offset on, second click maintain offset off.
		Constrain>orient. Created two objects, opened script editor and reviewed MEL command.
		Repeat with maintain offset unchecked.
		'''
	#3) Convert MEL to Python.

		#Maintain Offset Checked
		import pymel.core as pm
		selected=pm.ls(selection=True) 
		'object1', selected[0]
		'object2', selected[1]
		pm.orientConstraint(selected [0],selected[1],mo=True)

		#Maintain Offset Unchecked
		import pymel.core as pm
		selected=pm.ls(selection=True) 
		'object1', selected[0]
		'object2', selected[1]
		pm.orientConstraint(selected [0],selected[1],mo=False)

	#4) Important Flags
		'''
		mo=maintain offset
		'''

# Point Constraint
	#1) MEL Commmand

		#Maintain Offset Checked
		doCreatePointConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
		pointConstraint -mo -weight 1;

		#Maintain Offset Unchecked
		doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
		pointConstraint -offset 0 0 0 -weight 1;

	#2) What type of command is it and how did you find it?
		'''
		Drop down maya command. First click maintain offset on, second click maintain offset off.
		Constrain>point. Created two objects, opened script editor and reviewed MEL command.
		Repeat with maintain offset unchecked.
		'''
	#3) Convert MEL to Python.

		#Maintain Offset Checked
		import pymel.core as pm
		selected=pm.ls(selection=True) 
		'object1', selected[0]
		'object2', selected[1]
		pm.pointConstraint(selected [0],selected[1],mo=True)

		#Maintain Offset Unchecked
		import pymel.core as pm
		selected=pm.ls(selection=True) 
		'object1', selected[0]
		'object2', selected[1]
		pm.pointConstraint(selected [0],selected[1],mo=False)

	#4) Important Flags
		'''
		mo=maintain offset
		'''

# Pole Vector Constraint
	#1) MEL Commmand

		poleVectorConstraint -weight 1;

	#2) What type of command is it and how did you find it?
		'''
		Single click maya command. Constrain>pole vector.
		Created joints with ikRPsolver, created control icon, opened script editor and reviewed MEL command.
		'''
	#3) Convert MEL to Python.

		import pymel.core as pm
		selected=pm.ls(selection=True) 
		pm.poleVectorConstraint(selected [0],selected[1])

		OR

		import pymel.core as pm
		pm.poleVectorConstraint()
	#4) Important Flags
		'''
		none
		'''

	# How does this constraint differ from the previous three.
	'''
	The pole vector constraint does not have an offset option and has to be specifically
	made with a ikRPsolver and control icon. The others can be used with polygons, control icon etc.
	'''

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	#Python Command

		import pymel.core as pm
		selected=pm.ls(selection=True)
		first_selected=selected[0]
		print 'First Selected Object:', first_selected

		first_selected.addAttr('FLOAT', keyable=True)

# Create Separator Attribute
	#Python Command

		import pymel.core as pm
		selected=pm.ls(selection=True)
		first_selected=selected[0]
		print 'First Selected Object:', first_selected

		attribute_name=raw_input()
		first_selected.addAttr(attribute_name, keyable=True, at='enum', en="-------:")

# Template Attributes 
	#Python Command

	import pymel.core as pm
	selected=pm.ls(selection=True)
	first_selected=selected[0]
	print 'First Selected Object:', first_selected

	first_selected.addAttr('FLOAT', keyable=True, at='enum', en="-------:")
	first_selected.FLOAT.set(lock=True)


	attribute_name=raw_input()
	first_selected.addAttr(attribute_name, keyable=True)


# Create a group of attributes at one time.
	#Python Command

	import pymel.core as pm
	selected=pm.ls(selection=True)
	first_selected=selected[0]
	print 'First Selected Object:', first_selected

	attribute_name=raw_input()
	first_selected.addAttr(attribute_name, keyable=True)
	attribute_name=raw_input()
	first_selected.addAttr(attribute_name, keyable=True)
	attribute_name=raw_input()
	first_selected.addAttr(attribute_name, keyable=True)
	attribute_name=raw_input()
	first_selected.addAttr(attribute_name, keyable=True)
	attribute_name=raw_input()
	first_selected.addAttr(attribute_name, keyable=True)


# The finger attributes are an example.
	#Python Command 

import pymel.core as pm
selected=pm.ls(selection=True)
first_selected=selected[0]

first_selected.addAttr('FINGERS', keyable=True, at='enum', en="-------:")
first_selected.FINGERS.set(lock=True)

first_selected.addAttr('CURL', keyable=True, at='enum', en="-------:")
first_selected.CURL.set(lock=True)

first_selected.addAttr('Index', keyable=True)
first_selected.addAttr('Middle', keyable=True)
first_selected.addAttr('Pinky', keyable=True)

first_selected.addAttr('SPREAD', keyable=True, at='enum', en="-------:")
first_selected.SPREAD.set(lock=True)

first_selected.addAttr('index', keyable=True)
first_selected.addAttr('middle', keyable=True)
first_selected.addAttr('pinky', keyable=True)


first_selected.addAttr('THUMB', keyable=True, at='enum', en="-------:")
first_selected.THUMB.set(lock=True)

first_selected.addAttr('drop', keyable=True)
first_selected.addAttr('curl', keyable=True)


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


