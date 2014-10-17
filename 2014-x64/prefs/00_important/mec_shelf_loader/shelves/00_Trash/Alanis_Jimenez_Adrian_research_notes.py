'''
Research Notes

Adrian Alanis Jimenez

Current Shelf Tools: 



* Includes double click and drop down menu buttons.


# It is not required to have either double click buttons 
# 	or drop down menus.  Just make sure you document them 
# 	below for easier grading.

Double Click Buttons: None

Drop Down Menus: None

'''

'''
Each tool you will need document:
	1) MEL Commmand
	2) What type of command is it and how did you find it?
	3) Convert MEL to Python.
	4) Important Flags
'''

'''
General Tools Research
'''

# Freeze Transforms
	makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
	#Use echo all , second tested from working possible commands.
	pm.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
	apply , jointOrient, normal, preserveNormals, rotate, scale, translate.


# Delete History
	delete -ch
	#echo all able to find other wise, second tested from working possible commands when using  echo all.
	pm.delete(ch=True)
	attribute, channels, constraints, constructionHistory, controlPoints, hierarchy, shape, staticChannels, timeAnimationCurves, unitlessAnimationCurves


# Center Pivot
	xform -cp
	#Use echo all unable to find other wise, second tested from working possible commands.
	pm.xform (cp= True)


# Single Chain and Rotate Plan IKs
	ikHandle
	#NO echo all, found looking at the script editor after aplying the tool/ Maya comand doc.
	pm.ikHandle( n = "",ee="")
	solver(sol), jointList(jl),name(n), startJoint(sj), curve(c),endEffector(ee)


# Cluster
	Cluster 
	#found looking at the script editor after aplying the tool/ Maya comand doc.
	pm.cluster('','')
	name(n),ignoreSelected(ignoreSelected),weightedNode(wn)


# Grouping (Does not need to be included on Shelf!)
	group
	#Use eco all, third one tested
	pm.group('','')
	absolute, empty, name, parent, relative, world


# Parenting (Does not need to be included on Shelf!)
	parent
	#echo all on, first one tested, second one in the list.
	pm.paren('','')
	world(w), relative(r),removeObject(rm),shape(s),noConnections(nc)


# Duplicating (Does not need to be included on Shelf!)
	duplicate
	#echo all third in the list and tested.
	pm..duplicate('')
	name(n),smartTransform(st),returnRootsOnly(rr),renameChildren(rc),parentOnly(po)	

'''
Control Icons
- Circle, Square, Cube, and Arrow are the minimum requirements.
- Think about which direction the control should be pointed. 
	- Compare local oriented direction compared to world. 
- Nurbs square and cubes are NOT valid control icons.
'''

# Circle
	circle 
	#Explained in class,echo all disable.first tested.
	pm.circle()
	caching, center, centerX, centerY, centerZ, constructionHistory, degree, first, firstPointX, firstPointY, firstPointZ, fixCenter, name, nodeState, normal, normalX, normalY, normalZ, object, radius, sections, sweep, tolerance, useTolerance


# Square
	curve -d 1 -p 0 0 0 -p 0 0 2 -p 2 0 2 -p 2 0 0 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;
	#eco all off, aftter creating curve, using podcats way to get "python's version"
	mel_line="curve -d 1 -p 0 0 0 -p 0 0 2 -p 2 0 2 -p 2 0 0 -p 0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 ;"
	pm.mel.eval(mel_line)
	degree(d),replace(r),append(a),knot(k),worldSpace(ws),objectSpace(os).


# Cube
	curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 -1 -1 -p -1 -1 -1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 -p -1 -1 1 -p -1 1 1 -p -1 1 1 -p 1 1 1 -p 1 1 1 -p 1 -1 1 -p -1 -1 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;
	#eco all off, aftter creating a poly cube and a curve using the edges of cube to trace it, using podcats way to get "python's version"
	mel_line="curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 -1 -1 -p -1 -1 -1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 -p -1 -1 1 -p -1 1 1 -p -1 1 1 -p 1 1 1 -p 1 1 1 -p 1 -1 1 -p -1 -1 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 ;"
	pm.mel.eval(mel_line)
	degree(d),replace(r),append(a),knot(k),worldSpace(ws),objectSpace(os).


