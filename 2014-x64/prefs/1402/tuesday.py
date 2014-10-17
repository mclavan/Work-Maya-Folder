'''
tuesday.py
Michael Clavan

Description:

How to run:

import tuesday
reload(tuesday)

'''

import pymel.core as pm

print 'Tuesday Activated.'

def loop_practice():
	'''

	import tuesday
	reload(tuesday)
	tuesday.loop_practice()
	'''
	'''
	Input 
	'''
	# Get all selected joints in our scene. 
	selected_joints = pm.ls(selection=True)
	count = 0

	# chair_01_geo
	# chair1_geo

	# asset = raw_input()

	for current_joint in selected_joints:
		# Create a pad
		pad = pm.group(empty=True)

		# Move pad to target joint
		temp_constraint = pm.pointConstraint(current_joint, pad)
		pm.delete(temp_constraint)

		# Freeze Transforms
		pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

		# Parent joint to pad
		pm.parent(current_joint, pad)


		# count = count + 1
		# # print 'Current Joint:', count, current_joint
		# new_name = '{0}_{1}'.format(asset, count)
		# current_joint.rename(new_name)
		# print 'Current Joint - {0}: {1}'.format(count, current_joint)


	print 'Total Joints Selected:', count

	'''
	Output
	'''
	print 'Loop Practice.'





def rename_practice():
	'''

	import tuesday
	reload(tuesday)
	tuesday.rename_practice()
	'''
	print 'Rename Practice.'

	# We need to get two selected objects
	selection = pm.ls(selection=True)

	# print selection
	driver_joint = selection[0]
	control_icon = selection[1]

	driver_suffix = '_bind'
	driven_suffix = '_icon'
	# Use the replace method to get a new name.
	# ct_tail3_01_bind '_bind'
	# ct_tail3_01_icon '_icon'

	new_name = driver_joint.replace(driver_suffix, driven_suffix)
	control_icon.rename(new_name)
	# Use rename method.
	print 'Old Name', control_icon, 'New Name:', new_name


'''

'''

left_controls = pm.ls('lt_*_icon')
right_control = pm.ls('rt_*_icon')
center_control = pm.ls('ct_*_icon')


pm.ls('*_proxy')

pm.delete('*_proxy', constraints=True)


