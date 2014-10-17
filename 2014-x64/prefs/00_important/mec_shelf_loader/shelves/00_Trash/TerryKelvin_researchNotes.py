'''
Research Notes

Kelvin Terry 

Current Shelf Tools: ??
* Includes double click and drop down menu buttons.


# It is not required to have ether double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: ??

ikH 
parC 
oriC
poiC 


Drop Down Menus: ??

Markers

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
found from turning Echo all on
Run time command
Mel = FreezeTransformations;
performFreezeTransformations(0);
Flag = apply 
'''
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)



# Delete History
  '''
found from turning Echo all on
Run time command 
Mel = DeleteHistory;
delete -ch;
Flag = ch
'''

  pm.delete(ch=True)



# Center Pivot
  '''
Found from turning Echo all on
Run time command 
Mel = CenterPivot;
xform -cp;
Flags = cp
'''
pm.xform(cp=1)


# Single Chain and Rotate Plan IKs
 '''
found from command document
Maya command 
Mel = ikHandle
Flags = sj, ee, p, w, solver
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]

pm.ikHandle( sj=first_selected, ee=second_selected, p=1, w=1, solver='ikRPsolver' )


selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]

pm.ikHandle( sj=first_selected, ee=second_selected, p=1, w=1, solver='ikSCsolver' )

# Cluster
 '''
found from command document and echo all on 
Mel procedure command 
Mel = newCluster
Flags = no important flags 
'''
pm.cluster()

# Grouping (Does not need to be included on Shelf!)
 '''
found from ealrier class studies or help doc 
command = mel procedure 
Mel = doGroup 0 1 1;
Flags = selection, name 
'''
selected = pm.ls(selection=True)
pm.group(selected , name = '')
# Parenting (Does not need to be included on Shelf!)
 '''
found from earlier class studies or help doc
command = Maya command
Mel = parent
Flags = none 
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]

pm.parent(first_selected, second_selected) 

# Duplicating (Does not need to be included on Shelf!)
 '''
found from mel script 
command= Maya command 
Mel = duplicate 
Flags = none 
'''
pm.duplicate() 


'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
 '''
found from mel script
command = Maya command 
Mel = circle 
Flags = nr 
'''
pm.circle()

# Square
 '''
found from mel script
command = Maya command 
Mel = curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;
Flags = mel, eval 
'''
square='curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(square)
# Cube
 '''
found mel script
command = Maya command 
Mel = curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p -1 2 -1 -p 1 2 -1 -p 1 0 -1 -p 1 0 1 -p 1 2 1 -p 1 2 -1 -p -1 2 -1 -p -1 2 1 -p 1 2 1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p -1 2 -1 -p -1 2 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 ;
Flags = mel, eval 
'''
cube = 'curve -d 1 -p -1 0 -1 -p 1 0 -1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p -1 2 -1 -p 1 2 -1 -p 1 0 -1 -p 1 0 1 -p 1 2 1 -p 1 2 -1 -p -1 2 -1 -p -1 2 1 -p 1 2 1 -p 1 0 1 -p -1 0 1 -p -1 0 -1 -p -1 2 -1 -p -1 2 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 ;'
pm.mel.eval(cube)


# Arrow
 '''
found mel script
command = Maya command 
Mel = curve -d 1 -p 4 0 3 -p 2 0 1 -p 3 0 1 -p 3 0 -2 -p 5 0 -2 -p 5 0 1 -p 6 0 1 -p 4 0 3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
Flags = mel, eval 
'''
arrow = 'curve -d 1 -p 4 0 3 -p 2 0 1 -p 3 0 1 -p 3 0 -2 -p 5 0 -2 -p 5 0 1 -p 6 0 1 -p 4 0 3 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(arrow)



'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
 '''
found 
command = Maya command
Mel = parentConstraint 
Flags = mo 
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]

pm.parentConstraint(first_selected, second_selected, mo=True)

# Orient Constraint
 '''
found in mel script
command = Maya command
Mel = orientConstraint
Flags = mo
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]
pm.orientConstraint(first_selected, second_selected, mo=True)

# Point Constraint
 '''
found in mel script
command = Maya command
Mel = pointConstraint
Flags = mo
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]
pm.pointConstraint(first_selected, second_selected, mo=True)
# Pole Vector Constraint
# How does this constraint differ from the previous three.
 '''
found in mel script
command = Maya command
Mel = poleVectorConstraint
Flags = 
there is no maintain offset and needs to have ik selected for second selected 
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]
pm.poleVectorConstraint(first_selected, second_selected,)
'''
Attributes (Convered in Podcast)
'''
# Create float attribute
 '''
found 
command = Maya command
Mel = 
Flags = 
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
attribute_name = raw_input()
first_selected.addAttr(attribute_name,  keyable=True)

# Create Separator Attribute
 '''
found in mel script
command = Maya command
Mel = addAttr -ln "attName"  -at "enum" -en "----------:"  |curve2;
setAttr -e-keyable true |curve2.attName;

Flags = at, en, keyable, 
'''

selected = pm.ls(selection=True)
first_selected = selected[0]
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True,
	 at='enum' ,en="------------:")


# Template Attributes 
 '''
found in mel script
command = Maya command
Mel = addAttr -ln "attName"  -at double  |curve2;
setAttr -e-keyable true |curve2.attName;

Flags = at, keyable, 
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)


# Create a group of attributes at one time.  
# The finger attributes are an example.
 '''
found in mel script
command = Maya command
Mel = addAttr -ln "attName"  -at double  |curve2;
setAttr -e-keyable true |curve2.attName;

Flags = at, en, keyable, lock
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
first_selected.addAttr('FINGERS', keyable=True,
	 at='enum' ,en="------------:")
first_selected.FINGERS.set(lock=True)

selected = pm.ls(selection=True)
first_selected = selected[0]
first_selected.addAttr('CURL', keyable=True,
	 at='enum' ,en="------------:")
first_selected.CURL.set(lock=True)

first_selected.addAttr('indexCurl', keyable=True)
first_selected.addAttr('middleCurl', keyable=True)
first_selected.addAttr('pinkyCurl', keyable=True)

selected = pm.ls(selection=True)
first_selected = selected[0]
first_selected.addAttr('SPREAD', keyable=True,
	 at='enum' ,en="------------:")
first_selected.SPREAD.set(lock=True)

first_selected.addAttr('indexSpread', keyable=True)
first_selected.addAttr('middleSpread', keyable=True)
first_selected.addAttr('pinkySpread', keyable=True)

selected = pm.ls(selection=True)
first_selected = selected[0]
first_selected.addAttr('THUMB', keyable=True,
	 at='enum' ,en="------------:")
first_selected.THUMB.set(lock=True)

first_selected.addAttr('thumbCurl', keyable=True)
first_selected.addAttr('thumbDrop', keyable=True)



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


