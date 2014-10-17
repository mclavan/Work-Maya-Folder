'''
Research Notes

Name Rebecca Rivera

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
	import pymel.core as pm

	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	# apply(a) - implements the new values to t, r, s, n

# Delete History
	import pymel.core as pm

	pm.delete(ch=True)

# Center Pivot
	import pymel.core as pm

	pm.xform(cp=True)

# Single Chain and Rotate Plan IKs
import pymel.core as pm

pm.ikHandle()

pm.ikHandle(sol ='ikrpsolver')

	

# Cluster
	import pymel.core as pm

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	# pm.cluster
	# Python List range (slice)
	# pm.select(first_selected.cv[::2], r=True)
	for current_cv in first_selected.cv:
	    # Apply cluster to current cv
	    pm.cluster(current_cv)

# Grouping (Does not need to be included on Shelf!)
	import pymel.core as pm
	pm.group()
# Parenting (Does not need to be included on Shelf!)
	import pymel.core as pm
	pm.parent()
# Duplicating (Does not need to be included on Shelf!)
	import pymel.core as pm
	pm.duplicate()
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	import pymel.core as pm
	# pm.commandName()
	pm.circle()
	# command flags/attributes
	pm.circle(radius=2)
	# using multiple flags
	pm.circle(radius=3,sections=16)

# Square
	import pymel.core as pm
	pm.circle(degree=1, sections=4)
# Cube
  	import pymel.core as pm
# Arrow
	import pymel.core as pm

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
 	import pymel.core as pm
	pm.parentConstraint('driver', 'driven')
	pm.parentConstraint('driver', 'driven', maintainOffset=False)


	parentConstraint -mo -weight 1;
	pm.parentConstraint('driver', 'driven', mo=True)


# Orient Constraint
  	import pymel.core as pm
  	pm.orientContsraint()
# Point Constraint
	import pymel.core as pm
	pm.pointConstaint()

# Pole Vector Constraint
	import pymel.core as pm
	pm.poleVector()
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
	import pymel.core as pm
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

# Create Separator Attribute
	import pymel.core as pm
	first_selected.addAttr('Finger', key=True, at='enum', en="--------------:")
	first_selected.FINGERS.set(lock=True)

# Template Attributes
	'''
	Template Attributes
	FINGERS
	CURL
	index_curl
	middle_curl
	pinky_curl
	'''
	import pymel.core as pm

	first_selected.addAttr('Finger', key=True, at='enum', en="--------------:")
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('CURL', key=True, at='enum', en="--------------:")
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', key=True, at='enum', en="--------------:")
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('index_spraed', keyable=True)
	first_selected.addAttr('middle_spraed', keyable=True)
	first_selected.addAttr('pinky_spraed', keyable=True)

	first_selected.addAttr('THUMB', key=True, at='enum', en="--------------:")
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('thumb_curl', keyable=True)
	first_selected.addAttr('thumb_drop', keyable=True)
	


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



