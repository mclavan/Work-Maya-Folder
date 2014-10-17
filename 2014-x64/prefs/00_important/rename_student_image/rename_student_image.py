'''
Michael Clavan
rename_student_image.py

How To Run:
import rename_student_image
reload(rename_student_image)
rename_student_image.gui()

'''

'''
- Cover Shape and Trasform Nodes Better
- Shape Node Parenting

- Do some joint layout
- Then do some padding
- Then after a couple examples have them draw and padd

'''

import pymel.core as pm
import os
import glob

image_path = os.path.split(__file__)[0]
image_1 = os.path.join(image_path, 'student_pictures', 'ElenaBarreiro.jpeg')
image_2 = os.path.join(image_path, 'student_pictures', 'Jasmine Austin.jpeg')



def gui():

	window_width = 595
	window_height = 595
	window_name = 'mec_rename_student_win'
	window_object = pm.window(width=window_width, title='Rename Student Image')
	main_layout = pm.columnLayout()

	main_row_layout = pm.rowColumnLayout(numberOfColumns=3)

	drop_names(main_row_layout)
	student_names(main_row_layout)
	image_widget(main_row_layout)

	pm.setParent(main_layout)

	window_object.show()

def student_names(current_parent):
	widget_layout = pm.columnLayout(parent=current_parent)
	widget_width = 225
	widget_height = 595
	pm.text(width=widget_width, label='Adjusted Names')
	global student_name_tsl
	student_name_tsl = pm.textScrollList(width=widget_width, height=widget_height)	
	pm.button(width=widget_width, label='Add to List')
	pm.setParent(widget_layout)
	return widget_layout

def drop_names(current_parent):
	widget_layout = pm.columnLayout(parent=current_parent)
	widget_width = 225
	widget_height = 595
	pm.text(width=widget_width, label='From Excel')
	global excel_field
	excel_field = pm.scrollField(width=widget_width, height=widget_height, editable=True, wordWrap=False, text='' )
	pm.button(width=widget_width, label='Apply to Image', command=pm.Callback(format_excel))
	pm.setParent(widget_layout)
	return widget_layout


def image_widget(current_parent):
	# main_layout = pm.columnLayout(parent=current_parent)
	widget_width = 140
	widget_height = 595
	main_layout = pm.columnLayout(parent=current_parent)
	pm.text(width=widget_width, label='Student Pictures')

	pm.scrollLayout( width=widget_width, height=widget_height)
	pm.columnLayout()
	'''
	pm.iconTextButton( style='iconAndTextVertical', image1=image_1, label='cube',
		width=112, height=148)
	pm.iconTextButton( style='iconAndTextVertical', image1=image_2, label='cube',
		width=112, height=148 )
	'''
	load_images()
	'''
	pm.symbolCheckBox( image=image_2, width=112, height=148 )
	pm.symbolCheckBox( image=image_1, width=112, height=148 )
	pm.symbolCheckBox( image=image_2, width=112, height=148 )
	pm.symbolCheckBox( image=image_1, width=112, height=148 )
	pm.symbolCheckBox( image=image_1, width=112, height=148 )
	pm.symbolCheckBox( image=image_2, width=112, height=148 )
	'''
	pm.setParent(main_layout)
	pm.button(width=widget_width, label='Reload')
	pm.setParent(current_parent)
	return main_layout

student_images = []

class Student_Image():
	def __init__(self, image_path, image_width=112, image_height=148):
		self.image_path = image_path
		self.base_path, self.original_image_name = os.path.split(self.image_path)

		self.image_name, self.image_ext = os.path.splitext(self.original_image_name)
		self.button = pm.symbolButton(image=self.image_path, width=image_width, height=image_height,
			command=pm.Callback(self.rename_file))
		self.student_file_name = pm.text(label=self.original_image_name, width=image_width)

	def rename_file(self):
		# Take the current select tsl item
		selected_student_name = student_name_tsl.getSelectItem()
		print selected_student_name
		
		if selected_student_name:
			file_name = '{0}.{1}'.format(selected_student_name[0], 'jpeg')
			self.student_file_name.setLabel(file_name)
		# Use the file renaming command is os module
			new_image_path = os.path.join(self.base_path, file_name)
			
			os.rename(self.image_path, new_image_path)
			
			self.image_path = new_image_path
			self.base_path, self.original_image_name = os.path.split(self.image_path)
			self.image_name, self.image_ext = os.path.splitext(self.original_image_name)
			print 'New Image Path: {0}\n'.format(self.image_path)

def format_excel():
	excel_information = excel_field.getText()
	student_names = []
	split_excel_information = excel_information.split('\n')
	for current_student in split_excel_information:
		if current_student:
			student_name_pieces = current_student.split(' ')
			# print student_name_pieces
			first_name = student_name_pieces[0]
			last_name = student_name_pieces[-1]
			middle_name = ''.join(student_name_pieces[1:-1])
			student_data = '{1}_{0}'.format(first_name.capitalize(), last_name.capitalize())
			student_names.append(student_data)
			# print student_data

	student_name_tsl.extend(student_names)
	# print student_names

def load_images():
	image_paths = glob.glob(os.path.join(image_path, 'student_pictures', '*.jpeg'))
	# print image_paths
	global student_images
	for current_image in image_paths:
		temp_student = Student_Image(current_image)
		student_images.append(temp_student)



