'''
Michael Clavan
book.py

How to Run:

import book
reload(book)

'''

print 'Introductionn to Functions.'

import pymel.core as pm 

def chapter_1():
	print 'Chapter 1: The Beginning.'
	print 'It was the best of times.'
	print 'It was the worst of times.'


def chapter_2():
	print 'Chapter 2: The Journey.'

def chapter_27():
	print 'Chapter 27: Rejoice!'

def all_chapters():
	chapter_1()
	chapter_2()
	chapter_27()
	
