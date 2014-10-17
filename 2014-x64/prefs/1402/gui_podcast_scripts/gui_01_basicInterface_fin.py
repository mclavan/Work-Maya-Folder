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
	# with template:
	# Layout Required
	
	# GUI Components go here!


	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))


'''
# Template Information

template = pm.uiTemplate('mecTemplate', force=True)
template.define(pm.button, width=100, height=20)

window_object = pm.window(title='Test Window')
pm.setUITemplate( template.name(), pushTemplate=True )
pm.columnLayout()
pm.button()
pm.button()
pm.button()
window_object.show()

'''

'''
# Template Example using with 
# I need to explore the with statement a little more. 
# 	In this case it gives you indenting ability. 
#	However, how is it setting the template?
#	I don't thing it's very pythonic
#   with pm.columnLayout() as master_layout:

# with statement is used to push and pop through the different
# 	layouts.  I think this takes our code away from traditional
#	python.  I think its fine for advanced user but will confuse
#	novice programmers.  Especially if they have no knowledge of
#	the setParent command. 

template = pm.uiTemplate('mecTemplate', force=True)
template.define(pm.button, width=100, height=20)

with pm.window(title='Test Window') as window_object:
    with template:
    	with pm.columnLayout() as master_layout:
        	pm.button()
        	pm.button()
        	pm.button()
window_object.show()



'''