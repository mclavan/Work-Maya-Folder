import pymel.core as pm

# Circle
pm.circle()

pm.square()

pm.cube()

pm.arrow()

#Group
pm.group(em=True)

#Delete History
pm.delete(ch=True)

#Freeze Transforms
pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

#Center Pivot
pm.xform(cp=True)

#Cluster
pm.cluster()

#Constraints
pm.parentConstraint( 'cone1', 'cube1' )

pm.orientConstraint( 'cone1', 'cube1')

pm.pointConstraint( 'cone1', 'cube1')

pm.poleVectorConstraint( 'cone1', 'cube1')

# float

# integer

# string

