'''
Research Notes

Juan Forero

Current Shelf Tools: 12

- Delete History 
- Freeze Transforms
- Center Pivot
- Parent Constraint
- Joint Tool 
- NUKE (Delete History, Freeze Transforms, Center Pivot)
- Circle 
- Square 
- Cube 
- Arrow 
- Curve Tool 
- ikHandle 

* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 1

ikHandle sigle Chain 1 click
ikHandle rotate Plane 2 click 

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
	# 1 MEL Command
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

	# 2 General Command 

	# 3 MEL to Python
	import pymel.core as pm 
	pm.makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)

	# 4 Important Flags
		# apply (a)
		# translate (t)
		# rotate (r)
		# scale (s)
		# normal (n)
		# preserve normals (pn)


# Delete History
	# 1 MEL Command
	delete -ch; 

	# 2 General Command 

	# 3 MEL to Python
	import pymel.core as pm 
	pm.delete(ch=1)

	# 4 Important Flags

		# constructionHistory (-ch)


# Center Pivot
	# 1 MEL Command
	xform -cp; 

	# 2 General Command 

	# 3 MEL to Python
	import pymel.core as pm 
	pm.xform(cp=1)

	# 4 Important Flags

		# center pivot (cp)

# Single Chain and Rotate Plan IKs
	# 1 MEL Command
	ikHandle; 

	# 2 Animation Command 

	# 3 MEL to Python
	pm.ikHandle()
	ikHandle (sol=ikRPsolver)

	# 4 Important Flags

		# start joint (sj)
		# end efector (ee)
		# solver (sol)
		

# Cluster

	# 1 MEL Command
	cluster;

	# 2 Animation Command 

	# 3 MEL to Python
	pm.cluster()
	(animationm deformation command)

	# 4 Important Flags

		# envelope(-en)

# Grouping (Does not need to be included on Shelf!)
	# 1 MEL Command
	group;

	# 2 General Command 

	# 3 MEL to Python
	import pymel.core as pm 
	group()

	# 4 Important Flags

		There are no flags 

# Parenting (Does not need to be included on Shelf!)
	# 1 MEL Command
	parent;

	# 2 General Command 

	# 3 MEL to Python
	import pymel.core as pm 
	pm.parent()

	# 4 Important Flags



'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''


# Circle
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1;

	# center (c)
	# normal  (nr)
	# sweep (sw)
	# radius (r)
	# degree (d)
	# useTolerance (ut)
	# tolerance (tol)
	# sections (s)
	# constructionHistory (ch)

import pymel.core as pm
pm.circle(center=[0,0,0], normal=[0,1,0], sweep=360, radius=1, degree=3, useTolerance=0, tolerance=0.01, sections=8, constructionHistory=1)

# Square
curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;

	# degree (d)
	# point (p)
	# knot (k)

import pymel.core as pm
mel_line= 'curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4' ;
pm.mel.eval(mel_line)

# Cube
curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 ;

	# degree (d)
	# point (p)
	# knot (k)

import pymel.core as pm
mel_line= 'curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18' ;
pm.mel.eval(mel_line)

# Arrow
curve -d 1 -p 0.234424 0 -1.678227 -p -0.292624 0 -0.930674 -p 0.172426 0 -0.906301 -p 0.22267 0 0.265975 -p 0.646097 0 0.237461 -p 0.610373 0 -0.937608 -p 1.046616 0 -0.932869 -p 0.234424 0 -1.678227 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

	# degree (d)
	# point (p)
	# knot (k)

import pymel.core as pm
mel_line= 'curve -d 1 -p 0.234424 0 -1.678227 -p -0.292624 0 -0.930674 -p 0.172426 0 -0.906301 -p 0.22267 0 0.265975 -p 0.646097 0 0.237461 -p 0.610373 0 -0.937608 -p 1.046616 0 -0.932869 -p 0.234424 0 -1.678227 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7' ;
pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
parentConstraint -mo -weight 1;  # Parent Constraint with offset ON

parentConstraint -weight 1; # Parent Constraint with NO offset
	# mo- mantain offset


	# With offset on
	import pymel.core as pm
	pm.parentConstraint(mo=1, weight=1)  

	# With offset off
	import pymel.core as pm
	pm.parentConstraint(weight=1)  

# Orient Constraint
orientConstraint -mo -weight 1; # Orient Constraint with offset ON

orientConstraint -offset 0 0 0 -weight 1; # Orient Constraint with NO offset

	# With offset on
	import pymel.core as pm
	pm.orientConstraint(mo=1, weight=1) 

	# With offset off
	import pymel.core as pm
	pm.orientConstraint(offset=[0,0,0], weight=1) 

# Point Constraint
pointConstraint -offset 0 0 0 -weight 1; # Point Constraint with offset OFF
pointConstraint -mo -weight 1; # Point Constraint with offset ON
# mo - mantain offset

# With offset ON
import pymel.core as pm
pm.pointConstraint(offset=[0,0,0], weight=1) 


# With offset Off
import pymel.core as pm
pm.pointConstraint(mo=1, weight=1)

# Pole Vector Constraint
poleVectorConstraint -weight 1;


import pymel.core as pm
pm.poleVectorConstraint(weight=1)
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute

import pymel.core as pm

pm.addAttr(longName='index_curl', attributeType='double', keyable=True)
pm.addAttr(longName='middle_curl', attributeType='double', keyable=True)
pm.addAttr(longName='ring_curl', attributeType='double', keyable=True)
pm.addAttr(longName='pinky_curl', attributeType='double', keyable=True)
pm.addAttr(longName='thumb_curl', attributeType='double', keyable=True)


pm.addAttr(longName='index_spread', attributeType='double', keyable=True)
pm.addAttr(longName='middle_spread', attributeType='double', keyable=True)
pm.addAttr(longName='ring_spread', attributeType='double', keyable=True)
pm.addAttr(longName='pinky_spread', attributeType='double', keyable=True)
pm.addAttr(longName='thumb_spread', attributeType='double', keyable=True)

# Create Separator Attribute

import pymel.core as pm
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object:', first_selected

first_selected.addAttr('CURL', keyable=True,at='enum', en="---------------------------;")
first_selected.CURL.set(lock=True)

first_selected.addAttr('SPREAD', keyable=True,at='enum', en="---------------------------;")
first_selected.SPREAD.set(lock=True)

# Template Attributes 
import pymel.core as pm
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object:', first_selected


first_selected.addAttr('CURL', keyable=True,at='enum', en="---------------------------;")
first_selected.CURL.set(lock=True)

pm.addAttr(longName='index_curl', attributeType='double', keyable=True)
pm.addAttr(longName='middle_curl', attributeType='double', keyable=True)
pm.addAttr(longName='ring_curl', attributeType='double', keyable=True)
pm.addAttr(longName='pinky_curl', attributeType='double', keyable=True)
pm.addAttr(longName='thumb_curl', attributeType='double', keyable=True)



first_selected.addAttr('SPREAD', keyable=True,at='enum', en="---------------------------;")
first_selected.SPREAD.set(lock=True)


pm.addAttr(longName='index_spread', attributeType='double', keyable=True)
pm.addAttr(longName='middle_spread', attributeType='double', keyable=True)
pm.addAttr(longName='ring_spread', attributeType='double', keyable=True)
pm.addAttr(longName='pinky_spread', attributeType='double', keyable=True)
pm.addAttr(longName='thumb_spread', attributeType='double', keyable=True)

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


