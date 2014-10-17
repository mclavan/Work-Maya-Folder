'''
Research Notes

Michael Long

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

	FreezeTransformations;

	#sets all attrivbutes to zero without moving object back to origin
	#Found during RBA lecture

	pm.makeIdentity(apply=True)

	#FLAGS
	'''
	Command has translate, rotate scale and joint orient flags for induvidual control of Each
	'''
# Delete History
	DeleteHistory

	# Removes conscuction history from object giving the objects less attributs for maya to mess with
	# Found during RBA lecture

	pm.delete(constructionHistory=True)

	#FLAGS
	'''
	delete() has many flags to control most aspects of an object 
	A usefull one is hierarchy
		deletes hierarchy above or below selected object
	and timeAnimationCurves
		deletes all animation 
	'''

# Center Pivot
	CenterPivot

	# moves objects pivot point to the center of the object
	# Found during 3DF lecture

	pm.xform(centerPivots=True)

	#FLAGS
	'''
	reflection
		xfrom is what is used to cntrol reflections
	'''

# Single Chain and Rotate Plan IKs
	ikHandle
	ikHandle -sol ikRPsolver

	#Creates ik solver
	#Found during 3DF
	
	#single
	pm.ikHandle( )
	#rotate
	pm.ikHandle(srp = True,)

# Make RED
	string $sel[] = `ls -sl`;\nstring $obj;\nfor ($obj in $sel)\n{\n\tsetAttr ($obj + \".overrideEnabled\",1);\n    setAttr ($obj + \".overrideColor\",13)

	# makes control red
	# Found During Lecture

	selected=pm.ls(sl=True)
	for sel in selected:
	    pm.setAttr(sel+".overrideEnabled",1)
	    pm.setAttr(sel+".overrideColor",13)

	#FLAGS
	'''
	setAttr has many flags for changing roate, translate, and scale, is also used to add custom attributs to objects
	'''

# Make Blue
	string $sel[] = `ls -sl`;\nstring $obj;\nfor ($obj in $sel)\n{\n\tsetAttr ($obj + \".overrideEnabled\",1);\n    setAttr ($obj + \".overrideColor\",6)

	# makes control blue
	# Found During Lecture

	selected=pm.ls(sl=True)
	for sel in selected:
	    pm.setAttr(sel+".overrideEnabled",1)
	    pm.setAttr(sel+".overrideColor",6)


# Make Yellow
	string $sel[] = `ls -sl`;\nstring $obj;\nfor ($obj in $sel)\n{\n\tsetAttr ($obj + \".overrideEnabled\",1);\n    setAttr ($obj + \".overrideColor\",17)

	# makes control Yellow
	# Found During Lecture

	selected=pm.ls(sl=True)
	for sel in selected:
	    pm.setAttr(sel+".overrideEnabled",1)
	    pm.setAttr(sel+".overrideColor",)17

# Circle Curve
    mel.eval("circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1")
    
    # Makes Circle Curve
    # Found During Lecture

    pm.circle(name = iconName, r=2, normal=[1,0,0])[0]

    #FLAGS
    '''
    Flags exist such as normal and name for easy control of curve as it is being created
    '''

# Square Curve
    mel.eval("curve -d 1 -p -1 1 0 -p 1 1 0 -p 1 -1 0 -p -1 -1 0 -p -1 1 0 -k 0 -k 1 -k 2 -k 3 -k 4")

    # Makes Square Curve
    # Found During Lecture

    pm.curve(d=1, p=[(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1), (-1,0,-1)])

    #FLAGS

# parent constraint
	parentConstraint -weight 1;

	# put parent constrain on an object
	# found during 3DF lecture

	pm.parentConstraint()

	#orient constraint
	pm.orientConstraint(parent, child)

	#FLAGS
	'''
	remove 
		removes listed objects from constraint
	skipTranslate
	skipRotate
	skipScale
		skips those attributs
	maintainOffset (true/false)
	'''

# group
	nt.ParentConstraint(u'child')

	# Uses a parent constrait to group object
	# Found during MCR lecture

	pm.group(name = 'newName', em=True)

	#FLAGS
	#world/parent flags can be used to control the position of the group


#parent
	parent;

	# parents children to parent
	# Found during MCR Lecture

	pm.parent(child, parent)

	#flags
	#addObject/remove objects can be used to control/clean the hierarchy


#duplicate
	duplicate -rr;

	#duplicates object selected
	# found creating ik/fk switch

	pm.duplicate(objectName, n = 'newName')

	#flags 
	'''
	renameChildren	
		usefull for keeping hierarchy clean
	'''

#select
	select -r objectName;

	#grabs object named
	# found creating hierarchy tool

	pm.select( 'objectName')

	#Flags
	#add: adds objects to selection


# add attr
	addAttr;

	# adds attribute to an object
	# Found creating ik/fk switch

	new_controlIcon.addAttr('name', at = 'type', max = int, min = int, keyable = bool)

	#fLAGS
	'''
	hiddin(bool): Will this attribute be hidden from the UI?
	readable(bool): Can code read this attr 
'''






'''
failed Mirror Tools


Control Mirror

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

import math

#neg transX
#neg rotateY

newPrime_name = ""
newicon_name = ""


selected = pm.ls(selection = True, dag = True)
primeGroup = selected[0]

newPrime = pm.duplicate(selected, n = 'duplicated_prime')

duplicated_prime = newPrime[0]


#mirrorPrime = duplicated_prime

translate = pm.getAttr(primeGroup.translateX, lock=True)

traslateMirror_value = translate*4

pm.setAttr('duplicated_prime.translateX', traslateMirror_value)

translateValue = str(traslateMirror_value) 
print translateValue
'''

