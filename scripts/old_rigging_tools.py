# Creating Circles
import pymel.core as pm

# pm.commandName()
pm.circle()
# flag radius
pm.circle(radius=2)
# multiple flags
pm.circle(sections=16, radius=3, normal=[1, 0, 0])
# lists (multiple values)
pm.circle(normal=[1, 0, 0])

# Flags
    # r / radius
    # nr / normal ??? Explain in your own words.
    # s / sections
    # 
'''
Michael Clavan
rigging_tools.py

Description:
	A group of rigging related tools. 

How to Run:

import rigging_tools
reload(rigging_tools)

'''

print 'Rigging Tools Active'

import pymel.core as pm 

def tool():
	print 'Tool Active.'

def snapping_tool():
	'''
	This tools moves the first selected object to the second. 
		- Translates and Rotates the target object. 

	import rigging_tools
	rigging_tools.snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	kenny = pm.parentConstraint(selected[0], selected[1])
	pm.delete(kenny)

	print 'The first selected object was moved to the second.'

def point_snapping_tool():
	'''
	This tools moves the first selected object to the second. 
		- Translates the target object. 

	import rigging_tools
	rigging_tools.point_snapping_tool()
	'''

	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)

	target_joint = selected[0]
	control_icon = selected[1]

	# By default commands work on selected.
	kenny = pm.pointConstraint(selected[0], selected[1])
	pm.delete(kenny)

	print 'The first selected object was moved to the second.'

def world_icon():

	# Get selected
	selected = pm.ls(selection=True)
	print 'Selected: {0}'.format(selected)
	
	first_joint = selected[0]

	# Create a control icon.
	control_icon_1 = pm.circle(normal=[0, 1, 0], radius=2)[0]

	# Move the control to the target joint. 
	# Delete the constraint. 
	kenny = pm.pointConstraint(first_joint, control_icon_1)
	pm.delete(kenny)

	print 'Icons created.'

def hiearchy():
	print 'hi'

def padding_tool():
	print 'Padding!'

def joint_renamer():
	'''
	This tool renaming a selected joint chain. 

	Select a root joint and run the function. 
	- The script will prompt you first for the orientation ('lt', 'rt', 'ct') and 
		the name of the system ('arm', 'back', 'leg')

	import rigging_tools
	reload(rigging_tools)
	rigging_tools.joint_renamer()

	'''

	# Select the root joints and I will get its children.
	joint_chain = pm.ls(selection=True, dag=True)

	# Do not worry about the waste suffix.
	# ori_name_count_suffix
	# lt_arm_01_bind
	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'


	for current in joint_chain:
	    new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count, suffix)
	    print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)   
	 
	    # Rename commmand
	    # variable.rename(new_name)
	    current.rename(new_name)
	    
	    count = count + 1       

	new_name = '{0}_{1}_{2:02d}_{3}'.format(ori, name, count-1, 'waste')
	print 'Current Joint: {0} - New Name: {1}'.format(current, new_name)   
	current.rename(new_name)


