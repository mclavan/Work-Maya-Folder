'''
Command Anatomy
'''

# Commands
pm.circle()
# Flags
pm.circle(radius=3.5)
# Mutliple Flags
pm.circle(radius=3.5, sections=16)
# Flag order does not matter.
pm.circle(sections=16, radius=16)


'''
Affecting Objects
Commands typically ether creating or change objects in Maya.
Objects that affect another need to identify which Maya objects the will manipulate.
'''
# The circle command creates a nurbs circle.
pm.circle(normal=[0, 1, 0], radius=3.5, name='target_A')
pm.circle(normal=[0, 1, 0], name='affected')

# The point constraint command influences or changes objects in Maya.
# Affected objects will allways start at the beginning of a command.
# There order DOES MATTER!
pm.parentConstraint('target_A', 'affected')
# All constraints work simular.  You first select one or multiple object that will be 
# targets and then the last selected object will be constrained.

'''
Practice using flags
Look up the flag names and convert them into their longName version.
'''



'''
Converting from MEL to Python
'''
# Command name and line terminator.
circle;

# Flags
circle -radius 3.5;
circle -normal 0 1 0 -radius 3.5 -name "Ball";

# Affected 
# In MEL, Affected objects are at the end of the command.
pointConstraint -maintainOffset "target_A" "affected";
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 "target_A";


# Odd Examples
# Toogle Flags
delete -ch;
pointConstraint -maintainOffset;
select -r "target_A" "affected";


'''
Setting Values
'''
pm.setAttr('target_A.translateY', 5)
pm.xform('target_A', rotate=[0, 0, 45])


'''
Adding Attributes
'''
pm.addAttr('affected', longName='geometry_vis', attributeType='long', min=0, max=1, dv=1, keyable=True)

'''
Locking Attributes
'''
pm.setAttr('affected.geometry_vis', lock=True)



'''
Selected Objects
'''

'''
Moving Objects
'''

'''
Object Attribute Notation
'''
# object.attribute
# ball.translateY
# ball.ty
# lt_hand_icon.index_curl
# tiki_icon.geometry_vis

# The attribute is connected to the object through the use of the period.
# This is called dot notation.  Its a way of showing hierarchy.
# Understanding this concept of dot notation is extremely important.

# This concept is used through out programming.  Maya, Nuke, and Python use dot notation heavly.

pm.circle(normal=[0, 1, 0], radius=3.5, name='target_B')
pm.setAttr('target_B.translateY', 4)  # Move "target_A" up 4 units in the Y Axis.

pm.setAttr('target_B.rotateX', lock=True, keyable=False)
pm.setAttr('target_B.rotateY', lock=True, keyable=False)
pm.setAttr('target_B.rotateZ', lock=True, keyable=False)


'''
Hard Coded Values
'''
# Hard Coded Values are values that are fixed they will not change.
# The example below 'target_B.rotateX' is hard coded.  
# It will only l
pm.setAttr('target_B.rotateX', lock=False, keyable=True)
pm.setAttr('target_B.rotateY', lock=False, keyable=True)
pm.setAttr('target_B.rotateZ', lock=False, keyable=True)
