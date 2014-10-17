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
	# numberOfColumns flag
	# columnWidth flag
	# [[columnNum, columnWidth], [columnNum, columnWidth], ...]
	# [[1, 50], [2, 75], [3,50]]
	master_layout = pm.columnLayout()
	
	pm.rowColumnLayout(numberOfColumns=3, columnWidth=[[1, 50], [2, 75], [3,50]])
	# GUI Components go here!
	pm.button(width=50)
	pm.button(widht=75)
	pm.button(width=50)
	# Move back to master layout. 
	pm.setParent(master_layout)

	pm.button(width=200)

	pm.rowColumnLayout(numberOfColumns=3, columnWidth=[[1, 50], [2, 75], [3,50]])
	pm.button(width=50)
	pm.button(width=75)
	pm.button(width=50)
	pm.setParent(master_layout)


	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
