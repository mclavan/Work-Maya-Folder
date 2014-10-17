"""
ZetCode PySide tutorial 

In this example, we dispay an image
on the window. 

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011

import pixmap
reload(pixmap)
pixmap.gui()


"""

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap(":/k3b.png")
        p5 = QtGui.QPixmap(':/help-browser.png')

        lbl = QtGui.QLabel(parent=self)
        lbl.setPixmap(pixmap)

        btn = QtGui.QPushButton(icon=p5, parent=self)
        # btn.move(0, 50)
        # lbl.move(0, 75)
        hbox.addWidget(lbl)
        hbox.addWidget(btn)

        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Red Rock')
        self.show()        
 
def gui():
    global ex
    ex = Example()


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()