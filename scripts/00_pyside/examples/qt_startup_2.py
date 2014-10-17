'''
Michael Clavan
qt_startup.py

How to Run:

import qt_startup
reload(qt_startup)
qt_startup.gui()
'''


'''
Getting started with Qt in Python



'''

import sys
from PySide import QtCore, QtGui
 
class StarterExample(QtGui.QWidget):
    def __init__(self):
        super(StarterExample, self).__init__()

        self.widget()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('My Form Example')    
        self.show()

    def widget(self):
        btn = QtGui.QPushButton('My Button', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50) 
         

def gui():
	global qt_window_object
	qt_window_object = StarterExample()

'''

'''