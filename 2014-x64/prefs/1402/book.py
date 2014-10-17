'''
book.py 
Michael Clavan 

Description:

How to Run:

import book 
reload(book)

'''

import pymel.core as pm 

print 'Book has been open.'

def chapter_1():
	print 'Chapter 1 - Hello'
	print 'It was the best of times.'
	print "We cant stop here."
	print 'Its bat country.'

def chapter_2():

	print 'hi'

def chapter_27():

	print 'Hi, I am chapter 27.'

def delete_history():
	pm.delete(ch=True)
	print 'History has been deleted on selected objects.'

def unlock_and_keyable():
		# Get selected. 
	selected = pm.ls(selection=True)
	first_selected = selected[0]
	print 'First Selected:', first_selected

	# Set translate, rotate, and scale to keyable and unlocked.
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

	print 'Select object has had its attribute retuned.'



# Create the function chapter_27. 
# Run each one.
