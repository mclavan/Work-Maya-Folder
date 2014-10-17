'''
Ali Fossell
research_notes_final

How to run:
	import research_notes_final
	reload(research_notes_final)
	research_notes_final.tool_name
	
Buttons will run left to right in this order on shelf
'''

# General Tools

def freeze_transformations():
	'''
	Freeze Tansformations
	Freezes movement transformations on the selected object(s)
	'''
	MEL Version (Command)
		makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
		'''
	Flags
		t=transformations
		r=rotate
		s=scale
		n=normals
			- freezes normals
		pn=preserve normals
			- reverses normals if negative
		'''
	
	import pymel.core as pm
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

def delete_history():
	'''
	Delete History
	Deletes history on the selected object(s)
	'''

	MEL Version (Run Time Command, Command, MEL Script)
		DeleteHistory;
		delete -ch;
		editMenuUpdate MayaWindow|mainEditMenu;
	'''
	Flags
		ch=construction history
	'''

	pm.delete(ch=True)

def center_pivot():
	'''
	Center Pivot
	Centers the movement pivot on the selected object(s)
	'''

	MEL Version (Run Time Command, Command, MEL Script)
		CenterPivot;
		xform -cp;
		editMenuUpdate MayaWindow|mainEditMenu;
	'''
	Flags
		cp=center pivot
	'''

	pm.xform(cp=True)

def single_chain_ik():
	'''
	Single Chain ik
	Creates a single chain ik on the selected joints
	'''
	MEL Version (Run Time Command)
		IKHandleTool

	pm.mel.IKHandleTool()

def cluster():
	'''
	Create cluster
	creates a cluster on the selected joint
	'''

	MEL Version (Run Time Command)
		CreateCluster
	

	pm.mel.CreateCluster()

def create_empty_group():
	'''
	Create Empty Group
	Creates an empty group node on the middle of the grid
	'''

	MEL Version (MEL Script)
		doGroup 0 1 1
	

	import pymel.core as pm
	pm.group(empty=True)


# Control Icons

def create_circle():
	'''
	Create Circle Icon
	creates a NURBS circle shape flat on the grid
	'''

	MEL Version (command)
		circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1; objectMoveCommand;
	'''
	Flags
		c=center
		nr=normal
		sw=sweep
		r=radius
		d=degree
		ut=useTolerance
			- determines resolution if sections not specified
		tol=tolerance
			- determines resolution of circle. Only used if ut=True
		s=sections
		ch=constructionHistory

	'''

	pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, d=3, s=8)

def create_square():
	'''
	Create Square Icon
	creates a NURBS square shape
	'''
	MEL Version (Command)
		circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 1 -ut 0 -tol 0 -s 4 -ch 1; objectMoveCommand;
	'''
	Flags
		c=center
		nr=normal
		sw=sweep
		r=radius
		d=degree
		ut=useTolerance
			- determines resolution if sections not specified
		tol=tolerance
			- determines resolution of circle. Only used if ut=True
		s=sections
		ch=constructionHistory	
	'''

	pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, d=1, s=4)

def create_cube():
	'''
	Create Cube Icon
	'''
	MEL Version (Command)
		curve -d 1 -p 2.092617 -7.13867e-10 1.331443 -p 2.092617 3.075829 1.331443 -p 2.092617 3.075829 -1.867205 -p 2.092617 -7.13867e-10 -1.867205 -p 2.092617 -7.13867e-10 1.331443 -p -1.816699 -7.13867e-10 1.331443 -p -1.816699 3.075829 1.331443 -p 2.092617 3.075829 1.331443 -p -1.816699 3.075829 1.331443 -p -1.816699 3.075829 -1.867205 -p -1.816699 -7.13867e-10 -1.867205 -p -1.816699 -7.13867e-10 1.331443 -p -1.816699 -7.13867e-10 -1.867205 -p 2.092617 -7.13867e-10 -1.867205 -p 2.092617 3.075829 -1.867205 -p -1.816699 3.075829 -1.867205 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;
	'''
	Flags
		d=degree
		p=point
	'''

	pm.mel.eval(curve -d 1 -p 2.092617 -7.13867e-10 1.331443 -p 2.092617 3.075829 1.331443 -p 2.092617 3.075829 -1.867205 -p 2.092617 -7.13867e-10 -1.867205 -p 2.092617 -7.13867e-10 1.331443 -p -1.816699 -7.13867e-10 1.331443 -p -1.816699 3.075829 1.331443 -p 2.092617 3.075829 1.331443 -p -1.816699 3.075829 1.331443 -p -1.816699 3.075829 -1.867205 -p -1.816699 -7.13867e-10 -1.867205 -p -1.816699 -7.13867e-10 1.331443 -p -1.816699 -7.13867e-10 -1.867205 -p 2.092617 -7.13867e-10 -1.867205 -p 2.092617 3.075829 -1.867205 -p -1.816699 3.075829 -1.867205 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;)

def create_arrow():
	'''
	Create Arrow Icon
	creates a custom NURBS arrow
	'''
	MEL Version (Command)
		curve -d 1 -p 1 0 1 -p -1 0 1 -p -1 0 -2 -p -2 0 -2 -p 0 0 -4 -p 2 0 -2 -p 1 0 -2 -p 1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
	'''
	Flags
		d=degree
		p=point

	'''

	pm.mel.eval(curve -d 1 -p 1 0 1 -p -1 0 1 -p -1 0 -2 -p -2 0 -2 -p 0 0 -4 -p 2 0 -2 -p 1 0 -2 -p 1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;)


