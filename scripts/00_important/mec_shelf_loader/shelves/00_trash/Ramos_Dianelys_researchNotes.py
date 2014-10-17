'''
Research Notes

Name Ramos Dianelys

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
	2) Convert MEL to Python.
	3) Important Flags
		-Explain each Flag
		-Convert short to long
	4) What type of command is it and how did you find it?

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

# Center pivot
	import pymel.core as pm

	pm.xform(cp=True)

# Single Chain and Rotate Plane IKs
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

# Parenting (Grouping (Does not need to be included on Shelf!)
	import pymel.core as pm
	pm.parent()

# Duplicating (Grouping (Does not need to be included on Shelf!)
	import pymel.core as pm
	pm.duplicate()

	'''
Control Icons
- Circle, Square, Cube and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle 
	import pymel.core as pm

	# circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
	pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1)

# Square
	import pymel.core as pm

	# nurbsSquare -ch on -o on -nr 0 1 0 ;
	pm.nurbsSquare(ch=True, o=True, nr=[0, 1, 0])

# Cube
	import pymel.core as pm

	# nurbsCube -ch on -o on -po 0 -ax 0 1 0 ;
	pm.nurbsCube(ch=True, o=True, po=0, ax=[0, 1, 0]) 

# Arrow
	import pymel.core as pm

	# curve -d 1 -p -3.458785 0 -2.627 -p -3.45783 0 -2.612856 -p -4.984351 0 -0.978838 -p -3.988796 0 -0.992793 -p -3.99185 0 1.010187 -p -2.998996 0 1.015123 -p -2.990695 0 -0.992022 -p -2.004331 0 -0.975393 -p -3.443307 0 -2.613922 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 ;
	pm.curve(d=(1), p=[(-3.458785, 0, -2.627), (-3.45783, 0, -2.612856), (-4.984351, 0, -0.978838), (-3.988796, 0, -0.992793), (-3.99185, 0, 1.010187), (-2.998996, 0, 1.015123), (-2.990695, 0, -0.992022), (-2.004331, 0, -0.975393), (-3.443307, 0, -2.613922)], k=([0, 1, 2, 3, 4, 5, 6, 7, 8]))


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

# Point Contrainst
	import pymel.core as pm
	pm.pointConstaint()

# Pole Vector
	import pymel.core as pm
	pm.poleVector()

# How does this constraint differ from the previous three.

'''
Attributes (Covered in Podcast)
'''
# Create float Attributes
	import pymel.core as pm
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

# Create Seperator Attribute
import pymel.core as pm
	first_selected.addAttr('Finger', key=True, at='enum', en="--------------:")
	first_selected.FINGERS.set(lock=True)

#Template Attribute
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
	
#Create a group of attributes at one time.
#The finger attributes are an example.