'''
follow_curve.py
Michael Clavan

Description:
	- This script creates a curve that is attached to ether end to selected objects.
	- Mainly its snapping both ends and then appling a cluster.  These clusters
	are then point constraint to their respected selected object.
	- The script creates a group to store the curve and clusters the script generates.
	- The group can be parented under the master control icon for the rig.


'''
import pymel.core as pm

def create_follow_curve_selected():
	selected = pm.ls(selection=True)
	target_1 = selected[0]
	target_2 = selected[1]
	create_follow_curve(target_1, target_2)

def create_follow_curve(target_1, target_2):
	target_2_pieces = target_2.split('_')
	target_2_pieces[-1] = 'follow'
	point_line_name = '_'.join(target_2_pieces)

	point_line = pm.curve(d=1, name=point_line_name, p=((-1, 0, 0), (1, 0, 0)), k=(0, 1))
	cv_1 = point_line.cv[0]
	cv_2 = point_line.cv[1]

	target_2_pieces[-1] = 'clst1'
	cv_cluster_1_name = '_'.join(target_2_pieces)
	target_2_pieces[-1] = 'clst2'
	cv_cluster_2_name = '_'.join(target_2_pieces)

	cv_cluster_1 = pm.cluster(cv_1, relative=True, name=cv_cluster_1_name)
	cv_cluster_2 = pm.cluster(cv_2, relative=True, name=cv_cluster_2_name)
	pm.pointConstraint(target_1, cv_cluster_1)
	pm.pointConstraint(target_2, cv_cluster_2)

	target_2_pieces[-1] = 'folGrp'
	point_line_grp_name = '_'.join(target_2_pieces)
	point_line_grp = pm.group(cv_cluster_1, cv_cluster_2, point_line, world=True, name=point_line_grp_name)
	cv_cluster_1[1].attr('v').set(0)
	cv_cluster_2[1].attr('v').set(0)

	# Red
	icon_color = 13
	pm.setAttr('{0}.overrideEnabled'.format(point_line), 1)
	pm.setAttr('{0}.overrideColor'.format(point_line), icon_color)
	# While reference is turned on the color will NOT display.
	pm.setAttr('{0}.overrideDisplayType'.format(point_line), 2)