# Colors

def blue_color():
	'''
	Recolors Selected control icon to Blue
	'''
	MEL Version (Command, MEL Script, MEL Script)
		setAttr "nurbsCircleShape1.overrideEnabled" 1;
		changeObjColor nurbsCircleShape1.overrideColor MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdnurbsCurveFormLayout|scrollLayout2|columnLayout6|frameLayout46|columnLayout18|frameLayout51|columnLayout23|columnLayout25|objIndexColorSlider;
		updateLayerColor nurbsCircleShape1.overrideColor MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdnurbsCurveFormLayout|scrollLayout2|columnLayout6|frameLayout46|columnLayout18|frameLayout51|columnLayout23|columnLayout25|objIndexColorSlider;
	
	import pymel.core as pm

	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected:', first_selected

	first_selected.overrideEnabled.set(1)
	first_selected.overrideColor.set(6)

def yellow_color():
	'''
	Recolors Selected control icon to Yellow
	'''

	MEL Version (Command, MEL Script, MEL Script)
		setAttr "nurbsCircleShape1.overrideEnabled" 1;
		changeObjColor nurbsCircleShape1.overrideColor MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdnurbsCurveFormLayout|scrollLayout2|columnLayout17|frameLayout46|columnLayout18|frameLayout51|columnLayout23|columnLayout25|objIndexColorSlider;
		updateLayerColor nurbsCircleShape1.overrideColor MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdnurbsCurveFormLayout|scrollLayout2|columnLayout17|frameLayout46|columnLayout18|frameLayout51|columnLayout23|columnLayout25|objIndexColorSlider;
	
	import pymel.core as pm

	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected:', first_selected

	first_selected.overrideEnabled.set(1)
	first_selected.overrideColor.set(17)
	
def red_color():
	'''
	Recolors Selected control icon to Red
	'''

	MEL Version (Command, MEL Script, MEL Script)
		setAttr "nurbsCircleShape1.overrideEnabled" 1;
		changeObjColor nurbsCircleShape1.overrideColor MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdnurbsCurveFormLayout|scrollLayout2|columnLayout13|frameLayout46|columnLayout18|frameLayout51|columnLayout23|columnLayout25|objIndexColorSlider;
		updateLayerColor nurbsCircleShape1.overrideColor MayaWindow|MainAttributeEditorLayout|formLayout2|AEmenuBarLayout|AErootLayout|AEStackLayout|AErootLayoutPane|AEbaseFormLayout|AEcontrolFormLayout|AttrEdnurbsCurveFormLayout|scrollLayout2|columnLayout13|frameLayout46|columnLayout18|frameLayout51|columnLayout23|columnLayout25|objIndexColorSlider;
	
	import pymel.core as pm

	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected:', first_selected

	first_selected.overrideEnabled.set(1)
	first_selected.overrideColor.set(13)
	

# Constraints

def parent_constraint():
	'''
	Parent Constrain
	parent constraints the selected driver object to selected driven object 
	'''
	MEL Version (MEL Script, Command)
		doCreateParentConstraintArgList 1 { "1","0","0","0","0","0","0","1","","1" };
		parentConstraint -mo -weight 1;
	

	pm.parentConstraint()

def orient_constriant():
	'''
	Orient Constraint
	orient constaints the selected driver object to the selected driven object 
	'''
	MEL Version (MEL Script, Command)
		doCreateOrientConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
		orientConstraint -offset 0 0 0 -weight 1;
	

	pm.orientConstraint()

def point_constraint():
	'''
	Point Constrain
	point constaints the selected driven object to the selceted driver object \
	'''

	MEL Version (MEL Script, Command)
		doCreatePointConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
		pointConstraint -offset 0 0 0 -weight 1;
	

	pm.pointConstraint()


# Attributes

def lock_hide():
	'''
	Locks and Hides Attributes
		Scale and Visibility on the selcted object
	'''

	MEL Version
		setAttr -lock true -keyable false -channelBox false "curve1.sx";
		setAttr -lock true -keyable false -channelBox false "curve1.sy";
		setAttr -lock true -keyable false -channelBox false "curve1.sz";
		setAttr -lock true -keyable false -channelBox false "curve1.v";
	

	import pymel.core as pm
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	first_selected.sx.set(lock=True, keyable=False)
	first_selected.sy.set(lock=True, keyable=False)
	first_selected.sz.set(lock=True, keyable=False)
	first_selected.v.set(lock=True, keyable=False)

def unlock_show():
	'''
	Unlocks and Shows Attributes
		Scale and Visibility
	'''
	MEL Version

	
	import pymel.core as pm
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)

def create_float():
	'''
	Creates a Float Attribute
	'''

	MEL Version
		addAttr -ln "attribute"  -at double  |curve1;
		setAttr -e-keyable true |curve1.attribute;
	

	import pymel.core as pm
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	first_selected.addAttr(raw_input, keyable=True)

def create_seperator():
	'''
	Creates an Enum Attribute
	'''
	MEL Version
		addAttr -ln "attribute"  -at "enum" -en "--------------:"  |curve1;
		setAttr -e-keyable true |curve1.attribute;
	
	import pymel.core as pm
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected Object:', first_selected

	first_selected.addAttr(raw_input, at='enum', en='-------------------:', keyable=True, lock=True)







