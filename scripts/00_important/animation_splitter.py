'''
Animation Splitter

import animation_splitter
reload(animation_splitter)
animation_splitter.get_bound_joints()


import animation_splitter
reload(animation_splitter)
anim = animation_splitter.get_bound_joints()
anim.export_all()
anim.clear_sequences()
anim.add_anim_seqence([0,17], 'twist.ma')
anim.add_anim_seqence([18,30], 'bend.ma')


'''
import os
import pymel.core as pm

'''
Selected objects with keyframes
'''

'''
tracked_objects = pm.ls('*_bind')
pm.select(tracked_objects)

def save_cycle(tracked_objects, range=[0,30]):
	pm.select(tracked_objects)
'''

def get_bound_joints():
	bound_joints = pm.ls('*_bind')
	pm.select(bound_joints, r=True)
	original_path = '/Users/mclavan/Desktop/shoulder_animBaked.ma'
	output_path = '/Users/mclavan/Desktop/cycles'
	animation_sequences = Tracked_Cycles(original_path, output_path)
	animation_sequences.add_anim_seqence([0,10], '00_anim@walk.ma')
	animation_sequences.add_anim_seqence([10,20], '00_anim@idle.ma')
	animation_sequences.add_anim_seqence([20,30], '00_anim@jump.ma')

	return animation_sequences

class Tracked_Cycle():
	def __init__(self, tracked_objects, range, output_path, orginal_path):
		# File location
		# File Name
		self.range = range
		self.tracked_objects = tracked_objects
		self.output_path = output_path #  or self.work_space_path()
		self.orginal_path = orginal_path

	def work_space_path(self):
		return None	

	def export(self):
		# Select Objects
		pm.select(self.tracked_objects, r=True)
		# Copy Frames
		pm.copyKey(time=(self.range[0],self.range[1]))

		# Delete all keyframes
		pm.cutKey(time=[':'], clear=True)

		# Paste Frames
		pm.pasteKey(time=[0,0])

		# Save out file
		pm.saveAs(self.output_path)

		# Reopen file
		pm.openFile(self.orginal_path)



class Tracked_Cycles():
	def __init__(self, orginal_path, output_path=None, add_selected=True):
		self.file_path = orginal_path
		self.anim_sequences = []
		self.tracked_objects = []
		self.output_path = output_path
		self.orginal_path = orginal_path
		
		if add_selected:
			self.add_tracked(pm.ls(selection=True))

	def add_tracked(self, new_objects=[]):
		self.tracked_objects.extend(new_objects)

	def clear_sequences(self):
		self.anim_sequences = []

	def clear_tracked(self):
		self.tracked_objects = []

	def assign_output_path(self, output_path):
		self.output_path = output_path

	def add_anim_seqence(self, range, seqence_name):
		full_output_path = os.path.join(self.output_path, seqence_name)
		current_seqence = Tracked_Cycle(self.tracked_objects, range, full_output_path, self.orginal_path)
		self.anim_sequences.append(current_seqence)

	def export_all(self):
		if self.tracked_objects:
			for current_seqence in self.anim_sequences:
				current_seqence.export()


"""
'''
Research:

Copy, Paste, and Cut key frames.

'''
import pymel.core as pm
cut_keyframes = pm.cutKey(time=(18,30))

copy_frames = pm.copyKey(time=(0,18))

# Paste at zero keyframe 
pm.pasteKey(time=[0,0])

# Delete keyframes
# timeSliderClearKey requires that the keys are selected.
pm.mel.timeSliderClearKey()

pm.cutKey(time=[':'], clear=True)


'''
Process 
'''
# Select Objects

# Copy Frames
pm.copyKey(time=(0,18))

# Delete all keyframes
pm.cutKey(time=[':'], clear=True)

# Paste Frames
pm.pasteKey(time=[0,0])

# Save out file
pm.saveAs(full_path)

# Reopen file
pm.openFile(full_open_path)



'''
Saving Scenes and Reopening
- Do this in pymel they have some better processes.
'''
maya_file = 'shoulder@idle22.ma'
file_path = '/Users/mclavan/Documents/fullsail/'
full_path = '{0}{1}'.format(file_path, maya_file)
pm.saveAs(full_path)


full_open_path = '/Users/mclavan/Desktop/shoulder_animBaked.ma'
pm.openFile(full_open_path)

'''
This script will open, modify, save as, then reopen original file.
I feel this can be done under the hood in batch mode.  
'''

"""



