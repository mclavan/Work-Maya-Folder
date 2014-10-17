'''
Research Notes

Niles Keith

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: ??

Drop Down Menus: ??

'''



'''
Below are the minimum requirements.  Make sure to add addition tools to 
increase the affectiveness of your toolset. 

-- Please look at the project notes at the end of this document.
'''

'''
General Tools Research

'''

# Freeze Transforms
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
#Python Command
pm.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0)

# Delete History
DeleteHistory;
delete -ch;

#Python Version
pm.delete(-channelHistory=1)

# Center Pivot
#echo on is required to find this command
CenterPivot; #This is the Runtime Command
xform -cp; #This is the command we are looking for.
#Python Version
pm.xform(centerPivots=1)


# Single Chain and Rotate Plan IKs
ikHandle; -sol ikSCsolver;
#Python Command
pm.ikHandle(solver='ikSCsolver')

ikHandle -sol ikRPsolver;
#Python Command
pm.ikHandle(solver='ikRPsolver')
# Cluster

# Grouping (Does not need to be included on Shelf!)
doGroup 0 1 1;
#python
pm.group(empty=True)
# Parenting (Does not need to be included on Shelf!)
select -r circle 1;
select -add circle_2;
parent;
//circle_1//
pm.parent(circle_1, circle_2)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
'''
# Circle

#MEL
circle; -c 0 0 0 -nr 0 1 0 -sw 360 - r 1 -d 3 -ut 0 -tol 0 -s 12 -ch 1; objectMoveCommand;
#Python Command
import pymel.core as pm
pm.circle(nr=(0, 0, 1), c=(0, 0, 0) )

# Square

#MEl
nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1; objectMoveCommand
#Python command
import pymel.core as pm
pm.nurbsSquare(nr=(0, 0, 1), c=(0, 0, 0))

# Cube
#MEL
nurbsCube -p 0 0 0 -az 0 1 0 -w 1 -lr 1 -hr -d 3 -u 1 -v 1 -ch 1; objectMoveCommand;
#Pyhthon Command
import pymel.core as pm
pm.nurbsCube(nr=(0, 0, 1), c=(0, 0, 0,))

# Arrow
#MEl
curve -d 1 -p 0 0 0 -p -2 0 -2 -p -1 0 -2 -p -1 0 -5 -p 1 0 -5 -p 1 0 -2 -p 2 0 -2 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
#Python Command
import pymel.core as pm
mel_line= 'curve -d 1 -p 0 0 0 -p -2 0 -2 -p -1 0 -2 -p -1 0 -5 -p 1 0 -5 -p 1 0 -2 -p 2 0 -2 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)
arrow;

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
parentConstraint -mo -weight 1;
parentConstraint -weight 1;
#Python Command
pm.parentConstraint(weight=1)
pm.parentConstraint(maintatinOffset=True, weight=1)

# Orient Constraint
#offset off
orientConstraint -offset 0 0 0 -weight 1;
#offset on
orientConstraint -mo 0weight 1;
#Python Commands
pm.orientConstraint(offset=(0, 0, 0), weight=True)
pm.orientConstraint(maintainOffset=True, weight=True)

# Point Constraint
#offset off
pointConstraint -offset 0 0 0 -weight 1;
#offset on
pointConstraint -mo -weight 1;
#Python Command
pm.pointConstraint(offset=(0, 0, 0), weight=True)
pm.pointConstraint(maintainOffset=True, weight=True)

# Pole Vector Constraint
poleVectorConstraint(maintainOffset=True, weight=1, aimVector=(0, 0, 0))
# How does this constraint differ from the previous three.

'''
Attributes (Convered in lecture 9.)

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
'''
Research:

#Detach Component
DetachComponent;
performDetachComponents; #mel script
#Python Command
pm.mel.DetachComponent()

#Separate
polySeparate -sss 0 -ch 1 pSphereShape1;
#Python Command
pm.polySeparate(constructionHistory=1)

#Extract
#Combind
#Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot



'''
-- Project Notes --
'''
'''
Include any observation on how the commands and its flags work. 
	- Did the command work differently than other commands?
	- Did the command do something different than the interface version. 
Make sure notes included how you located the command.  
	- Did you use echo all?  
	- Did you get unexpected results when researching the command.  
Document important flags. 
	-t is -translate 
ALL COMMANDS NEED TO BE CONVERTED FROM MEL TO PYTHON.
	- Include MEL and python version.

'''

'''
** Comments on Run Time Commands and MEL Scripts.

Typically you want to user the Maya command when ever you can. 
However, there are some exceptions:
	- Maya command is extremely difficult to use. 
	- Single click process. 
		- Meaning this command isn't being used as part of a process. 
	- No maya command exists. 
		- It is uncommon but some processes are done with scripts only.
'''
