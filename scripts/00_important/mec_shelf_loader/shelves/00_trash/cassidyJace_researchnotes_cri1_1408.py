'''
Research Notes

Jace Cassidy

Current Shelf Tools: 17 tools on shelf 20 commands documented
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 0

Drop Down Menus: 0

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
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
'''
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
It's a MEL Procedure and I ran the procedure and found it in the script editor then found out what type of command in the help docs.
Important flags are apply, t -> translate, r-> rotate, s -> scale, n -> normals
'''

# Delete History
pm.delete(ch=True)
'''
pm.delete(ch=True) 
It's a run time command and I found that out by using the whatIs command in the script editor.
An important flag is ch -> construction history
'''

# Center Pivot
xform -cp;
'''
xform -cp;
It's an undoable, queryable, and not edible command and I found it by running the command and looking in the script editor.
An important flag is -cp -> -centerPivots
'''

# Single Chain and Rotate Plan IKs
ikHandle;
'''
ikHandle;
Single Chain
It is undoable, queryable, and editable command and I found it in the script editor after creating an Single Chain Ik.
Some flags are e -> edit, q -> query, sj -> startJoint, and ee -> endEffector.
'''
ikHandle -sol ikRPsolver;
'''
ikHandle -sol ikRPsolver;
Rotate Plane
It is undoable, queryable, and editable command and I found it in the script editor after creating an Rotate Plane Ik.
Some flags are e -> edit, q -> query, sj -> startJoint, and ee -> endEffector.
The difference between this and a SC solver is in the code of this command there is -sol ikRPsolver; added to the end of the command.
'''

# Cluster
newCluster " -relative -envelope 1";
'''
newCluster " -relative -envelope 1";
It is a MEL Procedure and I found it in the script editor after creating a cluster in Maya.
Some flags are n -> name, g -> geometry, rm -> remove.
'''


# Grouping (Does not need to be included on Shelf!)
pm.group()
doGroup 0 1 1;
'''
pm.group()
doGroup 0 1 1;
It is an undoable, not queryable, and not edible command and I found this info in the help docs and remember the command from the hierarchy project and found it in the script editor after I performed the action.
Important flags are em -> empty, p -> parent, w -> world
'''

# Parenting (Does not need to be included on Shelf!)
pm.parent()
parent -w;
'''
pm.parent()
parent -w;
It is an undoable, not queryable, and not editable cooman and I found this info in the help docs and remember using this command in the hierarchy project and found it in the script editor after I performed the action.
The command is run -> pm.parent(root_joint, root_pad) order is child -> parent. some flags are w -> world, and r -> relative, and a -> absolute.
'''

# Duplicating (Does not need to be included on Shelf!)
duplicate -rr;
'''
duplicate -rr;
It is an undoable, not queryable, and not edible command and I found it in the script editor after performing the action and in the maya help docs.
Some flags are n -> name, and st -> smartTransform.
'''

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
pm.circle()
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
'''
pm.circle()
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
It is an undoable, queryable, and editable command and I found it in the script editor after I ran the command and also remembered a version of it form the hierarchy project.
Important flags are nr -> normal, r -> radius

'''

# Square
curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
'''
curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
It is an undoable, not queryable, and not editable command and I found it in the script editor after I made the control icon.
Important flags are d -> degree, r -> replace, a -> append, and p -> point.
'''

# Cube
curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 ;
'''
curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 ;
It is an undoable, not queryable, and not editable command and I found it in the script editor after I finished snapping to the cube.
Important flags are d -> degree, r -> replace, a -> append, and p -> point.
'''

# Arrow
curve -d 1 -p 0 0 -3 -p 3 0 0 -p 1 0 0 -p 1 0 4 -p -1 0 4 -p -1 0 0 -p -3 0 0 -p 0 0 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
'''
curve -d 1 -p 0 0 -3 -p 3 0 0 -p 1 0 0 -p 1 0 4 -p -1 0 4 -p -1 0 0 -p -3 0 0 -p 0 0 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
It is an undoable, not queryable, and not editable command and I found it in the script editor after I finished snapping the points down on the grid.
'''


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;
'''
offset on
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;
It is a Mel Procedure andI found it in the script editor after using the procedure and by using the whatIs command.
Some flags are n -> name, w -> weight, rm -> remove.
Also noticed the difference between this command wiht offset ona nd off is the -mo in the code.
'''
doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
parentConstraint -weight 1;
'''
offset off
doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
parentConstraint -weight 1;
It is a Mel Procedure andI found it in the script editor after using the procedure and by using the whatIs command.
Some flags are n -> name, w -> weight, rm -> remove.
Also noticed the difference between this command wiht offset ona nd off is the -mo in the code.
'''

# Orient Constraint
doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
orientConstraint -mo -weight 1;
'''
offset on
doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
orientConstraint -mo -weight 1;
It is a Mel Procedure andI found it in the script editor after using the procedure and by using the whatIs command.
Some flags are n -> name, w -> weight, rm -> remove.
Also noticed the difference between this command with offset on and off is it says -offset 0 0 0 in the code.
'''
doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
orientConstraint -offset 0 0 0 -weight 1;
'''
offset off
doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
orientConstraint -offset 0 0 0 -weight 1;
It is a Mel Procedure andI found it in the script editor after using the procedure and by using the whatIs command.
Some flags are n -> name, w -> weight, rm -> remove.
Also noticed the difference between this command with offset on and off is it says -offset 0 0 0 in the code.
'''

# Point Constraint
doCreatePointConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
pointConstraint -mo -weight 1;
'''
offset on
doCreatePointConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
pointConstraint -mo -weight 1;
It is a Mel Procedure andI found it in the script editor after using the procedure and by using the whatIs command.
Some flags are n -> name, w -> weight, rm -> remove.
Also noticed the difference between this command with offset on and off is it says -offset 0 0 0 in the code.
'''
doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;
'''
offset off
doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;
It is a Mel Procedure andI found it in the script editor after using the procedure and by using the whatIs command.
Some flags are n -> name, w -> weight, rm -> remove.
Also noticed the difference between this command with offset on and off is it says -offset 0 0 0 in the code.
'''

# Pole Vector Constraint
poleVectorConstraint -weight 1;
'''
poleVectorConstraint -weight 1;
It is an undoable, queryable, adn editable command and I found it inside the script editor after creating a pole vector for my ik handle.
Some flags are n -> name, w -> weight, and rm -> remove.
The main difference between the other constraints and this one is that this one doesn't have a maintain offset option and can only be used wiht ikhandles.
'''
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


