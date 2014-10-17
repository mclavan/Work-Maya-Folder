'''
mec_shelf_loader.py
Michael Clavan

Description:
	This script is for easy loading and deleting of shelves.

Dependentices:
	Two MEL scripts are required for this script to execute.
	mecLoadShelf.mel
	mecDeleteShelfTab.mel

How to Run:

import mec_shelf_loader.mec_shelf_loader as mec_shelf_loader
reload(mec_shelf_loader)
mec_shelf_loader.gui()

'''
print 'Shelf Loader Activated.'

import sys
import os
import glob
import pymel.core as pm

# Deleting a shelf.
shelf_name = 'clavan_michael'
test_shelf_path = "/Users/mclavan/Desktop/shelf_clavan_michael.mel"


# Sourcing dependant MEL scripts
script_path = os.path.split(__file__)[0]
# pm.mel.source('{0}/mecLoadShelf.mel'.format(script_path))
# pm.mel.source('{0}/mecDeleteShelfTab.mel'.format(script_path))
print script_path

pm.mel.source(os.path.join(script_path, 'mecLoadShelf.mel'))
pm.mel.source(os.path.join(script_path, 'mecDeleteShelfTab.mel'))
shelf_path = os.path.join(script_path, 'shelves')
new_scripts_path = os.path.join(script_path, 'scripts')
sys.path.append(new_scripts_path)
sys.path.append(shelf_path)

def gui():
	window_name = 'mec_shelf_loader_gui'
	window_exists = pm.window(window_name, exists=True)
	if window_exists:
		pm.deleteUI(window_name)
	window_prefs_exists = pm.windowPref(window_name, exists=True)
	if window_prefs_exists:
		pm.windowPref(window_name)

	window_width = 300
	window_object = pm.window(window_name, width=window_width, title='Shelf Loader',
		sizeable=False)
	main_layout = pm.columnLayout()
	icon_size = 42
	'''
	pm.rowColumnLayout(numberOfColumns=2, columnWidth=[[1, window_width - icon_size]])
	global shelf_path_field
	shelf_path_field = pm.scrollField(height=48, text=shelf_path)
	pm.symbolButton(image='menuIconFile.png')
	pm.setParent(main_layout)
	'''
	pm.text(label='Shelf List', width=window_width)
	global shelf_list
	shelf_list = pm.textScrollList(height=250, width=window_width)
	pm.button(label='Reload', width=window_width, command=refresh_shelf_list)
	pm.rowColumnLayout(numberOfColumns=2, 
		columnWidth=[[1, window_width / 2], [2, window_width / 2]])
	pm.button(label='Load', width=window_width / 2, command=load_shelf)
	pm.button(label='Delete', width=window_width / 2, command=remove_shelf)
	pm.setParent(main_layout)

	window_object.show()
	refresh_shelf_list()


def refresh_shelf_list(*args):
	load_shelves()
	shelf_list.removeAll()
	for current_shelf in current_shelves:
		shelf_list.append(current_shelf.shelf_name)

current_shelves = []
def load_shelves():
	global current_shelves
	shelf_files = glob.glob(os.path.join(shelf_path, '*.mel'))	
	current_shelves = []
	for current_shelf in shelf_files:
		temp_shelf = Shelf(current_shelf)
		current_shelves.append(temp_shelf)

def load_shelf(*args):
	selected_index = shelf_list.getSelectIndexedItem()
	if selected_index:
		list_index = selected_index[0] - 1
		current_shelves[list_index].create_shelf()

def remove_shelf(*args):
	selected_index = shelf_list.getSelectIndexedItem()
	if selected_index:	
		list_index = selected_index[0] - 1
		current_shelves[list_index].delete_shelf()


class Shelf():
	def __init__(self, shelf_path):
		self.shelf_path = shelf_path
		self.retreive_shelf_name()

	def retreive_shelf_name(self):
		shelf_file = os.path.split(self.shelf_path)[-1]
		base_file_name = os.path.splitext(shelf_file)[0]
		shelf_name_pieces = base_file_name.split('_')
		self.shelf_name = '_'.join(shelf_name_pieces[1:])
		print shelf_file, base_file_name, shelf_name_pieces, self.shelf_name

	def delete_shelf(self):
		shelf_exists = pm.shelfLayout(self.shelf_name, exists=True)

		if shelf_exists:
		    pm.mel.mecDeleteShelfTab(self.shelf_name)
		else:
		    print 'Shelf: {0} - Does not exists!'.format(self.shelf_name)

	def create_shelf(self):
		shelf_exists = pm.shelfLayout(self.shelf_name, exists=True)

		if not shelf_exists:
		    pm.mel.mecLoadShelf(self.shelf_path)

		else:
		    print 'Shelf: {0} - Exists!'.format(self.shelf_name)		


def delete_shelf(shelf_name):
	shelf_exists = pm.shelfLayout(shelf_name, exists=True)

	if shelf_exists:
	    pm.mel.mecDeleteShelfTab(shelf_name)
	else:
	    print 'Shelf: {0} - Does not exists!'.format(shelf_name)
    

# Creating a shelf.


def create_shelf(shelf_name, shelf_path):
	shelf_exists = pm.shelfLayout(shelf_name, exists=True)

	if not shelf_exists:
	    pm.mel.mecLoadShelf(shelf_path)

	else:
	    print 'Shelf: {0} - Exists!'.format(shelf_name)