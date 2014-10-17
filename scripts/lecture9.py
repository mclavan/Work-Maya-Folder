'''
Michael Clavan
lecture9.py 

Description:

How To Run:

import lecture9
reload(lecture9)

'''

print 'Lecture 9 - Active'

import pymel.core as pm 

def print_selected():
	'''
	Tool Description.

	How to use the tool. 

	How to Run:

	'''
	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected 

	# print 'Current Selected: {0}'.format(selected)
	print 'hi'


def unlock_and_show():
	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected 

	first_selected = selected[0]    
	# Lock and Hide
	first_selected.tx.set(lock=False, keyable=True)
	first_selected.ty.set(lock=False, keyable=True)
	first_selected.tz.set(lock=False, keyable=True)
	first_selected.rx.set(lock=False, keyable=True)
	first_selected.ry.set(lock=False, keyable=True)
	first_selected.rz.set(lock=False, keyable=True)
	first_selected.sx.set(lock=False, keyable=True)
	first_selected.sy.set(lock=False, keyable=True)
	first_selected.sz.set(lock=False, keyable=True)
	first_selected.v.set(lock=False, keyable=True)

# Ideas?
# lock and hide (translates and rotates)

def create_fingers():
	'''
	import lecture9
	reload(lecture9)
	lecture9.create_fingers()
	'''

	selected = pm.ls(selection=True)
	print 'Currently Selected:', selected 

	first_selected = selected[0] 

	# addAttr
	first_selected.addAttr('FINGERS', at='enum', en="----------------:", keyable=True)
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)

	first_selected.addAttr('SPREAD', at='enum', en="----------------:", keyable=True)

	first_selected.addAttr('index_spread', keyable=True)
	first_selected.addAttr('middle_spread', keyable=True)
	first_selected.addAttr('pinky_spread', keyable=True)

	first_selected.addAttr('THUMB', at='enum', en="----------------:", keyable=True)



