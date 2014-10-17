'''
book.py 

Description:
	Functions - Splitting up your code. 

How to Run:

import book
reload(book)


'''

import pymel.core as pm 

print 'Script Activated.'

def chapter_2():
	print 'Chapter 2'

def chapter_1():
	print 'Chapter 1'
	print 'It was the best of times.'
	print 'It was the worst of times.'

	chapter_2()


