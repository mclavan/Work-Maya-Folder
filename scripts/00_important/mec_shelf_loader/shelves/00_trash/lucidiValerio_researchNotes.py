'''
Research Notes

lucidiValerio_researchNotes

'''

'''
# FT - Freeze Transforms 
Mel Command: makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
Python Command: pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
Flags: t = translate, r = rotate,  s = scale, n = normal, pn = preserve
normal

How did I find the Python code: This is pretty simple, all you have to do
to find the mel command is hit freeze transformations.

How do I use it: I use this command probably the most. This one as well as 
center pivot are used so much because it is important to always delete 
history. If there is too much history this can cause maya to crash 
and function improperly.  

# CP - Center Pivot
Mel Command: xform -cp;
Python Command: pm.xform(cp=1)
Flags: cp = center pivots

How did I find the Python code: In order to first find the mel command,
I have to create an object and move the pivot point elsewhere. In order 
to find this information, I had to echo all commands. 

How do I use it: Center Pivot - It is really frustrating when you hit "F" 
to pan your view to a selected object only find yourself looking in the 
wrong direction. By creating the CP shelf, now I can center the pivot 
to its correct location and not have to worry when I'm about to 
hit the "F" key. 

# HisS - Delete history of selected 
Mel Command: delete -ch;
Python Command: pm.delete(constructionHistory=True)
Flags: ch = construction history 

How did I find the Python code: In order to find the mel command, I had
to first create history by playing around with an object. In order to 
find this information, I had to echo all commands. 

How do I use it: Now this is an extremely important command to create
because this will prevent crashes. Too often will maya scenes break
down and freeze because there is too much history and that is just
too much information to retain. 

# HisA - Delete all history 
Mel Command: delete -all -constructionHistory;
Python Command: pm.delete(all=True, constructionHistory=True)
Flags: ch = construction history 

How did I find the Python code: In order to find the mel command, I had
to first create history by playing around with an object. In order to 
find this information, I had to echo all commands. 

How do I use it: This is pretty much the same as the command above but
acts as a bomb that destroys all the history in the scene. Using this
command is a faster method than selecting an object individually and
clearing history. 

# Joint - Joint tool 
Mel Command: setToolTo jointContext;
Python Command: pm.setToolTo(joint)
Flags: none

How did I find the Python code: In order to find the mel command all I
had to do is select the joint tool and it will appear in the script
editor

How do I use it: The essential bones of any rig; creating a joint system
will give a model the capacity to move.

# IKh - IK handle tool 
Mel Command: setToolTo ikHandleContext; 
Python Command: pm.setToolTo(ikHandle)
Flags: none

How did I find the Python code: In order to find this mel command I had
to first create three joints, then select the ikHandle tool and select
from one joint end to the other. 

How do I use it: You ca choose between having a single chain solver, or
a rotate plane solver. We used both of these methods when creating 
our bunny rig. Creating an ikHandle is an important part of rigging. 

# MirJ - Mirror joint
Mel Command: mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "lt" "rt";
Python Command:  pm.mirrorJoint(mirrorYZ=True, mirrorBehavior=True, searchReplace=True[lt=rt])
Flags: mxy = mirror xy, myz = mirror yz, mxz = mirror xz

How did I find the Python code: In order to find the mel command I had 
to create a joint system first. After I create several joints, I 
select the mirror joint.  

How do I use it: This command is incredibly more useful than what one
might expect. By having this command available, I can create a joint
system on a character, and then just mirror it so I instantly have
a full skeletal system in place. 

# OriJ - Orient joint 
Mel Command: joint -e  -oj none -zso;
Python Command:  pm.joint(e=0, oj=0, zso=0)
Flags: e = edit, oj = orient joint, zso = zero scale orient  

How did I find the Python code: In order to find the mel command, I had
to first create a joint system. After my joints have been created, I 
selected a joint and hit orient joint. 

How do I use it: Lets say that you have a joint system where one joint
is not oriented correctly, you use the orient joint tool to reorganize
that joint so it matches the orientation of the others in the system. 
I've only used this tool once but it nearly saved me from having to
recreate an entire system. 

# CntJ -Connect joint
Mel Command: connectJoint -cm;
Python Command: pm.connectJoint(cm=1)
Flags: cm = connect mode 

How did I find the Python code: In order to find the mel command, 
I created two sets of joints first. After my joints have been created,
I selected the end of one joint system and the root of another; then
hit connect joint.

How do I use it: I have never used the connect joint command. 
Although there is some use to it. As far as I know, you are supposed
to select the root joint of a system and the end joint of another
system. After selecting both joints, you click connect joints and they
will snap together. This seems handy though I will not know for sure
until I have used it. 

# Pole - Pole vector
Mel Command: poleVectorConstraint -weight 1;
Python Command: pm.poleVectorConstraint(weight=1)
Flags: w = weight float 

How did I find the Python code: To find the mel command, I created a
cube first. After I created my cube, I created a set of joints along 
with an ikHandle for them. I then selected my cube and my ikHandle and
hit pole vector. 

How do I use it: I really like this command. Maybe it's because I
like the word vector. Maybe it's because I can create functional
elbows and knees with it. Having the option to move the elbows in such
an intuitive way was much to my pleasure. 

# PRNT - Parent constraint
Mel Command: parentConstraint -mo -weight 1;
Python Command: pm.parentConstraint(weight=1)
Flags: mo = maintain offset, w = weight float 

How did I find the Python code: In order to find this mel command, 
I first created two cubes. After creating my cubes, I selected one of 
them, then another, and hit parent constraint. 

How do I use it: I use the parent constraint very often. This command is
useful for a wide variety of instances, such as: parenting geometry
to joints, joints to pads, and pads to icons.

# Ori - Orient
Mel Command: orientConstraint -offset 0 0 0 -weight 1;
Python Command: pm.orientConstraint(offset=(0, 0, 0), weight=1)
Flags: o = offset, w = weight float 

How did I find the Python code: In order to find this mel command, I
first created two cubes. After creating my cubes, I selected one and
then the other, and hit orient constraint. By playing around with the 
rotational values of the parent object, I am also changing those same
values for the child object. 

How do I use it: The orient command is an interesting command. by using
orient you are affecting other objects; but only in rotational values. 
You cannot scale or translate objects using orient. This can be useful 
in rigging in relation to moving the limbs of a character. 

# Crc - create circle
Mel Command: circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0 -s 12 -ch 1; 
Python Command: pm.circle(c=(0, 0, 0), nr=(0, 1, 0) , sw=360, r=1, d=3, ut=0, tol=0, s=12, ch=1)
Flags: c = center length, nr = normal length,  sw = sweep angle, r = 
radius length, d = degree int, ut = use tolerance, tol = tolerance length,
s = section int, ch = construction history 

How did I find the Python code: In order to find the mel command I
simply hit create circle. The mel command will be in the script editor. 

How do I use it: This command can be very useful if you're looking to 
create an icon for a rig. You can even use this to create more complicated and creative icons by manipulating the vertex. I like to use the circle icons for the spine and hips of a character rig. 

# Sqr - create square
Mel Command: nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ; 
Python Command: pm.nurbsSquare(c=(0, 0, 0), nr=(0, 1, 0), sl1=1, sl2=1, sps=1, d=3, ch=1)
nurbsSquare -c 0 0 0 -nr 0 1 0 -sl1 1 -sl2 1 -sps 1 -d 3 -ch 1 ; 
Flags: c = center length, nr = normal length, sl1 = side length 1, sl2 = 
side length 2, sps = spans per side int, d = degree int, ch = construction 
history

How did I find the Python code: In order to find this mel command, I 
opened up the script editor and hit create square. 

How do I use it: This command will create a square. Squares are 
quadrilaterals. Squares have four equal sides, and four right angles. 
The opposite sides of squares are parallel. I personally prefer using 
circles as icons for rigs. Don't be a square. 

# Cbe - create cube
Mel Command: polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
Python Command: pm.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
Flags: w = width length, h = height length, d - degree int, sx = 
subdivisions x, sy = subdivisions y, sz = subdivisions z, ax = axis 
length, cuv = create uvs, ch = construction history 

How did I find the Python code: In order to find the mel command I
opened up the script editor and hit create cube. 

How do I use it: Creating cubes are important from a perspective of 
modeling. As cubes are the starting shape of many objects, I often use 
cubes to create hard surface items. From a perspective of rigging, I 
can use a cube as an icon for the hands or feet. 

# Cst - cluster
Mel Command: newCluster " -envelope 1";
Python Command: pm.cluster(envelope=1)
Flags: 

How did I find the Python code: In order to find this mel command, I
opened up the script editor and hit cluster. In order to find this 
information, I had to echo all commands. 

How do I use it: This command used in the stretchy back process of 
rigging. You can use these clusters to create a more realistic spine 
with more functionality. 

# PoC - Point Constraint
Mel Command: pointConstraint -offset 0 0 0 -weight 1;
Python Command: pm.pointConstraint(offset=(0, 0, 0), weight=1)
Flags: o = offset, w = weight
 
How did I find the Python code: In order to find the mel command, I
created two cubes first. After creating my two cubes, I selected one 
and then the other and hit point constraint. 

How do I use it: The purpose of this tool is to constrain an objects 
position to another. I do not remember using this top and I don't find 
it very useful. I'm not sure what this tool is for. 

EXTRAS

# Spt - separate 
Mel Command:  polySeparate -sss 0 -ch 1 pCubeShape1;
Python Command: pm.polySeparate(sss=0, ch=1, polySurfaceShape1)
Flags: sss = seperate specific shell, ch = construction history 

How did I find the Python code: In order to find the mel command, I
first created two cubes and combines them. After combining my two cubes,
I selected the faces of one of them and hit seperate. In order to 
find this information, I had to echo all commands. 

How do I use it: The separate command is important because I use this 
when cutting up the geometry into smaller pieces. This process is 
required in order to give your model the slits and cuts needed to make 
it move anatomically correct.  

# Cmb - combine 
Mel Command: polyUnite -ch 1 -mergeUVSets 1 object2 object1;
Python Command: pm.polyUnite(ch=1, mergeUVSets=1)
Flags: ch = construction history, muv = mergeUV sets

How did I find the Python code: In order to find this mel command, I 
cerated two cubes first. After cerating my two cubes, I selected one
of them and then the other, and hit combine. I had to echo all commands 
to find this information. 

How do I use it: This command is useful as you can combine two 
different objects together and make them one. By doing this you can 
move them together and adjust rotate and values. If you wish to 
separate them again, all you have to do, is use to separate tool.

# Ext - extract
Mel Command: polyChipOff -ch 1 -kft 1 -dup 0 -off 0 pCube1.f[0];
Python Command: pm.polyChipOff(ch=1, kft=1, dup=0, off=0, pCubeShape6.f[0])
Flags: kft = keep faces together, ch = construction history, dup =
on/off

How did I find the Python code: In order to find the mel command, I 
first created a cube. Ater creating my cube, I selected a face, and then
hit extract. I had to echo all commands to find this information. 

How do I use it: I use this tool when there is a particular part of an 
object I want. I select the faces and hit the extract command to pull 
it off.

# NUKE - Nuke 
Mel Command: makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
delete -all -constructionHistory;
xform -cp;
Python Command: pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
pm.delete(all=True, constructionHistory=True)
pm.xform(cp=1)

How did I find the Python code: In order to create the NUKE command, I
found the mel commands for delete all history, center pivot, and freeze
transformations. After finding these commands I created a new shelf tool
and pasted these commands into the shelf editor. 

How do I use it: This has to be one of the most useful shelf tool I've 
created yet. This allows me to perform three commands with one click. 
