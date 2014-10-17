'''


'''

print 'String Formatting - Activated.'

'''
One of the most important aspects of programming is giving the user feedback.
This lesson will teach you different methods giving the user feedback.  
Using the print statement and a few other tools.
'''

warrior_name = 'Conan'
strength = 16
intelgence = 3
wizdom = 2
hit_points = 24

'''
Here we have a basic use of the print statement.
This is the results.  The information isn't very clear.
Conan
Warriors Stats 16 3 2 24
'''
print warrior_name
print 'Warriors Stats', strength, intelgence, wizdom, hit_points
print 'We are separating data in the print statement using commas.'
print 'We will learn better ways of print data later in this lesson.'


'''
To start, strings can be added together.
'''
print 'Warrior Name: ' + warrior_name

'''
However, number and strings can not be added together.
They have converted to be the same type.
'''
# print 'Strength: ' + strength
print 'Strength: ' + str(strength)

'''
What if you wanted to print out multiple pieces of information in one line?
Like:
	Warriors Name: Conan - Stats Strength: 16 Intelgence: 3 Wizdom: 2
It will not be fun but it would look like this.
'''
print 'Warriors Name: ' + warrior_name + ' - Stats Strength: ' + str(strength) + ' Intelgence: ' + str(intelgence) + ' Wizdom: ' + str(wizdom)
 
'''
It is not very fun, but every language allows you to add strings together.
The next method is formatting tool used with strings in python.
'''

warrior_name = 'Merlin'
strength = 2
intelgence = 16
wizdom = 16
hit_points = 8

'''
Strings have a series of built in tools to format output.

warrior_name.format()

You see the dot.  This is called dot notation.  
It allows you to access special tools inside data.
In this case the format method.
'''

character_status = 'Warriors Name:  - Stats Strength:  Intelgence:  Wizdom: '
# character_status = 'Warriors Name: {0} - Stats Strength: Intelgence:  Wizdom: '
# character_status = 'Warriors Name: {0} - Stats Strength: Intelgence:  Wizdom: '.format(warrior_name)
# character_status = 'Warriors Name: {0} - Stats Strength: {1} Intelgence: {2} Wizdom: {3}'.format(warrior_name, strength, intelgence, wizdom)

print character_status

