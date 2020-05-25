import vpython as vp
import math

# pip install Vpython
# https://www.glowscript.org/docs/VPythonDocs/index.html


class Arrow(object):
    '''
    Created an arrow using a cyclinder and a cone.
    Requires the vector and its position as well as a label
    and its position.
    '''

    def __init__(self, v, v_label, v_label_pos, v_color, v_pos):
        self.v = v                              # Vector
        self.v_label = v_label                  # Label for the vector
        self.v_color = v_color                  # Vector colour
        # Position of vector i.e. where its tail is.
        self.v_pos = v_pos
        # Axis of the cone; same as the vector's
        self.cone_axis = 0.1 * vp.norm(self.v)
        self.rod_radius = 0.02                  # Absolute radius of the rod
        self.cone_radius = 0.06                 # Absolute radius of the rod

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
        self.cone_tip = self.v + v_pos + 0.1 * vp.norm(self.v)

        self.axis_text = vp.label(text=v_label, pos=v_pos + v_label_pos * (
            self.cone_tip - v_pos), color=v_color, xoffset=3, yoffset=3, box=False)
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
x_axis = Arrow(i, 'x', 1, x_axis_color, o)  # Label position is 1 x vector i
y_axis = Arrow(j, 'y', 1, y_axis_color, o)
z_axis = Arrow(k, 'z', 1, z_axis_color, o)

# Define vector A
vec_A = vp.vector(1, 2, 1)
pos_A = vp.vector(0.5, 0.5, 0.5)
col_A = vp.color.magenta
A = Arrow(vec_A, 'A(1, 2, 1)', 0.5, col_A, pos_A)   # Label position is 0.5 A

# Define vector B
vec_B = vp.vector(2, 1, 3)
pos_B = vp.vector(0.5, 0.5, 0.5)
col_B = vp.color.orange
A = Arrow(vec_B, 'B(2, 1, 3)', 0.5, col_B, pos_B)


vec_C = vp.cross(vec_A, vec_B)
pos_C = pos_A
col_C = vp.color.purple
C = Arrow(vec_C, f'AxB({vec_C.x}, {vec_C.y}, {vec_C.z})', 0.5, col_C, pos_C)
