'''
Research Notes

Jennifer Schultz

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
	# Maya Command - makeIdentity
	# Runtime Command - FreezeTransformations
	# MEL Code
		makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	# Python Code
		pm.makeIdentity(apply=True, t=1, r=1, s=1, n=1, pn=1)
	# Flags
		#t (translate - boolean)
		#r (rotate - boolean)
		#s (scale - boolean)
		#n (normals - uint)
		#pn (preserveNormals - boolean)
	# Found with Echo All Active
	# Navigation: Modify > Freeze Transforms

# Delete History
	# Maya Command - delete
	# Runtime Command - DeleteHistory
	# MEL Code
		delete -ch;
	# Python Code
		pm.delete(ch=True)
	# Flags
		#ch (construction history - boolean)
	# Found with Echo All Active
	# Navigation: Edit > Delete by Type > History		

# Center Pivot
	# Maya Command - xform
	# Runtime Command - CenterPivot
	# MEL Code
		xform -cp;
	# Python Code
		pm.xform(cp=True)
	# Flags
		#cp (centerPivots - boolean)
	# Found with Echo All Active
	# Navigation: Modify > Center Pivot

# Single Chain and Rotate Plane IKs
	# Maya Command - ikHandle
	# Runtime Command - N/A
	# Single Chain IK
		# MEL Code
			ikHandle -sol ikSCsolver -s 0;
		# Python Code
			pm.ikHandle(sol='ikSCsolver', s=0)	
	# Rotate Plane IK - Maya Command
		# MEL Code
			ikHandle -sol ikRPsolver -s 0;
		# Python Code
			pm.ikHandle(sol='ikRPsolver', s=0)
	# Flags
		#s (sticky - string)
		#sol (solver -string)
	# Found with Echo All Active
	# Navigation: Skeleton > IK Handle Tool (Advance Settings - (SC/RP))

# Cluster
	# Maya Command - cluster
	# Runtime Command - N/A
	# MEL Code
		cluster
	# Python Code
		pm.cluster()
	# Flags
		#N/A
	# Found by typing 'cluster' into script editor
	# Navigation: Create Deformers > Cluster

# Grouping (Does not need to be included on Shelf!)
	# Maya Command - group
	# Runtime Command - NA
	# MEL Code
		group
	# Python Code
		pm.group()
	# Flags
		#N/A
	# Found by typing 'group' into script editor
	# Navigation: Type 'Command' + 'G'

# Parenting (Does not need to be included on Shelf!)
	# Maya Command - Parent
	# Runtime Command - Parent
	# MEL Code
		parent
	# Python Code
		pm.parent()
	# Flags
		#N/A
	# Found by typing 'group' into script editor
	# Navigation: Type 'Command' + 'P'

# Duplicating (Does not need to be included on Shelf!)
	# Maya Command - duplicate
	# Runtime Command - duplicate
	# MEL Code
		duplicate
	# Python Code
		pm.duplicate()
	# Flags
		#rr (returnRootsOnly - boolean)
	# Found by typing 'duplicate' into script editor
	# Navigation: Type 'Command' + 'D'

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''

# Circle
	# Maya Command - circle
	# Runtime Command - CreateNURBSCircle
	# MEL Code
		circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
	# Python Code
		pm.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1)
	# Flags
		#c (center - linear)
		#nr (normal - linear)
		#sw (sweep - angle)
		#r (radius - linear)
		#d (degree - int)
		#ut (useTolerance - boolean)
		#tol (tolerance - linear)
		#s (sections - int)
		#ch (constructionHistory - boolean)
	# Found with Echo All Active
	# Navigation: Create > Nurbs Primitives > Circle

# Square
	# Maya Command - curve
	# Runtime Command - N/A
	# MEL Code
		curve -d 1 -p 0 0 0 -p 1 0 0 -p 1 0 -1 -p 0 0 -1 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4
	# Python Code
		mel_code = "curve -d 1 -p 0 0 0 -p 1 0 0 -p 1 0 -1 -p 0 0 -1 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4;"
	# Flags
		#d (degree - float)
		#p (point - linear)
		#k (knot - float)
	# Navigation: Create > CV Curve Tool

# Cube
	# Maya Command - curve
	# Runtime Command - N/A
	# MEL Code
		curve -d 1 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 ;
	# Python Code
		mel_code = "curve -d 1 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 ;"
	# Flags
		#d (degree - float)
		#p (point - linear)
		#k (knot - float)
	# Navigation: Create > CV Curve Tool

# Arrow
	# Maya Command - curve
	# Runtime Command - N/A
	# MEL Code
		curve -d 1 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -2.959446 0 1.014276 -p -5.991247 0 0.995351 -p -5.975306 0 -1.063182 -p -2.961588 0 -1.023403 -p -2.945615 0 -3.00273 -p 0.0240137 0 -0.033468 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;
	# Python Code
		mel_code = "curve -d 1 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -0.0112317 0 0.0154087 -p -2.973494 0 2.959901 -p -2.959446 0 1.014276 -p -5.991247 0 0.995351 -p -5.975306 0 -1.063182 -p -2.961588 0 -1.023403 -p -2.945615 0 -3.00273 -p 0.0240137 0 -0.033468 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;"	
	# Flags
		#d (degree - float)
		#p (point - linear)
		#k (knot - float)
	# Navigation: Create > CV Curve Tool

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	# Maya Command - parentConstraint
	# Runtime Command - ParentConstraint
	# MEL Code
		parentConstraint
	# Python Code
		# Offset Active
			selected = pm.ls(selection=True)
			print 'current selected', selected
			pm.parentConstraint(selected, maintainOffset=True)
		# Offset Inactive
			selected = pm.ls(selection=True)
			print 'current selected', selected
			pm.parentConstraint(selected, maintainOffset=False)
	# Flags
		#N/A
	# Navigation: Constraint > Parent Constraint (maintain offset - on/off)

# Orient Constraint
	# Maya Command - orientConstraint
	# Runtime Command - OrientConstraint
	# MEL Code
		orientConstraint
	# Python Code
		# Offset Active
			selected = pm.ls(selection=True)
			print 'current selected', selected
			pm.orientConstraint(selected, maintainOffset=True)

		# Offset Inactive
			selected = pm.ls(selection=True)
			print 'current selected', selected
			pm.orientConstraint(selected, maintainOffset=False)
	# Flags
		#N/A
	# Navigation: Constraint > Orient Constraint (maintain offset on/off)
		
# Point Constraint
	# Maya Command - pointConstraint
	# Runtime Command - PointConstraint
	# MEL Code
		pointConstraint
	# Python Code
		# Offset Active
			selected = pm.ls(selection=True)
			print 'current selected', selected
			pm.pointConstraint(selected, maintainOffset=True)

		# Offset Inactive
			selected = pm.ls(selection=True)
			print 'current selected', selected
			pm.pointConstraint(selected, maintainOffset=False)
	# Flags
		#N/A
	# Navigation: Constraint > Point Constraint (maintain offset - on/off)
		
# Pole Vector Constraint
	# How does this constraint differ from the previous three?
		# There is no offset.
	# Maya Command - poleVectorConstraint
	# Runtime Command - PoleVectorConstraint
	# MEL Code
		poleVectorConstraint
	# Python Code
		selected = pm.ls(selection=True)
		print 'current selected', selected
		pm.poleVectorConstraint(selected)
	# Flags
		#N/A
	# Navigation: Constraint > Pole Vector

'''
Attributes (Covered in Podcast)
'''
# Create float attribute
	# Maya Command - addAttr
	# Runtime Command - N/A
	# MEL Code
		addAttr
	# Python Code
		first_selected.addAttr('index_curl', keyable=True)
		first_selected.addAttr('middle_curl', keyable=True)
		first_selected.addAttr('pinky_curl', keyable=True)
	# Flags
		#k (keyable - boolean)
		#ln (longname - string)
		#at (attributeType - string)
		#h (hidden - boolean)

# Create Separator Attribute
	# Maya Command - addAttr
	# Runtime Command - N/A
	# MEL Code
		addAttr -ln "FINGERS" -at "enum" -en "Green:Blue:" |group1;
		setAttr -e-keyable true |group1.FINGERS;
		addAttr -ln "CURL" -at "enum" -en "----------------------:" |group1;
		setAttr -e-keyable true |group1.CURL;
	# Python Code
		first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------------------:")
		first_selected.FINGERS.set(lock=True)
	# Flags
		#ln (longname - string)
		#at (attributeType - string)
		#en (enumName - string)

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
	# Maya Command - addAttr
	# Runtime Command - N/A
	# MEL Code
		addAttr
	# Python Code
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
	# Flags
		#ln (longname - string)
		#at (attributeType - string)
		#en (enumName - string)

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


