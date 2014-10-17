'''
layouts_01_columnLayout.py


How to Run:

import layouts_01_columnLayout

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window')

	# Layout Required
	pm.columnLayout()

	# numberOfColumns flag
	# columnWidth flag
	# [[columnNum, columnWidth], [columnNum, columnWidth], ...]
	# [[1, 50], [2, 75], [3,50]]

	# pm.rowColumnLayout()
	pm.rowColumnLayout(numberOfColumns=3, columnWidth=[[1, 50], [2, 75], [3,50]])	
		
	# GUI Components go here!
	pm.button()
	pm.button()
	pm.button()

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
