# basic_win.py

print 'hi'

import pymel.core as pm

def gui():

	window_obj = pm.window(width=300, height=400)
	main_layout = pm.columnLayout()
	# controls_layout = control_icons_widget(main_layout)
	global controls_obj, controls_obj2
	controls_obj = OOP_Control_Icon_Widget(main_layout)
	pm.separator(width=300, height=15)
	controls_obj2 = OOP_Control_Icon_Widget(main_layout)
	pm.separator(width=300, height=15)
	controls_obj3 = OOP_Control_Icon_Widget(main_layout)
	pm.separator(width=300, height=15)
	controls_obj4 = OOP_Control_Icon_Widget(main_layout)

	window_obj.show()


def control_icons_widget(current_parent):
	widget_layout = pm.rowColumnLayout(parent=current_parent, 
			numberOfColumns=3, cw=[[1, 100], [2, 100], [3, 100]])
	pm.button()
	pm.button()
	pm.button()
	pm.setParent(current_parent)
	return widget_layout



class OOP_Control_Icon_Widget():
	def __init__(self, current_parent):
		self.add_buttons = []
		self.main_layout = pm.columnLayout(parent=current_parent)
		self.widget_layout = pm.rowColumnLayout(numberOfColumns=3, 
			cw=[[1, 100], [2, 100], [3, 100]])
		pm.button()
		pm.button()
		pm.button()		

		pm.setParent(self.main_layout)
		pm.rowColumnLayout(nc=2, cw=[[1,150], [2,150]])
		pm.button(width=150, label='Increase', command=self.increase_buttons)
		pm.button(width=150, label='Decrease', command=self.decrease_buttons)
		pm.setParent(current_parent)

	def increase_buttons(self, *args):
		self.add_buttons.append(pm.button(parent=self.widget_layout))
		self.add_buttons.append(pm.button(parent=self.widget_layout))
		self.add_buttons.append(pm.button(parent=self.widget_layout))

	def decrease_buttons(self, *args):
		pm.deleteUI(self.add_buttons[-1])
		self.add_buttons.pop()		
		pm.deleteUI(self.add_buttons[-1])
		self.add_buttons.pop()	
		pm.deleteUI(self.add_buttons[-1])
		self.add_buttons.pop()	
