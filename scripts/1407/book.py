'''
Michael Clavan
book.py 

Description:
	Introduciton to Functions

How To Run:

import book
reload(book)

'''

print 'Book Script Active.'

import pymel.core as pm

'''
def function_name():
	print 'Inside the Function.'

'''

def chapter_1():
	print 'Chapter 1 - The Beginning'
	print 'It was the best of times.'
	print 'It was the worst of times.'
    
def chapter_2():
	print 'Chapter 2 - The journey starts.'

def chapter_27():
	print 'Chapter 27 - The end times.'	

'''
IK Example
'''
def build_ik():
	print 'IK System Built'
	# We need to get selected joints.
	# Only select the first joint of the joint system.
	leg_system = pm.ls(selection=True, dag=True)
	# leg_system[0]  1st Joint
	# leg_system[1]	 2nd joint
	# leg_system[2]  3rd joint
	root_joint = leg_system[0]
	ankle_joint = leg_system[2]
	ball_joint = leg_system[3]
	toe_joint = leg_system[4]

	print 'Selected:', leg_system
	# We need to apply ik handles to selected joints.

	# RP Solver 1-3 joints
	ankle_ik = pm.ikHandle(sj=root_joint, ee=ankle_joint, sol='ikRPsolver')
	# SC Solver 3-4 joints
	ball_ik = pm.ikHandle(sj=ankle_joint, ee=ball_joint, sol='ikSCsolver')
	# SC Solver 4-5 joints
	toe_ik = pm.ikHandle(sj=ball_joint, ee=toe_joint, sol='ikSCsolver')


	'''
	Connect the iks to the RFL System 
	'''


'''
Cluster Example (Loop)
'''

def joint_renamer():
	'''
	This tool renames a selected joint chain.
		- lt_leg_01_bind -> lt_leg_05_waste

	The user will select the root joint and tool will work on the 
		entire joint hierarchy.

	How to Run:

	import book
	reload(book)
	book.joint_renamer()
	'''

	'''
	Input Area 
	Get the entire selected joint heirarchy. 
	'''
	joint_chain = pm.ls(selection=True, dag=True, type='joint')

	ori = raw_input()
	name = raw_input()
	count = 0
	suffix = 'bind'

	for current_joint in joint_chain:
		count = count + 1		
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		print 'Renaming:', current_joint, ' New Name:', new_name
		current_joint.rename(new_name)

	'''
	Name last joint. 
	'''
	last_joint = joint_chain[-1]
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')
	print 'Renaming:', last_joint, ' New Name:', new_name
	last_joint.rename(new_name)

	print 'Joints have been renamed.'

def icon_renamer():
	'''
	This tool renames a selected joint chain.
		- lt_leg_01_bind -> lt_leg_05_waste

	The user will select the root joint and tool will work on the 
		entire joint hierarchy.

	How to Run:

	import book
	reload(book)
	book.joint_renamer()
	'''

	'''
	Input Area 
	Get the entire selected joint heirarchy. 
	'''
	joint_chain = pm.ls(selection=True, dag=True, type='transform')

	ori = raw_input()
	name = raw_input()
	count = 0
	suffix = 'icon'

	for current_joint in joint_chain:
		count = count + 1		
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		print 'Renaming:', current_joint, ' New Name:', new_name
		current_joint.rename(new_name)


	print 'Joints have been renamed.'

print 'Outside the function.'


