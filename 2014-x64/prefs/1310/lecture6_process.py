'''
Michael Clavan
lecture6_process.py

How to Run:
import lecture6_process
reload(lecture6_process)

'''

print 'The process can not be stopped.'

import pymel.core as pm 

"""
'''
Instructions
This is a snapping tool.
This tool snaps one object to another. 
'''
'''
Input or Given
'''
selected_objects = pm.ls(selection=True)
root_joint = selected_objects[0]
control_icon = selected_objects[1]

'''
Process 
'''
temp_constraint = pm.pointConstraint(root_joint, control_icon, maintainOffset=False)
pm.delete(temp_constraint)

'''
Output
'''
print 'Root Joint:', root_joint
print 'Control Icon:', control_icon

'''



'''
Example 2 - Creating controls and parenting them. 
We are going to create three controls are parent them together!
- Creating circles.
- Parenting 
- Transforming
'''

'''
Given
'''
# No given

'''
Process
'''
control_icon_1 = pm.circle()[0]  # [nt.Transform(u'nurbsCircle1'), ....
control_icon_2 = pm.circle()[0]
control_icon_3 = pm.circle()[0]
print control_icon_1

# pm.xform(control_icon_1, translation=[0, 5, 0])
# pm.xform(control_icon_2, translation=[5, 0, 0])
# pm.xform(control_icon_3, translation=[0, 0, 5])

# pm.setAttr(control_icon_1 + '.ty', 5)

control_icon_1.translateY.set(5)
control_icon_2.translateX.set(5)
control_icon_3.translateZ.set(5)


#                0                                   1
# [nt.Transform(u'nurbsCircle1'), nt.MakeNurbCircle(u'makeNurbCircle1')]

# pm.parent(control_icon_1, control_icon_2, control_icon_3)
pm.parent(control_icon_2, control_icon_1)
pm.parent(control_icon_3, control_icon_2)

'''
# Warning: Cannot parent components or objects in the underworld. # 

- control_icon_3
	control_icon_1
	control_icon_2
- control_icon_1
	- control_icon_2
		- control_icon_3
'''

'''
Output
'''
print 'Control Icons Created:', control_icon_1, control_icon_2, control_icon_3

"""



'''
Example 3 - RFL creating IK's for an RFL
'''

'''
Given
'''
selected_joints = pm.ls(selection=True, dag=True)
hip_joint = selected_joints[0]
ankle_joint = selected_joints[2]
ball_joint = selected_joints[3]
toe_joint = selected_joints[4]


'''
Process is expecting
a hip joint, ankle, ball, and toe joint. 
'''
# Three IK are needed.  The first on is RP while the second and thrid is SC.

# ikHandle -sol ikRPsolver;
# sol mean solver 
# sj or startJoint is the starting Joint
# ee or endEffector is the last joint
pm.ikHandle(startJoint=hip_joint, 
			endEffector=ankle_joint, 
			solver='ikRPsolver')[0]
pm.ikHandle(startJoint=ankle_joint, 
			endEffector=ball_joint,
			solver='ikSCsolver')[0]
pm.ikHandle(startJoint=ball_joint, 
			endEffector=toe_joint,
			solver='ikSCsolver')[0]

'''
Output
'''


