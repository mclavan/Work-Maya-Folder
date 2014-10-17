'''
Research Notes

Jovanny Zapata

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

Command, whatIs

pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

t=Translate r=Rotate s=scale n=normal pn=preserveNormals

# Delete History
delete -ch;

Command, whatIs	

pm.delete(ch=True)

-ch=constructionHistory
# Center Pivot
xform -cp;

Command, whatIs

pm.xform(cp=True)

cp= center Pivot
# Single Chain and Rotate Plan IKs
ikHandle;

Command, whatIs

pm.ikHandle(solver='ikSCsolver')

ikHandle -solver ikRPsolver;

Command, whatIs

pm.ikHandle(solver='ikRPsolver')

solver='ikRPsolver' solver='ikSCsolver'
# Cluster
newCluster -envelope 1;

mel procedure, whatIs

pm.cluster(envelope=True)

# Grouping (Does not need to be included on Shelf!)
Group;

Run time command, whatIs

pm.group(em=True)

Em=empty, Name=

# Parenting (Does not need to be included on Shelf!)
parent;

command, whatIs

pm.parent()

w=parent to world r= preserve existing local object transformations

# Duplicating (Does not need to be included on Shelf!)
duplicate -smartTransform;

command, whatIs

pm.duplicate(st=True)

-smartTransform= st

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 8 -ch 1;

command, whatIs

pm.circle()

c= center , r= radius

# Square
curve -d 1 -p 16 0 16 -p -16 0 16 -p -16 0 -16 -p 16 0 -16 -p 16 0 16 -k 0 -k 1 -k 2 -k 3 -k 4 ;

command, whatIs

mel_line = 'curve -d 1 -p 16 0 16 -p -16 0 16 -p -16 0 -16 -p 16 0 -16 -p 16 0 16 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)

# Cube
curve -d 1 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 ;
 
command, whatIs

mel_line = 'curve -d 1 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 ;'
pm.mel.eval(mel_line)


# Arrow
curve -d 1 -p 64 0 0 -p 0 0 -32 -p 0 0 -16 -p -48 0 -16 -p -48 0 16 -p 0 0 16 -p 0 0 32 -p 64 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;

command, whatIs

mel_line = 'curve -d 1 -p 64 0 0 -p 0 0 -32 -p 0 0 -16 -p -48 0 -16 -p -48 0 16 -p 0 0 16 -p 0 0 32 -p 64 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)

'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
parentConstraint -mo -weight 1;

command, whatIs

pm.parentConstraint()

-mo=maintainOffset, w=Weight
# Orient Constraint
orientConstraint -mo -weight 1;

command, whatIs

pm.orientConstraint()

-mo=maintainOffset, w=Weight
# Point Constraint
pointConstraint -offset 0 0 0 -weight 1;

command, whatIs

pm.pointConstraint()

o=offset, w=weight
# Pole Vector Constraint
# How does this constraint differ from the previous three.
poleVectorConstraint -weight 1;

command, whatIs

pm.poleVectorConstraint()

w=Weight

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
addAttr -ln"" -at double; 

command, whatIs

pm.addAttr(attributeType=double)

ln=LongName

# Create Separator Attribute
selected = pm.select()
addAttr -ln "FINGER"  -at "enum" -en "-------:"  |selected;
setAttr -e-keyable true |selected.Finga;

command,whatIs for both addAttr and setAttr

pm.addAttr(ln='', attributeType= "", enumName="")
pm.setAttr(k=True)

-ln=LongName, -at=attributeType, -en=enumName -e-keyable=keyable=k

# Template Attributes 
# Create a group of attributes at one time.  
# The finger attributes are an example.

addAttr -ln "FINGER"  -at "enum" -en "------:"  |select;
setAttr -e-keyable true |select.FINGER;
setAttr -lock true "select.FINGER";
addAttr -ln "CURL"  -at "enum" -en "-------:"  |select;
setAttr -e-keyable true |select.CURL;
setAttr -lock true "select.CURL";
addAttr -ln "Finger_Curl"  -at double  |select;
setAttr -e-keyable true |select.Finger_Curl;

command, whatIs

selected = pm.select()
pm.addAttr(ln="",attributeType="enum",en="------")
pm.setAttr(k=True, select)
pm.setAttr(k=True, select.FINGER)
pm.setAttr(lock=True, 'select.FINGER')
pm.addAttr(ln='CURL', at= 'enum', en='-------:', select)
pm.setAttr(keyable=true, select.CURL)
pm.addAttr(ln='Finger_Curl', at=double, select)
pm.setAttr(keyable=True, select.Finger_Curl)

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


