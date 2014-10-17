'''
Research Notes

Brandon Berry

Current Shelf Tools: 11
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
1) makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
2) MAYA command
3) pm.makeIdentity(apply = True, t = 1, r = 1, s = 1, n = 0)
4) -apply, -t, -r, -s, -n, -pn
'''

# Delete History
'''
1) delete -ch;
2) MAYA Command
3) pm.delete(ch = True)
4) -ch
'''

# Center Pivot
'''
1) xform -cp;
2) MAYA command
3) pm.xform(cp = True)
4) -cp, -p
'''
# Single Chain and Rotate Plane IKs
'''
Single Chain
1) ikHandle -sj ct_spine_01_bind -ee ct_spine_06_waste -sol ikSCsolver;
2) MAYA command
3) pm.ikHandle(sj = 'ct_spine_01_bind', ee = 'ct_spine_06_waste', sol = 'ikSCsolver')
4) -ce, -sj, -ee

Rotate Plane IK
1) ikHandle -sj rt_arm_01_bind -ee rt_arm_03_bind -sol ikRPsolver;
2) MAYA command
3) pm.ikHandle(sj = 'rt_arm_01_bind, ee = 'rt_arm_03_bind, sol = ikRPsolver)
4) -ce, -sj, -ee
'''
# Cluster
'''
1) cluster;
2) MAYA command
3) pm.cluster()
4) -bf, -af, -is, -rel
'''

# Grouping (Does not need to be included on Shelf!)
'''
1) group -em;
2) MAYA command
3) pm.group(empty = True)
4) -em
'''

# Parenting (Does not need to be included on Shelf!)
'''
1) parent rt_arm_03_local rt_arm_02_icon
2) MAYA command
3) pm.parent('rt_arm_03_local', 'rt_arm_02_icon')
4) -relative, -add, -removeObject
'''

# Duplicating (Does not need to be included on Shelf!)
'''
1) duplicate -rr;
2) MAYA command
3) pm.duplicate()
4) -po, -st
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
1) circle;
2) MAYA command
3) pm.circle()
4) -po, -st
'''

# Square
'''
1) curve -d 1 -p -1.14978 1.14978 -6.799105 -p 1.14978 1.14978 -6.799105 -p 1.14978 -1.14978 -6.799105 -p -1.14978 -1.14978 -6.799105 -p -1.14978 1.14978 -6.799105 -k 0 -k 1 -k 2 -k 3 -k 4 ;
2) MAYA command
3) mel_line = 'curve -d 1 -p -1.14978 1.14978 -6.799105 -p 1.14978 1.14978 -6.799105 -p 1.14978 -1.14978 -6.799105 -p -1.14978 -1.14978 -6.799105 -p -1.14978 1.14978 -6.799105 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
	pm.mel.eval(mel_line)
4) 
'''

# Cube
'''
1) curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 ;
2) MAYA command
3) mel_line = 'curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 ;'
	pm.mel.eval(mel_line)
4) 
'''

# Arrow
'''
1) curve -d 1 -p 0 0 4 -p -2 0 2 -p -2 0 3 -p -6 0 3 -p -6 0 5 -p -2 0 5 -p -2 0 6 -p 0 0 4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
2) MAYA command
3) mel_line = 'curve -d 1 -p 0 0 4 -p -2 0 2 -p -2 0 3 -p -6 0 3 -p -6 0 5 -p -2 0 5 -p -2 0 6 -p 0 0 4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
	pm.mel.eval(mel_line)
4)
'''


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
'''
1) parentConstraint -mo -weight 1; # maintain offset on| parentConstraint -weight 1;
2) MAYA command
3) pm.parentConstraint(mo = True) | pm.parentConstraint(mo = False)
4) -mo
'''

# Orient Constraint
'''
1) orientConstraint -offset 0 0 0 -weight 1;
2) MAYA command
3) pm.orientConstraint()
4) -mo, -offset
'''

# Point Constraint
'''
1) pointConstraint -offset 0 0 0 -weight 1;
2) MAYA command
3) pm.pointConstraint()
4) -mo, -offset
'''

# Pole Vector Constraint
# How does this constraint differ from the previous three.
'''
1)
2)
3)
4)

This constraint requires an existing IK handle to be created and function properly
'''

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
# Use following "pre-script" for Python
import pymel.core as pm
selected = pm.ls(selection = True)
first_selected = selected[0]
print 'First Selected Object;', first_selected
'''
1) 	addAttr -ln "index_curl"  -at double  |testCube;
	setAttr -e-keyable true |testCube.index_curl;
2) Maya command
3) first_selected.addAttr('index_curl', keyable = True)
4) -e-keyable
'''

# Create Separator Attribute
'''
1)	addAttr -ln "CURL"  -at "enum" -en "----------------:"  |testCube;
	setAttr -e-keyable true |testCube.CURL;
2) Maya command
3) first_selected.addAttr('CURL', keyable = True,
		at = 'enum', en = "----------------:")
4) -e-keyable
'''

# Template Attributes 
# Create a group of attributes at one time. 
# The finger attributes are an example.
'''
CURL
index_curl
'''
'''
1)	addAttr -ln "CURL"  -at "enum" -en "----------------:"  |testCube;
	setAttr -e-keyable true |testCube.CURL;
	addAttr -ln "index_curl"  -at double  |testCube;
	setAttr -e-keyable true |testCube.index_curl;

	addAttr -ln "SPREAD"  -at "enum" -en "----------------:"  |testCube;
	setAttr -e-keyable true |testCube.SPREAD;
	addAttr -ln "index_spred"  -at double  |testCube;
	setAttr -e-keyable true |testCube.index_dpread;
2) MAYA command
3)	first_selected.addAttr('CURL', keyable = True,
		at = 'enum', en = "----------------:")
	first_selected.addAttr('index_curl', keyable = True)

	first_selected.addAttr('SPREAD', keyable = True,
		at = 'enum', en = "----------------:")
	first_selected.addAttr('index_spread', keyable = True)
4) -en, -ln, -at
'''

'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.

Research:
Detach Component
Separate
Extract
Combine
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
'''


