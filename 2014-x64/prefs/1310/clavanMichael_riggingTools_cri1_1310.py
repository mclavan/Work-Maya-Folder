'''
Michael Clavan



'''

print 'CRI1 - Rigging Tools'

import pymel.core as pm 
def chapter_27():
	print 'Everything is ok.'

def chapter_1():
	print 'It was the best of times.  It was the worst of times.'

def delete_history():
	# Processing / Work
	pm.delete(constructionHistory=True)
	print 'History has been deleted on selected objects.'

def float_attribute_creation():
	# Input / Given
	attribute_name = raw_input()
	# Processing
	pm.addAttr(longName=attribute_name, keyable=True)

	# Output
	print 'Float attribute has been created.'

'''
setAttr -lock false -keyable true ".tx";
pm.setAttr('.tx', lock=False, keyable=True)

pm.mel.RuntimeCommand()


setAttr ".overrideEnabled" 1;
setAttr ".overrideColor" 17;
'''

import pymel.core as pm
def color_control_yellow():
	'''
	I'm a function header.
	'''
	pm.setAttr(".overrideEnabled", 1)
	pm.setAttr(".overrideColor", 17)

