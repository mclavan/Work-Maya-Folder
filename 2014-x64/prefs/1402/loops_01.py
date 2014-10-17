'''
Lesson - Loops

This exercise will introduce loops. 

How to Run:

import loops_01
reload(loops_01)

'''

import pymel.core as pm 

print 'Lesson - Loop practice.'

'''
Loops require a list:
'''

'''
Loop syntax

for aVariable in aList:
	statements... 

'''

'''
Create a loop to print out each name in the list.


names = ['Michael', 'Bob', 'George']
for name in names:
	print name 
'''

def basic_loop():
	customers = ['Michael', 'Bob', 'Susan']

	for serving_customer in customers:
		print 'Current Customer:', serving_customer

	print 'Basic Loop.'


'''
Looping through selected. 
selected = pm.ls(selection=True)
'''
def loop_selected():
	selected = pm.ls(selection=True)

	for current_item in selected:
		

	print 'Selected Loop Completed.'


'''
Lock and Selected 
selected = pm.ls(selection=True)
'''
def unlock_and_keyable():
	'''
	This function unlocks and makes keyable selected objects.
	
	How to Run:

	import loops_01
	reload(loops_01)
	loops_01.unlock_and_keyable()

	'''
	selected = pm.ls(selection=True)

	for current_item in selected:
		# tx, ty, tz, rx, ry, rz, v
		current_item.tx.set(lock=False, keyable=True)
		current_item.ty.set(lock=False, keyable=True)		
		current_item.tz.set(lock=False, keyable=True)
		current_item.rx.set(lock=False, keyable=True)
		current_item.ry.set(lock=False, keyable=True)		
		current_item.rz.set(lock=False, keyable=True)
		current_item.sx.set(lock=False, keyable=True)
		current_item.sy.set(lock=False, keyable=True)		
		current_item.sz.set(lock=False, keyable=True)				
		current_item.v.set(lock=False, keyable=True)
		print 'Current Item:', current_item

	print 'Selected channels unlocked and keyable.'

'''
Color Control Icon - Blue

selected = pm.ls(selection=True)
for current_item in selected:
	current_item.overrideEnabled.set(1)
	current_item.overrideColor.set(6)
'''







