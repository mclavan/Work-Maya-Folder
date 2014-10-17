'''
Michael Clavan
book.py 

How to Run:

import book
reload(book)

'''

print 'Function Practice'

import pymel.core as pm 

def delete_history():
	print 'Starting Chapter 1'
	print 'It was the best of times.'
	print 'It was the worst of times.'


def freeze_transforms():
	print 'Chapter 2 - A new beginning.'

def create_controls():
	print 'Controls Created.'
	control_icon_1 = pm.circle(normal=[0, 1, 0])[0]
	control_icon_2 = pm.circle(normal=[0, 1, 0])[0]

	control_icon_1.ty.set(2.5)
	control_icon_2.ty.set(5)

	pm.parent(control_icon_2, control_icon_1)

def create_reverse_footlock():
	print 'Foot lock created.'


def create_if_fk():
	print 'IKFK created.'

def joint_renamer():
	# Get selected root joint. 
	# How do I get the entire hierarchy of a joint chain?
	#   pm.ls(selection=True, dag=True)
	joint_chain = pm.ls(selection=True, dag=True)
	# print 'Joints:', joint_chain

	# Naming Convention Example
	# lt_arm_01_bind -> lt_arm_03_bind
	# orienation_systemName_count_suffix
	ori = raw_input()
	name = raw_input()
	count = 0
	suffix = 'bind'

	# Loop through selected.
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)
		print 'New Name:', new_name	
		current_joint.rename(new_name)
		# Compile new name

		# Add one to the count.

		# Rename the joint

		# Output to the user.


	# Name the waste joint
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, 'waste')
	# Output to the user
	joint_chain[-1].rename(new_name)	
