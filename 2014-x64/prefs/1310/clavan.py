'''
Author
ScriptName.py

Description:
	Starter Script

How to Run:

import clavan
reload(clavan)

'''


print 'Welcome, Michael'
print 'CRI'

import pymel.core as pm

# Create two controls
# pymel

#                  0							1
# [nt.Transform(u'nurbsCircle1'), nt.MakeNurbCircle(u'makeNurbCircle1')]
control_icon = pm.circle()[0]
# pm.circle()
# pm.circle()
print 'Control Icon:', control_icon
pm.delete(control_icon, ch=True)

