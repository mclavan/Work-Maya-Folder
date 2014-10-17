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

	tab_1 = pm.columnLayout(width=400)
	pm.button(label='In Tab 1', width=200)
	pm.button(label='In Tab 1', width=200)
	pm.button(label='In Tab 1', width=200)
	pm.setParent(main_tab)

	tab_2 = pm.columnLayout(width=400)
	pm.button(label='In Tab 2', width=200)
	pm.button(label='In Tab 2', width=200)
	pm.button(label='In Tab 2', width=200)
	pm.setParent(main_tab)

	tab_3 = pm.columnLayout(width=400)
	pm.button(label='In Tab 3', width=200)
	pm.button(label='In Tab 3', width=200)
	pm.button(label='In Tab 3', width=200)
	pm.setParent(main_tab)

	# Tab label area
	# [layoutName, label]
	# main_tab.setTabLabel([tab_1, 'TAB 1'])
	# main_tab.setTabLabel([tab_2, 'TAB 2'])
	# main_tab.setTabLabel([tab_3, 'TAB 3'])

	main_tab.setTabLabel([[tab_1, 'TAB 1'], [tab_2, 'TAB 2'], [tab_3, 'TAB 3']])

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
