'''
gui_01_window.py 

How to Run:

import comp_01_groups
reload(comp_01_groups)
comp_01_groups.gui() 

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window', width=400)

	# Layout Required
	pm.columnLayout()
	# Example group commands.
	# checkBoxGrp, floatFieldGrp, intFieldGrp, floatSliderGrp, 

	# Group commands are constructed of multiple gui components.
	# number of components
	# columnWidth flag

	global checkBox_field, int_field, float_field	
	int_field = pm.intFieldGrp( numberOfFields=3, label='Scale', extraLabel='cm', 
		value1=3, value2=5, value3=1 )

	float_field = pm.floatFieldGrp( numberOfFields=3, label='Scale', extraLabel='cm', 
		value1=0.3, value2=0.5, value3=0.1 )

	checkBox_field = pm.checkBoxGrp( numberOfCheckBoxes=3, label='Three Buttons', 
		labelArray3=['One', 'Two', 'Three'] )


	pm.button(width=400, label='Output Data', command=output_fields)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

def output_fields(*args):
	# 
	
	output = int_field.getValue()
	output = float_field.getValue()
	output = checkBox_field.getValue1()
	print 'Fields Output: {0}'.format(output)

	object.tx.set(lock=True, keyable=False)
	object.tx.get()
	
