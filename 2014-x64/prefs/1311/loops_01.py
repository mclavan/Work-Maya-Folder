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



for name in names:
	print name 

names = ['lt_arm_01_bind', 'lt_arm_02_bind', 'lt_arm_03_waste']
#                                     ^
for customer in names:
	print 'Serving Customer:', customer
'''

'''
Looping through selected. 


selected = pm.ls(selection=True)
for current_item in selected:
	print 'Current Item', current_item
'''

'''
Lock and Selected 
selected = pm.ls(selection=True)
'''

'''
selected = pm.ls(selection=True)
for current_item in selected:
	current_item.sx.set(lock=False, keyable=True)
	current_item.sy.set(lock=False, keyable=True)
	current_item.sz.set(lock=False, keyable=True)		
	print 'Current Item ', current_item

	
	current_item.overrideEnabled.set(1)
	current_item.overrideColor.set(6)
'''

# Color Control Icon - Blue

def color_icon_blue():
	'''
	Colors selected control icons blue. 

	Selected control icons. 
	Call Function: 
	import loops_01
	loops_01.color_icon_blue()
	'''
	selected = pm.ls(selection=True)
	for current_item in selected:
		current_item.overrideEnabled.set(1)
		current_item.overrideColor.set(6)








