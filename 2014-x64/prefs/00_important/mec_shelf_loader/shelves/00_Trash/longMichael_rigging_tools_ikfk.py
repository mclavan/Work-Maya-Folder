'''
Michael Long
ikfk.py

HOW TO RUN:
 
import ikfk
reload (ikfk)
ikfk.function()
'''

print
print 'ikfk.py is running.'
print

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

def function(*args):
    # calls all code from one clean function

    print
    print 'ikfk.function() has been activated'
    print

    ikfkCreator()

def ikfkCreator(*args):
	#Creates ik/fk joints and hierarchy

	print
	print 'ikfk.function() has been activated'
	print

	# Selection Variables
	userSelection = pm.ls(selection=True)
	joint_chain = pm.ls(selection=True, dag=True)
	jointName = str(joint_chain[0])

	#grabbing joints for orient constrins
	rootJoint = joint_chain[0]
	midRootJoint = joint_chain[1]

	# Naming script variables
	suffix = ""

	fkName = ""
	ikName = ""

	switchJoint = joint_chain[-1]

	# making suffixs for the FK groups and icons
	f = 'fk_prime'
	fk_controlSuffix = 'fk_icon'

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
	    #return

	# Print statments in editor. For debugging
	print 
	print ori
	print 

	# Exanmins jointName to find the SUFFIX (bind, piv, waste, end, or last)
	if "_bind"  in jointName:
	    suffix = 'bind'

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
	    #return

	# Print statments in editor. For debugging
	print 
	print suffix
	print

	# Uses ORIGIN and SUFFIX found in jointName to get location (arm, back, tail, etc)
	noSuffix = jointName.replace(suffix, "")
	noOrigin = noSuffix.replace(ori, "")

	#removes count and underscores from the remaing name (_back_03_ ---> back)
	location = noOrigin[1:-4]

	# Print statments in editor. For debugging
	print 
	print location
	print


	# Uses ORIGIN and SUFFIX found in jointName to get location (arm, back, tail, etc)
	fkSuffix = 'fk'
	ikSuffix = 'ik'
	fkWaste_Suffix = 'fk_waste'
	ikEnd_Suffix = 'ik_last'

	pm.duplicate(joint_chain, n = 'fk_cahin')
	pm.duplicate(joint_chain, n = 'ik_cahin')



	# FK RENAMER LOOP
	# loop statment travels down joint chain
	pm.select( 'fk_cahin')
	currentChain = pm.ls(selection=True, dag=True)


	# Creates a jointPad_group for the joints 
	jointPad_groupName = '{0}_{1}_00_pad'.format(ori, location)
	jointPad_group = pm.group(name = jointPad_groupName, em=True)

	# jointPad group cleanup
	pm.delete(constructionHistory=True)
	pm.makeIdentity(apply=True)
	pm.xform(centerPivots=True)
	    
	# Print statments in editor. For debugging
	print
	print 'Empty Group Created: ', jointPad_group
	print

	# Parents joints to thier pad
	# >jointPad_group
	#   ---> joints
	pm.parent(userSelection, jointPad_group)

	print 'Joint Chain has been padded'


	FKcount = 1
	for current_joint in currentChain:

		fkName = '{0}_{1}_0{2}_{3}'.format(ori, location, FKcount, fkSuffix)

		current_joint.rename(fkName)

		print 'FKJoint Name: ', fkName

		if FKcount == 1:
			# Giving first FK joint a variable
			firstFK_joint = current_joint
			FKcount = FKcount + 1
		elif FKcount == 2:
			# Gives the middle IK joint a variable for making a point constraint
			middleFK_joint = current_joint
			FKcount = FKcount + 1
		else:
			# The FKcount is used for naming purposes
			FKcount = FKcount + 1

	#renaming the last joint to 'waste,end,last...' and giving it a variable for creating a ikfk control icon
	fkName = '{0}_{1}_0{2}_{3}'.format(ori, location, FKcount-1, fkWaste_Suffix)
	current_joint.rename(fkName)

	lastFK_joint = current_joint

	print
	print 'First FKJoint Name: ', firstFK_joint
	print 'Last FKJoint Name: ', lastFK_joint
	print

	print
	print'FKJoint Chain Renamed'
	print


	# IK RENAMER LOOP
	# loop statment travels down joint chain
	pm.select( 'ik_cahin')
	currentChain = pm.ls(selection=True, dag=True)

	IKcount = 1
	for current_joint in currentChain:

		ikName = '{0}_{1}_0{2}_{3}'.format(ori, location, IKcount, ikSuffix)

		current_joint.rename(ikName)

		print 'IKJoint Name: ', ikName

		if IKcount == 1:
			# Giving first IK joint a variable
			firstIK_joint = current_joint
			IKcount = IKcount + 1

		elif IKcount == 2:
			# Gives the middle IK joint a variable for making a point constraint
			middleIK_joint = current_joint
			IKcount = IKcount + 1

		else:
			# The IKcount is used for naming purposes
			IKcount = IKcount + 1

	#renaming the last joint to 'waste,end,last...' and giving it a variable for creating a ikfk control icon
	ikName = '{0}_{1}_0{2}_{3}'.format(ori, location, IKcount-1, ikEnd_Suffix)
	current_joint.rename(ikName)

	lastIK_joint = current_joint

	print
	print 'First IKJoint Name: ', firstIK_joint
	print 'Last IKJoint Name: ', lastIK_joint
	print

	print
	print'IKJoint Chain Renamed'
	print

	# create FK joint pad, and primed controls for FK
	pm.select( firstFK_joint)
	currentChain = pm.ls(selection=True, dag=True)

	print currentChain

	# loop that move down joint chain and creates groups/icons/hierarchy
	count = 1
	for current_joint in currentChain:

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
	        groupName = '{0}_{1}_0{2}_fk_prime'.format(ori, location, count)
	        iconName = '{0}_{1}_0{2}_fk_icon'.format(ori, location, count)

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

	        #constraining control to joint
	        pm.orientConstraint(new_controlIcon, current_joint)

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







	# Creates a world group so joints and control arn't far aprt
	fkWorld_groupName = '{0}_{1}_fk_pad'.format(ori, location)
	fkWorld_group = pm.group(name = fkWorld_groupName, em=True)

	# world group cleanup
	pm.delete(constructionHistory=True)
	pm.makeIdentity(apply=True)
	pm.xform(centerPivots=True)
	    
	# Print statments in editor. For debugging
	print
	print 'Empty Group Created: ', fkWorld_group
	print



	# Creates a Pad_group for the fk_joints 
	fk_jointPad_groupName = '{0}_{1}_00_fk_pad'.format(ori, location)
	fk_jointPad_group = pm.group(name = fk_jointPad_groupName, em=True)

	# jointPad group cleanup
	pm.delete(constructionHistory=True)
	pm.makeIdentity(apply=True)
	pm.xform(centerPivots=True)
	    
	# Print statments in editor. For debugging
	print
	print 'Empty Group Created: ', fk_jointPad_group
	print



	# Parents joints to thier pad
	# >fk_jointPad_group
	#   ---> joints
	pm.parent(firstFK_joint, fk_jointPad_group)


	# parents both the joints and the pad/icons to the would group
	# Result
	# >HierarchyProject_world
	#   ---> pads/controls group
	#   ---> fk_jointPad_group
	pm.parent(fk_jointPad_group, fkWorld_group)
	pm.parent(parentPad, fkWorld_group)

	pm.select(firstIK_joint)
	currentChain = pm.ls(selection=True)


	# Creates a Pad_group for the ik_joints 
	ik_jointPad_groupName = '{0}_{1}_00_IK_pad'.format(ori, location)
	ik_jointPad_group = pm.group(name = ik_jointPad_groupName, em=True)

	# jointPad group cleanup
	pm.delete(constructionHistory=True)
	pm.makeIdentity(apply=True)
	pm.xform(centerPivots=True)
	    
	# Print statments in editor. For debugging
	print
	print 'Empty Group Created: ', ik_jointPad_group
	print

	# Parents joints to thier pad
	# >ik_jointPad_group
	#   ---> joints
	pm.parent(currentChain, ik_jointPad_group)

	# Create primed ik control
	# making the final names from the variables
	ikPrime_groupName = '{0}_{1}_00_{2}'.format(ori, location, 'ik_prime')
	ik_controlIcon_name = '{0}_{1}_{2}'.format(ori, location, 'ik_icon')
	ikHandle_name = '{0}_{1}_{2}'.format(ori, location, 'ik')

	# Create ik handle and effector
	new_ik = pm.ikHandle( n=ikHandle_name, sj=firstIK_joint, ee=lastIK_joint)#, srp = True,)
	ik_handle = pm.ls(new_ik)

	pm.select(new_ik)
	ik_handle = pm.ls(selection=True)
	noEffector = ik_handle[0]

	# Square control icon
	ik_controlIcon = pm.curve(d=1, p=[(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1), (-1,0,-1)])
	pm.setAttr('.rotateZ', -90)
	pm.makeIdentity(ik_controlIcon, apply=True, t=True, r=True, s=True)

	selectedIcon = pm.select(ik_controlIcon)
	pm.rename(selectedIcon, ik_controlIcon_name)

	# Print statments in editor. For debugging
	print
	print 'IK Control Icon created: ', ik_controlIcon
	print

	#GROUP CREATION
	new_group = pm.group(name = ikPrime_groupName, em=True)

	# group cleanup
	pm.delete(constructionHistory=True)
	pm.makeIdentity(apply=True)
	pm.xform(centerPivots=True)

	# Print statments in editor. For debugging
	print
	print 'Empty Group Created: ', new_group
	print

	# meeseeks is contraint code that moves the controls/groups and orients them to the joints
	# meeseeks then deleates itself having surved its purpose

	# meeseeks for the group (constrains to joint)
	meeseeks = pm.parentConstraint(lastIK_joint, new_group)
	pm.delete(meeseeks)

	# meeseeks for the icon (constrains to group)
	meeseeks = pm.parentConstraint(new_group, ik_controlIcon)
	pm.delete(meeseeks)

	# parents the helpless icon to the group so it can feel safe
	# result:
	#   >new_group
	#    -->ik_controlIcon
	#	 -->ik_handle
	pm.parent(ik_controlIcon, new_group)
	pm.parent(noEffector, new_group)

	#Constrains ik icon to ik handle
	pm.parentConstraint(ik_controlIcon, noEffector, mo = True)


	# create ik/fk switch control on last selected joint 
	#switchJoint

	switchJoint = lastIK_joint

	# making the final names from the variables
	ikfk_groupName = '{0}_{1}_ikfk_prime'.format(ori, location)
	ikfk_iconName = '{0}_{1}_ikfk_icon'.format(ori, location)

	#GROUP CREATION
	new_group = pm.group(name = ikfk_groupName, em=True)

	# group cleanup
	pm.delete(constructionHistory=True)
	pm.makeIdentity(apply=True)
	pm.xform(centerPivots=True)

	# Print statments in editor. For debugging
	print
	print 'Empty Group Created: ', new_group
	print

	#ICON CREATION
	new_controlIcon = pm.circle(name = ikfk_iconName, r=3, normal=[1,0,0])[0]

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
	meeseeks = pm.parentConstraint(switchJoint, new_group)
	pm.delete(meeseeks)

	# meeseeks for the icon (constrains to group)
	meeseeks = pm.parentConstraint(new_group, new_controlIcon)
	pm.delete(meeseeks)

	# parents the helpless icon to the group so it can feel safe
	# result:
	#   >new_group
	#    -->new_controlIcon
	pm.parent(new_controlIcon, new_group)

	# setting up first ik/fk joints to orient constrain to bind joints
	pm.orientConstraint(firstFK_joint, rootJoint)
	pm.orientConstraint(firstIK_joint, rootJoint)

	# setting up middle ik/fk joints to orient constrain to bind joints
	pm.orientConstraint(middleFK_joint, midRootJoint)
	pm.orientConstraint(middleIK_joint, midRootJoint)


	new_controlIcon.addAttr('switch', at = 'float', max = 10, min = 0, keyable = True)




	pm.select(userSelection)


print
print
print
print 'UNABLE TO CODE SET DRIVEN KEYS'
print
print
print










