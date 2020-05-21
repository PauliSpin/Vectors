import vpython as vp
import math

vec_o = vp.vector(0, 0, 0)

vec_i = vp.vector(10, 0, 0)
vec_j = vp.vector(0, 10, 0)
vec_k = vp.vector(0, 0, 10)

rod_radius = vp.mag(vec_i) * 0.01   # 0.01

x_rod = vp.cylinder(pos=vec_o, axis=vec_i,
                    radius=rod_radius, color=vp.color.red)
x_cone = vp.cone(pos=vec_i, axis=0.1 * vec_i,
                 radius=vp.mag(vec_i) * 0.03, color=vp.color.red)
x_axis_text = vp.text(text='x', pos=x_cone.pos +
                      0.1 * vec_i, color=vp.color.red)

y_rod = vp.cylinder(pos=vec_o, axis=vec_j,
                    radius=rod_radius, color=vp.color.cyan)
y_cone = vp.cone(pos=vec_j, axis=vp.vector(
    0, vp.mag(vec_i) * 0.1, 0), radius=vp.mag(vec_j) * 0.03, color=vp.color.cyan)

y_axis_text = vp.text(text='y', pos=y_cone.pos +
                      0.1 * vec_j, color=vp.color.cyan)


print(f'Camera Posn Vector = {vp.scene.camera.pos}')
print(f'Camera Axis Vector = {vp.scene.camera.axis}')


vp.scene.camera.pos = vp.vector(15, 15, 17.3205)
# z_rod = vp.cylinder(pos=vec_o, axis=vec_k,
#                     radius=rod_radius, color=vp.color.green)
# z_cone = vp.cone(pos=vec_k, axis=vp.vector(
#     0, 0, vp.mag(vec_i) * 0.1), radius=vp.mag(vec_k) * 0.03, color=vp.color.green)

# print(f'Camera Posn Vector = {vp.scene.camera.pos}')
# print(f'Camera Axis Vector = {vp.scene.camera.axis}')

# print()
# print(f'Camera Posn Vector = {vp.scene.camera.pos}')
# print(f'Camera Axis Vector = {vp.scene.camera.axis}')

# dtheta = 0.05
# theta = 0
# while (True):
#     vp.rate(20)
#     vec_camera_pos = vp.vector(
#         4 + 1*math.cos(theta), 4 + 1*math.sin(theta), 5)
#     vp.scene.camera.pos = vec_camera_pos

#     vec_camera_axis = vp.vector(
#         math.cos(theta), math.sin(theta), -1.73205)
#     vp.scene.camera.axis = vec_camera_axis

#     theta += dtheta
