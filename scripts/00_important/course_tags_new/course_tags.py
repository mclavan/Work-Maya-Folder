'''

How to Run:

imoprt course_tags
course_tags.gui()

'''

import xml.etree.ElementTree as ET
import os
import pymel.core as pm

script_location = os.path.split(__file__)[0]
activ8_folder = os.path.join(script_location, 'activ8')

'''
# Reading from an xml document.
xml_file_path = '/Users/mclavan/Desktop/Lession2_Controls.axml'
xml_file_path = os.path.join(activ8_folder, 'Lession2_Controls.axml')
xml_write_file = '/Users/mclavan/Desktop/test.axml'
xml_write_file = os.path.join(activ8_folder, 'test.axml')
# create_tags = ['Michael Clavan', 'John Doe', 'Dan Marino', 'Benjamin Sisco']
'''

print 'This worked'
def gui():
	window_width = 300
	window_name = 'mec_courseTags_win'
	window_exists = pm.window(window_name, exists=True)
	if window_exists:
		pm.deleteUI(window_name)
	window_pref_exists = pm.windowPref(window_name, exists=True)
	if window_pref_exists:
		pm.windowPref(window_name, r=True)

	window_object = pm.window(window_name, width=window_width, title='Tag Generator')
	main_layout = pm.columnLayout()
	pm.text(label='Paste tags below.', width=window_width)
	pm.text(label='Each line will be its own tag.', width=window_width)
	global tag_field
	tag_field = pm.scrollField( width=window_width, height=400, editable=True, wordWrap=False, text='' )

	pm.button(label='Do It', width=window_width, command=tags_gui_work)
	window_object.show()


def tags_gui_work(*args):
	tags_line = tag_field.getText()
	tags = tag_generator_list(tags_line)
	print '\n'.join(tags)
	activ8_files = get_xml_files()
	add_tags_to_multiple_xml(tags, activ8_files)

def get_xml_files():
	axml_base_files = os.listdir(activ8_folder)
	axml_files = []
	for current_file in axml_base_files:
		if current_file.endswith('.axml'):
			axml_files.append(os.path.join(activ8_folder, current_file))	
	return axml_files

def tag_generator(tags):
	split_tags = tags.split('\n')
	# print split_tags
	tags = []
	for current_tag in split_tags:
		# current_tag = 'Codec'
		if current_tag != '':
			tags_line = '\t\t\t<tag>{0}</tag>'.format(current_tag)
			tags.append(tags_line)
			 #print tags_line
	return tags

def tag_generator_list(tags):
	split_tags = tags.split('\n')
	# print split_tags
	tags = []
	for current_tag in split_tags:
		# current_tag = 'Codec'
		if current_tag != '':
			tags.append(current_tag)
			 #print tags_line
	return tags

def add_tags_to_multiple_xml(create_tags, xml_write_files):
	for current_xml_file in xml_write_files:
		add_tags_to_xml(create_tags, current_xml_file)

def add_tags_to_xml(create_tags, xml_write_file):

	tree = ET.parse(xml_write_file)
	root = tree.getroot()
	# Getting <tags> </tags>
	tags = root.findall('tags')[0]

	# Tails are ending information for the xml tag.  Allows indending.
	ending_tag_tail = '\t\t\t\t\t\n\t' 
	normal_tag_tail = '\n\t\t'

	if len(tags):
		tags[-1].tail = normal_tag_tail
	for current_tag in create_tags:
		# Creating a new <tag></tag>
		tag_element = ET.SubElement(tags, 'tag')
		tag_element.text = current_tag
		tag_element.tail = normal_tag_tail

	tags[-1].tail = ending_tag_tail

	# Writing to an xml document.
	tree.write(xml_write_file)

'''
Script Node Notes
scripts_path = "import maya.cmds as cmds;import pymel.core as pm;import sys;import os.path;scene_path = cmds.file(q=True, sn=True);base_path = os.path.split(scene_path);scripts_path = os.path.join(base_path[0], 'scripts');sys.path.append(scripts_path);sys.path.append(base_path[0])"
script_exe = "import course_tags; reload(course_tags);course_tags.gui()"
final_python_line = '{0};{1}'.format(scripts_path, script_exe)

generated_node = pm.scriptNode(scriptType=2, sourceType='python', 
                name='script_loader',
                beforeScript=final_python_line)

pm.scriptNode( generated_node, executeBefore=True )

# Basic Example

nodeName = pm.scriptNode( st=2, bs='import pymel.core as pm;pm.sphere()', n='script', stp='python')
cmds.scriptNode( nodeName, executeBefore=True )

'''
