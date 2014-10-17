'''
lesson_02_string_exercise.py
 
Description:
	Use the format method to print out the items below.

How to Run:



'''

print 'String Formatting - Exercise - Activated.'

ik_control_icon = 'lt_arm_icon'
pole_vector_icon = 'lt_armPV_icon'
arm_ik_handle = 'lt_arm_IK'

joint_1 = 'lt_arm_01_bind'
joint_2 = 'lt_arm_02_bind'
joint_3 = 'lt_arm_03_waste'

'''
Print out all three joints in the arm system.
'''
print 'First Joint:', joint_1
print 'Second Joint:', joint_2
print 'First and Third Joint', joint_1, joint_3

'''
Print out that an ik has been applied between the first and last joint.
'''

'First Joint: ?? Third Joint: ?? IK Control: ??'

# 'First Joint: ' + joint_1  + 'Third Joint: ' + joint_3 + ' IK Control: ??'

print 'First Joint: {0} - Third Joint: {0} - IK Control: {0}'.format(joint_1, joint_3, ik_control_icon)

# String methods
#    format method
# /n /t  Escape Sequences
# google python string formatting

'''
Print out that the first joint has been padded.
'''


'''
Print out that the arm ik has a pole vector applied to it.
'''










