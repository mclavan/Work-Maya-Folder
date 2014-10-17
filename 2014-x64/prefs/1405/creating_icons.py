'''
Exercise - Creating Padded Controls
creating_icons.py

Creating a padded control icon.

'''
import pymel.core as pm 

print 'Creating Icons Example'

'''
- Target -
Create three controls are parent them to each other.

- WATCH OUT -
Controls return more then just a transform node.
'''

# Create a control icon and store it in a variable.
control_icon_1 = pm.circle()[0]
control_icon_2 = pm.circle()[0]
control_icon_3 = pm.circle()[0]

'''
[nt.Transform(u'nurbsCircle1'), nt.MakeNurbCircle(u'makeNurbCircle1')]
'''

# Command that create items will RETURN values back to the user.
# These values are what is being stored into a variable.

# Print out the value contained in the variable.
print 'Control Icon:', control_icon_1, control_icon_2, control_icon_3


# Isolate the first object in the list.


# Create two addition controls are parent them to each other.
pm.parent(control_icon_3, control_icon_2)
pm.parent(control_icon_2, control_icon_1)




