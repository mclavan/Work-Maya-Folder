'''
Lesson - Joint Renamer
rigging_tools.py

Description:
    Pratical use of loops.
    Renaming joint based upon a naming convention.

How to Run:

import rigging_tools
reload(rigging_tools)


'''

print 'Rigging Tools Ative.'

import pymel.core as pm

def hierarchy():
   '''
   Creat hierarchy based upon a given system

   Select root joint chain and execute function.

   import rigging_tools
   rigging_tools.hierarchy()
   '''

   '''
   Input
   What are we wroking on?
   The root joint.
   '''
   joint_system = pm.ls(selection=True, dag=True)
   #print 'Joint System:', joint_system

   root_joint = joint_system[0]
   joint_2 = joint_system[2]
   joint_3 = joint_system[2]

   '''
   Padding Root Joint
   '''

   #Creat empty group.
   pm.group
   # Move Group over to the target joint.

   #Freeze Transforms on group.

   # Parent root joint to the group.

   '''
   Local Controls
   '''

   '''
   Control 1
   '''

   '''
   Control 2
   '''

   '''
   Control 3
   '''

   print 'hierarhy Created.'

