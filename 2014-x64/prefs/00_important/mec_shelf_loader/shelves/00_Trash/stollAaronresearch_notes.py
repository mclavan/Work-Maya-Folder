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
# MEL command:

# 	FreezeTransformations;
# 	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

# Command type:

# 	Maya Commmand
# 	Found using: Modify/FreezeTransformations

# Python Conversion:

# 	pm.makeIdentity( apply=True, t=1, r=1, s=1, n=0 )

# Important Flags: long name(short name)
# 	-apply(-a) when this is true all transfroms (translate, rotate, scale) are frozen
# 	-translate(-t)	freezes translations
# 	-rotate(-r)	freezes rotations
# 	-scale(-s)	freezes scale
# 	-normal(-n)	freezes the direction of the normals 	
# ###############################################################

# Delete History
# MEL command:

# 	delete -ch;
# 	found using: Edit/ Delete by Type/ History

# Command type:

# 	maya command

# Python Conversion:

# 	pm.delete(ch=True)


# Important Flags:

# -constructionHistory(-ch)	deletes all constructions history
# ###############################################################
# Center Pivot

# MEL command:

# 	xform -cp;
# 	found using: Modify/ Center Pivot

# Command type:

# 	maya command

# Python Conversion:

# 	pm.xform(cp=True)

# Important Flags:

# 	-centerPivots(-cp)	sets the pivot to the center of the target object.


###############################################################

# Single Chain and Rotate Plan IKs
'''
has double click command
'''
# MEL command:
# 	single chain - ikHandle -sj  -ee ;
# 	rotate plain - ikHandle -sol ikRPsolver -n  -sj  -ee ;
# 	found using Skeleton/ IK Handle Tool


# Command type:

# 	maya command

# Python Conversion:
# 	pm.ikHandle()
# 	pm.ikHandle(sol='ikRPsolver')



# Important Flags:
# 	-n = name 
# 	-sj = start joint
# 	-ee = end effector
	# -sol = solver, use with ikRPsolver
###########################################################

# Cluster

# MEL command:

# 	newCluster " -envelope 1";


# Command type:
# 	maya command

# Python Conversion:
	
# 	pm.cluster()

# Important Flags:

########################################################

# Grouping (Does not need to be included on Shelf!)

# MEL command:
# 	group ;
# 	found in Edit/ Group

# Command type:
# 	 maya command

# Python Conversion:
# pm.group( '', '', n='' )

# Important Flags:
# 	n = name 

####################################################################


# Parenting (Does not need to be included on Shelf!)

# MEL command:

# 	parent ; 
# 	found in Edit/ Parent

# Command type:
# 	maya command

# Python Conversion:

# 	pm.parent()

# Important Flags:


##############################################################


# Duplicating (Does not need to be included on Shelf!)
# MEL command:
# 	duplicate -rr;
# Command type:
# 	maya command

# Python Conversion:

# 	pm.duplicate('')

# Important Flags:




'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''


# Circle

# mel command
# 	 circle;
# Command type
# 	maya command
# Python Conversion
# 	pm.circle()
###############################################################

# Square

# MEL Command

# 	curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;


# Command Type

# 	maya command

# Python Conversion

# 	mel_line = 'curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4'

# 	pm.mel.eval(mel_line)
	
# Important Flags
# 	p = point 
# 	k = knot

###############################################################


# Cube


# Mel Command
# 	curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;
# Command Type
# 	Maya command
# Python Conversion
# 	mel_line = 'curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15'
# 	pm.mel.eval(mel_line)

###############################################################
# Arrow
# mel command
# 	curve -d 1 -p 0 0 -5 -p -2 0 -3 -p -1 0 -3 -p -1 0 -1 -p 1 0 -1 -p 1 0 -3 -p 2 0 -3 -p 0 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
# command type
# 	 maya
# python Conversion
# 	mel_line = 'curve -d 1 -p 0 0 -5 -p -2 0 -3 -p -1 0 -3 -p -1 0 -1 -p 1 0 -1 -p 1 0 -3 -p 2 0 -3 -p 0 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7'
# 	pm.mel.eval(mel_line)




'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
'''
has double click
'''
# mel command 
	# maintain offset is on - parentConstraint -mo;
	# maintain offset is off -  parentConstraint;
# command type
# 	maya 
# python Conversion
	# maintain offset is on - pm.parentConstraint(mo=True)
	# maintain offset is off - pm.parentConstraint()
# Important Flags
	# maintain offset (-mo)
################################################################
# Orient Constraint
'''
has double click
'''

# mel command 
	# maintain offset is on - orientConstraint -mo;
	# maintain offset is off - orientConstraint;
# command type
	# maya 
# python Conversion
	# maintain offset is on - pm.orientConstraint(mo=True)
	# maintain offset is off - pm.orientConstraint()

# Important Flags


################################################################

# Point Constraint
'''
has double click
'''

# mel command 
	# maintain offset is on - pointConstraint -mo;
	# maintain offset is off - pointConstraint;
# command type
	# maya 
# python Conversion
	# maintain offset is on - pm.pointConstraint(mo=True)
	# maintain offset is off - pm.pointConstraint()

################################################################

# Pole Vector Constraint

# mel command 
	# poleVectorConstraint

# command type
	# maya 

# python Conversion
	# pm.poleVectorConstraint()

# How does this constraint differ from the previous three.

# this contraint does not have a maintain offset function

################################################################

'''
Attributes (Convered in Podcast)
'''
# Create float attribute


# Create Separator Attribute

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


