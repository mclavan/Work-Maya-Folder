'''
Lesson - Loops
loops.py


'''
import pymel.core as pm 
'''
Loop Basics

For loop



# Requires a list
customers = ['Michael', 'Bob', 'Susan']
#                                       ^
for customer in customers:
	print 'Serving Customer:', customer

selected = pm.ls(selection=True)

for current_item in selected:
	
	print 'Current Item:', current_item
	new_name = current_item + '_proxy'
	current_item.rename(new_name)
'''

'''
For with range

'''
customers = ['Michael', 'Bob', 'Susan']
for i in range(len(customer)-1):
	print customers[i]


