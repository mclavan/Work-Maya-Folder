'''
QuinteroMichael_complex_CRI1_1404
Michael Quintero

How to Run:

import QuinteroMichael_complex_CRI1_1404
reload(QuinteroMichael_complex_CRI1_1404)

'''

import pymel.core as pm
print 'Window Opened'

def gui(*args):

	# Window opens all the tools created.
	# PoTaTools is the window name. Width changes width of button. Height changes height.
	# Heirarchy button is connected to the code for Ham.
	pm.window(title = 'PoTaTools')
	pm.columnLayout(width=250, height=40)
	pm.button(label="Heirachy", command=Ham, width=250, height=40)

	# 2 columns for the renaming tool
	pm.rowColumnLayout(numberOfColumns=2, columnWidth=[[1,100],[2,150]])

	# Orientation is the first part of naming. i.e lt for left or rt for right.
	pm.text(label='Orientation')
	global orient_field
	orient_field = pm.textField()

	# System name is the middle part of naming. i.e index used for index fingers or pinky for pinky fingers
	pm.text(label='System name')
	global name_field
	name_field = pm.textField()
	pm.columnLayout(width=250)

	# Button for Renaming tool. Connected to code for Naming.
	pm.button(label="Rename", command=Naming, width=250, height=40)

	# Button for Pad tool. Connected to code for Padding.
	pm.button(label= 'Pad', width=250, command=Padding, height=40)

	#shows window
	pm.showWindow()

#Code for the heirarchy tool
def Ham(*args):

	#GoHamOrGoHome
	print 'GoHamOrGoHome'
	selected_joint = pm.ls(selection=True)

	#bone is a variable for the root joint in a joint chain.
	for bone in selected_joint:
		print bone

		#dag flag is to continue down a joint chain.
		chain=pm.ls(bone, dag=True)
		chain.pop(-1)
		count = 1

		#limb is a variable for the child joints.
		#Print I Got it helps confirm that the script is working.
		for limb in chain:
			print limb
			print 'I Got it'


			icon_name = limb.replace('bind', 'icon')

			#makes a control icon circle.
			control_icon = pm.circle(name=icon_name, normal=[1, 0, 0])

			#clears selection.
			pm.select(cl=True)
			pad_name = limb.replace ('bind', 'prime')

			#makes the group for priming.
			prime = pm.group(name=pad_name)

			#adds temp constraints for the priming process
			temp_constraint1 = pm.parentConstraint(limb, prime)
			temp_constraint2 = pm.parentConstraint(limb, control_icon)

			#deletes the temp constraints after they've done there job.
			pm.delete(temp_constraint2, temp_constraint1)

			#parents the control_icon to the empty group
			pm.parent(control_icon, prime)

			#ch=True deletes the history on the prime
			#makeIdentity freezes transforms.
			pm.delete(prime, ch=True)
			pm.makeIdentity(prime, apply=True, t=1, r=1, s=1, n=0)

			#adds an orient constraint on the control_icon to the root_joint.
			#mo=True is for maintain offset.
			pm.orientConstraint(control_icon[0], limb, mo=True)

			#prints first pass for root joint and other pass for the child joints.
			if (count==1):
				print 'first pass'
			else:
				print 'other pass'
				pm.parent(prime, parent_prime)

			
			count = count + 1
			print count
			parent_prime = control_icon[0]


#Code for the renaming button
def Naming(*args):
	
	#Renames joints
	#rename_joints, orient, name, count, system_name are all variables
	#Selection selects the joint and dag continues down the joint chain
	#count will start the count at 0 and continue to go up
	#system_name will add bind to the end of the joints
	rename_joints = pm.ls(selection=True, dag=True)
	orient = orient_field.getText()
	name = name_field.getText()
	count = 0
	system_name = 'bind'

	#adds the count for all the joints in a chain.
	#the renaming works like orient_name_count_system_name. i.e lt_middle_01_bind
	for potato in rename_joints:
		count = count + 1
		new_name = '{0}_{1}_{2}_{3}'.format(orient, name, count, system_name)
		pm.rename(potato, new_name)

	#adds the waste to the last joint in a chain. i.e lt_middle_04_waste.
	waste_name = '{0}_{1}_{2}_{3}'.format(orient, name, count, 'waste')
	pm.rename(rename_joints[-1], waste_name)


#Code for the Padding tool
def Padding(*args):

	
	cat = pm.ls(selection=True)
	for mouse in cat:
		pm.select(cl=True)

		#names tha pad
		#makes group for pad
		pad_name = mouse.replace('bind', 'pad')
		pad = pm.group(name=pad_name)

		#temp constraint used for padding.
		temp_constraint = pm.parentConstraint(mouse, pad)

		#deletes temp_constraint.
		pm.delete(temp_constraint)

		#parents root joint to pad.
		pm.parent(mouse, pad)



gui()