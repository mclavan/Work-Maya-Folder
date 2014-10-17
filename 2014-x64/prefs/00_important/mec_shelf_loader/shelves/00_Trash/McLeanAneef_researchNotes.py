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

mel command = makeIdentity 

Maya command

pyhton command = cmds.makeIdentity 

Flags
'''-apply true 
-t 1 
-r 1 
-s 1 
-n 0 
-pn 1'''

# Delete History
mel command = delete 

Maya command

pyhton command = cmds.delete

Flags
'''-ch'''
# Center Pivot
mel command = xform 

maya command

pyhton command = cmds.xform

Flags
'''-cp'''
# Single Chain and Rotate Plan IKs
mel command = ikHandle 

maya command 

pyhton command = cmds.ikHandle

Flags
'''-sol ikRPsolver -s 0'''
# Cluster
mel command = newCluster 

maya command


mel command = cmds.cluster

Flags
" -envelope 1"
# Grouping (Does not need to be included on Shelf!)
mel command = Group

maya command


pyhton command = cmds.group

# Parenting (Does not need to be included on Shelf!)
mel command = Parent

maya command

mel command = cmds.parent


# Duplicating (Does not need to be included on Shelf!)
mel command = duplicate 

maya command

mel command = cmds.duplicate

Flags
'''
-rr'''
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
mel command = circle 


maya command
 
Flags
 '''-c 0 0 0 
 -nr 0 1 0 
 -sw 360 
 -r 1 
 -d 3 
 -ut 0 
 -tol 0 
 -s 8 
 -ch 1'''
# Square
mel command = nurbsSquare


maya command

pyhton command =  

mel_line="curve -d 1 -p 0 0 0 -p 0 0 1 -p 1 0 1 -p 1 0 0 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;"
pm.mel.eval(mel_line)


Flags
'''-c 0 0 0 
-nr 0 1 0 
-sl1 1 
-sl2 1 
-sps 1 
-d 3 
-ch 1 '''
# Cube
mel command = nurbsCube 


maya command

pyhton command = 

mel_line="curve -d 1 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 ;"
pm.mel.eval(mel_line)

Flags
'''-p 0 0 0 
-ax 0 1 0 
-w 1 
-lr 1 
-hr 1 
-d 3 
-u 1 
-v 1 
-ch 1'''
# Arrow
mel command = curve 


maya command



python command =

mel_line="curve -d 1 -p -1.193544 0 -0.249049 -p -1.195521 0 0.317346 -p -0.0194022 0 0.347562 -p -0.00778073 0 0.902027 -p 0.837515 0 0.0112026 -p -0.0291822 0 -0.734218 -p -0.0309758 0 -0.22039 -p -1.207121 0 -0.222098 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;"
pm.mel.eval(mel_line)



Flags
'''-d 1 
-p 
-1.193544 0 
-0.249049 
-p 
-1.195521 0 0.317346 
-p 
-0.0194022 0 0.347562 
-p -0.00778073 0 0.902027 
-p 0.837515 0 0.0112026 
-p 
-0.0291822 0 
-0.734218 
-p 
-0.0309758 0 
-0.22039 
-p 
-1.207121 0 
-0.222098 
-k 0 
-k 1 
-k 2 
-k 3 
-k 4 
-k 5 
-k 6 
-k 7 '''

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
mel command = parentConstraint 

maya command

pyhton command = cmds.parentConstraint

Flags
'''-mo 
-weight 1'''
# Orient Constraint
mel command = orientConstraint 

maya command


pyhton command = cmds.orientConstraint

Flags
'''-offset 0 0 0 
-weight 1'''
# Point Constraint
pointConstraint 

maya command 


pyhton command = cmds.pointConstraint


Flags
'''-offset 0 0 0 
-weight 1'''
# Pole Vector Constraint
# How does this constraint differ from the previous three.
mel command = poleVectorConstraint 


maya command


pyhton command = cmds.poleVectorConstraint

Flags
'''-weight 1
'''
'''
Attributes (Convered in Podcast)
'''
# Create float attribute

first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

# Create Separator Attribute

'''
addAttr -ln "FINGERS" -at "enum" -en "Green:Blue:" |group1;
setAttr -e-keyable true |group1.FINGERS;

addAttr -ln "CURL" -at "enum" -en "----------------------:" |group1;
setAttr -e-keyable true |group1.CURL;
'''

first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------------------:")
first_selected.FINGERS.set(lock=True)

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.

'''
FINGERS
CURL
index_curl
middle_curl
pinky_curl
'''

first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------------------:")
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('CURL', keyable=True, at='enum', en="----------------------:")
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('SPREAD', keyable=True, at='enum', en="----------------------:")
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB', keyable=True, at='enum', en="----------------------:")
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_spread', keyable=True)
first_selected.addAttr('thumb_curl', keyable=True)

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


