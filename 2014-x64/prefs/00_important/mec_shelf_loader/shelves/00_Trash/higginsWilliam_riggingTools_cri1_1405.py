'''
Higgins Project 4 Hierarchy

Description: Script for Project 4 of CRI1

'''


print "Rigging Tools Active"

import pymel.core as pm 

def hierarchy():
	'''
Run:

	Create a hierarchy based upon a given system
	
	Select root joint chain and execute function

	import higginsWilliam_riggingTools_cri1_1405
	reload(higginsWilliam_riggingTools_cri1_1405)
	higginsWilliam_riggingTools_cri1_1405.hierarchy()

	'''

	jointSystem = pm.ls(selection=True, dag=True)

	#print "Joint System:", jointSystem

	rootJoint = jointSystem[0]
	joint2 = jointSystem[1]
	joint3 = jointSystem[2]

	'''

	Padding Root Joint

	'''

	#Create an empty group 
	rootPadName = rootJoint.replace("_bind", "_pad")
	rootPad = pm.group(empty=True, name=rootPadName)
	#Move group over to the target joint
	tempConstraint = pm.pointConstraint(rootJoint, rootPad)
	pm.delete(tempConstraint)
	#Freeze Transforms
	pm.makeIdentity(rootPad, apply=True, t=1, r=1, s=1, n=0)
	#Parent Joint back to the group
	pm.parent(rootJoint, rootPad)

	'''
	Local Controls:

	Control 1 - root Joint
	'''
	#Create a control.
	#normal = [1, 0, 0], radius = 2
	icon1Name = rootJoint.replace("_bind", "_icon")
	controlIcon1 = pm.circle(normal=[1, 0, 0], radius=2, name=icon1Name)

	#Create a group. 
	#Grouping control during the process.
	pad1Name = rootJoint.replace("_bind", "_local") 
	localPad1 = pm.group(name=pad1Name)

	#Output control and pad.
	print "Control 1 Created:", controlIcon1
	print " Local Pad 1 Created:", localPad1

	#Move group over to the target joint. 
	#Delete constraint after snapping.
	#Driver: joint
	#Driven: group
	tempConstraint = pm.parentConstraint(rootJoint, localPad1)
	pm.delete(tempConstraint)

	#Orient Constrain the joint to the control. 
	#Driver then Driven
	#Control then Joint
	pm.orientConstraint(controlIcon1, rootJoint)


	'''

	Control 2
	'''
	#Create a control.
	#normal = [1, 0, 0], radius = 2
	icon2Name = joint2.replace("_bind", "_icon")
	controlIcon2 = pm.circle(normal=[1, 0, 0], radius=2, name=icon2Name)

	#Create a group. 
	#Grouping control during the process. 
	pad2Name = joint2.replace("_bind", "_local")
	localPad2 = pm.group(name=pad2Name)

	#Output control and pad.
	print "Control 2 Created:", controlIcon2
	print " Local Pad 2 Created:", localPad2

	#Move group over to the target joint. 
	#Delete constraint after snapping.
	#Driver: joint
	#Driven: group
	tempConstraint = pm.parentConstraint(joint2, localPad2)
	pm.delete(tempConstraint)

	#Orient Constrain the joint to the control. 
	#Driver then Driven
	#Control then Joint
	pm.orientConstraint(controlIcon2, joint2)

	

	'''
	Control 3

	'''
	#Create a control.
	#normal = [1, 0, 0], radius = 2

	icon3Name = joint3.replace("_bind", "_icon")
	controlIcon3 = pm.circle(normal=[1, 0, 0], radius=2, name=icon3Name)

	#Create a group. 
	#Grouping control during the process. 
	pad3Name = joint3.replace("_bind", "_local")
	localPad3 = pm.group(name=pad3Name)

	#Output control and pad.
	print "Control 3 Created:", controlIcon3
	print " Local Pad 3 Created:", localPad3

	#Move group over to the target joint. 
	#Delete constraint after snapping.
	#Driver: joint
	#Driven: group
	tempConstraint = pm.parentConstraint(joint3, localPad3)
	pm.delete(tempConstraint)

	#Orient Constrain the joint to the control. 
	#Driver then Driven
	#Control then Joint
	pm.orientConstraint(controlIcon3, joint3)

	'''
	Parent Control together.

	'''

	pm.parent(localPad3, controlIcon2)
	pm.parent(localPad2, controlIcon1)


	print "Hierarchy created."


