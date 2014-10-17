'''
Research Notes

Nico Majersky

Current Shelf Tools: 22
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: 00

Drop Down Menus: 00

'''

'''
Each tool you will need document:
	1) MEL Command
	2) What type of command is it and how did you find it?
	3) Convert MEL to Python.
	4) Important Flags
'''

'''
General Tools Research
'''

# Freeze Transforms
1) makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
2) Maya command: lower case "makeIdentity" with flags and values
3) import pymel.core as pm
   pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
4) a=apply, t=translate, r=rotate, s=scale, n=normal, pn=preserveNormals
# Delete History
1) delete -ch;
2) Maya command: lower case "delete" with flag
3) import pymel.core as pm
   pm.delete(ch=True)
4) ch=constructionHistory
# Center Pivot
1) xform -cp;
2) Maya command: lower case with flags
3) import pymel.core as pm
   pm.xform(cp=True)
4) cp=centerPivots
# Single Chain and Rotate Plane IKs
1) ikHandle -n 'lf_clav' -sj 'lf_clav_01' -ee 'lf_clav_02';
2) Maya command: lower case with flags and values
3) import pymel.core as pm
   pm.ikhandle(n='lf_clav', sj='lf_clav_01', ee='lf_clav_02')
4) n=name, sj=startJoint, ee=endEffector

1) ikHandle -sol ikRPsolver -n 'rt_arm' -sj 'rt_arm_01' -ee 'rt_arm_03';
2) Maya command: lower case with flags and values
3) import pymel.core as pm
   pm.ikHandle(sol='ikRPsolver', n='rt_arm', sj='rt_arm_01', ee='rt_arm_03')
4) sol=solver, n=name, sj=startJoint, ee=endEffector
# Cluster
1) cluster -n cluster1 -bf true -af false -sp true;
2) Maya command: flags and values
3) import pymel.core as pm
   pm.cluster(n='cluster1', bf=True, af=False, sp=True)
4) n=name, bf=before, af=after, sp=split
# Grouping (Does not need to be included on Shelf!)
1) group -n grp1 -em;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.group(n='grp1', em=True)
4) n=name, em=empty
# Parenting (Does not need to be included on Shelf!)
1) parent;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.parent
4) add=addObject, rm=removeObject, nc=noConnections
# Duplicating (Does not need to be included on Shelf!)
1) duplicate;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.duplicate
4) n=name, rc=renameChildren, po=parentOnly
'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
1) circle -o on -nr 0 1 0 -r 1
2) Maya command: lower case title
3) import pymel.core as pm
   pm.circle(o=True, nr=[0, 1, 0], r=1)
4) o=object, nr=normal, n=name, r=radius, s=sections
# Square
1) curve -n square1 -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.mel.eval(-n square1 -d 1 -p -1 0 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;)
4) n=name, d=degree, p=point, k=knot
# Cube
1) curve -n cube1 -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.mel.eval(-n cube1 -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15;)
4) n=name, d=degree, p=point, k=knot
# Arrow
1) curve -n arrow1 -d 1 -p 0 0 -3 -p 2 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p -2 0 -1 -p 0 0 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.mel.eval(-n arrow1 -d 1 -p 0 0 -3 -p 2 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p -2 0 -1 -p 0 0 -3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7;)
4) n=name, d=degree, p=point, k=knot

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
1) parentConstraint -mo -weight 1;
   parentConstraint -weight 1;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.parentConstraint(mo=True, w=1)
   pm.parentConstraint(w=1)
4) mo=maintainOffset, w=weight
# Orient Constraint
1) orientConstraint -offset 0 0 0 -weight 1;
   orientConstraint -mo -weight 1;
2) Maya command: lower case title
3) import pymel.core as pm
   orientConstraint(o=[0, 0, 0], w=1)
   orientconstraint(mo=True, w=1)
4) o=offset, mo=maintainOffset, w=weight
# Point Constraint
1) pointConstraint -offset 0 0 0 -weight 1;
   pointConstraint -mo -weight 1;
2) Maya command: lower case title
3) import pymel.core as pm
   pointConstraint(o=[0, 0, 0], w=1)
   pointConstraint(mo=True, w=1)
4) o=offset, mo=maintainOffset, w=weight
# Pole Vector Constraint
# How does this constraint differ from the previous three.
1) poleVectorConstraint -weight 1;
2) Maya command: lower case title
3) import pymel.core as pm
   pm.poleVectorConstraint(w=1)
4) w=weight
'''
Attributes (Convered in Podcast)
'''

import pymel.core as pm
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object: ', first_selected
# Create float attribute
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)

# Create Separator Attribute
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True, at='enum', en='----------:')

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
first_selected.addAttr('FINGERS', keyable=True, at='enum', en="----------:")
first_selected.FINGERS.set(lock=True)

first_selected.addAttr('CURL', keyable=True, at='enum', en="----------:")
first_selected.CURL.set(lock=True)
first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('ring_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('SPREAD', keyable=True, at='enum', en="----------:")
first_selected.SPREAD.set(lock=True)
first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('ring_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB', keyable=True, at='enum', en="----------:")
first_selected.THUMB.set(lock=True)
first_selected.addAttr('thumb_curl', keyable=True)
first_selected.addAttr('thumb_drop', keyable=True)

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


