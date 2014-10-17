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
names = ['Michael', 'Bob', 'George']

for name in names:
	print name 


'''
Looping through selected. 
selected = pm.ls(selection=True)
'''



'''
Lock and Selected 
selected = pm.ls(selection=True)
'''


'''
Color Control Icon - Blue

selected = pm.ls(selection=True)
for current_item in selected:
	current_item.overrideEnabled.set(1)
	current_item.overrideColor.set(6)
'''







