'''
lesson1_00_lists.py

Description:
	Lists are used to group together data.

How to Run:


'''

print 'Lists - Activated.'


'''
Why will be code below not work?
'''
binding_joint = 'ct_back_01_bind'
binding_joint = 'ct_back_02_bind'
binding_joint = 'ct_back_03_bind'
print binding_joint, binding_joint, binding_joint

'''
An alternative is creating a variable for each binding joint.
'''

binding_joint_01 = 'ct_back_01_bind'
binding_joint_02 = 'ct_back_02_bind'
binding_joint_03 = 'ct_back_03_bind'

print binding_joint_01, binding_joint_02, binding_joint_03

'''
The issue here is we have create a unique name for each variable.
We also need to know how many variables to create.
'''

'''
We now introduce a data structure call the list.
'''

names = []  # This is a empty list.
print names

'''
Items are placed between the squared brackets separated by commas.
'''
# This list called names contains five string values.
names = ['Michael', 'Seth', 'Ken', 'Jennifer', 'David']
print names

'''
We can access each piece of data individualy.
'''

print names[0]  # This is the first item in the list.
print names[1]  # This is the second item in the list.
print names[-1] # This is the last item in the list.
print names[-2] # This is the second to last item in the list.


'''
Items can be over writen.  Just like in variables.
'''

names[0] = 'Michael Clavan'
names[1] = 'Seth Freeman'

print names

'''
Why are list important?  
Many elements in Maya are grouped together.  
Examples: are 
	rotation values
	uv coordinates 
	rgb values
'''





