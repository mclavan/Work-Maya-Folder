
# General Python Modules
import sys
import pprint
import os 

# Pyside Modules
from PySide.QtCore import *
from PySide.QtGui import *

# Maya Modules
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from pysideuic import compileUi

# Custom Interface Module
import uic_exporter
reload(uic_exporter)


class UIC_Window(QDialog, uic_exporter.Ui_Dialog):
	def __init__(self, parent=None):
		super(UIC_Window, self).__init__(parent)
		self.setupUi(self)

		self.output_path = ''
		self.ui_path = ''

		self.connect(self.export_btn, SIGNAL('clicked()'), self.export)
		self.connect(self.ui_btn, SIGNAL('clicked()'), self.get_uic)	
		self.connect(self.output_btn, SIGNAL('clicked()'), self.get_output)


	def get_output(self):
		print 'Button has been pressed.'
		self.output_path, _ = QFileDialog.getSaveFileName(self, 'Open file', '/home')
		self.output_input.setText(self.output_path)

	def get_uic(self):
		self.ui_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home', "UI File (*.ui)")
		self.ui_input.setText(self.ui_path)
		temp_path, ui_file = os.path.split(self.ui_path)
		new_file = '{0}.py'.format(ui_file.split('.')[0])
		expected_path = os.path.join(temp_path, new_file)
		self.output_input.setText(expected_path)

	def export(self):
		self.ui_path = self.ui_input.text()
		self.output_path = self.output_input.text()

		pyfile = open(self.output_path, 'w')
		compileUi(self.ui_path, pyfile, False, 4, False)
		pyfile.close()

		# Orginal Code - Maya uic generator
		# ui_file_path = r'/Users/mclavan/Desktop/testWin.ui'
		# python_output = r'/Users/mclavan/Desktop/testWin.py'
		# pyfile = open(python_output, 'w')
		# compileUi(ui_file_path, pyfile, False, 4, False)
		# pyfile.close()


class MyDockableWindow(MayaQWidgetDockableMixin, UIC_Window):
    def __init__(self, parent=None):
        super(MyDockableWindow, self).__init__(parent=parent)
        # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred )
        #self.setText('Push Me')


def gui(dock=False):
	button = MyDockableWindow()
	button.show(dockable=dock)    


