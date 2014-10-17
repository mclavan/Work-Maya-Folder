'''
Michael Long
primeing.py


import primeing
reload (primeing)
primeing.function()
'''

print
print 'primeing.py is running.'
print

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

def function(*args):
    # calls all code from one clean function

    print
    print 'primeing.function() has been activated'
    print

    primeingCreator()

def primeingCreator(*args):
    # Creates/Names/Organizes new control icons and groups

    print
    print 'primeing.primeingCreator() has been activated'
    print

    # Selection Variables
    userSelection = pm.ls(selection=True)
    joint_chain = pm.ls(selection=True, dag=True)
    jointName = str(joint_chain[0])

    # Naming script variables
    ori = ""
    suffix = ""
    location = ""

    groupName = ""
    iconName = ""

    # making suffixs for the groups and icons
    groupSuffix = 'prime'
    controlSuffix = 'icon'

    # Print statments in editor. For debugging
    print
    print jointName
    print 

    # Exanmins jointName to find the ORIGIN (lt, rt, or cnt)
    if 'rt_'  in jointName:
        ori = 'rt'
        
    elif "lt_" in jointName:
        ori = 'lt'
        
    elif "cnt_" in jointName:
        ori = 'cnt'

    else:
        # Error message
        print 'Joint Origin not found.'
        print 'Plese fix joint naming convention.'
        print 'This code needs joint origin to be lt, rt, or cnt'
        return

    # Print statments in editor. For debugging
    print 
    print ori
    print 

    # Exanmins jointName to find the SUFFIX (bind, piv, waste, end, or last)
    if "_bind"  in jointName:
        suffix = '_bind'

    elif "_piv" in jointName:
        suffix = 'piv'
        
    elif "_waste" in jointName:
        suffix = 'waste'

    elif "_end" in jointName:
        suffix = 'end'

    elif "_last" in jointName:
        suffix = 'last'

    else:
        # Error message
        print 'Joint Suffix not found.'
        print 'Plese fix joint naming convention.'
        print 'This code needs joint sufix to be bind, piv, end, waste, last, or end'
        return

    # Print statments in editor. For debugging
    print 
    print suffix
    print

    # Uses ORIGIN and SUFFIX found in jointName to get location (arm, back, tail, etc)
    noSuffix = jointName.replace(suffix, "")
    noOrigin = noSuffix.replace(ori, "")

    #removes count and underscores from the remaing name (_back_03_ ---> back)
    location = noOrigin[1:-3]

    # Print statments in editor. For debugging
    print 
    print location
    print

    # loop that move down joint chain and creates groups/icons/hierarchy
    count = 1
    for current_joint in joint_chain:

        currentJoint_name = str(current_joint)

        # elif code to find end/waste joints so extra pads/icons are not made
        if "_waste"  in currentJoint_name:
            
            # Print statments in editor. For debugging
            print
            print 'Found WASTE joint. No pad created'
            print

        elif "_last" in currentJoint_name:

            # Print statments in editor. For debugging
            print
            print 'Found LAST joint. No pad created'
            print

        elif "_end" in currentJoint_name:

            # Print statments in editor. For debugging
            print 
            print 'Found END joint. No pad created'
            print 

        # if not an end/waste joint then the naming and creation continues
        else: 

            # making the final names from the variables
            groupName = '{0}_{1}_0{2}_{3}'.format(ori, location, count, groupSuffix)
            iconName = '{0}_{1}_0{2}_{3}'.format(ori, location, count, controlSuffix)

            #GROUP CREATION
            new_group = pm.group(name = groupName, em=True)

            # group cleanup
            pm.delete(constructionHistory=True)
            pm.makeIdentity(apply=True)
            pm.xform(centerPivots=True)

            # Print statments in editor. For debugging
            print
            print 'Empty Group Created: ', new_group
            print

            #ICON CREATION
            new_controlIcon = pm.circle(name = iconName, r=2, normal=[1,0,0])[0]

            # icon cleanup
            pm.delete(constructionHistory=True)
            pm.makeIdentity(apply=True)
            pm.xform(centerPivots=True)

            # Print statments in editor. For debugging
            print
            print 'Control Icon created: ', new_controlIcon
            print

            # meeseeks is contraint code that moves the controls/groups and orients them to the joints
            # meeseeks then deleates itself having surved its purpose

            # meeseeks for the group (constrains to joint)
            meeseeks = pm.parentConstraint(current_joint, new_group)
            pm.delete(meeseeks)

            # meeseeks for the icon (constrains to group)
            meeseeks = pm.parentConstraint(new_group, new_controlIcon)
            pm.delete(meeseeks)

            # parents the helpless icon to the group so it can feel safe
            # result:
            #   >new_group
            #    -->new_controlIcon
            pm.parent(new_controlIcon, new_group)

            # Print statments in editor. For debugging
            print 
            print 'Pad: ', count, ' created'
            print

            # if/else loop for parenting pads to create proper hierarchy
            if count == 1:
                parentIcon = new_controlIcon
                parentPad = new_group
            else:
                pm.parent(new_group, parentIcon)
                parentIcon = new_controlIcon             

            # Count von Count makes sure the count is updated
            # count is used for naming things in order of creation and is used for hierarchy control 
            count = count + 1





