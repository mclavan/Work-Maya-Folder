'''
layouts_02_rowColumnLayout.py


How to Run:

import layouts_02_rowColumnLayout
reload(layouts_02_rowColumnLayout)
layouts_02_rowColumnLayout.gui()

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window')

	# Layout Required
	main_layout = pm.columnLayout()
	
	# GUI Components go here!
	# columnWidth=[[1, 100], [2, 150], [3, 100]]
	pm.rowColumnLayout(nc=3, 
		columnWidth=[[1, 100], [2, 150], [3, 100]])
	pm.button(width=100)
	pm.button(width=150)
	pm.button(width=100)
	pm.setParent(main_layout)

	pm.button(width=350)

	pm.rowColumnLayout(nc=3, 
		columnWidth=[[1, 100], [2, 150], [3, 100]])
	pm.button(width=100)
	pm.button(width=150)
	pm.button(width=100)
	pm.setParent(main_layout)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
