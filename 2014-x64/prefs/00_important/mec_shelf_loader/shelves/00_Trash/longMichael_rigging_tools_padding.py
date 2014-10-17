'''
Michael Long
padding.py

HOW TO RUN:
 
import padding
reload (padding)
padding.function()
'''

print
print 'padding is running.'
print

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

def function(*args):
    # calls all code from one clean function

    print
    print 'padding.py has been activated'
    print

    paddingCreator()

def paddingCreator(*args):

	print
	print 'padding.paddingCreator() has been activated'
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
	groupSuffix = 'pad'
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






