# Arrow
	curve -d 1 -p -0.2 0 -0.2 -p -0.0666667 0 -0.2 -p -0.0666667 0 -0.0666667 -p 0 0 -0.0666667 -p -0.133333 0 0.133333 -p -0.266667 0 -0.0666667 -p -0.2 0 -0.0666667 -p -0.2 0 -0.2 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;
	#eco all off, aftter creating curve snaping to grid, using podcats way to get "python's version"
	mel_line="curve -d 1 -p -0.2 0 -0.2 -p -0.0666667 0 -0.2 -p -0.0666667 0 -0.0666667 -p 0 0 -0.0666667 -p -0.133333 0 0.133333 -p -0.266667 0 -0.0666667 -p -0.2 0 -0.0666667 -p -0.2 0 -0.2 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;"
	pm.mel.eval(mel_line)
	degree(d),replace(r),append(a),knot(k),worldSpace(ws),objectSpace(os).


'''
Constraints
- Remember to test offset on and off with these commands.
****Shelf buttons are used in a specific object in the maya scene
'''
# Parent Constraint
	parentConstraint -mo -weight 1;
	#this is a mel button found in the animation window under constraint
	pm.parentConstraint('','')	
	weight(w), skipTranslate(st),targetList(tl), weightAliasList(wal)
	

# Orient Constraint
	orientConstraint -offset 0 0 0 -weight 1;
	#this is a mel button found in the animation window under constraint
	pm.orientConstraint('','')
	targetList(tl), weightAliasList(wal), weight(w), skipTranslate(st)
	

# Point Constraint
	pointConstraint -offset 0 0 0 -weight 1;
	#this is a mel button found in the animation window under constraint
	pm.pointConstraint('','')
	targetList(tl), weightAliasList(wal), offset(o)
		

# Pole Vector Constraint
	poleVectorConstraint -weight 1;
	#this is a mel button found in the animation window under constraint
	pm.poleVectorConstraint('','')
	targetList(tl), weightAliasList(wal), weight(w)
	

# How does this constraint differ from the previous three.
	#The pole vector has less flags and is adjust such that the in weighted average of the world space position target objects lies is the "rotate plane" of the handle.
	
'''
Attributes (Covered in Podcast)
'''

# Create float attribute
	addAttr -ln "Float"  -at double;
	setAttr -e-keyable true;
	#Mel code found in script editor, adding a attribute inside the channel box of an object
	#Phyton code was found in podcast.
	.addAttr('Float', keyable=True)

	 -longName (-ln), -attributeType (-at),-enumerated (-e), -keyable (-k)


# Create Separator Attribute
	addAttr -ln "Separator"  -at "enum" -en "---";
	setAttr -e-keyable true;
	setAttr -lock true;
	#Mel code found in script editor, adding a attribute inside the channel box of an object
	#Phyton code was found in podcast.
	.addAttr('Separator', at='enum', en='---', keyable=True)
	.Separator.set(lock=True)
	
	-longName (-ln), -attributeType (-at), -enumName (-en), -enumerated (-e) -keyable (-k)



# Template Attributes 
	
	addAttr -ln "index_curl"  -at double;
	setAttr -e-keyable true;
	addAttr -ln "middle_curl"  -at double;
	setAttr -e-keyable true;
	addAttr -ln "pinky_curl"  -at double;
	setAttr -e-keyable true;
	#Mel code found in script editor, adding a attribute inside the channel box of an object
	#Phyton code was found in podcast.
	selected =pm.ls(selection=True)
	first_selected =selected[0]
	first_selected.addAttr('index_curl', keyable=True)
	first_selected.addAttr('middle_curl', keyable=True)
	first_selected.addAttr('pinky_curl', keyable=True)
	-longName (-ln), -attributeType (-at), -enumerated (-e)





