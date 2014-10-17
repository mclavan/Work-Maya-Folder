'''
Benjamin Ilarraza
lesson_process.py

Description:
	Learning processes.
	Padding the selected joint.

How to Run:
import lesson_process
reload(lesson_process)
'''

print 'Lesson Process'
import pymel.core as pm
#Select a joint
selected_joints=pm.ls(selection=True)
root_joint=selected_joints[0]
print 'Root Joint', root_joint
#Deselect
pm.select(clear=True)

#Empty creating a group
pad=pm.group()
print 'pad created', pad

#Point Constraint with offset
temp_constraint=pm.pointConstraint(root_joint, pad, maintainOffset=False)

#Delete the constraint
pm.delete(temp_constraint)

#Freeze transform of group
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
#Parent the joint into the group

#Renaming the group

