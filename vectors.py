import vpython as vp
import math

# pip install Vpython
# https://www.glowscript.org/docs/VPythonDocs/index.html


class Arrow(object):

    def __init__(self, v, axis_label, axis_color, arrow_pos):

        # If we are drawing the axis-triad arrows
        # then set the vec_u 'unit vector' accordingley.
        # This ignores v in the argument list.
        if axis_label == 'x':
            self.vec_u = vec_i  # Arrow.vec_i
        elif axis_label == 'y':
            self.vec_u = vec_j  # Arrow.vec_j
        elif axis_label == 'z':
            self.vec_u = vec_k  # Arrow.vec_k
        else:
            # Not drawing the axis triad
            # so just set tvec_u to the vector itself
            self.vec_u = v

        if axis_label in 'xyz':
            self.rod_radius = vp.mag(self.vec_u) * 0.01
            self.cone_radius = vp.mag(self.vec_u) * 0.03
        else:
            self.rod_radius = 0.02
            self.cone_radius = 0.06

        # Reduced Rod length = Rod length - Cone's axial length
        # Arrow length = Reduced Rod + Cone Axial Length
        # Use a fixed size of axis of the cone
        self.cone_axis = 0.1 * vp.norm(self.vec_u)

        # Reduce the size of the rod by the axial size of the cone
        self.rod = vp.cylinder(pos=arrow_pos, axis=self.vec_u - self.cone_axis,
                               radius=self.rod_radius, color=axis_color)

        # Place the base of the cone at the end of rod
        # which has been reduced by the cone's axial length
        self.cone = vp.cone(pos=self.vec_u - self.cone_axis + arrow_pos, axis=self.cone_axis,
                            radius=self.cone_radius, color=axis_color)

        # Note where the tip of the cone is,
        # which will define the starting point of
        # of the axis line
        self.cone_tip = self.vec_u + arrow_pos + 0.1 * vp.norm(self.vec_u)

        if axis_label in 'xyz':
            self.axis_text = vp.label(text=axis_label, pos=self.cone.pos +
                                      0.1 * self.vec_u, color=axis_color, xoffset=3, yoffset=3, box=False)
        else:
            self.axis_text = vp.label(text=axis_label, pos=arrow_pos +
                                      0.5 * self.vec_u, color=axis_color, xoffset=3, yoffset=3, box=False)

        self.axis_text.height = 0.6 * self.axis_text.height


# Initialize
vec_o = vp.vector(0, 0, 0)
vec_i = vp.vector(1, 0, 0)
vec_j = vp.vector(0, 1, 0)
vec_k = vp.vector(0, 0, 1)

# Axis colours
x_axis_color = vp.color.red
y_axis_color = vp.color.cyan
z_axis_color = vp.color.green

# Axes Triad
x_axis = Arrow(vec_o, 'x', x_axis_color, vec_o)
y_axis = Arrow(vec_o, 'y', y_axis_color, vec_o)
z_axis = Arrow(vec_o, 'z', z_axis_color, vec_o)

# Axes
x_axis_line = vp.curve(x_axis.cone_tip, 3 * vec_i,
                       radius=0.01, color=x_axis_color)
y_axis_line = vp.curve(y_axis.cone_tip, 3 * vec_j,
                       radius=0.01, color=y_axis_color)
z_axis_line = vp.curve(z_axis.cone_tip, 3 * vec_k,
                       radius=0.01, color=z_axis_color)


# Define vector A
vec_A = vp.vector(1, 2, 1)
pos_A = vp.vector(0.5, 0.5, 0.5)
col_A = vp.color.magenta
A = Arrow(vec_A, 'A(1, 2, 1)', col_A, pos_A)

# Define vector B
vec_B = vp.vector(2, 1, 3)
pos_B = pos_A + vec_A  # vp.vector(0.5, 0.5, 0.5)
col_B = vp.color.orange
A = Arrow(vec_B, 'B(2, 1, 3)', col_B, pos_B)

vec_C = vec_A + vec_B
pos_C = pos_A
col_C = vp.color.purple
C = Arrow(vec_C, f'C({vec_C.x}, {vec_C.y}, {vec_C.z})', col_C, pos_C)
