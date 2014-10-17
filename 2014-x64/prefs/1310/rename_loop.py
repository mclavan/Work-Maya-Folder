'''
rename_loop.py

How to Run:
import rename_loop
reload(rename_loop)

'''
print 'Renaming Joints'
import pymel.core as pm

def renaming_joints():
    # What are we going to loop through???
    joint_system = pm.ls(selection=True, dag=True)
    
    # What is our naming convention?
    # ct_back_01_bind
    # ori_systemName_count_systemType
    # What are the parts of our naming convention  
    result = pm.promptDialog(
                    title='Orientation',
                    message='Enter Orientation:',
                    button=['OK', 'Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')
    
    orientation = pm.promptDialog(query=True, text=True)

    result = pm.promptDialog(
                    title='System Name',
                    message='Enter System Name:',
                    button=['OK', 'Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')
    
    system_name = pm.promptDialog(query=True, text=True)
            
    # orientation = 'rt'
    # system_name = 'arm'
    count = 1
    system_type = 'bind' 
    
    # I want the loop to stop before the last joint!
    # joint_system[0:-1]
    for current_joint in joint_system[0:-1]:    
        joint_name = '{0}_{1}_0{2}_{3}'.format(orientation, system_name, count, system_type)
        print joint_name
        current_joint.rename(joint_name)
        count = count + 1
    
    system_type = 'waste'
    waste_joint = joint_system[-1]
    
    joint_name = '{0}_{1}_0{2}_{3}'.format(orientation, system_name, count, system_type)
    waste_joint.rename(joint_name)
    print 'Waste Joint: ', waste_joint, 'New Name:', joint_name