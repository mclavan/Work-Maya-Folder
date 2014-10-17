'''
Lesson - Functions

This exercise will introduce functions. 

How to Run:

import functions_01
reload(functions_01)

'''

import pymel.core as pm 

print 'Lesson - Function practice.'

'''
# Think of a function as a chapter of a book.  
#   Functions allow the user to run any part of a script on demand. 

def function_name():
	print 'Statements are indented under the function.' 

'''

'''
Create a basic function and call it from the script editor. 

import functions_01
reload(functions_01)
functions_01.simple_function()

'''

'''
Create a basic function called simple_function.
'''

def simple_function():
	print 'Simple Function Called.'


'''
# Create a function called:
# 		create_controls

# Check to make sure to the code works.
# Add the code below in the create_controls function. 

'''
def create_controls():

	control_icon_1 = pm.circle(normal=[0, 1, 0])[0]
	control_icon_2 = pm.circle(normal=[0, 1, 0])[0]

	control_icon_1.ty.set(2.5)
	control_icon_2.ty.set(5)

	pm.parent(control_icon_2, control_icon_1)

	control_icon_1.tx.set(lock=True, keyable=False)
	control_icon_1.ty.set(lock=True, keyable=False)
	control_icon_1.tz.set(lock=True, keyable=False)
	control_icon_1.sx.set(lock=True, keyable=False)
	control_icon_1.sy.set(lock=True, keyable=False)
	control_icon_1.sz.set(lock=True, keyable=False)
	control_icon_1.v.set(lock=True, keyable=False)


	control_icon_2.tx.set(lock=True, keyable=False)
	control_icon_2.ty.set(lock=True, keyable=False)
	control_icon_2.tz.set(lock=True, keyable=False)
	control_icon_2.sx.set(lock=True, keyable=False)
	control_icon_2.sy.set(lock=True, keyable=False)
	control_icon_2.sz.set(lock=True, keyable=False)
	control_icon_2.v.set(lock=True, keyable=False)


