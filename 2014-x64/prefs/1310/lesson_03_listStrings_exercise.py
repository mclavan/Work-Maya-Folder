'''
lesson_03_list_exercise.py
 
Description:
	Use the format method to print out the items below.

How to Run:



'''
print 'hi'

back_joints = ['ct_back_01_bind', 'ct_back_02_bind', 'ct_back_03_bind', 'ct_back_04_bind', 'ct_back_05_waste']
neck_joints = ['ct_neck_01_bind', 'ct_neck_02_waste']

back_pad = 'ct_back_00_pad1'
neck_pad = 'ct_neck_00_pad1'

'''
Print out the back pad and which joint is parented to it.
'''
print 'Back Pad:', back_pad
print 'Back Root Joint', back_joints[-1]
print back_joints[0], back_joints[2], back_joints[-1]

print 'Children:', back_joints[0:-1], 'Father:', back_joints[-1]

'''
Print out the neck pad and which joint is parented to it.
'''

'''
Print out how the neck is connected to the back.
Make sure to remember the correct order.
'''


leg_joints = ['lt_leg_01_bind', 'lt_leg_02_bind', 'lt_leg_03_bind', 'lt_leg_04_bind', 'lt_leg_05_bind']

leg_icon = 'lt_leg_icon'
'''
leg_ik = 'lt_leg_IK'
leg_pv_icon = 'lt_legPV_icon'


Print out the joints for the RFL system.
Starting with the leg, then ball, and finally the toe.
'''
