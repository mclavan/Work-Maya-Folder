'''
Michael Clavan
lecture6.py

Description:
	Lecture 6 Notes

How to Run:
import lecture6
reload(lecture6)

lecture6.prime_selected()

'''
print 'Lecture 6'

import pymel.core as pm

'''
Creaate a function for padding tool. 
Functions should be descriptive. Verbs. 

create_pad
padding_tool
padding_system

prime_tool
prime_selected

rename_joints
joint_renamer
'''



def hiearchy():
	pass

def joint_rename():
	pass

def padding_tool():
	pass

def prime_multiple():

	selected_joints = pm.ls(selection=True)

	for current_joint in selected_joints:
		pm.select(current_joint, replace=True)
		prime_selected()

	'''
	pm.select(selected_joints[1], replace=True)	
	prime_selected()

	pm.select(selected_joints[2], replace=True)	
	prime_selected()
	'''

def prime_selected():
	'''
	Locally orients a control based upon a 
		target joint or transform.
	Instructions:
		Select a given root joint. 
	'''

	'''
	Given
	'''
	# Get selected joint
	root_joint = pm.ls(selection=True)[0]
	# root_joint = 'joint1'

	print 'Selected:', root_joint

	'''
	Process
	'''
	'''
	Naming Area
	'''
	# lt_arm_01_bind == lt_arm_01_icon
	control_icon_name = root_joint.replace('_bind', '_icon')
	# lt_arm_01_prime
	prime_name = root_joint.replace('_bind', '_prime')
	# lt_arm_01_pad2
	pad_name = root_joint.replace('_bind', '_pad2')

	# Make a control icon.
	# # Result: [nt.Transform(u'nurbsCircle2'), nt.MakeNurbCircle(u'makeNurbCircle2')] # 
	control_icon = pm.circle(normal=[1, 0, 0], name=control_icon_name)[0]
	# control_icon.rename(control_icon_name)
	# Cube icons

	# mel_line = 'curve -d 1 -p 0.970694 0.970694 0.970694 -p 0.970694 -0.970694 0.970694 -p -0.970694 -0.970694 0.970694 -p -0.970694 0.970694 0.970694 -p 0.970694 0.970694 0.970694 -p 0.970694 0.970694 -0.970694 -p 0.970694 -0.970694 -0.970694 -p 0.970694 -0.970694 0.970694 -p 0.970694 -0.970694 -0.970694 -p -0.970694 -0.970694 -0.970694 -p -0.970694 0.970694 -0.970694 -p 0.970694 0.970694 -0.970694 -p -0.970694 0.970694 -0.970694 -p -0.970694 0.970694 0.970694 -p -0.970694 -0.970694 0.970694 -p -0.970694 -0.970694 -0.970694 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;'
	# control_icon = pm.mel.eval(mel_line)
	print 'Control Icon Created:', control_icon
	
	# Group control icon
	pad_group = pm.group(control_icon)
	prime_group = pm.group(pad_group)

	print 'Top Group Created:', prime_group
	print '2nd pad Created:', pad_group

	# Snap to target joint. Parent Constraint
	temp_constraint = pm.parentConstraint(root_joint, prime_group)
	
	# Delete constraint
	pm.delete(temp_constraint)

	# Option
	# orient constrain it to the joint
	pm.orientConstraint(control_icon, root_joint)


	'''
	Output
	'''
	print 'Locally oriented control created.'



