'''
Michael Clavan
lecture_5_welcome.py


Description:
    Starter script for lecture 5.
    
How to Run:

import lecture_5_welcome
reload(lecture_5_welcome)

'''
print 'Lecture 5 - Notes'

import pymel.core as pm

'''
def functionName():
'''

def freezing_transforms():
    print 'Transforms Frozen.'

def chapter_1():
    print 'It was the best of time it was the worst of time.'

'''
Calling functions means running a function!

chapter_1()
freezing_transforms()
'''


def nuke():
    '''
    The nuke function will freeze transforms, delete history and
      center pivots.
    '''
    
    pm.delete(ch=True)
    pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    pm.xform(cp=True)
    
    print 'Nuking Selected!'


def create_hierarchy():
    '''
    The create hierarchy function will generate the desired hierarchy.
    '''

    print 'Project 2 - Hierarchy Created.'
    
    
