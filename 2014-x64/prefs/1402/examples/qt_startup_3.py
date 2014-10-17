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
        self.btn = QtGui.QPushButton('My Button', self)
        # Event Handling (Signals and Slots)
        # http://qt-project.org/wiki/Signals_and_Slots_in_PySide
        self.btn.clicked.connect(self.clicked)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50) 


    def clicked(self):
    	'''
    	Connections are done between single and slots.
    	'''
    	print 'Button Clicked....'


def gui():
	global qt_window_object
	qt_window_object = StarterExample()

'''

'''