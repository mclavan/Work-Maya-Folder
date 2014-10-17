'''
McLean Aneef

Description:

How to Run:

import rigging_tools
reload(rigging_tools)
'''

print 'rig tool started'

import pymel.core as pm
import maya.cmds as mc  

# create and rename each of the tools 
def pad_tool():
	
	selected_joint = pm.ls(selection = True)
	print 'selected joints', selected_joint

	#create empty group
	
	pad = pm.group(empty=True, name = 'pad')
	
	print 'root pad made:', pad

	cst_temp = pm.parentConstraint(selected_joint, pad , maintainOffset = False)

	pm.delete(cst_temp)
	print 'deleted constraint'


	print 'pad name'


	print 'pad created'	

def name_tool():
		

	joint_chain = pm.ls(selection=True, dag=True)
	print 'joint_chain', joint_chain
	

	ori = raw_input()
	name = raw_input()
	count = 1
	suffix = 'bind'

	for current_joint in joint_chain:

		new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count, suffix)
		print 'joint name:', new_name

		count = count + 1

		current_joint.rename(new_name)
	new_name = '{0}_{1}_{2}_{3}'.format(ori, name, count-1, 'waste')
	print 'Joint name: ', new_name
	current_joint.rename(new_name)



	print 'joint chain renamed'

def priming_tool():
	

	selected_joint_pt = pm.ls(selection=True, dag=True)

	selected_joint_pt.pop(-1)


	for priming in selected_joint_pt:

		icon = pm.circle(normal=[1,0,0])[0]
		print 'created icon'

		grp = pm.group()
		print 'group created'

		temp = pm.parentConstraint(priming, grp, maintainOffset=False)

		pm.delete(temp)
		print 'removed constraint'

		pm.delete(icon, ch=True)

		print 'deleted history'

		new_name = priming.replace('bind', 'icon')
		icon.rename(new_name)
		new_name = priming.replace('bind', 'null')
		grp.rename(new_name)

def mirror_controls():



	user_input = raw_input()

	selected_icons = pm.ls(selection=True)


	duplicated = pm.duplicate(selected_icons)

	print 'duplicated icons'

	grp = pm.group(empty=True)
	pm.parent(duplicated, grp)
	print 'grouped icons'

	pm.setAttr(grp + '.s' + user_input, -1)


	print 'mirrored objects'

def color_change():



	selected_objects = pm.ls(selection=True)[0]
	print 'objects selected:', selected_objects


	selected_objects.setAttr('overrideEnabled', 1)
	print 'override enabled'


	selected_objects.setAttr('overrideColor', 13)


















































