'''
gui_06_windowExists.py 

How to Run:

import gui_06_windowExists
gui_06_windowExists.gui() 

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	'''
	1) Name the Window. 
	2) Check to see if window exists. 
	3) Delete window if it exists. 
	'''

	# Creating a variable for the window name. 
	window_name = 'mecTestWindow'

	# Check to see if the window exists. 
	window_exists = pm.window(window_name, exists=True)
	if window_exists:
		pm.deleteUI(window_name)

	# Same thing can be done with the window's preferences. 
	# Instead of the window command we use windowPref
	window_pref_exists = pm.windowPref(window_name, exists=True)
	if window_pref_exists:
		pm.windowPref(window_name, remove=True)

	# Creating and naming the window. 
	window_object = pm.window(window_name, title='Test Window')

	# Layout Required
	main_layout = pm.columnLayout()

	# GUI Components go here!
	pm.rowColumnLayout(numberOfColumns=3, columnWidth=[[1, 50], [2, 100], [3, 50]])
	pm.button(width=50)
	pm.button(width=100)
	pm.button(width=50)
	pm.setParent(main_layout)
	pm.button(width=200)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

