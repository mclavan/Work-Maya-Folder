'''
Research Notes

kailee batchelder

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
# editMenuUpdate Maya Window/ EditMenu; 
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
# mec: CreateCluster;
# performCluster false;
# newCluster " -envelope 1";
pm.cluster(em =1)

# Grouping (Does not need to be included on Shelf!)
# Mel Command : CreateEmptyGroup;
# group -empty;
# Found in Maya Help Ref
pm.group(em=True)


# Parenting (Does not need to be included on Shelf!)
# this was in Constraint -  in Maya Help 
# Mel Command : parent;
#performParent false;
pm.parent('Ct_control_icon_01', 'Ct_control_icon_02', relative=True)

# Duplicating (Does not need to be included on Shelf!)
# this cant be done -  in Maya help
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
# mel command : CreateNURBSCircle;
# circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;
pm.circle(c= [0, 0, 0], nr= [0, 1, 0], sw=360, r=1, d=3, ut=0, tol=0, s=8, ch=1)

# Square
# curve -d 1 -p -0.5 0 0.5 -p -0.5 0 -0.5 -p 0.5 0 -0.5 -p 0.5 0 0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;
mel_line ='curve -d 1 -p -0.5 0 0.5 -p -0.5 0 -0.5 -p 0.5 0 -0.5 -p 0.5 0 0.5 -p -0.5 0 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)


# Cube
# curve -d 1 -p -0.5 1.053916 0.5 -p 0.5 1.053916 0.5 -p 0.5 0.0539161 0.5 -p -0.5 0.0539161 0.5 -p -0.5 1.053916 0.5 -p -0.5 1.053916 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 0.0539161 0.5 -p 0.5 0.0539161 0.5 -p 0.5 0.0539161 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 1.053916 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 0.0539161 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 1.053916 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;

# Arrow
'curve -d 1 -p -0.5 1.053916 0.5 -p 0.5 1.053916 0.5 -p 0.5 0.0539161 0.5 -p -0.5 0.0539161 0.5 -p -0.5 1.053916 0.5 -p -0.5 1.053916 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 0.0539161 0.5 -p 0.5 0.0539161 0.5 -p 0.5 0.0539161 -0.5 -p -0.5 0.0539161 -0.5 -p -0.5 1.053916 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 0.0539161 -0.5 -p 0.5 1.053916 -0.5 -p 0.5 1.053916 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
# doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
# Mel Command : parentConstraint -mo -weight 1;
pm.parentConstraint(mo=True, weight=1)

# Orient Constraint
# doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
# Mel Command : orientConstraint -offset 0 0 0 -weight 1;
pm.orientConstraint(offset=[0, 0, 0], weight=1)

# Point Constraint
# doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
# Mel Command : pointConstraint -offset 0 0 0 -weight 1;
pm.pointConstraint(offset=[0, 0, 0], weight=1)

# Pole Vector Constraint
# This is different because it can only be put on  an IK handle to make it run.
# Mel Command : poleVectorConstraint -weight 1;
pm.poleVectorConstraint(weight=1)

# How does this constraint differ from the previous three.
# This is different because it can only be put on  an IK handle to make it run.
# Mel Command : poleVectorConstraint -weight 1;
pm.poleVectorConstraint(weight=1)

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
# Found under Att Editor > Edit > Add Att.

# mel command : addAttr -ln "Float_Att"  -at double  |curve2;

# setAttr -e-keyable true |curve2.Float_Att;

pm.addAttr(ln= name, at=double)


pm.setAttr(name, keyable=True)

# Create Separator Attribute

# Att Editor > Edit > Add Att. > Enum

# Mel Command : addAttr -ln "______"  -at "enum" -en "________:"  

|curve3;

# setAttr -e-keyable true |curve3.______;

pm.addAttr(ln= ______, at= 'enum', en=________)

pm.setAttr(name, keyable=True)


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


