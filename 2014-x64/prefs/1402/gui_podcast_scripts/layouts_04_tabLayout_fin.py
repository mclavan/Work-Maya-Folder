'''
layouts_01_columnLayout.py


How to Run:

import layouts_04_tabLayout
reload(layouts_04_tabLayout)
layouts_04_tabLayout.gui()

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
	main_tab = pm.tabLayout()
	tab_1 = pm.columnLayout(width=300)
	pm.button(label='In Tab 1')
	pm.button(label='In Tab 1')
	pm.button(label='In Tab 1')
	pm.setParent(main_tab)

	tab_2 = pm.columnLayout(width=300)
	pm.button(label='In Tab 2')
	pm.button(label='In Tab 2')
	pm.button(label='In Tab 2')
	pm.setParent(main_tab)

	tab_3 = pm.columnLayout(width=300)
	pm.button(label='In Tab 3')
	pm.button(label='In Tab 3')
	pm.button(label='In Tab 3')
	pm.setParent(main_tab)

	main_tab.setTabLabel([tab_1, 'TAB 1'])

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
