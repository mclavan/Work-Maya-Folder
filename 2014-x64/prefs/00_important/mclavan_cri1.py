import pymel.core as pm


def invalid_transform_detection(root_naming='01_bind'):
    '''
    This function will detect if invalid transforms exists on joints 
        in the scene. 
        - Rotations of any kind will be detected. 
        - Translation Y or Z on children joints will be detected. 
        - Root joints will be by passed for tranlation check if joints
         follow the naming convention provided in the argument.

    '''

    rig_joints = pm.ls(type='joint')
    print 'Rig Joints: {0}'.format(rig_joints)

    problem_joints = []
    for current_joint in rig_joints:
        error_line = ''
        translation = current_joint.t.get()
        # Maya defaults to 16 digits.  I'm rounding down to get a better
        #   error detection.
        translation[0] = pm.dt.round(translation[0], 5)
        translation[1] = pm.dt.round(translation[1], 5)
        translation[2] = pm.dt.round(translation[2], 5)
        translation_error = False
        rotation_error = False
        

        if (current_joint.find(root_naming) == -1) and not is_root_joint(current_joint):
            # if pm.dt.round(translation[0], 5) !=0:
            #     translation_error = True
        
            if pm.dt.round(translation[1], 5) != 0:
                translation_error = True
          
            if pm.dt.round(translation[2], 5) != 0:
                translation_error = True    
            
            if translation_error:
                error_line += '\t\tSuspect Translations: {0}\n'.format(round_vector(translation))    
        
        rotations = current_joint.r.get()
        zero_rotations = pm.dt.Vector()
        if rotations != zero_rotations:
            error_line += '\t\tSuspect Rotations: {0}\n'.format(round_vector(rotations))
            rotation_error = True

        if error_line != '':
            print 'Joint: {0}\n'.format(current_joint)
            print '{0}'.format(error_line)

            problem_joints.append(current_joint)

    return problem_joints

def round_vector(current_vector):
    rounded_vector = pm.dt.Vector()
    
    rounded_vector[0] = pm.dt.round(current_vector[0], 4)
    rounded_vector[1] = pm.dt.round(current_vector[1], 4)
    rounded_vector[2] = pm.dt.round(current_vector[2], 4)
    return rounded_vector

def quick_orientation_mode(root_joints='*_01_bind'):
    '''
    This function will select all the root joints and jump into 
        component mode.  The orientation mode will also be turned on.

    Concept:
        The reason for this script is to quickly toggle back and forth
            between component mode and object mode.  

    Requirement:

        - I would have to talk about converting mel procedures 
        for this one.

    Level: Odd
    '''
    if root_joints != '':
        pm.select(root_joints, replace=True)
    # Only mel procedures popped up.  However, they were easy to convert.
    pm.mel.changeSelectMode('-component')
    pm.mel.setComponentPickMask('Other', True)

def quick_object_mode():
    '''
        This function is the second half of the quick orientation 
            mode swap tool. 
        This tool jumps to object mode and clears selection. 

    Level: Odd
    '''
    pm.mel.changeSelectMode('-object')
    pm.select(clear=True)

def select_children_joints():
    '''
    This tool will select all the children joints of the selected joint. 
    The end joint will not be seleced. 

    Concept:
        This tool will allow you to test a rigs orientation, proxy, 
            and skin.  By allow the user to quickly rotate and curl 
            multiple jonts.  

    Requirement:
        Slice/Range will need to be discussed in solving this problem. 

    Level: Easy
    '''
    joint_system = pm.ls(selection=True, dag=True)[:-1]
    pm.select(joint_system, replace=True)    


def is_root_joint(check_joint):
    '''
    This tool will return if the given joint is a root joint.
    '''
    results = False

    # firstParent2 uses the listRelative command instead of search by string.
    joint_parent = check_joint.firstParent2()

    if (joint_parent.nodeType() != 'joint') and (joint_parent.nodeType() == 'transform'):
        results = True

    return results




