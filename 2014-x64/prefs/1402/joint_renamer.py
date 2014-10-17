'''
Lesson - Joint Renamer
joint_renamer.py

Description:
	Practical use of loops.
	Renaming joint based upon a naming convention.

How to Run:

import joint_renamer
reload(joint_renamer)


'''

print 'Joint Renamer - Active'

import pymel.core as pm

'''
Get Selected.

pm.ls(selection=True)

'''

joint_chain = pm.ls(selection=True, dag=True)
print 'Selected items:', joint_chain

'''
Figure out naming convention. 
'lt_arm_01_bind' -> 'lt_arm_03_waste'
'ct_tail_01_bind', -> 'ct_tail_06_waste'
'''

ori = raw_input()
system_name = raw_input()
count = 0
suffix = 'bind'



'''
Loop through joint chain.
'''
for current_joint in joint_chain:
	count = count + 1	
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
	print 'New Name:', new_name	

	# Rename joint
	current_joint.rename(new_name)


new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
current_joint.rename(new_name)


