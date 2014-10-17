'''
Michael Clavan
lecture5.py

Description:
	- Introduction to Functions
	- Basic Hiearchy
	- Hierarchy
	- Selection

	- lastnameFirstname_hierarchy_cri_1311.py 
	- shelf_lastnameFirstname.mel
	- lastnameFirstname_research_cri_1311.py

How to Run:

import lecture5
reload(lecture5)

'''
print 'Lecture 5'

import pymel.core as pm

'''
def function_name():
	print 'Steps'
'''

def create_hierarchy():
	'''
	How do I use this function/tool???

	Examples:
	- Select the root joint.
	- Select joint followed by control icon. 
	'''

	'''
	Input / Given
	'''


	'''
	Process
	'''


	'''
	Output
	'''
	print 'Hierarchy created.'	

def build_rfl_ik_system():
	'''

	'''

	'''
	Given
	'''
	selected_items = pm.ls(selection=True)
	hip_joint = selected_items[0]
	# Knee is selected_items[1]	
	ankle_joint = selected_items[2]  
	ball_joint = selected_items[3]
	toe_joint = selected_items[4]

	'''
	Processing
	pm.ikHandle(solver='ikRPsolver')
	ex. 
	pm.ikHandle( startJoint='joint1', endEffector='joint5', solver='ikSCsolver'  )
	'''
	# Creating an RP IK handle hip to ankle joint
	pm.ikHandle(startJoint=hip_joint, endEffector=ankle_joint, solver='ikRPsolver')
	# Creating an SC Ik handle from ankle to ball
	pm.ikHandle(startJoint=ankle_joint, endEffector=ball_joint, solver='ikSCsolver')
	# Create SC IK from ball to toe
	pm.ikHandle(startJoint=ball_joint, endEffector=toe_joint, solver='ikSCsolver')



	'''
	Output
	'''
	print 'IK system built.'

def local_orientation_snap():
	'''
	Snap one object to another, with local orientation.
	'''
	'''
	Given
	Selected objects from the scene. 
	'''

	selected_items = pm.ls(selection=True)
	first_item = selected_items[0]
	second_item = selected_items[1]

	print 'First Selected:', first_item
	print 'Second Selected:', second_item
	print 'Second Object moved to the first object.'

	'''
	Process 
	'''
	# Snap second object to first
	temp_constraint = pm.parentConstraint(first_item, second_item, maintainOffset=False)

	# Delete constraint it is no longer needed.
	pm.delete(temp_constraint)


	'''
	Output
	'''
	print 'Objects Snapped.'


# Function required for joint renamer

# Function padding tool.

# Function priming tool.




