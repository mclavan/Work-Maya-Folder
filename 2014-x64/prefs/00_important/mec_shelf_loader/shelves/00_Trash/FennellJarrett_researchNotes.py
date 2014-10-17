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
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;


#it is a mel command found in the history

# Delete History

DeleteHistory;
delete -ch;

pm.delete()
#it is a mel command found in the history

# Center Pivot
CenterPivot;
xform -cp;

#it is a mel command found in the history


# Single Chain and Rotate Plan IKs
ikHandle;
pm.ikHandle(sj='starting_joint', ee='end_effector', p='priority', w='weight')

#it is a mel command found in the history


ikHandle -sol ikRPsolver;

#it is a mel command found in the history
pm.ikHandle(sj='starting_joint', ee='end_effector', p='priority', w='weight')


# Cluster
CreateCluster;
#it is a mel command found in the history

# Grouping (Does not need to be included on Shelf!)
doGroup 0 1 1;
#it is a mel command found in the history
pm.group()

#ungroup
ungroup;
#it is a mel command found in the history (not needed for the assignment but can be useful)
pm.ungroup()

# Parenting (Does not need to be included on Shelf!)
parent;
#it is a mel command found in the history

pm.parentConstraint()


# Duplicating (Does not need to be included on Shelf!)
duplicate -rr;
#it is a mel command found in the history
pm.duplicate('asset' rr=True)  (rr=return_roots)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;

# Square
curve -d 1 -p -2 0 -2 -p 2 0 -2 -p 2 0 2 -p -2 0 2 -p -2 0 -2 -k 0 -k 1 -k 2 -k 3 -k 4 ;

# Cube
curve -d 1 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;

# Arrow
curve -d 1 -p -1 0 -1 -p -3 0 -1 -p -3 0 -2 -p -5 0 0 -p -3 0 2 -p -3 0 1 -p -1 0 1 -p -1 0 3 -p -2 0 3 -p 0 0 5 -p 2 0 3 -p 1 0 3 -p 1 0 1 -p 3 0 1 -p 3 0 2 -p 5 0 0 -p 3 0 -2 -p 3 0 -1 -p 1 0 -1 -p 1 0 -3 -p 2 0 -3 -p 0 0 -5 -p -2 0 -3 -p -1 0 -3 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 ;

#for creating a curve
	mel_line = 'curve;'

	pm.mel.eval(curve_script)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint

#offset on
parentConstraint -mo -weight 1;
#offset off
parentConstraint -weight 1;

pm.parentConstraint()
# Orient Constraint

#offset off
orientConstraint -offset 0 0 0 -weight 1;
#offset on
orientConstraint -mo -weight 1;

pm.orientConstraint()

# Point Constraint
#offset off
pointConstraint -offset 0 0 0 -weight 1;
#offset on
pointConstraint -mo -weight 1;


pm.pointConstraint()

# Pole Vector Constraint
poleVectorConstraint -weight 1;

# How does this constraint differ from the previous three.

#there is no option to turn the offset on and off
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

#DETACH


#SEPARATE


#EXTRACT
performPolyChipOff 0 0;

#COMBINE

#NUKE

FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
DeleteAllHistory;
CenterPivot;


