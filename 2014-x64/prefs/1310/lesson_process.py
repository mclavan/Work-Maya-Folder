'''
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

def create_skynet():
    print 'Skynet has been created.'


def padding_tool():
    # Selecting a joint.
    selected_joints = pm.ls(selection=True)
    root_joint = selected_joints[0]
    print 'Root Joint:', root_joint
    
    # Deselect
    # select -cl  ;
    pm.select(clear=True)
    
    # Empty creating a group.
    # mel group needs to have something selected.
    pad = pm.group()
    print 'Pad Created:', pad
    
    # Point Constraint with offset
    #   turned off.
    temp_constraint = pm.pointConstraint(root_joint, pad,
                                    maintainOffset=False)
    
    # Delete the constraint
    pm.delete(temp_constraint)
    
    
    # Freeze Transform of group.
    pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
    
    # Parent the joint into the group
    pm.parent(root_joint, pad)
    '''
    # Renaming the group
    # We have not done this yet!!!
    
    '''

    print 'Padding Tool Activated'

