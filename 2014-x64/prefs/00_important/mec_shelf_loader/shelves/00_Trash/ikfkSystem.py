
#import ikfkSystem as ifs
#reload(ifs)

import pymel.core as pm

# assume that naming convention is correct
# select root joint
# get hierarchy
driveSystem = pm.ls(selection = True, dag = True)

#figure out naming convention
rootDriveName = driveSystem[0]
count = 0
tempIKName = "IK"
tempFKName = "FK"

# duplicate twice and assign to variables
temp_IK = pm.duplicate(driveSystem, n = tempIKName)
ikSystem = pm.ls(temp_IK, dag = True)

temp_FK = pm.duplicate(driveSystem, n = tempFKName)
fkSystem = pm.ls(temp_FK, dag = True)

# rename the new joint systems

for newIKName in ikSystem:
	count = count + 1
	pm.rename(newIKName, rootDriveName.replace("_01_bind", "_0%d" % count + "_IK") )



count = 0
for newFKName in fkSystem:

	count = count + 1
	pm.rename(newFKName, rootDriveName.replace("_01_bind", "_0%d" % count + "_FK") )
	
	
