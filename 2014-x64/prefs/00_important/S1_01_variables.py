'''
CR1 - Variables
S1_01_variables.py 

'''

'''
Creating variables is to store data.
Before we can cover variables we need to understand what types of data is 
present in Python and Maya.

'''

'''
float (real values or numbers with decimals)
'''
3.14
-0.01
98.6

'''
integers or int (whole numbers or numbers with out decimals)
'''
0
-32
42


'''
string (characters or numbers that are not meant to be counted)
Always in encapsulated between single or double quotes.
'''
'John Doe'
"3300 University Blvd."
'888-FILM'


'''
Math Operators
'''
# Adding Numbers
24.5 + 0.5
11 + 22
3.14 + 1

# Subtracting Numbers
24.5 - 0.5
11 - 22
3.14 - 1

# Multipling Numbers
24.5 * 0.5
11 * 22
3.14 * 1

# Dividing Numbers
24.5 / 2
22 / 11
3.14 / 1

# Remainder or Modulus
10 % 3
33 & 3


'''
You can add strings together too but we will cover that in a later time.
'''

'''
Storing Values (VARIABLES)
'''
# When you add two values together you are producing a results.  
# This results can be stored or caught in a variable.

'''
# You create a variable by typing a name and using an assignment operator, which is mainly a equals symbol.
'''

results = 2 + 2

'''
What happens here is 2 + 2 is calculated first then stored into the variable called results.
Then the variable called results can be used later on the script.
'''

print results

add_results = 24.5 + 0.5
sub_results = 24.5 - 0.5
mult_results = 24.5 * 0.5
divide_results = 24.5 / 3

print add_results
print sub_results
print mult_results
print divide_results

'''
Variables can be reused.
'''

count = 1
print count
count = 2
print count
count = count + 1
print count
count = count + 1
print count

'''
Rules for naming variables.
- No spaces
- No numbers at the beginning
- NO invalid characters (),.{}[]!*@#$%^


Good naming practices
- Do not cap first letter.
- Separate words with underscores.
	rt_hand
	control_icon
- Be descriptive.  Variables should be nouns.  Person, Place, Thing, or Idea.
	If you can't read a variable and understand what it contains that rethink your naming.
- Camel Case
	If you must group two words together then capitalize the first letter of the next world.


control_icon
rt_hand_icon
control_translate_x
counter
checkBox_results
segment_value
'''


# You can easily read what the four variables will be used for below.
control_icon = 'ct_head_icon'
control_translateY = 2
control_rotateX = 180
control_scaleX = 2


'''
Practice create variables and print out their values.
Practice using different math operators on number variables.
'''

offset = 0.5
control_translateY = 0

print control_translateY

control_translateY = control_translateY + offset
print control_translateY

control_translateY = control_translateY + offset
control_translateY = control_translateY + offset
print control_translateY
















