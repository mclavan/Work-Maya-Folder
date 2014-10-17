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
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	#Found this by creating an object in Maya, froze the transforms, and opened the
	#	script editor to see the command.
	#Python: 
		makeIdentity( apply=True, t=1, r=1, s=1, n=1 )
	# Flags: -apply, -t(Translate), -r(rotate), -s(scale), -n(normal)



# Delete History
DeleteHistory;
delete -ch;
	#Turned on Echo Command to have DH show up, then copied
	#Python
		pm.delete(ch=True)
	# Flags: -ch(Construction History)



# Center Pivot
CenterPivot;
xform -cp;
editMenuUpdate MayaWindow|mainEditMenu;
	#Turned on Echo Command to have CP show up, then copied
	#Python:
		pm.xform(cp=True)
	# Flags: -cp(Center Pivots)



# Single Chain and Rotate Plan IKs
#Single Chain:
	ikHandle -s 0;
	#Drew out joints, applied SC IK handle, then copied from script editor
	#Python:
		pm.ikHandle(s=0)
	#Flags: -s(sticky)

#Rotate Plane:
	ikHandle -sol ikRPsolver -s 0;
	#Same thing as the SC, changed settings to RP instead
	#Python:
		pm.ikHandle(sol='ikRPsolver')
	#Flags: -sol(solver), -s(sticky)



# Cluster
CreateCluster;
newCluster " -envelope 1";
	#Clicked on the cluster option in the Animation menus, then copied from 
	#	script editor
	#Python:
		pm.cluster()
	#Flags: -en(envelope)



# Grouping (Does not need to be included on Shelf!)
doGroup 0 1 1;
	#Grouped two objects, copied from script editor
	#Python:
		pm.group()
	#Flags: ?



# Parenting (Does not need to be included on Shelf!)
parent;
	#Parented two joints together, then copied from SE
	#Python:
		pm.parent()
	#Flags: ?



# Duplicating (Does not need to be included on Shelf!)
duplicate -rr;
	#Duplicated a cube, copied from SE
	#Python:
		pm.duplicate(returnRootsOnly=True)
	#Flags: -rr(returnRootsOnly)



'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	#Mel:
	mel = circle -normal 0 1 0
	#Python:
	import pymel.core as pm
	pm.circle(normal=[0, 1, 0])
# Square
	#Mel:
	mel = curve -d 1 -p -0.5 0 0.5 -p -0.5 0 -0.5 -p 0.5 0 -0.5 -p 0.5 0 0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;
	#Python
	import pymel.core as pm
	mel_line = 'curve -d 1 -p -0.5 0 0.5 -p -0.5 0 -0.5 -p 0.5 0 -0.5 -p 0.5 0 0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
	pm.mel.eval(mel_line)
# Cube
	#Mel:
	mel = curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;
	#python
	import pymel.core as pm
	mel_line = 'curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
	pm.mel.eval(mel_line)
# Arrow
	#Mel:
	mel = curve -d 1 -p 2 0 0 -p 1 0 1 -p 0 0 2 -p -1 0 1 -p -2 0 0 -p -1 0 0 -p -1 0 -1 -p -1 0 -2 -p 0 0 -2 -p 1 0 -2 -p 1 0 -1 -p 1 0 0 -p 2 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;
	#Python
	import pymel.core as pm
	mel_line = 'curve -d 1 -p 2 0 0 -p 1 0 1 -p 0 0 2 -p -1 0 1 -p -2 0 0 -p -1 0 0 -p -1 0 -1 -p -1 0 -2 -p 0 0 -2 -p 1 0 -2 -p 1 0 -1 -p 1 0 0 -p 2 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 ;'
	pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	#Maintain Offset on
		#Mel
		parentConstraint -mo -weight 1;
		#Python
		pm.parentConstraint(maintainOffset=True, weight=1)

	#Maintain Offset off
		#Mel
		parentConstraint -weight 1;
		#Python
		pm.parentConstraint(maintainOffset=False, weight=1)


# Orient Constraint
	#Maintain Offset on
		#Mel
		orientConstraint -mo -weight 1;
		#Python
		pm.orientConstraint(maintianOffset=True, weight=1)

	#Maintain Offset off
		#Mel
		orientConstraint -weight 1;
		#Python
		pm.orientConstraint(maintainOffset=False, weight=1)

# Point Constraint
	#Maitain Offset on
		#Mel
		pointConstraint -mo weight 1;
		#Python
		pm.pointConstraint(maintainOffset=True, weight=1)

	#Maintain Offset off
		#Mel
		pointConstraint weight 1;
		#Python 
		pm.pointConstraint(maintainOffset=False, weight=1)

# Pole Vector Constraint
		#Mel
		poleVectorConstraint -weight 1;
		#Pyhon
		pm.poleVectorConstraint(weight=1)

# How does this constraint differ from the previous three.
	#Maintain offset is not need
'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	#Mel 
	addAttr -longName "Name" attributeType double -min 0 -max 10
	#Python
	import pymel.core as pm 
	pm.addAttr(longName='Name', attributeType='double', min=0, max=10, k=True)


# Create Separator Attribute
	#Mel
	addAttr -longName "finger_Spreads" -at "enum" -en "-------------"
	setAttr  -e-channelBox true
	#Python
	pm.addAttr(longName="Finger_Curls", attributeType="enum", enumName="------------")
	pm.setAttr(".Finger_Curls", e=True, channelBox=True)


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


