'''
layouts_02_rowColumnLayout.py


How to Run:

import layouts_03_frameLayout
reload(layouts_03_frameLayout)
layouts_03_frameLayout.gui()

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window', sizeable=False)

	# Layout Required
	main_layout = pm.columnLayout()
	
	pm.frameLayout(label='Frame 1', width=200,
		collapsable=True, collapse=True)
	pm.columnLayout()
	pm.button(label='Inside Frame 1', width=200)
	pm.button(label='Inside Frame 1', width=200)
	pm.button(label='Inside Frame 1', width=200)
	pm.setParent(main_layout)

	pm.frameLayout(label='Frame 2', width=200,
		collapsable=True, collapse=True)
	pm.columnLayout()
	pm.button(label='Inside Frame 2')
	pm.button(label='Inside Frame 2')
	pm.button(label='Inside Frame 2')
	pm.setParent(main_layout)

	pm.frameLayout(label='Frame 3', width=200,
		collapsable=True, collapse=True)
	pm.columnLayout()	
	pm.button(label='Inside Frame 3')
	pm.button(label='Inside Frame 3')
	pm.button(label='Inside Frame 3')		
	pm.setParent(main_layout)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
