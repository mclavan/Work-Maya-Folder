'''
clavanMichael_riggingTools_cri1401.py
Michael Clavan

Description:
	Rigging Toolset
	This script included contains a variety of
		different tools.

How to Run:

import clavanMichael_riggingTools_cri1401
reload(clavanMichael_riggingTools_cri1401)

'''

import pymel.core as pm

print 'Toolset Active.'


def hierarchy():
	'''
	Creates a based upon a given hierarchy. 

	Select the root joint then run the function. 

	import clavanMichael_riggingTools_cri1401
	reload(clavanMichael_riggingTools_cri1401)
	clavanMichael_riggingTools_cri1401.hierarchy()
	'''

	# Input
	joint_system = pm.ls(selection=True, dag=True)
	joint_1 = joint_system[0]
	joint_2 = joint_system[1]
	joint_3	= joint_system[2]

	print 'First Joint:', joint_1
	print 'Joint Chain:', joint_system

	# Process

	'''
	Pad Root Joint 
	'''

	'''
	Prime finger joints. 
	'''
	'''
	Digit 1
	'''
	# Create control icon 
	control_icon_1 = pm.circle(normal=[1, 0, 0])[0]
	# Group conrol icon
	pad_1 = pm.group()

	# Snap group to first joint 
	temp_constraint = pm.parentConstraint(joint_1, pad_1)
	# Delete constraint used for snapping.
	pm.delete(temp_constraint)

	# Delete History on Control

	# Lock and Hide tx, ty, tz, sx, sy, sz, v
	# control_icon_1.tx.set()

	# Orient constraint 
	pm.orientConstraint(control_icon_1, joint_1)

	'''
	Digit 2
	'''
	control_icon_2 = pm.circle(normal=[1, 0, 0])[0]
	# Group conrol icon
	pad_2 = pm.group()

	'''
	Digit 3
	'''
	control_icon_3 = pm.circle(normal=[1, 0, 0])[0]
	# Group conrol icon
	pad_3 = pm.group()

	'''
	Parenting Area
	'''
	pm.parent(pad_3, control_icon_2)
	pm.parent(pad_2, control_icon_1)


	# Output
	print 'Hierarchy has been created.'









"""
def padding():
	'''

	'''

	print 'Selected has been padded.'

def priming():
	'''

	'''

	print 'Selected now has a local control.'

def renaming_joints():
	'''

	'''

	print 'Selected joint chain has been renamed.'

"""

def IKFK_system():

	# Get selected joints
	binding_joint_system = pm.ls(selection=True, dag=True)

	import pymel.core as pm
	fk_root = pm.duplicate()
	ik_root = pm.duplicate()
	fk_system = pm.ls(fk_root, dag=True)
	ik_system = pm.ls(ik_root, dag=True)

	'''
	IK Area
	'''

	# Create controls for the elbow (pointer) and wrist (cube)

	# Snap controls to elbow and wrist

	# Create IK from 1st joint to 3rd joint

	# Parent IK hand to wrist icon. 


	'''
	FK Area
	'''


	'''
	IKFK Switch (adv)
	'''



def reset_override():
	geometry = pm.ls(selection=True, dag=True, type='transforms')

	for current_geometry in geometry:
		# Turn back to normal (instead or reference or template)
		current_geometry.overrideDisplayType(0)
		# Turn off override enabled.
		current_geometry.overrideEnabled.set(0)



def proxy_reset():

	proxy_geometry = pm.ls('*_proxy')

	for current_proxy in proxy_geometry:
		pm.delete(current_proxy, constraints=True)


def color_icons():

	# Define what I am working on.
	# lt control
	left_icons = pm.ls('lt_*_icon')
	center_icons = pm.ls('ct_*_icon')
	right_icon = pm.ls('rt_*_icon')

	for current_icon in left_icons:
		current_icon.overrideEnabled.set(1)
		current_icon.overrideColor.set(6)

	for current_icon in right_icons:
		current_icon.overrideEnabled.set(1)
		current_icon.overrideColor.set(13)


def renaming_controls():
	pass 

def create_finger_attributes():
	pass

def reference_off():
	'''
	Turns reference mode and override enabled 
		off on selected.
	'''
	pass



