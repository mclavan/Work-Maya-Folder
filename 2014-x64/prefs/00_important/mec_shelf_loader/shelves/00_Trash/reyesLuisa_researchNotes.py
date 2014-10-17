'''
Research Notes

Name: Reyes Luisa 

Current Shelf Tools: 
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 

Drop Down Menus: 

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
Maya Command - makeIdentity
Runtime Command - FreezeTransformations
Flags Used:
	t (translate - boolean)
	r (rotate - boolean)
	s (scale - boolean)
	n (normals - uint)
	pn (preserveNormals - boolean)
Found with echo all active
Navigation:
	Modify > Freeze Transformations
Mel Code:
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
Python Code:
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=1, pn=1)



# Delete History
Maya Command - delete
Runtime Command - DeleteHistory
Flags Used:
	ch (construction history - boolean)
Found with echo all active
Navigation:
	Edit > Delete by Type > History
Mel Code:
	delete -ch
Python Code:
	pm.delete(ch=True)



# Center Pivot
Maya Command - xform
Runtime Command - CenterPivot
Flags Used:
	cp (centerPivots - boolean)
Found with each all active
Mavigation:
	Modify > Center Pivot
Mel Code:
	xform -cp
Python Code:
	pm.xform(cp=True)



# Single Chain and Rotate Plan IKs
Maya Command - ikHandle
Runtime Command - NA
Flags Used:
	s (sticky - string)
	sol (solver -string)
Found with echo all active
Navigation:
	Skeleton > IK Handle Tool (Advance Settings - (SC/RP))
Mel Code RP:
	ikHandle -sol ikRPsolver -s 0;
Python Code RP:
	pm.ikHandle(sol='ikRPsolver', s=0)
Mel Code SP:
	ikHandle -sol ikSCsolver -s 0;
Python Code SP:
	pm.ikHandle(sol='ikSCsolver', s=0)



# Cluster
Maya Command - cluster
Runtime Command - NA
Flags Used: NA
Found by entering 'cluster' into script editor
Navigation:
	Create Deformers > Cluster
Mel Code:
	cluster
Python Code:
	pm.cluster()



# Grouping (Does not need to be included on Shelf!)
Maya Command - group
Runtime Command - NA
Flags Used: NA
Found by entering 'group' into script editor
Navigation: 
	'Command G'
Mel Code:
	group
Python Code:
	pm.group()



# Parenting (Does not need to be included on Shelf!)
Maya Command - Parent
Runtime Command - Parent
Flags Used: NA
Navigation:
	Hotkey Parent
Mel Code:
	parent
Python Code:
	pm.parent()



# Duplicating (Does not need to be included on Shelf!)
Maya Command - duplicate
Runtime Command - duplicate
Flags Used:
	rr (returnRootsOnly - boolean)
Navigation:
	'Command D'
Mel Code:
	duplicate
Python Code:
	pm.duplicate()






'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''




# Circle
Maya Command - circle
Runtime Command - CreateNURBSCircle
Flags Used:
	c (center - linear)
	nr (normal - linear)
	sw (sweep - angle)
	r (radius - linear)
	d (degree - int)
	ut (useTolerance - boolean)
	tol (tolerance - linear)
	s (sections - int)
	ch (constructionHistory - boolean)
Found with echo all on
Navigation:
	Create > Nurbs Primitives > Circle
Mel Code:
	circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
Python Code:
	pm.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1)



# Square
Maya Command - curve
Runtime Command - NA
Flags Used:
	d (degree - float)
	p (point - linear)
	k (knot - float)
Navigation:
	Create > CV Curve Tool
Mel Code:
	curve -d 1 -p 0 0 0 -p 1 0 0 -p 1 0 -1 -p 0 0 -1 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4
Python Code:
	mel_code = "curve -d 1 -p 0 0 0 -p 1 0 0 -p 1 0 -1 -p 0 0 -1 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4;"
	pm.mel.eval(mel_code)



# Cube
Maya Command
Runtime Command - NA
Flags Used:
	d (degree - float)
	p (point - linear)
	k (knot - float)
Navigation:
	Create > Curve Tool
Mel Code:
	curve -d 1 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 ;
Python Code:
	mel_code = "curve -d 1 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 ;"
	pm.mel.eval(mel_code)



# Arrow
Maya Command
Runtime Command - NA
Flags Used:
	d (degree - float)
	p (point - linear)
	k (knot - float)
Navigation:
	Create > Curve Tool
Mel Code:
	curve -d 1 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -2.959446 0 1.014276 -p -5.991247 0 0.995351 -p -5.975306 0 -1.063182 -p -2.961588 0 -1.023403 -p -2.945615 0 -3.00273 -p 0.0240137 0 -0.033468 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;
Python Code:
	mel_code = "curve -d 1 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -2.959446 0 1.014276 -p -5.991247 0 0.995351 -p -5.975306 0 -1.063182 -p -2.961588 0 -1.023403 -p -2.945615 0 -3.00273 -p 0.0240137 0 -0.033468 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;"
	pm.mel.eval(mel_code)




'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
Maya Command - parentConstraint
Runtime Command - ParentConstraint
Flags Used: NA
Navigation:
	Constraint > Parent Constrait (maintain offset - on/off)
Mel Code:
	parentConstraint
Python Code:
	selected = pm.ls(selection=True)
	print 'current selected', selected
	pm.parentConstraint(selected, maintainOffset=True)
Python Code:
	selected = pm.ls(selection=True)
	print 'current selected', selected
	pm.parentConstraint(selected, maintainOffset=False)



# Orient Constraint
Maya Command - orientConstraint
Runtime Command - OrientConstraint
Flags Used: NA
Navigation:
	Constraint > Orient Constraint (maintain offset on/off)
Mel Code:
	orientConstraint
Python Code:
	selected = pm.ls(selection=True)
	print 'current selected', selected
	pm.orientConstraint(selected, maintainOffset=True)
Python Code:
	selected = pm.ls(selection=True)
	print 'current selected', selected
	pm.orientConstraint(selected, maintainOffset=False)


# Point Constraint
Maya Command - pointConstraint
Runtime Command - PointConstraint
Flags Used: NA
Navigation:
	Constraint > Point Constraint (maintain offset - on/off)
Mel Code:
	pointConstraint
Python Code:
	selected = pm.ls(selection=True)
	print 'current selected', selected
	pm.pointConstraint(selected, maintainOffset=True)
Python Code:
	selected = pm.ls(selection=True)
	print 'current selected', selected
	pm.pointConstraint(selected, maintainOffset=False)



# Pole Vector Constraint
Maya Command - poleVectorConstraint
Runtime Command - PoleVectorConstraint
Flags Used: NA
Navigation:
	Constraint > Pole Vector
Mel Code:
	poleVectorConstraint
Python:
	selected = pm.ls(selection=True)
	print 'current selected', selected
	pm.poleVectorConstraint(selected)



# How does this constraint differ from the previous three.



'''
Attributes (Convered in Podcast)
'''
# Create float attribute
Maya Command - addAttr
Runtime Command - NA
Flags Used:
	k - (keyable - boolean)
	ln - (longname - string)
	at - (attributeType - string)
	h (hidden - boolean)
Mel Code: addAttr
Python Code:
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)




# Create Separator Attribute
Maya Command - addAttr
Runtime Command - NA
Flags Used:
	ln (longname - string)
	at (attributeType - string)
	en (enumName - string)
Mel Code:
	addAttr -ln "FINGERS" -at "enum" -en "Green:Blue:" |group1;
	setAttr -e-keyable true |group1.FINGERS;

	addAttr -ln "CURL" -at "enum" -en "----------------------:" |group1;
	setAttr -e-keyable true |group1.CURL;
Python Code:
	first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------------------:")
	first_selected.FINGERS.set(lock=True)





# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
Maya Command - addAttr
Runtime Command - NA
Flags Used:
	ln (longname - string)
	at (attributeType - string)
	en (enumname - string)
Mel Code: addAttr
Python Code:
	first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------------------:")
	first_selected.FINGERS.set(lock=True)
	first_selected.addAttr('CURL', keyable=True, at='enum', en="----------------------:")
	first_selected.CURL.set(lock=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', keyable=True, at='enum', en="----------------------:")
	first_selected.SPREAD.set(lock=True)
	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	first_selected.addAttr('THUMB', keyable=True, at='enum', en="----------------------:")
	first_selected.THUMB.set(lock=True)
	first_selected.addAttr('thumb_spread', keyable=True)
	first_selected.addAttr('thumb_curl', keyable=True)










'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.

Research:
Detach Component
-DetachComponent
Separate
-SeperatePolygon
Extract
-ExtractFace
Combine
-CombinePolygons
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
-FreezeTransformations
-DeleteHistory
-CenterPivot
'''



