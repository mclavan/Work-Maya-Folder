'''
Lesson - Loops

This exercise will introduce loops. 

How to Run:

import loops_01
reload(loops_01)

'''

import pymel.core as pm 

print 'Lesson - Function practice.'

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
'''
#            -3       -2       -1
#            0        1        2
waiting_list = ['Michael', 'Bob', 'George']
#                                     ^
for customer in waiting_list:
	print customer 


'''
Looping through selected. 
selected = pm.ls(selection=True)
'''
selected = pm.ls(selection=True)
count = 1
for current_item in selected:
	print count, 'Serving Item:', current_item
	count = count + 1


'''
Lock and Selected 
selected = pm.ls(selection=True)


'''
selected = pm.ls(selection=True)
for current_item in selected:
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

'''
Color Control Icon - Blue

selected = pm.ls(selection=True)
for current_item in selected:
	current_item.overrideEnabled.set(1)
	current_item.overrideColor.set(6)
'''







