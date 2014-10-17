'''
Lesson - String Method Replace
string_replace.py


'''

print 'Lesson - String Method Replace'

import pymel.core as pm

'''
Naming Conventions

Root Joint - 'ct_head_01_bind'
Root Pad - 'ct_head_00_pad'
Proxy Geo - 'ct_head_01_proxy'
Local Pad - 'ct_head_01_local'
Control Icon - 'ct_head_01_icon'



root_joint = 'ct_head_01_bind'

proxy_name = root_joint.replace('_bind', '_proxy')
icon_name = root_joint.replace('_bind', '_icon')
root_pad_name = root_joint.replace('01_bind', '00_pad')


print 'Old Name: ', root_joint
print 'Proxy Name: ', proxy_name
print 'Control Name:', icon_name
print 'Root Pad Name:', root_pad_name
'''

'''
Get selected

selected = pm.ls(selection=True)
first_selected = selected[0]
second_selected = selected[1]

new_proxy_name = first_selected.replace('_bind', '_proxy')

second_selected.rename(new_proxy_name)
print 'New Proxy Name:', second_selected
'''

selected = pm.ls(selection=True)
root_joint = selected[0]

new_pad_name = root_joint.replace('01_bind', '00_pad')
print 'Pad Name:', new_pad_name
pad = pm.group(empty=True, name=new_pad_name)

