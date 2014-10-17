'''
mec_startup_tools.py 
Michael Clavan

How to Run:

import mec_startup_tools
mec_startup_tools.init_project_setup()
mec_startup_tools.project_gui()

'''

print 'Startup Tools Activated.'

import os
import pymel.core as pm



project_paths = ['/Users/mclavan/Documents/fullsail/00_CAN-Rigs/00_Bunnsy',
				'/Users/mclavan/Documents/fullsail/00_CAN-Rigs/Bugsy',
				'/Users/mclavan/Desktop',
				'/Users/mclavan/Downloads/animus_RIG']

class Project():
    def __init__(self, project_path=None, project_name=None, description=None):
        self.project_path = project_path
        self.project_name = project_name
        self.description = description
        
    def set_project_path(self, project_path):
    	self.project_path = project_path

    def activate_project(self):
    	if self.project_path:
    		pm.mel.setProject(self.project_path)


def init_project_setup():

	# Load Previous Projects
	global projects
	projects = []
	for current_project in project_paths:
		project_name = os.path.split(current_project)[-1]
		temp_project = Project(current_project, project_name, current_project)
		projects.append(temp_project)

def project_gui():
	window_name = 'mec_project_window'
	window_exists = pm.window(window_name, exists=True)
	window_pref_exists = pm.windowPref(window_name, exists=True)
	if window_exists:
		pm.deleteUI(window_name)
	if window_pref_exists:
		pm.windowPref(window_name, r=True)

	window_width = 200
	window_object = pm.window(window_name, title='Quick Project Set', sizeable=False)
	main_layout = pm.columnLayout()

	pm.separator(width=window_width, height=15)
	pm.text(width=window_width, label='Projects')
	pm.separator(width=window_width, height=15)

	for current_project in projects:
		pm.button(width=window_width, label=current_project.project_name, 
			command=pm.Callback(current_project.activate_project),
			ann=current_project.description)
	window_object.show()
