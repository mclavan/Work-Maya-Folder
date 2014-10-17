'''
gui_02_components.py 

How to Run:

import gui_02_components
reload(gui_02_components)
gui_02_components.gui() 

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window', width=300, height=300)

	# Layout Required
	pm.columnLayout()

	# GUI Components go here!
	# Basic
	pm.button(label='Test Button', width=300)
	pm.separator(width=300, height=25)
	pm.text(label='Example Text', width=300)

	# checkBox
	pm.checkBox(label='ON / OFF', annotation='This is a checkBox!')

	# sliders
	pm.floatSliderGrp(label='Slider', field=True)

	# check out separate podcast on groups.

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

