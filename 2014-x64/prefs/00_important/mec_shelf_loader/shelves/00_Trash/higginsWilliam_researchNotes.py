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
'''
# Freeze Transforms
1) makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
2) This is a Maya command Found by: Modify>Freeze Transforms
3) pm.makeIdentity(apply=True, t = 1, r = 1, s = 1)
4) editMenuUpdate MayaWindow|mainEditMenu;

'''
'''
# Delete History
1) DeleteHistory;
2) This is a Maya command - Found by: Edit>Delete by type>History
3) pm.delete(ch=True)
4) editMenuUpdate MayaWindow|mainEditMenu;

'''
'''
# Center Pivot
1) xform -cp
2) This is a Maya command - Found by: Modify>Center Pivot
3) pm.xform(cp=True)
4) editMenuUpdate MayaWindow|mainEditMenu;

'''
'''

# Single Chain and Rotate Plan IKs
1) IKHandleTool
2) This is a Maya command - Found by Skeleton>IKHandleTool(options)
3)pm.mel.IKHandleTool
4)setToolTo ikHandleContext; editMenuUpdate MayaWindow|mainEditMenu; changeToolIcon; dR_contextChanged; currentCtx;
'''
'''
# Cluster
1)cluster -rel
2) This is a Maya command - Found by Create Deformations>Cluster
3)cmds.cluster(rel=True)
4) refreshAE; autoUpdateAttrEd; updateAnimLayerEditor("AnimLayerTab"); if (!`exists polyNormalSizeMenuUpdate`) {source buildDisplayMenu;} polyNormalSizeMenuUpdate;
statusLineUpdateInputField; dR_updateCounter; dR_updateSymButton; ikSelectionChanged("MayaWindow|mainKeysMenu|menuItem1115|ikFKStateItem");
editMenuUpdate MayaWindow|mainEditMenu; dR_updateCommandPanel;


'''
'''
# Grouping (Does not need to be included on Shelf!)
1) group
2) This is a Maya command - Found by Edit>Group
3) cmds.group()
4) autoUpdateAttrEd; updateAnimLayerEditor("AnimLayerTab"); if (!`exists polyNormalSizeMenuUpdate`) {source buildDisplayMenu;} polyNormalSizeMenuUpdate; statusLineUpdateInputField;
dR_updateCounter; dR_updateSymButton; ikSelectionChanged("MayaWindow|mainKeysMenu|menuItem1115|ikFKStateItem"); dR_updateCommandPanel;
'''
'''
# Parenting (Does not need to be included on Shelf!)
1) Parent
2) This is a Maya command - Shortkey 'P'
3) cmds.parent()
4) statusLineUpdateInputField; dR_updateCounter; dR_updateSymButton; ikSelectionChanged("MayaWindow|mainKeysMenu|menuItem1115|ikFKStateItem");
dR_updateCommandPanel;
'''
'''
# Duplicating (Does not need to be included on Shelf!)
1) duplicate
2) Shortkey 'Command>"D"'
3) cmds.duplicate()
4) statusLineUpdateInputField; dR_updateCounter; dR_updateSymButton; ikSelectionChanged("MayaWindow|mainKeysMenu|menuItem1115|ikFKStateItem");
dR_updateCommandPanel;
'''

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
'''
# Circle
1) circle
2) Maya Command - Create>Nurbs>Circle
3) pm.circle()
4) dR_updateCounter; dR_updateSymButton; ikSelectionChanged("MayaWindow|mainKeysMenu|menuItem1115|ikFKStateItem");
editMenuUpdate MayaWindow|mainEditMenu; dR_updateCommandPanel;
'''
'''
# Square
1) CreateNURBSSquare
2) Maya Command - Create>Nurbs>Square
3) cmds.nurbsSquare()
4) MayaWindow|mainEditMenu; dR_contextChanged; currentCtx;
'''
'''
# Cube
1) CreateNURBSCube
2) Maya Command - Create>Nurbs>Cube
3) cmds.nurbsCube()
4)  

'''
'''
# Arrow
1) curve -d 1 -p -1 0 2 -p 1 0 2 -p 1 0 0 -p 1 0 -1 -p 2 0 -1 -p 0 0 -3 -p -2 0 -1 -p -1 0 -1 -p -1 0 2 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 ;
2) Maya Command - Create>CV Curve Tool
3) cmds.curve(Per=True [p = (-1, 0, 2,) (1, 0, 2,) (1, 0, 0) (1, 0, -1,) (2, 0, -1) (0, 0, -3) (-2, 0, -1) (-1, 0, -1) (-1, 0, 2)] k=[0,1,2,3,4,5,6,7,8])
4) CompleteCurrentTool; ctxCompletion; inViewMessage -cl midCenter;
'''
'''
Constraints
- Remember to test offset on and off with these commands.
'''
'''
# Parent Constraint
1) doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
2) Maya Command - Constrain>Parent
3) cmds.parentConstraint( 'shape1', 'shape2' )
4) Apparently none.
'''
'''
# Orient Constraint
1) doCreateOrientConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" }
2) Maya Command - Constrain>Orient
3) cmds.orientConstraint( 'shape1', 'shape2' )
4) Apparently none once more. These were the only results - orientConstraint -mo -weight 1; // Result: curve1_orientConstraint1 // 
'''
'''
# Point Constraint
1) doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
2) Maya Command - Constraint>Point
3) cmds.pointConstraint( 'shape1', 'shape2' )
4) Like before, these are the results. pointConstraint -offset 0 0 0 -weight 1; // Result: curve1_pointConstraint1 // 
'''
'''
# Pole Vector Constraint
1) poleVectorConstraint -weight 1;
2) Maya Command - Constrain>Pole Vector
3) cmds.poleVectorConstraint('numbersCircle1', 'ikhandle1')
4) This was literally the only result - // Result: ikHandle1_poleVectorConstraint1 // 
'''
'''
# How does this constraint differ from the previous three.
I noticed two things in particular. One, it required a Rotate Plane-Solver IK handle in order to work at all. Secondly, it only had the result where the flags would be.
The others had very few flags, but this one appeared to literally have zero. 
'''
'''
Attributes (Convered in Podcast)
'''
'''
# Create float attribute
1) addAttr -ln Test
2) Unsure, I googled it. Assumed to be a Maya command.
3) cmds.addAttr(longName=Test)
4) None were seen 
'''
'''
# Create Separator Attribute
1) separator
2) I googled it once again. Assumed to be a Maya command. 
3) cmds.separator()
4) None appeared when I ran the MEL in Maya
'''
'''
# Template Attributes 
1) editorTemplate
2) Assumed to be a Maya command.
3) import maya.cmds as cmds - cmds.editorTemplate
4) None appeared when I ran the MEL in Maya
'''
'''
# Create a group of attributes at one time.
1)addAttr -longName redBow -attributeType "float" -parent rainbow;
  addAttr -longName greenBow -attributeType "float" -parent rainbow;
  addAttr -longName blueBow -attributeType "float" -parent rainbow;
2) Maya command
3)cmds.addAttr(longName='rainbow', usedAsColor=True, attributeType='float3')
  cmds.addAttr(longName='redBow', attributeType='float', parent='rainbow')
  cmds.addAttr(longName='greenBow', attributeType='float', parent='rainbow')
4) attributeType; binaryTag; cachedInternally; dataType; defaultValue; enumName; exists; hasMaxValue; hasMinValue; 
hasSoftMaxValue; hasSoftMinValue; hidden; indexMatters; internalSet; keyable; longName; 

'''
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


