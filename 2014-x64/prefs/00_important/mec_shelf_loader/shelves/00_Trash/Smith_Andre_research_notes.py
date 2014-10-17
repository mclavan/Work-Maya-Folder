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
# Mel
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
the T flag is for translates
the R flag is for Rotate
the S flag is for Scale
the N flag is for the normals
the PN flag is True for normals on polygonal objects
# Pyton
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

# Delete History
#Mel
delete -ch;
-constructionHistory(-ch)
pm.delete(ch=True)
#Python
the ch flag removes the constructionHistory
the c flag removes the animation
the e flag removes the expressions
the cn flags deletes the Constraints


# Center Pivot
	# Mel
	#xform -cp;
	#sets the pivot to the Center
	#I turned on echo all commands in maya to get info
	#it perfroms transformations
	#it is true when is deletes the constructions
# Python
#centerPivots(cp)
#looked in python command ref
pm.xform(cp = True)



# Single Chain and Rotate Plan IKs
#Mel : ikHandle -sol ikRPsolver;

#Python
pm.ikHandle(sol= "ikRPsolver")
pm.ikHandle(ss = jointfirst, ee = jointlast)



# Cluster
#Mel
newCluster " -envelope 1";
// Result: cluster1 cluster1Handle // 

#Python
pm.Cluster(float=1)

# Grouping (Does not need to be included on Shelf!)
#Mel
it assigns new names to groups
it assigns groups under world
it assigns groups under given Parent
it creates empty groups

#python
pm. em=True, name='null1' )

# Parenting (Does not need to be included on Shelf!)
# Mel
parent;
it can unpaarent given objects
it can add preserve existing local object transformations
#Python
parent( 'circle1', 'group2', add=True )

# Duplicating (Does not need to be included on Shelf!)
#Mel
it gives name to give duplicated objects
#python
move -r -os -wd 0 0 4.258179 ;

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
#Mel
#circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 3.80125e-10 -s 8 -ch 1; objectMoveCommand;

#Python
mel_line = "circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 3.80125e-10 -s 8 -ch 1; objectMoveCommand;"
pm.mel.eval(mel_line)


# Square
#Mel
#curve -d 1 -p -0.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;

#Python
mel_line = "curve -d 1 -p -0.5 0 0.5 -p 0.5 0 0.5 -p 0.5 0 -0.5 -p -0.5 0 -0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;"
pm.mel.eval(mel_line)
# Cube
#Mel
#curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;

#Python
mel_line = "curve -d 1 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;"
pm.mel.eval(mel_line)

# Arrow
#Mel
#curve -d 1 -p -2.020608 0 -1.954654 -p -4.025926 0 -3.978521 -p -2.020608 0 -1.954654 -p -4.022857 0 0.0137884 -p -4.020705 0 -0.979702 -p -6.987076 0 -0.995835 -p -7.021415 0 -2.986562 -p -4.040282 0 -2.980424 -p -4.025926 0 -3.978521 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 ;
#Python
mel_line = "curve -d 1 -p -2.020608 0 -1.954654 -p -4.025926 0 -3.978521 -p -2.020608 0 -1.954654 -p -4.022857 0 0.0137884 -p -4.020705 0 -0.979702 -p -6.987076 0 -0.995835 -p -7.021415 0 -2.986562 -p -4.040282 0 -2.980424 -p -4.025926 0 -3.978521 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 ;"
pm.mel.eval(mel_line)


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
#Mel
parentConstraint -weight 1;
Sets the weight value for the specified targets
#Python
parentConstraint {1, 0, 1, 1};
pm.parentConstraint(weight=1)
# Orient Constraint
#Mel
Sets the weight value for the specified targets
#Python
orientConstraint -offset 0 0 0 -weight 1;
pm.orientConstraint(offset=(0, 0, 0), weight=1 )

# Point Constraint
#Mel
pointConstraint -offset 0 0 0 -weight 1;
Sets or queries the value of the offset
Sets the weight value for the specified targets
#Python
pointConstraint( 'joint1', 'joint2' )
pm.pointConstraint(offset=(0, 0, 0),weight=1)

# Pole Vector Constraint
#Mel
poleVectorConstraint -weight 1;
Sets the weight value for the specified targets
#Python
poleVectorConstraint( 'weight = 1', 'weight = 2' )
pm.poleVectorConstraint(weight=1)
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
#Mel
addAttr -ln "steve"  -at double  |nurbsCircle1;
#Python
addAttr(longName='steve', attributeType='double')

# Create Separator Attribute
#Mel
addAttr -ln "woooooo"  -at "enum" -en "-----------------:"  |nurbsCircle1;
#Python
addAttr(longName='woooooo', attributeType='enum', en= "----------------:")

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


