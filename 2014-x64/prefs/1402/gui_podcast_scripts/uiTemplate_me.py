'''
gui_02_basicInterface.py


How to Run:

import gui_02_basicInterface
gui_02_basicInterface.gui()

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window')

	# Create a new template
	template = pm.uiTemplate('mecTemplate', force=True)
	# Defining the default look for a button
	template.define(pm.button, width=200, height=20, bgc=[.7, 0, 0])
	template.define(pm.frameLayout, cll=True, cl=True, width=200)
	window_object = pm.window(title='Test Window')

	# Point to existing template
	pm.setUITemplate( template.name(), pushTemplate=True )
	master_layout = pm.columnLayout()
	
	pm.frameLayout(parent=master_layout)
	pm.columnLayout()
	pm.button()
	pm.button()
	pm.button()


	pm.frameLayout(parent=master_layout)
	pm.columnLayout()
	pm.button()
	pm.button()
	pm.button()

	pm.frameLayout(parent=master_layout)
	pm.columnLayout()
	pm.button()
	pm.button()
	pm.button()	
	pm.setParent(master_layout)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))


def gui_template_ex2():
	'''
	Using the with statement. 
	Creates nice indenting, but isn't very pythonic. 
	You don't have to use setParent command. 
	'''
	template = pm.uiTemplate('mecTemplate', force=True)
	template.define(pm.button, width=200, height=20, bgc=[.7, 0, 0])
	template.define(pm.frameLayout, cll=True, cl=True, width=200)

	# window_object = pm.window(title='Test Window')
	with pm.window(title='Test Window') as window_object:
	    with template:
	    	# master_layout = pm.columnLayout()
	    	with pm.columnLayout() as master_layout:
		    	with pm.frameLayout():
			    	with pm.columnLayout():
			        	pm.button()
			        	pm.button()
			        	pm.button()

		    	with pm.frameLayout():
			    	with pm.columnLayout():
			        	pm.button()
			        	pm.button()
			        	pm.button()

		    	with pm.frameLayout():
			    	with pm.columnLayout():
			        	pm.button()
			        	pm.button()
			        	pm.button()
		        		        
	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))




