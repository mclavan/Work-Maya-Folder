#### Renamer Tool ######
# Shane King
#### Renames all of your selection and more!#######
#Instructions

# Make your selection
##Do one part at a time
## example : Do the prefix, than press accept, than do the suffix , accept, then search and replace, accept
## doing it in an order of operation will prevent problems.

import maya.cmds as mc
from functools import partial

def addPrefixOrSuffix(type, text):
    
    #get our selection
    selection = mc.ls(sl = True)
    
    if len(selection) > 0:
        
        
        #ask the user for prefix or suffix
        
        if text != "": 
        
            if type == "prefix":
                for object in selection:
                    mc.rename(object, text + "_" + object)
                  
            if type == "suffix":
                for object in selection:
                    mc.rename(object, object + "_" + text)
           

def checkBoxChanged(type, *args):

    # get the value of checkbox
    value = mc.checkBox(type + "CB", q = True, v = True)

    #highlight the text field if the checkbox is clicked

    if value == True:
        if type == "searchReplace":
            mc.textField("searchTF", edit = True, enable = True)
            mc.textField("replaceTF", edit = True, enable = True)


        else:
            mc.textField(type + "TF", edit = True, enable = True)

    if value == False:
        if type == "searchReplace":
            mc.textField("searchTF", edit = True, enable = False)
            mc.textField("replaceTF", edit = True, enable = False)

        else:
            mc.textField(type + "TF", edit = True, enable = False)







def accept(*args):

    # get the values of the checkbox
    prefixCB = mc.checkBox("prefixCB", q = True, v = True)
    suffixCB = mc.checkBox("suffixCB", q = True, v = True)
    searchReplaceCB = mc.checkBox("searchReplaceCB", q = True, v = True)

    if prefixCB:

        text = mc.textField("prefixTF", q = True, text = True)
        addPrefixOrSuffix("prefix", text)

    if suffixCB: 

        text = mc.textField("suffixTF", q = True, text = True)
        addPrefixOrSuffix("suffix", text)

    if searchReplaceCB:
        searchText = mc.textField("searchTF", q = True, text = True)
        replaceText = mc.textField("replaceTF", q = True, text = True)
        searchAndReplace(searchText, replaceText)


    

def searchAndReplace(searchText, replaceText):
    # get selection
    selection = mc.ls(sl = True)
    notFound = False

    
    if len(selection) > 0:
        
        for object in selection:
            if object.find(searchText) != 0:
                newName = object.replace(searchText, replaceText)
                mc.rename(object, newName)

            if object.find(searchText) == -1:
                notFound = True

    if notFound:
        mc.warning("Search Text Was Not Found")
                

def cancel(*args):

    mc.deleteUI("RenamerUI")

def UI():
    #if the window, exists, delete window
    if mc.window("RenamerUI", exists = True):
        mc.deleteUI("RenamerUI")

    window = mc.window("RenamerUI", w = 300, h = 200, title = "Renamer",
        mxb = False, mnb = False, sizeable = False)

    #create the layout
    layout = mc.formLayout()

    #create prefix and suffix checkboxes

    prefixCB = mc.checkBox("prefixCB", label = "Add Prefix", v = False, cc = partial(checkBoxChanged, "prefix"))
    suffixCB = mc.checkBox("suffixCB", label = "Add Suffix", v = False, cc = partial(checkBoxChanged, "suffix"))
    searchReplaceCB = mc.checkBox("searchReplaceCB", label = "Search/Replace", v = False, cc = partial(checkBoxChanged, "searchReplace"))

    #Create a text field
    textA = mc.text(label = "Prefix:")
    textB = mc.text(label = "Suffix:")
    prefixTF = mc.textField("prefixTF", w = 200, enable = False)
    suffixTF = mc.textField("suffixTF", w = 200, enable = False)

    textC = mc.text(label = "Search For:")
    textD = mc.text(label = "Replace With:")
    searchTF = mc.textField("searchTF", w = 200, enable = False)
    replaceTF = mc.textField("replaceTF", w = 200, enable = False)

    #Create button

    acceptButton = mc.button(label = "Accept", w = 135, command = accept)
    cancelButton = mc.button(label = "Cancel", w = 135, command = cancel)

    #layout the items
    mc.formLayout(layout, edit = True, af = [(prefixCB, "left", 10 ), (prefixCB, "top", 10 ) ])
    mc.formLayout(layout, edit = True, af = [(suffixCB, "left", 100 ), (suffixCB, "top", 10 ) ])
    mc.formLayout(layout, edit = True, af = [(searchReplaceCB, "right", 10 ), (searchReplaceCB, "top", 10 ) ])
    mc.formLayout(layout, edit = True, af = [(prefixTF, "left", 80 ), (prefixTF, "top", 35 ) ])
    mc.formLayout(layout, edit = True, af = [(suffixTF, "left", 80 ), (suffixTF, "top", 60 ) ])
    mc.formLayout(layout, edit = True, af = [(textA, "left", 10 ), (textA, "top", 35 ) ])
    mc.formLayout(layout, edit = True, af = [(textB, "left", 10 ), (textB, "top", 60 ) ])

    mc.formLayout(layout, edit = True, af = [(searchTF, "left", 80 ), (searchTF, "top", 100 ) ])
    mc.formLayout(layout, edit = True, af = [(replaceTF, "left", 80 ), (replaceTF, "top", 130 ) ])
    mc.formLayout(layout, edit = True, af = [(textC, "left", 10 ), (textC, "top", 100 ) ])
    mc.formLayout(layout, edit = True, af = [(textD, "left", 10 ), (textD, "top", 130 ) ])



    mc.formLayout(layout, edit = True, af = [(acceptButton, "left", 10 ), (acceptButton, "bottom", 10 ) ])
    mc.formLayout(layout, edit = True, af = [(cancelButton, "right", 10 ), (cancelButton, "bottom", 10 ) ])

    #show the window 
    mc.showWindow(window)

