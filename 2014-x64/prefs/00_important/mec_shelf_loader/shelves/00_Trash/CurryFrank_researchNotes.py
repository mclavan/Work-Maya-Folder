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

'''
Interesting note. Maya 2015 command page is broken,
so I can not look up the mel or python commands that way.

'''
# Freeze Transforms

	# 1. makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	# 2. It is a mel command, I found by doing the command and seeing the 
	# 	mel command in the script editor
	# 3. Mel to python conversion is:

# Delete History

DeleteHistory;

# Center Pivot

CenterPivot;

# Single Chain 

select -r joint4.rotatePivot ;
select -add joint5.rotatePivot ;
ikHandle;

#Rotate Plane IK

select -r joint1.rotatePivot ;
select -add joint3.rotatePivot ;
ikHandle -sol ikRPsolver;

# Cluster

Forgot how to create clusters

# Grouping (Does not need to be included on Shelf!)

doGroup 0 1 1;

# Parenting (Does not need to be included on Shelf!)

parent;

# Duplicating (Does not need to be included on Shelf!)

duplicate -rr;

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle

circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;

# Square

curve -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;

# Cube

curve -d 1 -p -1.041856 1.93409 0.984303 -p 0.958144 1.93409 0.984303 -p 0.958144 -0.0659103 0.984303 -p -1.041856 -0.0659103 0.984303 -p -1.041856 1.93409 0.984303 -p -1.041856 1.93409 -1.015697 -p -1.041856 -0.0659103 -1.015697 -p -1.041856 -0.0659103 0.984303 -p 0.958144 -0.0659103 0.984303 -p 0.958144 -0.0659103 -1.015697 -p -1.041856 -0.0659103 -1.015697 -p -1.041856 1.93409 -1.015697 -p 0.958144 1.93409 -1.015697 -p 0.958144 -0.0659103 -1.015697 -p 0.958144 -0.0659103 0.984303 -p 0.958144 1.93409 0.984303 -p 0.958144 1.93409 -1.015697 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;

# Arrow

curve -d 1 -p -1 0 2 -p -1 0 -2 -p -2 0 -2 -p 0 0 -4 -p 2 0 -2 -p 1 0 -2 -p 1 0 2 -p -1 0 2 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

# My own are next

# 4 way Arrow

curve -d 1 -p -1 0 -1 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 -1 -p 3 0 -1 -p 3 0 -2 -p 5 0 0 -p 3 0 2 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p 2 0 3 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 1 -p -3 0 1 -p -3 0 2 -p -5 0 0 -p -3 0 -2 -p -3 0 -1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;

# Piramid

curve -d 1 -p -0.991506 1.991506 -0.991506 -p 0.00424719 0.995753 1 -p -0.991506 0 -0.991506 -p -0.991506 1.991506 -0.991506 -p 1 1.991506 -0.991506 -p 0.00424719 0.995753 1 -p 1 0 -0.991506 -p -0.991506 0 -0.991506 -p 0.00424719 0.995753 1 -p 1 1.991506 -0.991506 -p 1 0 -0.991506 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 ;

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint

# Orient Constraint

# Point Constraint

# Pole Vector Constraint
# How does this constraint differ from the previous three.

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


