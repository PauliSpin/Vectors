import vpython as vp
import math


class Arrow(object):

    vec_i = vp.vector(10, 0, 0)
    vec_j = vp.vector(0, 10, 0)
    vec_k = vp.vector(0, 0, 10)

    def __init__(self,  axis_label, axis_color, arrow_pos):

        if axis_label == 'x':
            vec_u = Arrow.vec_i
        elif axis_label == 'y':
            vec_u = Arrow.vec_j
        elif axis_label == 'z':
            vec_u = Arrow.vec_k

        self.rod_radius = vp.mag(vec_u) * 0.01

        self.rod = vp.cylinder(pos=arrow_pos, axis=vec_u,
                               radius=self.rod_radius, color=axis_color)
        self.cone = vp.cone(pos=vec_u, axis=0.1 * vec_u,
                            radius=vp.mag(vec_u) * 0.03, color=axis_color)
        if axis_label in 'xyz':
            self.axis_text = vp.text(text=axis_label, pos=self.cone.pos +
                                     0.1 * vec_u, color=axis_color)


vec_o = vp.vector(0, 0, 0)
x_axis = Arrow('x', vp.color.red, vec_o)
y_axis = Arrow('y', vp.color.cyan, vec_o)
z_axis = Arrow('z', vp.color.green, vec_o)
