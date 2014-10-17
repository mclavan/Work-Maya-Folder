# Easy Control Colors Tool
# Shane King
# Changes the colors of your Icons based on orientation naming convention
#### ASSUMPTIONS
#### 1. The suffix of your controls end with _icon
##### 2. Your prefix is your orientation


#### Instructions:
# Select ONE color at a time by clicking the checkbox.
### It will not work with more than one color selected at once.

## next, Enter the naming convention for your orientation
# Example : "lt", "cnt", "rt"
# Press the Go! button

# to close the window , simply press the red x at the upper left corner.



# import EasyColorControls as ECC
# reload(ECC)
#ECC.UI()



import pymel.core as pm



def goButton(*args):
	# take text from textfield
	oriText = pm.textField("oriTF", q = True, text = True)
	# search for the oriText and objects with the suffix icon

	oriControlIcons = pm.ls(oriText + '*_icon')

	# if nothing is entered , give a warning
	if oriText == '':
		pm.warning("No Orientation Has Been Typed.")

	# set up if statements for the checkboxes

	redCB = pm.checkBox('redCB',q = True, v = True)
	blueCB = pm.checkBox('blueCB',q = True, v = True)
	yellowCB = pm.checkBox('yellowCB',q = True, v = True)

	##setAttr "lt_index_01_icon.overrideEnabled" 1;

	if redCB:

		for icon in oriControlIcons:
			icon.overrideEnabled.set(1)
			icon.overrideColor.set(13)

		#pm.color(oriControlIcons, ud = 1)

	elif blueCB:

		for icon in oriControlIcons:
			icon.overrideEnabled.set(1)
			icon.overrideColor.set(6)

		#pm.color(oriControlIcons, ud = 2)

	elif yellowCB:

		for icon in oriControlIcons:
			icon.overrideEnabled.set(1)
			icon.overrideColor.set(17)

		#pm.color(oriControlIcons, ud = 3)



	print 'Control Colors Have Been Assigned.'

	
def UI():
	# Create a window that has the Set up You want

	#if the window, exists, delete window
	if pm.window("ECC", exists = True):
	    pm.deleteUI("ECC")

	window = pm.window("ECC", w = 300, h = 200, title = "ECC",
	    mxb = False, mnb = False, sizeable = False)

	#create the layout
	layout = pm.formLayout()

	# Create Check Boxes for Red , Blue, and Yellow

	redCB = pm.checkBox('redCB',label = 'RED')
	blueCB = pm.checkBox('blueCB',label = 'BLUE')

	yellowCB = pm.checkBox('yellowCB',label = 'YELLOW')


	


	# Assign Text Variables

	boldTitle = pm.text(label = 'EASY CONTROL COLORS')
	insText = pm.text(label = 'Enter the orientation for the control icon')


	# Assign Text Field

	oriInput = pm.textField("oriTF", w = 80, enable = True)


	# Create the go button

	gobutton = pm.button(label = 'GO!', w = 80, command = goButton)


	# Layout the items

	pm.formLayout(layout, edit = True, af = [(boldTitle, 'left', 85), (boldTitle, 'top', 10) ])
	pm.formLayout(layout, edit = True, af = [(oriInput, 'left', 110), (oriInput, 'bottom', 40) ])
	pm.formLayout(layout, edit = True, af = [(redCB, 'left', 40), (redCB, 'top', 40) ])
	pm.formLayout(layout, edit = True, af = [(blueCB, 'left', 110), (blueCB, 'top', 40) ])
	pm.formLayout(layout, edit = True, af = [(yellowCB, 'right', 40), (yellowCB, 'top', 40) ])
	pm.formLayout(layout, edit = True, af = [(insText, 'left', 45), (insText, 'bottom', 65) ])
	pm.formLayout(layout, edit = True, af = [(gobutton, 'left', 110), (gobutton, 'bottom', 10) ])


	#show the window 
	pm.showWindow(window)	



