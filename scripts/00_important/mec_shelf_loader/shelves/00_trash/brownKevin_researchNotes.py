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
	# Freezes currently selected objects.
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

	# Freezes selected objects stated.
	pm.makeIdentity(bat_grp, apply=True, t=1, r=1, s=1, n=0)


# Delete History
def delete_history():
	'''
	import research_notes
	reload(research_notes)
	research_notes.delete_history()
	'''

	# Delete Command deletes objects in 3D space.
	#	The ch flag is for deleting construction history.
	pm.delete(ch=True)

	print 'History has been deleted on all selected objects.'

# Center Pivot
	CenterPivot;


# Single Chain and Rotate Plan IKs
	'''
	Get selected
	'''
	selected_joints = pm.ls(selection=True)
	print 'Selected Joints:', selected_joints

	# Get the root joint.
	root_joint = selected_joints[0]

	# Get the hierarchy
	leg_system = pm.ls(root_joint, dag=True)
	print 'Leg System:', leg_system

	ankle_joint = leg_system[2]
	ball_joint = leg_system[3]
	toe_joint = leg_system[4]
	# Research creating IKs.
	# RPIK ikHandle -sol ikRPsolver;
	# cmds.ikHandle( startJoint='joint1', endEffector='joint5', p=2, w=.5 )
	leg_ik = pm.ikHandle(startJoint=root_joint, endEffector=ankle_joint, sol='ikRPsolver')[0]
	print 'Leg IK', leg_ik
	# SCIK ikHandle;
	pm.ikHandle(startJoint=ankle_joint, endEffector=ball_joint)
	pm.ikHandle(startJoint=ball_joint, endEffector=toe_joint)

# Cluster
pm.cluster()

# Grouping (Does not need to be included on Shelf!)
	pm.group()

	# ----- Flags -----
	name(n) = name the group.
	empty(e) = Creates an empty group.

	# Grouping by default parents selected objects in the scene.
	# In this exaple son would be the top node.
	pm.group(name='grandFather')
	pm.group(name='father')
	pm.group(name='son')

	# Empty groups can be created too.
	pm.group(name='grandFather', empty=True)
	pm.group(name='father', empty=True)
	pm.group(name='son', empty=True)


# Parenting (Does not need to be included on Shelf!)

# Duplicating (Does not need to be included on Shelf!)

# Unlocking and Showing attributes
def unlock_and_show():
	'''
	unlock and make keyable all channels of the selected object.

	research_notes
	research_notes.unlock_and_show()

	'''

	selected = pm.ls(selection=True)
	first_selected = selected[0]

	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)


	print 'First selected object has all channels shown.'

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''
# Circle
	pm.circle()
	# Control is facing the y-axis. Good for FK back controls. World oriented.
	pm.circle(normal=[0, 1, 0])
	# Control is facing the x-axis. Good for local oriented conrols.
	pm.circle(normal=[1, 0, 0])

	# ----- Flags -----
	normal = Direction of control.
	radius = Size of the control
	sections = How many sections the conrols has.

# Square
	
	pm.circle(normal=[0, 1, 0], degree=1, sections=4)
# The curve command creates cv curces. The curve command below will create an arc
import pymel.core as pm
mel_line = 'curve -d 1 -p 1.25 0 -1.25 -p -1.25 0 -1.25 -p -1.25 0 1.25 -p 1.25 0 1.25 -p 1.25 0 -1.25 -k 0 -k 1 -k 2 -k 3 -k 4 ;'
pm.mel.eval(mel_line)




# Cube
mel_line = 'curve -d 1 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
pm.mel.eval(mel_line)

# Arrow
mel_line = 'curve -d 1 -p 0 0 -0.625 -p 0.625 0 0 -p 0.296799 0 0 -p 0.296799 0 1.253716 -p -0.323347 0 1.253716 -p -0.323347 0 0.0134231 -p -0.625 0 0 -p 0 0 -0.625 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;'
pm.mel.eval(mel_line)


'''
Constraints
- Remember to test offset on and off with these commands.
'''
# Parent Constraint
# Parent constraint defaults to maintain offset is off by default (snapping)
pm.parentConstraint('driver, driven')
# Maintail offsest
parentConstraint -mo -weight 1;

# Orient Constraint
# Orient Constrains selected.
pm.orientConstraint

# Orient Constrains stated objects.
pm.orientConstraint(control_icon_3, third_joint)

# Point Constraint
pointConstraint;
pm.pointConstraint()

# Pole Vector Constraint
# How does this constraint differ from the previous three.

'''
Attributes (Convered in Podcast)
'''
# Create float attribute
selected = pm.ls(selection=True)
first_selected = selected[0]

attribute_name = raw_input()
first_selected.addAttr(attribute_name, keyable=True)


# Create Separator Attribute
attribute_name = raw_input()
first_selected.addAttr(attribute_name, at='enum', en='---------------:', keyable=True)
attribute = first_selected.attr(attribute_name)
attribute.set(lock=True)

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


