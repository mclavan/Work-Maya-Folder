'''
Control Creator
mec_controls.py



'''

import pymel.core as pm

'''
2D Shapes
'''

def circle_icon(name=None):
	control_icon = pm.circle(normal=[0, 1, 0])[0]
	if name:
		control_icon.rename(name)
	print 'Circle Icon Created: {0}.'.format(control_icon)
	return control_icon

def square_icon(name=None):
	control_icon = pm.curve(p=[(-1, 0, 1), (1, 0, 1), (1, 0, -1), (-1, 0, -1), (-1, 0, 1)],k=[0, 1, 2, 3, 4],d=1)
	if name:
		control_icon.rename(name)
	print 'Square Icon Created: {0}'.format(control_icon)
	return control_icon

'''
3D Shapes
'''

def cube_icon(name=None):
	control_icon = pm.curve(p=[(-0.967569, 0.871822, 0.685975), (0.849927, 0.871822, 0.685975), (0.849927, -0.945674, 0.685975), (-0.967569, -0.945674, 0.685975), (-0.967569, 0.871822, 0.685975), (-0.967569, 0.871822, -1.131521), (-0.967569, -0.945674, -1.131521), (-0.967569, -0.945674, 0.685975), (-0.967569, -0.945674, -1.131521), (0.849927, -0.945674, -1.131521), (0.849927, 0.871822, -1.131521), (-0.967569, 0.871822, -1.131521), (0.849927, 0.871822, -1.131521), (0.849927, 0.871822, 0.685975), (0.849927, -0.945674, 0.685975), (0.849927, -0.945674, -1.131521)],k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],d=1)
	if name:
		control_icon.rename(name)
	print 'Cube Icon Created: {0}'.format(control_icon)
	return control_icon


'''
Arrows
'''
# Curved Arrow
# curve(p=[(1.310304, 0, -2.377778), (1.339503, 0, -3.377351), (1.339503, 0, -3.377351), (1.339503, 0, -3.377351), (0.774864, 0, -3.303075), (0.262254, 0, -3.054952), (-0.146283, 0, -2.658175), (-0.409268, 0, -2.153029), (-0.409268, 0, -2.153029), (-0.409268, 0, -2.153029), (-0.5, 0, -1.590799), (-0.5, 0, -1.590799), (-1.017779, 0, -1.762164), (-1.017779, 0, -1.762164), (-0.1, 0, 0.0569633), (-0.1, 0, 0.0569633), (1.017779, 0, -1.762164), (1.017779, 0, -1.762164), (0.5, 0, -1.590799), (0.5, 0, -1.590799), (0.539968, 0, -1.838462), (0.655813, 0, -2.06098), (0.835774, 0, -2.23576), (1.061579, 0, -2.345059), (1.310304, 0, -2.377778)],k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 22, 22],d=3)

def arrow_icon(name=None):
	control_icon = pm.curve(p=[(-0.356461, 0, -2.947244), (0.356461, 0, -2.947244), (0.356461, 0, -1.299482), (1.017779, 0, -1.762164), (0, 0, 0.0112178), (-1.017779, 0, -1.762164), (-0.356461, 0, -1.299482), (-0.356461, 0, -2.947244)],k=[0, 1, 2, 3, 4, 5, 6, 7],d=1)
	if name:
		control_icon.rename(name)
	print 'Single Arror Icon Created: {0}'.format(control_icon)
	return control_icon

'''
General Control Tools
'''

def select_all_cvs():
	selected_control = pm.ls(selection=True)[0]
	pm.select(selected_control.cv[:], replace=True)

def select_alternate_cvs(start=0):
	selected_control = pm.ls(selection=True)[0]
	pm.select(selected_control.cv[start::2], replace=True)	

def snap_control(target_object, control_icon, orient=False):	
	if orient:
		temp_constraint = pm.parentConstraint(target_object, control_icon)
	else:
		temp_constraint = pm.pointConstraint(target_object, control_icon)

	pm.delete(temp_constraint)
	print 'Control: {0} Snapped to {1}.'.format(control_icon, target_object)

def snap_selected_control(orient=False):
	selected = pm.ls(selection=True)
	snap_control(selected[0], selected[1], orient)

def prime_control(target_joint, control_icon, pads=0):

	prime_hierarchy = []
	prime_group_name = control_icon.replace('_icon', '_prime')
	prime_group = pm.group(empty=True, name=prime_group_name)
	prime_hierarchy.append(prime_group)

	temp_constraint = pm.parentConstraint(target_joint, prime_group)
	pm.delete(temp_constraint)
	temp_constraint = pm.parentConstraint(target_joint, control_icon)
	pm.delete(temp_constraint)
	pm.parent(control_icon, prime_group)
	pm.makeIdentity(control_icon)

	# Adding Pads
	i = 0
	while i < pads:
		pad_name = control_icon.replace('_icon', '_pad{0}'.format(i+1))
		pad = pm.group(control_icon, name=pad_name)
		pm.xform(pad, piv=[0, 0, 0])
		prime_hierarchy.append(pad)
		i = i + 1

	return prime_hierarchy

'''
GUI
'''







	
