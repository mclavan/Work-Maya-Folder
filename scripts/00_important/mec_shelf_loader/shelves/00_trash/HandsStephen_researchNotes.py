'''
Research Notes

Stephen Hands

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
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1; 

import pymel.core as pm
mel_line = 'makeIdentity -a true -t 1 -r 1 -s 1 -n 0 -pn 1;'
pm.mel.eval(mel_line)
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1);

apply(a), translate(t), rotate(r), scale(s), normal(n), preserveNormals(pn)


# Delete History
delete -ch;

import pymel.core as pm
mel_line = 'delete -ch'
pm.mel.eval(mel_line)

constructionHistory(ch)

# Center Pivot
xform -cp;

 import pymel.core as pm
mel_line = 'xform -cp;'
pm.mel.eval(mel_line)

centerPivots(cp)

# Single Chain and Rotate Plan IKs
# Rotate-Plane Solver
ikHandle -sol ikRPsolver;

import pymel.core as pm
mel_line = 'ikHandle -sol ikRPsolver;'
pm.mel.eval(mel_line)

solver(sol)

# Single-Chain Solver
ikHandle -sol ikSCsolver;

import pymel.core as pm
mel_line = 'ikHandle -sol ikSCsolver;'
pm.mel.eval(mel_line)

solver(sol)

# Cluster
import pymel.core as pm
mel_line = 'CreateCluster;'
pm.mel.eval(mel_line)

envelope(en)

# Grouping (Does not need to be included on Shelf!)
doGroup 0 1 1;

import pymel.core as pm
mel_line = 'doGroup 0 1 1;'
pm.mel.eval(mel_line)

group(g)

# Empty Group
import pymel.core as pm
pm.group(empty=True)

empty(em)

# Parenting (Does not need to be included on Shelf!)
parentPreset(0,1)

import pymel.core as pm 
pm.parent();

parent(p)

# Duplicating (Does not need to be included on Shelf!)
duplicate -rr;

import pymel.core as pm
pm.duplicate();

returnRootsOnly(rr)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;

import pymel.core as pm
mel_line = 'circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;'
pm.mel.eval(mel_line)

center(c), normal(nr), sweep(sw), radius(r), degree(d), useTolerance(ut), sections(s), constructionHistory(ch)

# Square
curve -d 1 -p 1 0 -5 -p 4 0 -5 -p 4 0 -2 -p 1 0 -2 -p 1 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 ;

import pymel.core as pm
mel_line = '-d 1 -p 5 0 10 -p 9 0 10 -p 9 0 6 -p 5 0 6 -p 5 0 10 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)

degree (d), point(p), knot(k)

# Cube
curve -d 1 -p 2.081335 3.063188 1.417424 -p 2.081335 3.063188 -2.763051 -p 2.081335 5.75563e-08 -2.763051 -p 2.081335 5.75563e-08 1.417424 -p 2.081335 3.063188 1.417424 -p -1.995252 3.063188 1.417424 -p -1.995252 5.75563e-08 1.417424 -p 2.081335 5.75563e-08 1.417424 -p -1.995252 5.75563e-08 1.417424 -p -1.995252 5.75563e-08 -2.763051 -p -1.995252 3.063188 -2.763051 -p -1.995252 3.063188 1.417424 -p -1.995252 3.063188 -2.763051 -p 2.081335 3.063188 -2.763051 -p 2.081335 5.75563e-08 -2.763051 -p -1.995252 5.75563e-08 -2.763051 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;

import pymel.core as pm
mel_line = 'curve -d 1 -p 2.081335 3.063188 1.417424 -p 2.081335 3.063188 -2.763051 -p 2.081335 5.75563e-08 -2.763051 -p 2.081335 5.75563e-08 1.417424 -p 2.081335 3.063188 1.417424 -p -1.995252 3.063188 1.417424 -p -1.995252 5.75563e-08 1.417424 -p 2.081335 5.75563e-08 1.417424 -p -1.995252 5.75563e-08 1.417424 -p -1.995252 5.75563e-08 -2.763051 -p -1.995252 3.063188 -2.763051 -p -1.995252 3.063188 1.417424 -p -1.995252 3.063188 -2.763051 -p 2.081335 3.063188 -2.763051 -p 2.081335 5.75563e-08 -2.763051 -p -1.995252 5.75563e-08 -2.763051 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
pm.mel.eval(mel_line)

degree (d), point(p), knot(k)

# Arrow
curve -d 1 -p -2 0 -5 -p -4 0 -5 -p -4 0 -4 -p -5.941816 0 -5.600373 -p -4 0 -7 -p -4 0 -6 -p -2 0 -6 -p -2 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

import pymel.core as pm
mel_line = 'curve -d 1 -p -2 0 -5 -p -4 0 -5 -p -4 0 -4 -p -5.941816 0 -5.600373 -p -4 0 -7 -p -4 0 -6 -p -2 0 -6 -p -2 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)

degree (d), point(p), knot(k)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
# Offset off 
doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
parentConstraint -weight 1;

import pymel.core as pm
pm.parentConstraint(mo=False);

maintainOffset(mo), weight(w)

# Offset on
doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
parentConstraint -mo -weight 1;

import pymel.core as pm
pm.parentConstraint(mo=True);

maintainOffset(mo), weight(w)

# Orient Constraint
# Offset off
doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
orientConstraint -offset 0 0 0 -weight 1;

import pymel.core as pm
pm.orientConstraint(mo=0);

offset(o), weight(w)

# Offset on
doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
orientConstraint -mo -weight 1;

import pymel.core as pm
pm.orientConstraint(mo=True);

maintainOffset(mo), weight(w)

# Point Constraint
# Offset off
doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
pointConstraint -offset 0 0 0 -weight 1;

import pymel.core as pm
pm.pointConstraint(mo=0);

offset(o), weight(w)

# Offset on
doCreatePointConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
pointConstraint -mo -weight 1;

import pymel.core as pm
pm.pointConstraint(mo=True);

maintainOffset(mo), weight(w)


# Pole Vector Constraint
poleVectorConstraint -weight 1;

import pymel.core as pm
mel_line = 'poleVectorConstraint'
pm.mel.eval(mel_line)

weight(w)

# How does this constraint differ from the previous three.
In order for this icon to be created you need a rotate-plane and an
ikHandle and the joint stays facing the icon.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
import pymel.core as pymel
selected = pm.ls(selection=True)
first selected = selected[0]

print 'First Selected Object:', first selected

# Create Separator Attribute
import pymel.core as pymel
selected = pm.ls(selection=True)
first_selected = selected[0]

print 'First Selected Object:', first_selected

first_selected.tx.set[0]
first_selected.ty.set[0]
first_selected.tz.set[0]

first_selected.t.set([0, 0, 0])

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
first_selected.addAttr('FINGERS', at='enum', en="---------------:", keyable=True)
first_selected.FINGERS.set(lock=True)
first_selected.addAttr('CURLS', at='enum', en="---------------:", keyable=True)
first_selected.CURLS.set(lock=True)

first_selected.addAttr('index_curl', keyable=True)
first_selected.addAttr('middle_curl', keyable=True)
first_selected.addAttr('pinky_curl', keyable=True)

first_selected.addAttr('SPREAD', at='enum', en="---------------:", keyable=True)
first_selected.SPREAD.set(lock=True)

first_selected.addAttr('index_spread', keyable=True)
first_selected.addAttr('middle_spread', keyable=True)
first_selected.addAttr('pinky_spread', keyable=True)

first_selected.addAttr('THUMB', at='enum', en="---------------:", keyable=True)
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
Combind
Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot
'''
