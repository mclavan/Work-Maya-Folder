'''
Lesson - if statements
'''


'''
Basic if statement

if condition:
	print 'The condition is True.'
'''

if True:
	print 'The condition is True.'

if False:
	print 'The condition is True'

'''
What is the condition?

2 == 2
2 == 3
'''


'''
Operators
==	Equals
!=  Not Equals
> 	Greater Than
>=  Greater Than or equal to
<	Less Than
<= 	Less Than or equal to
'''

if 2 == 2:
	print '2 is equal to 2.'

if 2 != 3:
	print '2 is not equal to 3.'

'''
Using multiple conditions

and
or
not

'''

if 2 == 2 and 2 != 3:
	print 'Both conditions are True.'

if 2 == 2 and 2 == 3:
	print 'Both conditions are True.'

if 2 == 2 or 2 == 3:
	print 'Both conditions are True.'

'''
What if I want to react to False?
else statement
'''
if 2 == 3:
	print 'The condition is True.'
else:
	print 'The condition is False.'

'''
What if I want to have multiple paths?
elif statement. 
'''

'''
about command
pm.about()
# os=True returns operating system
# windows=True returns true if currently on windows. 
# macOs=True returns true if currently on osx.

'''

if pm.about(windows=True):
	print 'You are using a computer with windows.'
elif pm.about(macOs=True):
	print 'You are using a computer with osx.'
else:
	print 'You are using a different os.'




