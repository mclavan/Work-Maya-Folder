'''
Michael Long
jointRenamer.py

HOW TO RUN:
 
import jointRenamer
reload (jointRenamer)
jointRenamer.function()
'''

print' '
print 'jointRenamer.py is running.'
print' '

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm



def jointRenamer_inputGUI():
	#The window and layout for the GUI
	#Was made adjustable so the tool could be miniminzed and take up less space
	inputGUI_win = pm.window(w=500, h=300, title='Joint Renamer: Input Window')
	main = pm.columnLayout(w=500, h=300, adjustableColumn=False)

	print
	print 'jointRenamer.jointRenamer_inputGUI is running'
	print

	# needed global variables
	global nf_origin
	global nf_name
	global nf_suffix
	global nf_lastSuffix

	# the text inputs feilds 
	# when  user hits enter the foucus is set on the next feild
	# last enter command lauches code that gather all the inputs
	nf_origin = 	pm.textFieldGrp('nf_origin', 	label='     Joint Origin: ', pht='lt,rt,cnt...         Enter When Complete', changeCommand='pm.setFocus("nf_name")' )
	nf_name = 		pm.textFieldGrp('nf_name', 		label='       Joint Name: ', pht='arm,leg,index...     Enter When Complete', changeCommand='pm.setFocus("nf_suffix")' )
	nf_suffix =     pm.textFieldGrp('nf_suffix', 	label='     Joint Suffix: ', pht='bind,waste,piv...    Enter When Complete', changeCommand='pm.setFocus("nf_lastSuffix")' )
	nf_lastSuffix = pm.textFieldGrp('nf_lastSuffix',label='Last Joint Suffix: ', pht='end,waste,last...    Enter When Complete', changeCommand=finishedTextFeilds_command) # add delete window code

	#Shows the GUI
	inputGUI_win.show()

	# Sets foucus on first field as field is created so user can start typing imediatly
	pm.setFocus("nf_origin")

def finishedTextFeilds_command(*args):
	# function gathers all user inputs and allows other funtions to call the inputs as variables

	# Needed Global variables
	global jointOrigin
	global jointName
	global jointSuffix
	global jointLastSuffix
	
	# Getting user input
	jointOrigin     = nf_origin.getText()
	jointName       = nf_name.getText()
	jointSuffix     = nf_suffix.getText()
	jointLastSuffix = nf_lastSuffix.getText()

	#print statments for debugging
	print
	print
	print jointOrigin
	print jointName
	print jointSuffix
	print jointLastSuffix
	print
	print

	print
	print'Joint Names Recived'
	print

	
	#Put code to close 'inputGUI_win' without crashing maya here

	# Launches the renaming code 
	jointRenamer_renameCommand()


def jointRenamer_renameCommand():

	print
	print "jointRename_function is running"
	print

	#grabs user selection
	joint_chain = pm.ls(selection=True, dag=True)
	print
	print 'Items Selected: ', joint_chain
	print

	# declares naming variables and grabes them from other funtions
	ori = jointOrigin
	name = jointName
	count = 1
	suffix = jointSuffix
	lastSuffix = jointLastSuffix

	# loop statment travels down joint chain
	for current_joint in joint_chain:

		new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count, suffix)

		current_joint.rename(new_name)

		print 'Joint Name: ', new_name

		# The count is used for naming purposes
		count = count + 1

	#renaming the last joint to 'waste,end,last...'
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, name, count-1, jointLastSuffix)
	current_joint.rename(new_name)
	print 'Last Joint Name: ', new_name
	print

	print
	print'Joint Chain Renamed'
	print












