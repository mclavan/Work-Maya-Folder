'''
Steffan Lones
Renaming tool
Description:
	To add prefixes, suffixes, and to search for and replace words

how to run:
import renameTool
reload(renameTool)
'''

import maya.cmds as cmds
from functools import partial

#Start with getting Suffix
def addPrefixOrSuffix(type, text):

	#get our selection
	selection = cmds.ls(sl=True)
	if len(selection) > 0:
		
		#prevent things from being added if string is empty
		if text != "":
		
			if type == "prefix":
				for object in selection:
					cmds.rename(object, text + "_" + object)
			
			if type == "suffix":
				for object in selection:
					cmds.rename(object, object + "_" + text)


def checkBoxChanged(type, *args):

	#get the value of the passed in checkbox
	value = cmds.checkBox(type + "CB", q = True, v = True)

	if value == True:
		if type == "searchReplace":
			cmds.textField("searchTF",edit = True, enable = True)
			cmds.textField("replaceTF",edit = True, enable = True)


		else:		
			cmds.textField(type + "TF" , edit = True, enable = True)
	if value == False:
		if type == "searchReplace":
			cmds.textField("searchTF",edit = True, enable = False)
			cmds.textField("replaceTF",edit = True, enable = False)


		else:
			cmds.textField(type + "TF", edit = True , enable = False)


def accept(*args):

	#get the value of the checkboxes
	prefixCB = cmds.checkBox("prefixCB", q = True, v = True)
	suffixCB = cmds.checkBox("suffixCB", q = True, v = True)
	searchReplaceCB = cmds.checkBox("searchReplaceCB", q = True , v = True)

	if prefixCB:
		text = cmds.textField("prefixTF" , q = True, text = True)
		addPrefixOrSuffix("prefix" , text)
		cmds.textField("prefixTF" , edit = True, text = "",enable = False)

	if suffixCB:
		text = cmds.textField("suffixTF" , q = True , text = True)
		addPrefixOrSuffix("suffix", text)
		cmds.textField("suffixTF" , edit = True , text = "", enable = False)

	if searchReplaceCB:
		searchText = cmds.textField("searchTF" , q = True , text = True)
		replaceText = cmds.textField("replaceTF" , q = True , text = True)
		searchAndReplace(searchText, replaceText)
		cmds.textField("searchTF" , edit = True , text = "" , enable = False)
		cmds.textField("replaceTF" , edit = True , text = "" , enable = False)

	for checkbox in["prefixCB", "suffixCB" , "searchReplaceCB"]:
		cmds.checkBox(checkbox, edit = True , v = False)


def searchAndReplace(searchText, replaceText):
	
	selection = cmds.ls(sl=True)
	notFound = False
	if len(selection) > 0:
		for object in selection:
			if object.find(searchText) !=-1:
				newName = object.replace(searchText, replaceText)
				cmds.rename(object, newName)
			if object.find(searchText) == -1:
				notFound = True 
	if notFound:
		cmds.warning("Search text is invalid")


def cancel(*args):
	cmds.deleteUI("renamerUI")


def UI():

	#if the window exsists, kill the window
	if cmds.window("renamerUI", exists = True):
		cmds.deleteUI("renamerUI")

	window = cmds.window("renamerUI", w = 300 , h = 200 , title = "Renamer", mxb = False , mnb = False , sizeable = False)

	#create the layout
	layout = cmds.formLayout()

	# create prefix and suffix and suffix checkboxes
	prefixCB = cmds.checkBox("prefixCB" , label = "Add Prefix" , v = False , cc = partial(checkBoxChanged , "prefix"))
	suffixCB = cmds.checkBox("suffixCB" , label = "Add Suffix" , v = False , cc = partial(checkBoxChanged , "suffix"))
	searchReplaceCB = cmds.checkBox("searchReplaceCB", label = "Search/Replace", v = False , cc = partial(checkBoxChanged, "searchReplace"))

	textA = cmds.text(label = "Prefix:")
	textB = cmds.text(label = "Suffix:")
	prefixTF = cmds.textField("prefixTF" , w = 200, enable = False)
	suffixTF = cmds.textField("suffixTF" , w = 200, enable = False)

	textC = cmds.text(label = "Search For:")
	textD = cmds.text(label = "Replace With:")
	searchTF = cmds.textField("searchTF" , w = 200, enable = False)
	replaceTF = cmds.textField("replaceTF" , w = 200, enable = False)

	acceptButton = cmds.button(label = "Accept" , w = 135 , command = accept)
	cancelButton = cmds.button(label = "Cancel" , w = 135 , command = cancel)

	# layout the items
	cmds.formLayout(layout, edit = True, af = [(prefixCB, "left" , 10) , (prefixCB, "top" , 10 )])
	cmds.formLayout(layout, edit = True, af = [(suffixCB, "left" , 100) , (suffixCB, "top" , 10 )])
	cmds.formLayout(layout, edit = True, af = [(searchReplaceCB, "right" , 10) , (searchReplaceCB, "top" , 10 )])
	cmds.formLayout(layout, edit = True, af = [(prefixTF, "left" , 80) , (prefixTF, "top" , 35 )])
	cmds.formLayout(layout, edit = True, af = [(suffixTF, "left" , 80) , (suffixTF, "top" , 60 )])
	cmds.formLayout(layout, edit = True, af = [(textA, "left" , 10) , (textA, "top" , 35 )])
	cmds.formLayout(layout, edit = True, af = [(textB, "left" , 10) , (textB, "top" , 60 )])
	cmds.formLayout(layout, edit = True, af = [(searchTF, "left" , 80) , (searchTF, "top" , 100 )])
	cmds.formLayout(layout, edit = True, af = [(replaceTF, "left" , 80) , (replaceTF, "top" , 130 )])
	cmds.formLayout(layout, edit = True, af = [(textC, "left" , 10) , (textC, "top" , 100 )])
	cmds.formLayout(layout, edit = True, af = [(textD, "left" , 10) , (textD, "top" , 130 )])
	cmds.formLayout(layout, edit = True, af = [(acceptButton, "left" , 10) , (acceptButton, "bottom" , 10 )])
	cmds.formLayout(layout, edit = True, af = [(cancelButton, "right" , 10) , (cancelButton, "bottom" , 10 )])

	#show the window
	cmds.showWindow(window)
