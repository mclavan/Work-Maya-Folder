'''
Michael Clavan
layout_play.py

How to Run:

import layout_play
reload(layout_play)
layout_play.gui()
'''


'''
Getting started with Qt in Python



'''

import sys
from PySide import QtCore, QtGui

# import states_rc
 
class StarterExample(QtGui.QWidget):
    def __init__(self):
        super(StarterExample, self).__init__()
               
        self.master_wiget()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('My Form Example')    
        self.show()

    def master_wiget(self):
        group_1 = self.widget()
        group_2 = self.widget()

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(group_1)
        vbox.addSpacing(0)
        vbox.addLayout(group_2)
        vbox.setContentsMargins(0, 11, 0, -1)
        vbox.setDirection(QtGui.QBoxLayout.BottomToTop)

        self.setLayout(vbox)
        
    def widget(self):
        # p5 = Pixmap(QtGui.QPixmap(':/help-browser.png'))
        p5 = QtGui.QPixmap(':/help-browser.png')

        btn_1 = QtGui.QPushButton('Ok')
        btn_1.setMinimumSize(75,24)
        text = QtGui.QLineEdit()
        text.setMinimumSize(200, 24)
        # btn_2 = QtGui.QPushButton('Cancel', self)
        btn_2 = QtGui.QPushButton(icon=p5)

        btn_2.setMinimumSize(75,24)

        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(11, -1, 11, -1)
        hbox.addWidget(btn_1)
        
        hbox.addWidget(text)  
        # hbox.addStretch(1)      
        # hbox.addSpacing(250)
        hbox.addWidget(btn_2)

        return hbox

        '''
        self.btn = QtGui.QPushButton('My Button', self)
        # Event Handling (Signals and Slots)
        # http://qt-project.org/wiki/Signals_and_Slots_in_PySide
        self.btn.clicked.connect(self.clicked)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50) 
        '''

    def clicked(self):
    	'''
    	Connections are done between single and slots.
    	'''
    	print 'Button Clicked....'

class Pixmap(QtGui.QGraphicsObject):
    def __init__(self, pix):
        super(Pixmap, self).__init__()

        self.p = QtGui.QPixmap(pix)

    def paint(self, painter, option, widget):
        painter.drawPixmap(QtCore.QPointF(), self.p)

    def boundingRect(self):
        return QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QSizeF(self.p.size()))


def gui():
	global qt_window_object
	qt_window_object = StarterExample()

'''

'''