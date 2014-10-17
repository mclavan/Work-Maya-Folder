# Hide Show Lock Attributes
#Shane King
# This tool Will Hide Show And Lock The Checked Attributes
# Select the attribute that you want to hide, show, or lock, then press the associated button
# show button , will show and unlock your attributes.


import pymel.core as pm
def lockButton(*args):

	translateCB = pm.checkBox('translateCB',q = True, v = True)
	rotateCB = pm.checkBox('rotateCB',q = True, v = True)
	scaleCB = pm.checkBox('scaleCB',q = True, v = True)
	visibilityCB = pm.checkBox('visibilityCB',q = True, v = True)

	if translateCB:
		pm.setAttr(".tx", lock = True)
		pm.setAttr(".ty", lock = True)
		pm.setAttr(".tz", lock = True)
		print "Translate Attributes Have Been Locked."

	if rotateCB:
		pm.setAttr(".rx", lock = True)
		pm.setAttr(".ry", lock = True)
		pm.setAttr(".rz", lock = True)
		print "Rotate Attributes Have Been Locked."

	if scaleCB:
		pm.setAttr(".sx", lock = True)
		pm.setAttr(".sy", lock = True)
		pm.setAttr(".sz", lock = True)
		print "Scale Attributes Have Been Locked."

	if visibilityCB:
		pm.setAttr(".v", lock = True)
		pm.setAttr(".v", lock = True)
		pm.setAttr(".v", lock = True)
		print "Visibility Attribute Has Been Locked."

def hideButton(*args):

	translateCB = pm.checkBox('translateCB',q = True, v = True)
	rotateCB = pm.checkBox('rotateCB',q = True, v = True)
	scaleCB = pm.checkBox('scaleCB',q = True, v = True)
	visibilityCB = pm.checkBox('visibilityCB',q = True, v = True)

	if translateCB:
		pm.setAttr(".tx", keyable = False)
		pm.setAttr(".ty", keyable = False)
		pm.setAttr(".tz", keyable = False)
		print "Translate Attributes Have Been Hidden."

	if rotateCB:
		pm.setAttr(".rx", keyable = False)
		pm.setAttr(".ry", keyable = False)
		pm.setAttr(".rz", keyable = False)
		print "Rotate Attributes Have Been Hidden."

	if scaleCB:
		pm.setAttr(".sx", keyable = False)
		pm.setAttr(".sy", keyable = False)
		pm.setAttr(".sz", keyable = False)
		print "Scale Attributes Have Been Hidden."

	if visibilityCB:
		pm.setAttr(".v", keyable = False)
		pm.setAttr(".v", keyable = False)
		pm.setAttr(".v", keyable = False)
		print "Visibility Attribute Has Been Hidden."

def showButton(*args):

	translateCB = pm.checkBox('translateCB',q = True, v = True)
	rotateCB = pm.checkBox('rotateCB',q = True, v = True)
	scaleCB = pm.checkBox('scaleCB',q = True, v = True)
	visibilityCB = pm.checkBox('visibilityCB',q = True, v = True)

	if translateCB:
		pm.setAttr(".tx", lock = False, keyable = True)
		pm.setAttr(".ty", lock = False, keyable = True)
		pm.setAttr(".tz", lock = False, keyable = True)
		print "Translate Attributes Have Been Hidden."

	if rotateCB:
		pm.setAttr(".rx", lock = False, keyable = True)
		pm.setAttr(".ry", lock = False, keyable = True)
		pm.setAttr(".rz", lock = False, keyable = True)
		print "Rotate Attributes Have Been Hidden."

	if scaleCB:
		pm.setAttr(".sx", lock = False, keyable = True)
		pm.setAttr(".sy", lock = False, keyable = True)
		pm.setAttr(".sz", lock = False, keyable = True)
		print "Scale Attributes Have Been Hidden."

	if visibilityCB:
		pm.setAttr(".v", lock = False, keyable = True)
		pm.setAttr(".v", lock = False, keyable = True)
		pm.setAttr(".v", lock = False, keyable = True)
		print "Visibility Attribute Has Been Hidden."

def UI():

	# Create a window that has the Set up You want


	#if the window, exists, delete window
	if pm.window("HSL", exists = True):
	    pm.deleteUI("HSL")

	window = pm.window("HSL", w = 300, h = 200, title = "HSL",
	    mxb = False, mnb = False, sizeable = False)

	#create the layout
	layout = pm.formLayout()

	#Create Color Title
	redHideText = pm.text('HIDE, SHOW, AND LOCK TOOL', fn = "obliqueLabelFont",  bgc = [.6, 0.3, 0.0])
	

	# Create Info Text

	infoText = pm.text('Select the attributes that you would like to affect.')


	# Create Check Boxes for Translate , Rotate , Scale, and Visability

	translateCB = pm.checkBox('translateCB',label = 'Translate')
	rotateCB = pm.checkBox('rotateCB',label = 'Rotate')
	scaleCB = pm.checkBox('scaleCB',label = 'Scale')
	visibilityCB = pm.checkBox('visibilityCB',label = 'Visibility')

	# Create 3 buttons

	lockbutton = pm.button(label = "LOCK", h = 40, w = 60, command = lockButton)
	hidebutton = pm.button(label = "HIDE", h = 40, w = 60, command = hideButton)
	showbutton = pm.button(label = "SHOW", h = 40, w = 60, command = showButton)

	# Layout the Items

	pm.formLayout(layout, edit = True, af = [(lockbutton, 'left', 45), (lockbutton, 'bottom', 10) ])
	pm.formLayout(layout, edit = True, af = [(hidebutton, 'left', 120), (hidebutton, 'bottom', 10) ])
	pm.formLayout(layout, edit = True, af = [(showbutton, 'left', 200), (showbutton, 'bottom', 10) ])


	pm.formLayout(layout, edit = True, af = [(translateCB, 'left', 45), (translateCB, 'top', 40) ])
	pm.formLayout(layout, edit = True, af = [(rotateCB, 'left', 200), (rotateCB, 'top', 40) ])
	pm.formLayout(layout, edit = True, af = [(scaleCB, 'left', 45), (scaleCB, 'top', 60) ])
	pm.formLayout(layout, edit = True, af = [(visibilityCB, 'left', 200), (visibilityCB, 'top', 60) ])

	pm.formLayout(layout, edit = True, af = [(infoText, 'left', 20), (infoText, 'bottom', 90) ])
	pm.formLayout(layout, edit = True, af = [(redHideText, 'left', 65), (redHideText, 'top', 10) ])

	#show the window 
	pm.showWindow(window)	

UI()