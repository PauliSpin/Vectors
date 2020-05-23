import vpython as vp
import math


class Arrow(object):

    vec_i = vp.vector(10, 0, 0)
    vec_j = vp.vector(0, 10, 0)
    vec_k = vp.vector(0, 0, 10)

    def __init__(self, v, arrow_label, arrow_color, arrow_pos):

        if arrow_label == 'x':
            vec_u = Arrow.vec_i
        elif arrow_label == 'y':
            vec_u = Arrow.vec_j
        elif arrow_label == 'z':
            vec_u = Arrow.vec_k
        else:
            vec_u = vp.vector(v.x * Arrow.vec_i.x, v.y *
                              Arrow.vec_j.y, v.z * Arrow.vec_k.z)

        self.rod_radius = vp.mag(vec_u) * 0.01
        scaled_arrow_pos = vp.vector(
            arrow_pos.x * Arrow.vec_i.x, arrow_pos.y * Arrow.vec_i.y, arrow_pos.z * Arrow.vec_i.z)
        self.rod = vp.cylinder(pos=scaled_arrow_pos, axis=vec_u,
                               radius=self.rod_radius, color=arrow_color)
        self.cone = vp.cone(pos=vec_u, axis=0.1 * vec_u,
                            radius=vp.mag(vec_u) * 0.03, color=arrow_color)
        if arrow_label in 'xyz':
            self.axis_text = vp.text(text=arrow_label, pos=self.cone.pos +
                                     0.1 * vec_u, color=arrow_color)


i = vp.vector(1, 0, 0)
j = vp.vector(0, 1, 0)
k = vp.vector(0, 0, 1)

vec_o = vp.vector(0, 0, 0)
x_axis = Arrow(i, 'x', vp.color.red, vec_o)
y_axis = Arrow(j, 'y', vp.color.cyan, vec_o)
z_axis = Arrow(k, 'z', vp.color.green, vec_o)

v_pos = vp.vector(2, 2, 2)
v = vp.vector(3, 4, 5)

my_v = Arrow(v, 'a', vp.color.magenta, v_pos)

print(f'Camera Posn Vector = {vp.scene.camera.pos}')
print(f'Camera Axis Vector = {vp.scene.camera.axis}')


vp.scene.camera.pos = vp.vector(10, 10, 7.3205)
