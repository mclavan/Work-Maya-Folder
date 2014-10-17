'''
PyMel Objects and Attributes

- Lists are required for these examples. 
'''
import pymel.core as pm

'''
Setting Attribute Values
Dot Notation Example
'''

# Getting the selected Object
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object:', first_selected


'''
Moving Object
tx, ty, and tz
'''
first_selected.tx.set(0)
first_selected.ty.set(0)
first_selected.tz.set(0)

# Moving all the rotates at once.
first_selected.r.set([0, 0, 0])
print first_selected, 'Moved to default rotate and translate.'
# This can be done with long and short name of the attributes
# All attributes can be manipulated this way.


'''
Getting Attribute Values
'''
# Storing the first two objects selected.
selected = pm.ls(selection=True)
driver_object = selected[0]
driven_object = Selected[1]
print 'First Selected:', driver_object, 'Second Selected:', driven_object

# Getting the values from the first object.
drivers_rotations = driver_object.r.get()
# Applying rotation from the driver_object to the driver_object
driven_object.r.set(drivers_rotations)
print driver_object, 'Rotation values applied to:', driven_object

'''
Control Color
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object:', first_selected

# Enable overrides and setting color
# Look at the attribute spreadsheet
color = 6
first_selected.overrideEnabled.set(1)
first_selected.overrideColor.set(color)

'''
# Appling on the shape node.
control_shape_object = first_selected.shape()
control_shape_object.overrideEnabled.set(1)
control_shape_object.overrideColor.set(color)
'''

'''
Lock and Hide
The set method can also change the state of the attribute
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object:', first_selected

# Lock
first_selected.tx.set(lock=True)
# Lock and Hide
first_selected.tx.set(lock=True, keyable=False)
# Unlock
first_selected.tx.set(lock=False)
# Unlock and UnHide
first_selected.tx.set(lock=False, keyable=True)

# Unlock and UnHide all scale and visibility
first_selected.sx.set(lock=False, keyable=True)
first_selected.sy.set(lock=False, keyable=True)
first_selected.sz.set(lock=False, keyable=True)
first_selected.v.set(lock=False, keyable=True)

'''
The set method is a little buggy. 
- Doesn't make the channels keyable. 
first_selected.s.set(lock=False, keyable=True)
'''

'''
Adding Attributes 
'''
selected = pm.ls(selection=True)
first_selected = selected[0]
print 'First Selected Object:', first_selected


'''
Pushing Further
- These examples are restricted to the first selected object. 
	It would make more sense to apply changes to attributes 
	to all selected objects. 
- Watch the Loops Podcast. 
'''

