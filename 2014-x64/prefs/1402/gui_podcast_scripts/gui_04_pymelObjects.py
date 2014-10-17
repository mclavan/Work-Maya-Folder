'''
gui_04_pymelObjects.py 

How to Run:

import gui_04_pymelObjects
gui_04_pymelObjects.gui() 

'''

import pymel.core as pm 

window_object = pm.window(title='Test Window')

# Layout Required
pm.columnLayout()

# GUI Components go here!
on_off_checkBox = pm.checkBox(label='On / Off')

# Integer Fields
dx_field = pm.intField(min=2, value=2)
dy_field = pm.intField(min=2, value=4)
dz_field = pm.intField(min=2, value=2)

name_field = pm.textField()

window_object.show()

print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
Maya Commands Help Docs
'''


'''
Pymel Help Docs
'''

'''
Manipulating the window. 
'''
# Window size

# Window location

'''
Getting Values
'''

'''
Setting Values
'''

