'''
Lesson - String Manip
string_manip.py

During this script we will explore string methods. 
Google Search: python string methods
http://docs.python.org/release/2.5.2/lib/string-methods.html

How to Run:

import string_manip
reload(string_manip)

'''

import pymel.core as pm 

# Replacing bind with proxy
index_finger_1 = 'lt_index_01_bind'
print 'Orginal Name:', index_finger_1

# string method replace
# lt_index_01_bind  -> lt_index_01_icon
# lt_index_01_bind  -> lt_index_01_proxy
print index_finger_1.upper()
print index_finger_1.replace('_bind', '_icon')
print index_finger_1.replace('_bind', '_proxy')

control_icon = pm.circle()[0]
new_name = index_finger_1.replace('_bind', '_icon')
control_icon.rename(new_name)

# This could be done for renaming proxy geometry too.


# Create a joint and a piece of geometry.
# Call the joint in the scene.
#	ct_back_01_bind
# Have the user select the joint then the geometry. 


# Get the selected object in the scene.

# Use the string method replace on the joint.
# Swap out _bind with _proxy. 


# Rename proxy geometry.






