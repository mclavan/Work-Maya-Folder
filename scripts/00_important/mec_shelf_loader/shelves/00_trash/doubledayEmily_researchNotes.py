'''
Research Notes

Emily Doubleday

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

		pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Delete History

		pm.delete(ch=True,)

	# Center Pivot

		pm.xform(cp=True)

	# Single Chain and Rotate Plan IKs

		pm.ikHandle(n='joint1', sj='bind', ee='waste')

		pm.ikSolver( st='ikRPsolver', ep=0.5, n='fooSolver' )

	# Cluster

		pm.cluster( wn=('example1', 'example1') )

	# Grouping (Does not need to be included on Shelf!)

		pm.group(empty=True, name='Doubleday_Emily_exampleGroup')

	# Parenting (Does not need to be included on Shelf!)

		pm.parent('driven', 'driver', r=True) 

	# Duplicating (Does not need to be included on Shelf!)

		pm.duplicate('example1')

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
	# Circle

		pm.circle()


	# Square

		pm.nurbsSquare()
		
	# Cube

		pm.nurbsCube()

	# Arrow


'''
Constraints
- Remember to test offset on and off with these commands.
'''
	# Parent Constraint

		pm.parentConstraint('exampleShape1', 'exampleShape2')

	# Orient Constraint
		
		pm.orientConstraint('exampleShape1', 'exampleShape2')

	# Point Constraint

		pm.pointConstraint('exampleShape1', 'exampleShape2')

	# Pole Vector Constraint
		# How does this constraint differ from the previous three?
			#It doesn't have all of the save flags as the other three.

		pm.poleVector('exampleShape1', 'exampleShape2')

'''
Attributes (Covered in Podcast)
'''
	# Create float attribute

		first_selected.addAttr('example1', keyable=True)

	# Create Separator Attribute

		first_selected.addAttr('EXAMPLE', keyable=True, at='enum' en='-------:')
		first_selected.EXAMPLE.set(lock=True)

	# Template Attributes 
	# Create a group of attributes at one time.  
	# The finger attributes are an example.
		#This where I use fingers

		first_selected.addAttr('FINGERS', keyable=True, at='enum' en='-------:')
		first_selected.FINGERS.set(lock=True)

		first_selected.addAttr('CURLS', keyable=True, at='enum' en='-------:')
		first_selected.FINGERS.set(lock=True)
		first_selected.addAttr('index_curl', keyable=True)
		first_selected.addAttr('middle_curl', keyable=True)
		first_selected.addAttr('pinky_curl', keyable=True)

		first_selected.addAttr('SPREAD', keyable=True, at='enum' en='-------:')
		first_selected.FINGERS.set(lock=True)


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


