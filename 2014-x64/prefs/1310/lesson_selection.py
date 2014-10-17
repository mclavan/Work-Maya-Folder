'''
Michael Clavan
lesson_selection.py

How to Run:

import lesson_selection
reload(lesson_selection)

'''
print 'Selection Lesson'

import pymel.core as pm

'''
We want to build the IKs for the RFL.
Top -> Ankle RPsolver
Ankle -> Ball SCsolver
Ball -> Toe SCsolver
'''

root_joint = 'joint1'
ankle_joint = 'joint3'
ball_joint = 'joint4'
toe_joint = 'joint5'

print 'RPSolver to', root_joint, ankle_joint
pm.ikHandle(startJoint=root_joint,
            endEffector=ankle_joint,
            solver='ikRPsolver')

pm.ikHandle(startJoint=ankle_joint,
            endEffector=ball_joint)

