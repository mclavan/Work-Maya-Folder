'''
Research Notes

Name Seany Snow Tyler

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
'''
1.makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1
2.Its a command that sets and freezes the values to 0 within its current position. turned on
echo to find the longer command
3.pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
4. flags: -t, -r, -s, -n, -pn
'''

# Delete History
'''
1. delete -ch (contructionHistory)
2.Its a create/multiuse function. Turned on the echo and played around with the commands that look important
3. pm.delete(ch=True)
4. flags: -ch
'''

# Center Pivot
'''
1.xform -cp
2. places the pivot point in the center of a selected object. 
3.pm.xform(cp=True)
4. flags: -cp
'''

# Single Chain and Rotate Plan IKs
'''
#Single Chain
1.ikHandle -shf false -s 0;
2.makes single chain IK handles between two selected joints. 
3.pm.ikHandle(shf=False, s ='0')
4. flags: -shf, -s
'''
'''
Rotate Plan
1.ikHandle -sol ikRPsolver -shf false -s 0;
2.Makes rotate plane IK handles. this could be found without echo
3.pm.ikHandle( sol='ikRPsolver', shf=False, s='0')
4. Flags: -sol, ikRPsolver, -shf, s
'''

# Cluster
'''
1.newCluster " -relative -envelope 1";
2.Makes the curve inside the spline easy to control.
3.pm.cluster(relative=True, en=1) 
4. flags: -rel , -en
'''
# Grouping (Does not need to be included on Shelf!)
'''
1. Group
2. Hitting command+g
3.pm.group()
4. flags: 
'''
# Parenting (Does not need to be included on Shelf!)
'''
1.Parent;
2. hit 'P'
3.pm.parent()
4. flags:
'''

# Duplicating (Does not need to be included on Shelf!)
'''
1.duplicate -rr;
2. command+d 
3.pm.duplicate(rr=True)
4. flags: -rr
'''

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
'''
1.circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;
2.create a nurbs primitive circle
3.pm.circle(c=[0,0,0], nr=[0,1,0], sw=360, r=1, d=3, ut=False , tol=0, s=8, ch=True)
4. flags: c , nr , sw, r, d, ut, tol, s, ch 
'''

# Square
'''
1.nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1
2. create a nurbs square
3.pm.nurbsSquare(c=[0,0,0], nr=[0,1,0], sl1=1, sl2=1, sps=1, d=3, ch=True
4. flags, c , nr, sl1, sl2 , sps, d, ch
'''

# Cube
'''
1.nurbsCube -p 0 0 0 -ax 0 1 0 -w 1 -lr 1 -hr 1 -d 3 -u 1 -v 1 -ch 1;
2.create a nurbs cube
3. pm.nurbsCube(p=[0,0,0], ax=[0,1,0] ,w=1, lr=1, hr=1 ,d=3, u=1, v=1, ch=True)
4. flags: p, ax, w, lr, hr, d, u, v, ch
'''

# Arrow
'''
1.curve -d 1 -p -1 0 0.25 -p -1 0 1.25 -p -2 0 0 -p -1 0 -1.25 -p -1 0 -0.25 -p 0.75 0 -0.25 -p 0.75 0 0.25 -p -1 0 0.25 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
2. create a CV curve, hold down X and draw out an Arrow
3.pm.curve( d=1 ,p=[1 ,0 ,0.25 ],p=[1 ,0 ,1.25] ,p=[2 ,0 ,0] ,p=[1 ,0 ,1.25 ],p=[-1 ,0 ,0.25],p=[0.75 ,0 ,0.25],p=[ 0.75 ,0 ,0.25],p=[-1,0,0.25] ,k=0,k=1,k=2,k=3,k=4,k=5,k=6,k=7)
'''


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
'''
1.parentConstraint -weight 1;
2.make a parent constraint
3.pm.parentConstraint()
4. flags: weight
'''

# Orient Constraint
'''
1.orientConstraint -offset 0 0 0 -weight 1;
2. make an orient Constraint
3. pm.orientConstraint()
4. flags: offset, weight
'''

# Point Constraint
'''
1.pointConstraint -offset 0 0 0 -weight 1;
2.make a point Constraint
3.pm.pointConstraint()
4. flags: offset, weight
'''

# Pole Vector Constraint
'''
1.poleVectorConstraint -weight 1;
2.make a pole pole Vector Constraint
3.pm.poleVectorConstraint()
'''
# How does this constraint differ from the previous three.
'''
utilizes an icon to translate the mid joint in an ikRPsolver
'''

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


