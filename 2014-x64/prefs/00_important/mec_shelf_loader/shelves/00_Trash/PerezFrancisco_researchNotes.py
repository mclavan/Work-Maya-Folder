'''
Research Notes

Name Francisco Perez

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: No

Drop Down Menus: No

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
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1; Boolean
I found the command by using it manually and looking through the 
script editor. cho all commands was on.
Python Version: pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
Flags: -t is translate, -r is rotate, -s is scale, and -pn means perserve 
normals

# Delete History
delete -ch;(General)
I found it by using delete by type history manually and then searching 
the scipt editor with Echo all commands on, to find the line of code 
with the command.
Python Version:pm.delete(ch)
Flag: -ch, means construction history. It is necessary in order to delete 
history other flags indicate other things to delete. Ex: delete -cp; means 
to d

# Center Pivot
xform -cp;(Boolean)
I found it by using it manually and with Echo all commands turned on in the 
script editor I searched the script and found the line with the command.
Python Version:
Flag: -cp; means center pivot 

# Single Chain and Rotate Plan IKs
ikHandle; List
I found it by using it manually and then searching the script editor with 
echo all commands on.
Python Version: pm.ikHandle()
Flags. It is important to make a selection

# Cluster
CreateCluster;
To fing it I used it manually and then searched the script edtor to find 
the command. Echo all commands was on.
Python Version: pm.cluster()
Flags: bf means before and af means after, 


# Grouping (Does not need to be included on Shelf!)
doGroup 0 1 1; List
I found it by using it manually then with echo all commands on, I searched 
the script editor and found the line that contained the command.
Python Version: pm.group()
Flags: p is parent, em is empty, n is the name

# Parenting (Does not need to be included on Shelf!)
parent; 
found it by using it manually and then searching the script edotor for 
the command.
Python Version: pm.parent()
Flags: s is shape rm is remove object, a is absolute.

# Duplicating (Does not need to be included on Shelf!)
duplicate -rr; List
found it by using it manually and then searching the script editor for the 
command.
Python Version: pm.duplicate() 
Flags: -rr is returnRootsOnly, -po is parentOnly


'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
circle; is the Mel script.
I found it by creating a circle manually and then searching the script 
editor to find the line of code that contained the command. 
The ';' signifies the end of a line
Python Version: pm.circle()
Flags: -nr refers to the normals of the circle this is important for aiming 
the circle where you want it. Ex: circle -nr 0 1 0 will have the circle flat 
at the origin.
-r refers to the radius Ex. circle -r 3 giving the circle a radius of 3.
-c refers to the center positioning

# Square
curve -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4;, 
List
To figure iit out i had echo all commands turned on and mel history output 
then i manually created a square using the cv curve tool. I searched the 
script editor for the command with all the specific attributes. I copied the 
entire line and the used the Mel Script for curve command for and within the 
parenthesis pasted the copied command. Then I converted by using 
pm.mel.eval(mel_line)
Python Version: mel_line = 'curve -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4'
pm.mel.eval(mel_line)
Flags: -p means point

# Cube
curve -d 1 -p -0.5 2.404901 0.5 -p 0.5 2.404901 0.5 -p 0.5 1.404901 0.5 -p -0.5 1.404901 0.5 -p -0.5 2.404901 0.5 -p -0.5 2.404901 -0.5 -p -0.5 1.404901 -0.5 -p -0.5 1.404901 0.5 -p -0.5 1.404901 -0.5 -p 0.5 1.404901 -0.5 -p 0.5 2.404901 -0.5 -p -0.5 2.404901 -0.5 -p 0.5 2.404901 -0.5 -p 0.5 2.404901 0.5 -p 0.5 1.404901 0.5 -p 0.5 1.404901 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;, 
List
To figure it out I manually created a cube usng the cv curve tool and traced a 
cube. I then serached the Script editor for the command line. The rest was 
the same as the sqaure.
Python Version:mel_line = 'curve -d 1 -p -0.5 2.404901 0.5 -p 0.5 2.404901 0.5 -p 0.5 1.404901 0.5 -p -0.5 1.404901 0.5 -p -0.5 2.404901 0.5 -p -0.5 2.404901 -0.5 -p -0.5 1.404901 -0.5 -p -0.5 1.404901 0.5 -p -0.5 1.404901 -0.5 -p 0.5 1.404901 -0.5 -p 0.5 2.404901 -0.5 -p -0.5 2.404901 -0.5 -p 0.5 2.404901 -0.5 -p 0.5 2.404901 0.5 -p 0.5 1.404901 0.5 -p 0.5 1.404901 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15'
pm.mel.eval(mel_line) 
Flags: -p means point

# Arrow
curve -d 1 -p 8 0 4 -p 8 0 3 -p 8 0 2 -p 7 0 2 -p 9 0 0 -p 11 0 2 -p 10 0 2 -p 10 0 3 -p 10 0 4 -p 8 0 4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 ;
List
To figure it out i did the same process as the cube and square. By using the 
cv curve tool and creating the icon and then finding the command in the 
script editor. 
Python Version: mel_line = 'curve -d 1 -p 8 0 4 -p 8 0 3 -p 8 0 2 -p 7 0 2 -p 9 0 0 -p 11 0 2 -p 10 0 2 -p 10 0 3 -p 10 0 4 -p 8 0 4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9'
pm.mel.eval(mel_line)
Flags: -p means point
 

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
ParentConstraint; List
I found this one out by doing it manually and then searching the script 
editor for the command line.
Python Version: pm.parentConstraint()
Flags: -w means weight, -rm means to remove, -st means skip translate

# Orient Constraint
OrientConstraint; List
I found this one out by doing it manually and then searching the script 
editor for the command line.
Python Version: pm.orientConstraint()
Flags: -mo means mantain offset, o means offset, -w means weight

# Point Constraint
OrientConstraint; List
I found this one out by doing it manually and then searching the script 
editor for the command line.
Python Version: pm.pointConstraint()
Flags: -w means weight, -rm means remove, -n means name

# Pole Vector Constraint
# How does this constraint differ from the previous three.
PoleVectorConstraint; List
I found this one out by doing it manually and then searching the script 
editor for the command line.
Python Version: pm.poleVectorConstraint 
Flags: -w means weight, - rm means remove
-n means name
This one differs fromt eh other three because and ikHandle is necessary for 
this to be applied

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
addAttr; List
I found this by using the python version and then using deductiong trying out
what it thought the mel version to be and found it immeadiatly.
Python Version: first_selected = selected[0]
first_selected.addAttr('middle_curl', keyable=True)
Flags: -at means attribute type, -nn means nickname, -ln means longname, 
-min means minimum value.

# Create Separator Attribute
addAttr -ln "Boom"  -at "enum" -en "Green:Blue:"  |pCylinder1;
setAttr -e-keyable true |pCylinder1.Boom; List
I found this one out by doing it manually and then searching the script 
editor for the command line.
Python Version: first_selected.addAttr
('Fingers', at=enum, en'----------------:', keyable=True)
Flags: -at means attribute type, -nn means nickname, -ln means longname, 
-min means minimum value.

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
MEL: addAttr -ln "Finger"  -at "enum" -en "----------------"  |pCylinder1;
setAttr -e-keyable true 
addAttr -ln "Curl"  -at "enum" -en "----------------"  |pCylinder1;
setAttr -e-keyable true 
addAttr "Middle"; setAttr -e-keyable true
etc.........

Python: first_selected.addAttr
('Fingers', at=enum, en'----------------:', keyable=True)
first_selected.addAttr
('Curl', at=enum, en'----------------:', keyable=True)
first_selected = selected[0]
first_selected.addAttr('middle_curl', keyable=True)
first_selected = selected[0]
first_selected.addAttr('pinky_curl', keyable=True)
etc......
Flags: -at means attri type, -en means enum name, -ln means longname

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


