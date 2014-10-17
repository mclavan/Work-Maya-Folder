'''
lesson_loops.py

How to Run
import lesson_loops
reload(lesson_loops)

'''
print 'Lesson Loops'
import pymel.core as pm

'''
for variable_name in a_list:
    ...statements...

while, do while
'''

# for-in loop
names = ['Michael', 'George', 'Susan', 'Seth:(']
#                                         ^
print 'Names:', names

for customer in names:
    print 'Now serving customer:', customer

# joint_system = ['lt_arm_01_bind', 'lt_arm_02_bind']
joint_system = pm.ls(selection=True, dag=True)

for current_joint in joint_system:
    print 'Current Joint:', current_joint
    new_name = current_joint.replace('_bind', '_icon')
    print 'New Control Icon Name is:', new_name
    control_icon = pm.circle(normal=[1, 0, 0], name=new_name)[0]
    # How would I move the control to the current joint.
    # pm.addAttr(control_icon, longName='strechy', at='double', keyable=True)
    
    
    
