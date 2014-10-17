'''
Michael Clavan
unique_tags.py

How to Run:

import unique_tags
unique_tags.print_tags()

'''
import xml.etree.ElementTree as ET
import os

script_location = os.path.split(__file__)[0]
activ8_folder = os.path.join(script_location, 'activ8')

def get_xml_files():
	axml_base_files = os.listdir(activ8_folder)
	axml_files = []
	for current_file in axml_base_files:
		if current_file.endswith('.axml'):
			axml_files.append(os.path.join(activ8_folder, current_file))	
	return axml_files


def get_tags():
	xml_files = get_xml_files()
	all_tags = []
	# print xml_files[0]
	for xml_file in xml_files:
		current_tags = get_tags_from_xml(xml_file)
		for tag in current_tags:
			if tag not in all_tags:
				all_tags.append(tag)
	return all_tags 

def print_tags():
	all_tags = get_tags()
	all_tags.sort()
	print '\n'.join(all_tags)

def get_tags_from_xml(xml_file):

	current_tags = []
	tree = ET.parse(xml_file)
	root = tree.getroot()
	# Getting <tags> </tags>
	tags = root.findall('tags')[0]
	for tag in tags:
		tag_text = tag.text
		tag_text = tag_text.lower()
		tag_text = tag_text.lstrip()
		tag_text = tag_text.rstrip()		
		current_tags.append(tag_text) 

	return current_tags

def export_file(file_name='tag_out.txt'):

	file_path = os.path.join(script_location, file_name)
	file_info = open(file_path, 'w')
	tags = get_tags()
	tags.sort()
	file_info.writelines('\n'.join(tags))
	file_info.close()



print_tags()
export_file()