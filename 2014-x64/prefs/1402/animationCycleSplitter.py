'''
Animation Cycle Splitter

Anargyros Kotsaris
2014

This script will take a Maya scene with a continuous
stream of animation and break it up according to
user specifications exporting each animation sequence
as a separate Maya file. All keys are joint based.

If other means unprovided, to use this script place it in
the Maya scripts folder and run the following in the 
script editor:

import animationCycleSplitter
win = animationCycleSplitter.AnimationCycleSplitter()

Must be running Maya 2014+ to use or have PySide installed
'''

from PySide import QtGui, QtCore
from maya.OpenMayaUI import MQtUtil
from shiboken import wrapInstance
import pymel.core as pm
import os
from collections import OrderedDict

def mayaMainWindow():
    mainWinPtr = MQtUtil.mainWindow()
    return wrapInstance(long(mainWinPtr), QtGui.QWidget)

class ExportBar(QtGui.QFrame):
    def __init__(self, parent=None):
        super(ExportBar, self).__init__(parent)
        
        self._parent = parent
        self.resize(parent.width(), 75)
        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        self.setLineWidth(2)
        
        self.initUI()
        
    def initUI(self):
        mainLO = QtGui.QHBoxLayout()
        self.setLayout(mainLO)
        self.setContentsMargins(1, 1, 1, 1)
        
        self.widgets = OrderedDict([
            ("textField", QtGui.QLineEdit()),
            ("fileType", QtGui.QComboBox()),
            ("minFrame", QtGui.QSpinBox()),
            ("dash", QtGui.QLabel("-")),
            ("maxFrame", QtGui.QSpinBox()),
            ("exportButton", QtGui.QPushButton("Export")),
            ("delButton", QtGui.QPushButton("Delete"))
        ])
        
        self.widgets["textField"].setPlaceholderText("File Name")
        self.widgets["fileType"].addItems([".ma", ".mb"])
        self.widgets["minFrame"].setMaximum(99999)
        self.widgets["maxFrame"].setMaximum(99999)
        self.widgets["exportButton"].clicked.connect(self.exportAnimation)
        self.widgets["delButton"].clicked.connect(self.deleteWidget)
        
        for w in self.widgets.values():
            mainLO.addWidget(w)
    
    def deleteWidget(self):
        self._parent.exportBars.remove(self)
        self.close()
        if self._parent.exportBars == []:
            self._parent.newExportBar()
    
    def exportAnimation(self):
        beg, end = self.widgets["minFrame"].value(), self.widgets["maxFrame"].value()
        if self.widgets["textField"].text() != "":
            joints = pm.ls(type="joint")
            pm.select(joints)
            fullPathToFile = os.path.join(self._parent.pathBar.text(), self.widgets["textField"].text() + self.widgets["fileType"].currentText())
            keys = getKeysForFramerange(beg, end, joints)
            keys.insert(0, tPose(joints))
            pm.copyKey()
            pm.cutKey()
            pasteKeysForFramerange(keys)
            pm.currentTime(0)
            pm.exportAll(fullPathToFile, force=1)
            pm.pasteKey()
        else:
            print "# Error: Range {0} - {1} has no specified file name, not exported".format(beg, end),
    

class AnimationCycleSplitter(QtGui.QWidget):
    def __init__(self, parent=None):
        if parent == None:
            parent = mayaMainWindow()
        super(AnimationCycleSplitter, self).__init__(parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setGeometry(1000, 300, 600, 350)
        self.setWindowTitle("Animation Cycle Splitter")
        self.exportBars = []
        self.initUI()
    
    def initUI(self):
        self.mainLO = QtGui.QVBoxLayout()
        self.mainLO.setSpacing(10)
        self.setLayout(self.mainLO)
        
        self.initUpperLO()
        self.initScrollArea()
        self.initLowerLO()
        
        self.show()
    
    def initUpperLO(self):
        upperLO = QtGui.QHBoxLayout()
        
        workScenePath = os.path.join(os.path.normpath(pm.workspace.path), 'scenes\\').replace("\\", "/")
        self.pathBar = QtGui.QLineEdit(workScenePath)
        
        fileButton = QtGui.QPushButton("Browse Files")
        fileButton.clicked.connect(self.changePath)
        
        upperLO.addWidget(self.pathBar)
        upperLO.addWidget(fileButton)
        
        self.mainLO.addLayout(upperLO)
    
    def initScrollArea(self):
        holder = QtGui.QWidget()
        holder.setContentsMargins(1, 1, 1, 1)
        holder.resize(self.width(), 0)
        self.holderLO = QtGui.QVBoxLayout()
        self.holderLO.setContentsMargins(1, 1, 1, 1)
        holder.setLayout(self.holderLO)
        
        self.newExportBar()
        
        scrollArea = QtGui.QScrollArea()
        scrollArea.setWidget(holder)
        scrollArea.setWidgetResizable(True)
        
        self.mainLO.addWidget(scrollArea)
    
    def initLowerLO(self):
        lowerLO = QtGui.QHBoxLayout()
        
        newExpBarButton = QtGui.QPushButton("New Cycle")
        newExpBarButton.clicked.connect(self.newExportBar)
        
        exportAllButton = QtGui.QPushButton("Export All")
        exportAllButton.clicked.connect(self.exportAll)
        
        lowerLO.addWidget(newExpBarButton)
        lowerLO.addWidget(exportAllButton)
        self.mainLO.addLayout(lowerLO)
        
    def changePath(self):
        newPath = pm.fileDialog2(fileMode=3, okc="Select")[0]
        # changing the text of the pathBar will fail since
        # fileDialog2 returns nothing if the user does not select anything
        try:
            self.pathBar.setText(newPath)
        except Exception:
            pass
    
    def newExportBar(self):
        newEB = ExportBar(self)
        self.exportBars.append(newEB)
        self.holderLO.addWidget(newEB)
    
    def exportAll(self):
        for eb in self.exportBars:
            eb.exportAnimation()
    

class Keyframe(object):
    def __init__(self, objs):
        self._frame = pm.currentTime()
        self._values = {attr:attr.get() for obj in objs for attr in obj.listAnimatable()}
        self._objs = objs
    
    def paste(self, frame):
        pm.currentTime(frame)
        for attr in self._values.keys():
            try:
                attr.set(self._values[attr])
            except RuntimeError:
                pass
        pm.setKeyframe(self._objs)
    

def getKeysForFramerange(beg, end, joints):
    keys = []
    for num, frame in enumerate(range(beg, end)):
        pm.currentTime(frame)
        keys.append(Keyframe(joints))
    return keys

def pasteKeysForFramerange(keys):
    for frame, key in enumerate(keys):
        key.paste(frame)

def tPose(joints):
    pm.currentTime(0)
    return Keyframe(joints)

