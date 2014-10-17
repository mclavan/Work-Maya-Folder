'''
Research Notes

Name:
Yael Valentin

Current Shelf Tools:
center Pivot
Nuke
joint tool



* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 

Drop Down Menus: ??
drop down menus are layered bottons added to the shelp bottons you currently have
in order for a botton to have multiple uses.

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
#flags can find them by highlighting command and go to quick help.

'''
			# Freeze Transforms
'''
'''
first I ran command from the modifi menu with the script editor open and echo all on.
 this gave me the mel command I needed to find. then I created an object and manipulated
  it accordingly. After i clicked on shelf button and it worked.
   
these are the flags you can use.
-preserveNormals(-pn)
-normal(-n)
-jointOrient(-jo)
-scale(-s)
-rotate(-r)
-translate(-t)
-apply(-a)
'''
#mel
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
#pymel
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
'''
			# Delete History

'''
#mel
delete -ch;

#pymel
pm.delete(ch=True)

'''

			# Center Pivot
'''
#MEL
xform -cp

#python
pm.xform(cp=True)

'''
# joimt tool
'''
#mel

JointTool;
setToolTo jointContext;
changeToolIcon;
editMenuUpdate MayaWindow|mainEditMenu;

'''
			# Single Chain and Rotate Plan IKs

'''

IKHandleTool;
setToolTo ikHandleContext;
changeToolIcon;

# Cluster
'''
			# Grouping (Does not need to be included on Shelf!)
'''

#mel
doGroup 0 1 1;
#Python
pm.group()
# Parenting (Does not need to be included on Shelf!)
#you ahve to select child then parent
#mel
Parent;
performParent false;

#pythom
pm.parent()
'''
			# Duplicating (Does not need to be included on Shelf!)
'''
#mel
duplicatePreset(1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1);

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
#each control has  flags you can change. thios will manipulate its rotations
#ie-nr 1 0 0  to -nr 1 2 1
'''
		# Circle
'''
'''
i rotated the circle by  changing the flag after -nr
'''
#mel
circle -c 0 0 0 -nr 1 0 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; 
#python
pm.circle(r=2,sections=8,normal=[1,0,0])[0]) 
'''
			# Square
'''

#MEL
nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ;
'''
			#cube
'''

polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;

#PYTHON
PM.nurbsSquare(c=[0,0,0],nr=[1,0,0], sl1=1, sl2=1, sps=1, d=3,ch=1)
'''
			# Arrow
'''

'''
Constraints
- Remember to test offset on and off with these commands.
'''
'''
			# Parent Constraint
'''
#mel
parentConstraint -mo -weight 1;
#python
pm.parentConstraint()
'''
			# Orient Constraint
'''
#mel
orientConstraint -offset 0 0 0 -weight 1;

#python

pm.orientConstraint()
'''
			# Point Constraint
'''

pointConstraint -offset 0 0 0 -weight 1;
# Pole Vector Constraint
poleVectorConstraint -weight 1;
# How does this constraint differ from the previous three.
#parent contraints move objects
'''
Attributes (Convered in Podcast)
'''
'''
			# Create float attribute
'''
#firs you have to run the ls. command then specify what you want selected.
first_selected.tx.set(5)

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


