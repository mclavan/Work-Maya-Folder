'''
Starter PySide Window
starter_pyside.py

import starter_pyside
reload(starter_pyside)
starter_pyside.gui()

'''

from PySide import QtGui, QtCore
from shiboken import wrapInstance
from maya.OpenMayaUI import MQtUtil
import pymel.core as pm

import os

def mayaMainWindow():
    mainWinPtr = MQtUtil.mainWindow()
    return wrapInstance(long(mainWinPtr), QtGui.QWidget)

class StarterWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        if parent == None:
            parent = mayaMainWindow()
        super(StarterWindow, self).__init__(parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setGeometry(300, 300, 300, 350)
        self.setWindowTitle("Starter Window")
        self.initUI()
    
    def initUI(self):
        self.mainLO = QtGui.QVBoxLayout()
        self.mainLO.setSpacing(10)
        self.btns_layout = self.button_items()
        self.mainLO.addLayout(self.btns_layout)
        self.setLayout(self.mainLO)

        self.show()

    def button_items(self):
    	button_layout = QtGui.QHBoxLayout()
        # QIcon(":/images/print.png")
        pix_icon = QtGui.QPixmap(':/akregator.png')
        p5 = QtGui.QPixmap(':/examples/help-browser.png')
        # p5 = QtGui.QPixmap(':/help-browser.png')
        icon = QtGui.QIcon(pix_icon)
    	btn1 = QtGui.QPushButton(icon=pix_icon)
    	# btn1.setIcon(QtGui.QIcon(':/examples/kchart.png'))
        # btn1.setIcon(icon)
        

        button_layout.addWidget(btn1)
    	return button_layout


def gui():
	global win
	win = StarterWindow()

