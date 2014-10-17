'''
Functions - 
	Arguments and Return Statements - Part 2

functions_args_03.py

How to Run:
import functions_args_03_final
reload(functions_args_03_final)
'''

import pymel.core as pm 

print 'Functions - args and return - part 2'

def create_back_system():
	'''
	Select root joint and curve. 

	import functions_args_03_final
	functions_args_03_final.create_back_system()

	'''
	selected = pm.ls(selection=True)
	root_joint = selected[0]
	back_curve = selected[1]

	# back_clusters = create_clusters(back_curve)

	print 'Back Hierarchy Created.'


def create_clusters(given_curve):
	'''
	Create clusters on a given curve. 

	import functions_args_02_final
	functions_args_02_final.create_clusters()

	'''
	
	# Loop through all the cvs in curve.
	clusters = []
	for current_cv in given_curve.cv:
		print 'Working on cv:', current_cv
		current_cluster = pm.cluster(current_cv)
		print 'Cluster Created:', current_cluster
		clusters.append(current_cluster)

	print 'Clusters Created.'

	return clusters

