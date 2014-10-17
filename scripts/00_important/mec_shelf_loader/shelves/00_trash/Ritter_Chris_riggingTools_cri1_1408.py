'''
import Ritter_Chris_riggingTools_cri1_1408
reload (Ritter_Chris_riggingTools_cri1_1408)
'''


def padding_tool():
	'''
	import Ritter_Chris_riggingTools_cri1_1408
	reload (Ritter_Chris_riggingTools_cri1_1408)
	Ritter_Chris_riggingTools_cri1_1408.padding_tool
	'''

	selected = pm.ls(selection=True)
	#print 'Current Selected:', selected
	root_joint = selected[0]

	print 'Padding group created.'

	#Create empty group
	pad = pm.group(empty=True)

	#Move group to joint and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	#Freeze transforms on the group
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)

	#Parent joint to group
	pm.parent(root_joint, pad)

	#Renaming
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)



def priming_tool():
	
	selected = pm.ls(selection=True)
	print 'Joints Selected:', selected

	control_icon = pm.circle(normal=[1, 0, 0], radius=1.8)[0]

	local_pad = pm.group()

	print 'Control Icon:', control_icon
	print 'Pad Created:', local_pad

	print 'Local Oriented Controls Created.'



def joint_renamer():
	
	print 'Joint Renamer - Active'

	import pymel.core as pm

	joint_chain = pm.ls(selection=True, dag=True)

	print 'Selected Items:', joint_chain

	ori = 'ct'
	system_name = 'tail'
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:
		new_name = '{0}_{1}_{2}_{3}'.format(ori, system_name, count, suffix)
		print 'New Name:', new_name
		current_joint.rename(new_name)
		count = count + 1

