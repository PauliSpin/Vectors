import vpython as vp
import math
'''
# pip install Vpython
# https://www.glowscript.org/docs/VPythonDocs/index.html
'''
# vp.scene.width = 800
# vp.scene.height = 600
# vp.scene.title = "3D Axes"

vec_o = vp.vector(0, 0, 0)

vec_i = vp.vector(10, 0, 0)
vec_j = vp.vector(0, 10, 0)
vec_k = vp.vector(0, 0, 10)

text_size_scale = 0.1
unit_vec_x = vp.curve(vec_o, vec_i, color=vp.color.red)
x_text = vp.text(text='x', pos=vec_i, color=vp.color.red)

unit_vec_y = vp.curve(vec_o, vec_j, color=vp.color.orange)
y_text = vp.text(text='y', pos=vec_j, color=vp.color.orange)

unit_vec_z = vp.curve(vec_o, vec_k, color=vp.color.green)
z_text = vp.text(text='z', pos=vec_k, color=vp.color.green)

vp.scene.camera.pos = vp.vector(1, 1, 1)
print(f'Camera Axis Vector = {vp.scene.camera.axis}')
# vp.scene.camera.axis = vp.vector(1, 1, -1)

# print(vp.scene.camera.pos)
# print(vp.scene.camera.axis)
# pos  <0, 0, 1.73205>
# axis <0, 0, -1.73205>
# dtheta = 0.05
# theta = 0
# while (True):
#     vp.rate(20)
#     # vp.scene.camera.pos = vp.vector(10*math.cos(theta), 10*math.sin(theta), 5)
#     vp.scene.camera.axis = vp.vector(
#         10*math.cos(theta), 10*math.sin(theta), -31)
#     theta += dtheta
