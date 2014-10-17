'''
Michael Clavan
tag_generator.py

How to Run:

import tag_generator
tag_generator.gui()

'''

try:
	import pymel.core as pm

except:
	print 'Pymel does not exists.'

def gui():
	window_width = 300
	window_height = 700
	window_object = pm.window(width=window_width, height=window_height, sizeable=False)
	pm.columnLayout(width=window_width)
	global tag_field
	tag_field = pm.scrollField( width=window_width, editable=True, 
			wordWrap=False, text='' )
	# pm.button(width+window_width, label='Generate Tags')
	pm.button(width=window_width, label='Generate Tags', command=tags_gui_work)
	window_object.show()



# Remember unit testing

def tags_gui_work(*args):
	tags_line = tag_field.getText()
	tags = tag_generator(tags_line)
	print '\n'.join(tags)


def tag_generator(tags):
	split_tags = tags.split('\n')
	# print split_tags
	tags = []
	for current_tag in split_tags:
		# current_tag = 'Codec'
		if current_tag != '':
			tags_line = '\t\t\t<tag>{0}</tag>'.format(current_tag)
			tags.append(tags_line)
			 #print tags_line
	return tags




'''
# Result: 'Retopology\nAnatomy\nPolygons\nTopology\nProportions\nScale\nHardsurface\nOrganic\nEdge Quality\nHolding Edges\nEdge Flow\nBevel\nBuilding In Parts\nInsert Edge Loop\nExtrude Tool\nGrouping\nLayering\nPrimitives\nTranslation Tool\nSnapping\nPivots\nSilhouette\nScale\nProportions\nThree Mode\nNURBS Curves\nRevolve Tool\nLoft Tool\nEdge Flow Reduction\nEdge Flow Additions\nNon-Manifold Geometry\nClean Up Tool\nUV Layout\nTexturing\nPlanar Mapping\nSpherical Mapping\nCylindrical Mapping\nAutomatic Mapping\nShot Camera\nPerspective Camera\nDense Geometry\nLattice Tool\nOutiner\nRough Boards\nFinal Boards\nMove\nScale\nRotate\nReference\nNavigation\nStory\nNarrative\nHypershade\nCharacter Modeling\nProp Modeling\nRender\nMaps\nUV Seams\nUV Stretching\nUV Zero To One\nRigging\nSet Up\nJoints\nIk\nFk\nRigging Controls\nKey Frames\nPrincipels of Animation\nCharacter Set\nVisibility Swap\nLighting\nShadows\nRaytracing\nMaterials\nLambert\nRender View\nRender Settings\nSpot Light\nCodec' # 

'''

# These will be place inside of tags.  I'm looking for new lines.

# There might be tabs latter.



