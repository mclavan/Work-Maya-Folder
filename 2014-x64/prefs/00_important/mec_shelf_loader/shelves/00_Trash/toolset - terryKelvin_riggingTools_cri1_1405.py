'''
Kelvin Terry
hierarchy.py

Description:

How to Run
import hierarchy
reload(hierarchy)
hierarchy.hierarchy()
'''



'''
import hierarchy
reload(hierarchy)
hierarchy.hierarchy()
'''
def hierarchy():
    print 'Hierarchy Genereated'


    import pymel.core as pm
    # The user will select the root joint and the tool
    #	will apply the systems.

    root_joint = 'lt_middle_01_bind'
    second_joint = 'lt_middle_02_bind'
    third_joint = 'lt_middle_03_bind'
    fourth_joint = 'lt_middle_04_waste'

    '''
    # Pad the root joint.
    ''' 

    #create an empty group.
    pad = pm.group(empty=True, name = 'lt_middle_00_pad')
    print 'Root Pad Created:', pad

    #Move group to root joint
    # Point constrain group to root joint.
    #	offest off (Snapping)
    pC = pm.pointConstraint(root_joint, pad)

    # Delete Constraint
    pm.delete(pC)

    # Freeze transforms on group
    pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

    # Parent root joint to group.
    pm.parent(root_joint, pad)


    # Create a local oriented control for each joint.
    # lt_middle_01_bind, lt_middle_02_bind, lt_middle_03_bind, lt_middle_04_waste


    # Create control (circle)
    control_icon_1 = pm.circle(name = 'lt_middle_01_icon', 
    		normal =[90, 0, 0])[0]

    # Create group (NOT EMpty)
    #	This will automaticly parent the contol under 
    #	the group.
    local1= pm.group(control_icon_1, name = 'lt_middle_01_local')

    # Move group to the target joint.
    # Use a parent constraint driver is the joint.
    # 	where driven is the pad.
    #	Offset is off (Snapping)
    parentC = pm.parentConstraint(root_joint, local1)

    # Destroy the Constarint 
    pm.delete(parentC)

    # Delete History on control 
    pm.delete(ch=True)


    # Orient constraint driver: control, driven: joint 
    pm.orientConstraint(control_icon_1, root_joint)






    # Create control (circle)
    control_icon_2 = pm.circle(name = 'lt_middle_02_icon', 
    		normal =[90, 0, 0])[0]

    # Create group (NOT EMpty)
    #	This will automaticly parent the contol under 
    #	the group.
    local2= pm.group(control_icon_2, name = 'lt_middle_02_local')

    # Move group to the target joint.
    # Use a parent constraint driver is the joint.
    # 	where driven is the pad.
    #	Offset is off (Snapping)
    parentC = pm.parentConstraint(second_joint, local2)

    # Destroy the Constarint 
    pm.delete(parentC)

    # Delete History on control 
    pm.delete(ch=True)


    # Orient constraint driver: control, driven: joint 
    pm.orientConstraint(control_icon_2, second_joint)





    # Create control (circle)
    control_icon_3 = pm.circle(name = 'lt_middle_03_icon', 
    		normal =[90, 0, 0])[0]

    # Create group (NOT EMpty)
    #	This will automaticly parent the contol under 
    #	the group.
    local3= pm.group(control_icon_3, name = 'lt_middle_03_local')

    # Move group to the target joint.
    # Use a parent constraint driver is the joint.
    # 	where driven is the pad.
    #	Offset is off (Snapping)
    parentC = pm.parentConstraint(third_joint, local3)

    # Destroy the Constarint 
    pm.delete(parentC)

    # Delete History on control 
    pm.delete(ch=True)


    # Orient constraint driver: control, driven: joint 
    pm.orientConstraint(control_icon_3, third_joint)


    # Parent middle _02 local group to control icon 1
    pm.parent(local2, control_icon_1)

    #Parent middle _03 group to control icon 2

    pm.parent(local3, control_icon_2)


    # Create empty group
    master = pm.group( empty =True, name = 'lt_middle_group')

    # Parent middle pad and middle local groups to lt_middle_group
    pm.parent(pad, local1, master)

    

    # Selet controls and only controls 

    selected = pm.ls('lt_middle*_icon')
    print 'Current Selected:' , selected


    # Loop so it locks and hides all controls
    for current_item in selected:
        current_item.tx.set(lock=True, keyable=False)
        current_item.ty.set(lock=True, keyable=False)
        current_item.tz.set(lock=True, keyable=False)
        current_item.sx.set(lock=True, keyable=False)
        current_item.sy.set(lock=True, keyable=False)
        current_item.sz.set(lock=True, keyable=False)
        current_item.v.set(lock=True, keyable=False)

        # Set color of icons


    #Select controls
    selected = pm.ls('selection=True ')
    print 'Current Selected:' , selected
        
    # loop color for all icons
    for current_item in selected:
        current_item.overrideEnabled.set(1)
        blue=6
        current_item.overrideColor.set(blue)


    # print done
    print 'Hierarchy Has Been Created.'



'''
import hierarchy
reload(hierarchy)
hierarchy.padding()
'''
def padding():

    import pymel.core as pm
    # get selected joint
    selected = pm.ls(selection=True)
    print 'Current Selected:' , selected

    first_selected = selected[0]



    # #create an empty group.
    pad = pm.group(empty=True, name = 'lt_middle_00_pad')
    print 'Root Pad Created:', pad

    #Move group to root joint
    # Point constrain group to root joint.
    #   offest off (Snapping)
    pC = pm.pointConstraint(first_selected, pad)

    # Delete Constraint
    pm.delete(pC)

    # Freeze transforms on group
    pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

    # Parent root joint to group.
    pm.parent(first_selected, pad)


    # print done
    print 'Padding Has Been Completed!'



'''
import hierarchy
reload(hierarchy)
hierarchy.priming()
'''
def priming():

    import pymel.core as pm

    # get selected joint
    selected = pm.ls(selection=True)
    # print 'Joint Selected:' , selected

    #target_joint =  selected[0]

    for target_joint in selected:
        control_icon_name = target_joint.replace('joint', raw_input())
        local_pad_name = target_joint.replace('joint', raw_input())
        
        # Create Control

        control_icon = pm.circle(normal=[1,0,0], radius=1.8, 
            name=control_icon_name)[0]

        # Group control (Not empty group)

        local_pad = pm.group(name=local_pad_name)

        print 'Control Icon:',control_icon
        print 'Pad Created:', local_pad 

        #Move group to target joint.

        temp_constraint = pm.parentConstraint(target_joint, local_pad)
        # delete contraint 
        pm.delete(temp_constraint)

        # Orient Contraint joint to control.
        pm.orientConstraint(control_icon, target_joint)



    
'''
import hierarchy
reload(hierarchy)
hierarchy.jointRenaming()
'''
def jointRenaming():
    import pymel.core as pm

    # Select joints

    joint_chain = pm.ls(selection=True, dag=True)
    print 'Selected items:', joint_chain

    # Find out naming convention

    ori= raw_input()
    system_name = raw_input() 
    count = 0
    suffix = 'bind' 


    # Loop Joint Chain Naming



    for current_joint in joint_chain:
        count = count + 1
        new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
        print 'New Name:', new_name
        current_joint.rename(new_name)
        

    new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
    current_joint.rename(new_name)



    print 'Joints Have Been Renamed!'

