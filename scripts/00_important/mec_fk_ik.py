'''
mec_fk_ik.py
Michael Clavan

FK / IK Builder

How to Run:

import mec_fk_ik
reload(mec_fk_ik)

'''

import pymel.core as pm

import mec_controls

'''
This script currently works of a selected joint chain.
- The user will select the root and the script will do the rest 
while giving the user some additional design choices.

'''

class RootJoint():
	def __init__(self, root_joint):
		self.joint_pieces = root_joint.split('_')
		self.ori = joint_pieces[0]
		self.system_name = joint_pieces[1]
		self.count = joint_pieces[2]
		self.system_type = pieces[-1]
		self.name = root_joint

'''
Setup

These are test values that are dedicated to a scene for testing.
They will be removed in the long run.
'''

'''
bind_joints = pm.ls(selection=True, dag=True)
root_bind_joint = bind_joints[0]
root_ori = root_bind_joint.split('_')[0]

sdk_icon = pm.nt.Transform('lt_hand_FKIK')
sdk_attr = pm.Attribute('lt_hand_FKIK.fkik')
'''

def build_fk_ik_attributes(sdk_icon):
	if not pm.attributeQuery('fkik', node=sdk_icon, exists=True):
		sdk_icon.addAttr('fkik', keyable=True, min=0, max=10, dv=0)
	if not pm.attributeQuery('fk_vis', node=sdk_icon, exists=True):
		sdk_icon.addAttr('fk_vis', at='long', keyable=True, min=0, max=1, dv=1)
	if not pm.attributeQuery('ik_vis', node=sdk_icon, exists=True):	
		sdk_icon.addAttr('ik_vis', at='long', keyable=True, min=0, max=1, dv=1)
	return pm.Attribute('{0}.fkik'.format(sdk_icon))

def build_fk_ik_selected():
	selected = pm.ls(selection=True)
	build_fk_ik(selected[0], selected[1])

def build_fk_ik(root_bind_joint, sdk_icon):
	bind_joints = pm.ls(root_bind_joint, dag=True)

	'''
	Build Attributes

	'''
	sdk_attr = build_fk_ik_attributes(sdk_icon)

	root_ori = root_bind_joint.split('_')[0]
	'''
	Duplication
	'''
	root_fk_joint = pm.duplicate(root_bind_joint, renameChildren=True)
	fk_joints = pm.ls(root_fk_joint, dag=True)
	root_ik_joints = pm.duplicate(root_bind_joint, renameChildren=True)
	ik_joints = pm.ls(root_ik_joints, dag=True)

	'''
	Renaming

	lt_arm_01_bind
	lt_arm_01_FK
	lt_arm_01_IK
	'''
	for i, current_joint in enumerate(bind_joints):
		joint_name_pieces = current_joint.split('_')
		joint_name_pieces[-1] = 'FK'
		fk_joints[i].rename('_'.join(joint_name_pieces))
		joint_name_pieces[-1] = 'IK'
		ik_joints[i].rename('_'.join(joint_name_pieces))

	# Controls
	'''
	Creating control icons
	'''
	fk_control_icons = []
	# lt_fkArm_01_icon
	# lt_fkArm_02_icon

	fk_1_control_icon = mec_controls.circle_icon('{0}_armFK_01_icon'.format(root_ori))
	fk_1_control_prime = mec_controls.prime_control(fk_joints[0], fk_1_control_icon)
	fk_control_icons.append(fk_1_control_icon)


	fk_2_control_icon = mec_controls.circle_icon('{0}_armFK_02_icon'.format(root_ori))
	fk_2_control_prime = mec_controls.prime_control(fk_joints[1], fk_2_control_icon)
	fk_control_icons.append(fk_2_control_icon)

	# Connecting the first fk control icon to the prime group of the fk 2 system.
	pm.parent(fk_2_control_prime[0], fk_1_control_icon)


	# hand and pv for IK
	pole_vector_icon = mec_controls.arrow_icon('{0}_armPV_icon'.format(root_ori))
	mec_controls.snap_control(ik_joints[1], pole_vector_icon)

	ik_hand_icon = mec_controls.cube_icon('{0}_armIK_icon'.format(root_ori))
	mec_controls.snap_control(ik_joints[-1], ik_hand_icon)

	'''
	Setup Controls
	'''
	'''
	FK
	'''
	pm.orientConstraint(fk_1_control_icon, fk_joints[0])
	pm.orientConstraint(fk_2_control_icon, fk_joints[1])

	'''
	IK
	'''
	# Result: [nt.IkHandle(u'ikHandle1'), nt.IkEffector(u'effector1')] # 
	ik_handle = pm.ikHandle(startJoint=ik_joints[0], endEffector=ik_joints[-1] , 
							solver='ikRPsolver', name='{0}_armIK_ikHandle'.format(root_ori))
	pm.poleVectorConstraint(pole_vector_icon, ik_handle[0])
	pm.parent(ik_handle[0], ik_hand_icon)


	'''
	Constraint Switching
	'''
	arm_1_constraint = pm.orientConstraint(fk_joints[0], ik_joints[0], bind_joints[0])
	arm_2_constraint = pm.orientConstraint(fk_joints[1], ik_joints[1], bind_joints[1])

	driven_1_weigths = arm_1_constraint.getWeightAliasList()
	driven_2_weigths = arm_2_constraint.getWeightAliasList()
	fk_1_driven_weight = driven_1_weigths[0]
	fk_2_driven_weight = driven_2_weigths[0]
	ik_1_driven_weight = driven_1_weigths[1]
	ik_2_driven_weight = driven_2_weigths[1]

	pm.setDrivenKeyframe(fk_1_driven_weight, value=1, currentDriver=sdk_attr, driverValue=0)
	pm.setDrivenKeyframe(fk_2_driven_weight, value=1, currentDriver=sdk_attr, driverValue=0)
	pm.setDrivenKeyframe(ik_1_driven_weight, value=0, currentDriver=sdk_attr, driverValue=0)
	pm.setDrivenKeyframe(ik_2_driven_weight, value=0, currentDriver=sdk_attr, driverValue=0)

	pm.setDrivenKeyframe(fk_1_driven_weight, value=0, currentDriver=sdk_attr, driverValue=10)
	pm.setDrivenKeyframe(fk_2_driven_weight, value=0, currentDriver=sdk_attr, driverValue=10)
	pm.setDrivenKeyframe(ik_1_driven_weight, value=1, currentDriver=sdk_attr, driverValue=10)
	pm.setDrivenKeyframe(ik_2_driven_weight, value=1, currentDriver=sdk_attr, driverValue=10)

	pm.setAttr(sdk_attr, 0)
	# sdk_attr.set(0)

	'''
	Visbility Swapping
	'''

	sdk_icon.attr('fk_vis') >> fk_1_control_prime[0].attr('visibility')
	sdk_icon.attr('fk_vis') >> fk_joints[0].attr('visibility')
	sdk_icon.attr('ik_vis') >> ik_hand_icon.attr('visibility')
	sdk_icon.attr('ik_vis') >> pole_vector_icon.attr('visibility')
	sdk_icon.attr('ik_vis') >> ik_joints[0].attr('visibility')



