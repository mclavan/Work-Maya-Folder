'''
Research Notes

Tanat Kriengkomol
'''
'''
**NOTE!: Remember to run:
	import pymel.core as pm
before every Python command!!**
'''

'''
General Tools Research
'''

# Freeze Transforms
	# MEL Command:
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	# This command is used to freeze transformations on objects, resetting the
	# transform, rotate, and scale to 1.
	#Python Command:
pm.makeIdentity (apply=True, t=1, r=1, s=1, n=0, pn=1)
	# The -apply flag applies the command
	# The -t, -r, and -s flags set the Transform, Rotate, and Scale to 1

# Delete History
	#Mel Command:
delete -ch;
	# This command deletes the history of a selected object.
	#Python Command:
pm.delete (ch=True)

# Center Pivot
	#Mel Command:
xform -cp;
	# This command sets the pivot point of an object to it's absolute center.
	# Python Command:
pm.xform (cp=True)

# Single Chain and Rotate Plan IKs
	# SINGLE CHAIN
	# Mel Command:
ikHandle;
	# Python Command:
pm.ikHandle()

	# ROTATE PLANE
# Mel Command:
ikHandle;
	# Identical to above command, with the exception of the flag -sol
	# The flag -sol stands for Solver, which sets the type of solver on the joint.
	# The options/flags for this flag are: ikRPsolver, ikSCsolver, and ikSplineSolver.

# Grouping (Does not need to be included on Shelf!)
	# Mel Command
group;
	# Python Command
pm.group()
	# The command groups selected objects together.
	# Flags for grouping include w and p
	# These change whether the group is a parent, or is a child.
	# The names of specific objects that are to be grouped can also be included as flags.

# Parenting (Does not need to be included on Shelf!)
	# MEL Command
parent;
	# Python Command
pm.parent()
	# This command allows an object to be parented to another object.
	# The order of this operation always goes DRIVER --> DRIVEN.
	# The only flag for this command is -r , which allows the object to keep it's local transforms.

# Duplicating (Does not need to be included on Shelf!)
	# MEL Command
duplicate -rr;
	# Python Command
pm.duplicate(rr=True)
	# Duplicates selected objects (in same position)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	# MEL Command:
circle -c 0 0 0 -nr 0 0 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;
	# Python Command:
pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1)
	# This command makes a circle or an arc.
	# The -c flag determines the center of the circle (world position)
	# The -nr flag sets the normal of the axis of the circle
	# The -sw flag determines Sweep, or the completeness of the circle (in degrees)

# Square
	# MEL Command:
nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ;
	# Python Command:
pm.nurbsSquare(c=[0, 0, 0], nr=[0, 1, 0], sl1=1, sl2=1, sps=1, d=3, ch=1)
	# This command makes a square or rectangle (2D shape)
	# -sl1 controls the first side's length
	# -sl2 controls the second side's length
	# -c determines the center of the shape in world space
	# -nr dtermines axis

# Cube
	# MEL Command
nurbsCube -p 0 0 0 -ax 0 1 0 -w 1 -lr 1 -hr 1 -d 3 -u 1 -v 1 -ch 1;
	# Python Command
pm.nurbsCube(p=[0, 0, 0], ax=[0, 1, 0], w=1, lr=1, hr= 1, d=3, u=1, v=1, ch=1)
	# Creates a Nurbs Cube.
	# -p controls the pivot point, and -ax controls the axis (width, length, and height)


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
	# MEL Command
parentConstraint -mo -weight 1;
	# Python Command
pm.parentConstraint(mo=True, weight=1)
	# This creates a parent constraint, a standard Driver -> Driven relationship.
	# The -mo flag determines whether the original transforms of the objects are kept (boolean)
	# The -weight flag sets the threshold(?) of the constraint. Default is 1.

# Orient Constraint
	# MEL Command
orientConstraint -mo -weight 1;
	# Python Command
import pymel.core as pm
pm.orientConstraint(mo=True, weight=1)
	# This creates an orientConstraint between two objects.
	# Similar to normal constraints but allows orientation
	# Same flags as Parent Constraint; Maintin Offset and Weight.

# Point Constraint
	# MEL Command
pointConstraint -offset 0 0 0 -weight 1;
	# Python Command
pm.pointConstraint(offset=[0, 0, 0], weight=1)
	# Creates a constraint at a point at the center of the target.
	# Same -mo and -weight flags as above, with the addition of -o
	# -o controls offset (X, Y, or Z values).

# Pole Vector Constraint
	# MEL Command
poleVectorConstraint -weight 1;
	# Python Command
pm.poleVectorConstraint(weight=1)
	# Creates a pole vector constraint.
	# Applied to ikRP Solvers and used as an "aiming mechanism" for translation of
	# elbow or knee joints. Very useful for realistic animations.
	# -weight flag
	# -wal flag, or WeightAliasList echoes the names of attributes set to the object.

# Nuke
	# MEL Command
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
CenterPivot;
DeleteAllHistory;
	# Very helpful set of commands to "nuke" object, or completely reset it's transforms,
	# pivot points and history. I personally find it useful for modeling.