'''
#CHECKBOXES AND TEXTBOXES OH MY

import shane_cmds
reload(shane_cmds)
shane_cmds.mainGUI()
'''

import maya.cmds as cmds
import pymel.core as pm 

'''
def mainGUI():
    if cmds.window('mainWindow', ex=True):
        cmds.deleteUI('mainWindow', window=True)
      
    cmds.window('mainWindow', title='TEST', width=140)
    cmds.columnLayout()
    
    cmds.checkBox('myCheck', label='History', onc=swapOn, ofc=swapOn)
    cmds.text(label='')
    
    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 60), (2, 80)])
    cmds.text(label='Name')
    cmds.textField('tFieldname', w=80)
    cmds.text(label='Width')
    cmds.textField('tFieldx', w=80)
    cmds.text(label='Height')
    cmds.textField('tFieldy', w=80)
    cmds.text(label='Depth')    
    cmds.textField('tFieldz', w=80)
    cmds.setParent('..')
    cmds.text(label='')
    cmds.button('myButton', l='Execute', w=140, c=executeButton)
    
    cmds.showWindow('mainWindow')
'''
def mainGUI():    
    global window_name
    window_name = 'shane_main_window'

    if pm.window(window_name, ex=True):
        pm.deleteUI(window_name, window=True)
      
    window_obj = pm.window(window_name, title='TEST', width=140)
    pm.columnLayout()
    
    global history_checkBox, name_field, width_field, hieght_field, depth_field, execute_button
    history_checkBox = pm.checkBox(label='History', onc=pm.Callback(swapOn), ofc=pm.Callback(swapOn))
    pm.text(label='')
    
    pm.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 60), (2, 80)])
    pm.text(label='Name')
    name_field = pm.textField(w=80)
    pm.text(label='Width')
    width_field = pm.floatField(w=80, value=2)
    pm.text(label='Height')
    hieght_field = pm.floatField(w=80, value=2)
    pm.text(label='Depth')    
    depth_field = pm.floatField(w=80, value=2)
    pm.setParent('..')
    pm.text(label='')
    execute_button = pm.button(l='Execute', w=140, c=pm.Callback(executeButton))
    
    window_obj.show()

# def querySelected(*args):
#     return cmds.checkBox('myCheck', q=True, v=True)
    
def executeButton():
    cube_name = name_field.getText()
    cube_width = width_field.getValue()
    cube_height = hieght_field.getValue()
    cube_depth = depth_field.getValue()
    history_state = history_checkBox.getValue()

    pm.polyCube(ch=history_state, 
        w=cube_width, 
        h=cube_height,
        d=cube_depth,
        n=cube_name)

    # cmds.polyCube(ch=querySelected(), 
    #     w=cmds.textField('tFieldx', q=True, tx=True),
    #     h=cmds.textField('tFieldy', q=True, tx=True),
    #     d=cmds.textField('tFieldz', q=True, tx=True),
    #     n=cmds.textField('tFieldname', q=True, tx=True))

def swapOn():
    history_state = history_checkBox.getValue()
    if history_state:
        execute_button.setLabel('With History')
        # cmds.button('myButton', e=True, l='With History')
    else:
        execute_button.setLabel('Without History')
        # cmds.button('myButton', e=True, l='Without History')
