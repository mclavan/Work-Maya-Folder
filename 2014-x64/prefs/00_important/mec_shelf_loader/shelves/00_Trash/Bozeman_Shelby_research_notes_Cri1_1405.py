'''
Research Notes

Shelby Bozeman


Current Shelf Tools: Hide & Lock, Undo Hide & Lock, FreezeTransformations, Center Pivot, Delete History, 
Red, Blue & Yellow Color Changes,Snap Tool, Renamer tool, Priming tool, Create Empty Group, 
Circle, Square, Cube, Arrow,
Parent Constraint, Orient Constraint, Point Constraint.

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
# Mel Command: FreezeTransformations;
# performFreezeTransformations(0);
# makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
pm.makeidentity(apply = True [-t 1 -r 1 -s 1 -n 0 -pn 1;])

# Delete History
# Mel Command : DeleteHistory; 
# delete -ch;
# Looked up python command 
pm.delete(ch = True)

# Center Pivot
# Mel Command : CenterPivot;
# xform -cp;
# editMenuUpdate MayaWindow|mainEditMenu; 
pm.xform(cp = True)

# Single Chain and Rotate Plan IKs
#Reserched and found in Maya Help
# SC
# MEl Command : ikHandle -p 0;
pm.ikHandle(p = True, sj = joint1, ee=joint3)
#Rp
# Mel Command : ikHandle -p 0 -sol ikRPsolver;
pm.ikHandle(p = 0, sj=joint1, ee=joint3, sol= ikRPsolver;)


# Cluster
# Found under Create Deformation
# Mel Command: CreateCluster;
# performCluster false;
# newCluster " -envelope 1";
pm.cluster(em =1)

# Grouping (Does not need to be included on Shelf!)
# Mel Command : CreateEmptyGroup;
# group -empty;
# Found in Maya Help Ref
pm.group(em=True)

# Parenting (Does not need to be included on Shelf!)
# Found under Constraint - Looked up in Maya Help Ref
# Mel Command : parent;
#performParent false;
pm.parent('Ct_control_icon_01', 'Ct_control_icon_02', relative=True)

# Duplicating (Does not need to be included on Shelf!)
# Can be done ( Command + D) Found in Maya Ref.
# Mel Command : duplicate -rr;
pm.duplicate(rr=True)

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
# Found in Maya Ref, Create under Curves Tab.
# Mel Command : CreateNURBSCircle;
# circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;
pm.circle(c= [0, 0, 0], nr= [0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1)

# Square
# curve -d 1 -p -0.5 0 0.5 -p -0.5 0 -0.5 -p 0.5 0 -0.5 -p 0.5 0 0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;
mel_line ='curve -d 1 -p -0.5 0 0.5 -p -0.5 0 -0.5 -p 0.5 0 -0.5 -p 0.5 0 0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)


# Cube
# curve -d 1 -p -0.5 1.053916 0.5 -p 0.5 1.053916 0.5 -p 0.5 0.0539161 0.5 -p -0.5 0.0539161 0.5 -p -0.5 1.053916 0.5 -p -0.5 1.053916 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 0.0539161 0.5 -p 0.5 0.0539161 0.5 -p 0.5 0.0539161 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 1.053916 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 0.0539161 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 1.053916 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;
mel_line ='curve -d 1 -p -0.5 1.053916 0.5 -p 0.5 1.053916 0.5 -p 0.5 0.0539161 0.5 -p -0.5 0.0539161 0.5 -p -0.5 1.053916 0.5 -p -0.5 1.053916 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 0.0539161 0.5 -p 0.5 0.0539161 0.5 -p 0.5 0.0539161 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 1.053916 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 0.0539161 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 1.053916 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
pm.mel.eval(mel_line)


# Arrow
# curve -d 1 -p 4 0 3 -p 5 0 3 -p 5 0 1 -p 6 0 1 -p 4.444444 0 -0.952381 -p 3 0 1 -p 4 0 1 -p 4 0 3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
mel_line ='curve -d 1 -p 4 0 3 -p 5 0 3 -p 5 0 1 -p 6 0 1 -p 4.444444 0 -0.952381 -p 3 0 1 -p 4 0 1 -p 4 0 3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
# I created a parent constraint under Constrain tab in maya
# doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
# Mel Command : parentConstraint -mo -weight 1;
pm.parentConstraint(mo=True, weight=1)

# Orient Constraint
# I Created a orient constraint in maya under constrain tab.
# doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
# Mel Command : orientConstraint -offset 0 0 0 -weight 1;
pm.orientConstraint(offset=[0, 0, 0], weight=1)

# Point Constraint
# Created in Maya under constrains, found in Maya Ref.
# doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
# Mel Command : pointConstraint -offset 0 0 0 -weight 1;
pm.pointConstraint(offset=[0, 0, 0], weight=1)

# Pole Vector Constraint
# Located in constrain tab, found in maya ref.
# This constrain is different because it can only be applied to a IK source in order to control it.
# Mel Command : poleVectorConstraint -weight 1;
pm.poleVectorConstraint(weight=1)


'''
Attributes (Covered in Podcast)
'''
# Create float attribute
# Found under Att Editor > Edit > Add Att.
# Mel Command : addAttr -ln "Float_Att"  -at double  |curve2;
# setAttr -e-keyable true |curve2.Float_Att;
pm.addAttr(ln= name, at=double)
pm.setAttr(name, keyable=True)

# Create Separator Attribute
# Att Editor > Edit > Add Att. > Enum
# Mel Command : addAttr -ln "______"  -at "enum" -en "________:"  |curve3;
# setAttr -e-keyable true |curve3.______;
pm.addAttr(ln= ______, at= 'enum', en=________)
pm.setAttr(name, keyable=True)

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.
pm.addAttr(ln= name, at=double)
pm.setAttr(object1 , keyable=True)

pm.addAttr(ln= name, at=double)
pm.setAttr(object2, keyable=True)

pm.addAttr(ln= name, at=double)
pm.setAttr(object3, keyable=True)

'''
Proxy (Extra)
Modeling commands can be difficult to use.  In creating a proxy toolset, 
	we don't need to use them as a part of a bigger process.  
	I typically use the Run Time Commands in this case.

Research:

'''

Detach Component
Separate
# Found under Mesh > Seperate
# Mel Command : performPolyShellSeparate;
# polySeparate -ch 1 polySurfaceShape1;
pm.polySeparate(ch=1, polySurfaceShape1)
#parent -relative polySurface2 polySurface1 ;
pm.parent(relative=True, polySurface2, polySurface1)

Extract

Combind
# Found under Mesh > Combind , Maya Ref.
# Mel Command : CombinePolygons;
# polyPerformAction polyUnite o 0;
# polyUnite -ch 1 -mergeUVSets 1 pCube2 pCube1;
pm.polyUnite(ch=1, mergeUVSets=1, pCube1, pCube2)
# parent -relative transform1 pCube1 ;
pm.parent(relative=True, transform=1, pCube1)

Nuke - (3 in one button) Delete History, Freeze Transforms, and Center Pivot



