'''
layouts_01_columnLayout.py


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
	template = pm.uiTemplate('mecTemplate', force=True)
	template.define(pm.button, width=200, height=20, bgc=[0.8, .5, 0])
	
	template.define(pm.frameLayout, cll=True, cl=True, width=200)
	window_object = pm.window(title='Test Window')

	# pm.setUITemplate( template.name(), pushTemplate=True )

	# Layout Required
	with template:
		with pm.columnLayout() as master_layout:
		# master_layout = pm.columnLayout()
		
			# GUI Components go here!
			with pm.frameLayout(cl=False, label='Frame 1'):
				with pm.columnLayout():
					pm.button(label='Inside Frame 1')
					pm.button(label='Inside Frame 1')
					pm.button(label='Inside Frame 1')


			# pm.frameLayout(cll=True, label='Frame 2')
			# pm.columnLayout()
			with pm.frameLayout(label='Frame 2'):
				with pm.columnLayout():
					pm.button(label='Inside Frame 2')
					pm.button(label='Inside Frame 2')
					pm.button(label='Inside Frame 2')
			# pm.setParent(master_layout)

			with pm.frameLayout(label='Frame 3'):
				with pm.columnLayout():
					pm.button(label='Inside Frame 3')
					pm.button(label='Inside Frame 3')
					pm.button(label='Inside Frame 3')

			pm.button(bgc=[0, .8, .5])

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
