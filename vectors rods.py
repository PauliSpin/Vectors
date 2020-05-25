import vpython as vp
import math

# pip install Vpython
# https://www.glowscript.org/docs/VPythonDocs/index.html


class Arrow(object):
    def __init__(self, v, v_label, v_label_pos, v_color, v_pos):
        self.v = v
        self.v_label = v_label
        self.v_color = v_color
        self.v_pos = v_pos
        self.cone_axis = 0.1 * vp.norm(self.v)
        self.rod_radius = 0.02
        self.cone_radius = 0.06
        self.cone_axis = 0.1 * vp.norm(self.v)

        # Reduce the size of the rod by the axial size of the cone
        self.rod = vp.cylinder(pos=v_pos, axis=self.v - self.cone_axis,
                               radius=self.rod_radius, color=v_color)

        # Place the base of the cone at the end of rod
        # which has been reduced by the cone's axial length
        self.cone = vp.cone(pos=self.v - self.cone_axis + v_pos, axis=self.cone_axis,
                            radius=self.cone_radius, color=v_color)
        # Note where the tip of the cone is,
        # which will define the starting point of
        # of the axis line
        # self.cone_tip = self.v + v_pos + 0.1 * vp.norm(self.v)

        # self.axis_text = vp.label(text=v_label, pos=self.cone.pos + v_label_pos *
        #                           self.v, color=v_color, xoffset=3, yoffset=3, box=False)
        # self.axis_text.height = 0.6 * self.axis_text.height


# Initialize
o = vp.vector(0, 0, 0)
i = vp.vector(1, 0, 0)
j = vp.vector(0, 1, 0)
k = vp.vector(0, 0, 1)

# Axis colours
x_axis_color = vp.color.red
y_axis_color = vp.color.cyan
z_axis_color = vp.color.green

# Axes Triad
x_axis = Arrow(i, 'x', i, x_axis_color, o)
y_axis = Arrow(j, 'y', j, y_axis_color, o)
z_axis = Arrow(k, 'z', k, z_axis_color, o)
