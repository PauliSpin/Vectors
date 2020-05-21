import vpython as vp

# https://www.glowscript.org/docs/VPythonDocs/vector.html

v1 = vp.vector(2, 3, 5)
v2 = vp.vector(4, 7, 1)

v = v1 + v2

print(f'      v1 = {v1}')
print(f'      v2 = {v2}')
print(f' v1 + v2 = {v}')
print(f' mag(v1) = {vp.mag(v1)} (Magnitude)')
print(f'mag2(v1) = {vp.mag2(v1)} (Magnitude ** 2)')
print(f'norm(v1) = {vp.norm(v1)} (Unit Vector in the direction of v1)')
print(f' hat(v1) = {vp.hat(v1)} (Unit Vector in the direction of v1)')
print()
print(f'  dot(v1, v2) = {vp.dot(v1, v2)}')
print(f'cross(v1, v2) = {vp.cross(v1, v2)}')
print()
print(
    f'diff_angle(v1, v2) = {vp.diff_angle(v1, v2)} (Angle between v1 and v2 in radians)')
print()
print(f'proj(v1, v2) = {v1.proj(v2)} (Vector projection of v1 along v2)')
print(f'comp(v1, v2) = {v1.comp(v2)} (Scalar projection of v1 onto v2)')
print(f'v1.equals(v2) = {v1.equals(v2)}')

# To normalise a vector i.e. set its length to 1:
v3 = vp.vector(2, 3, 5)
norm_v3 = vp.norm(v3)
print(f'norm(v3) = {norm_v3}')
print(f'Magnitude(norm(v3)) = {vp.mag(norm_v3)}')

# Change the direction of v1 without changing its magnitude
v2.hat = v1  # Changes the direction of v2 to that of v1
# but not its magnitude

# Rotating a Vector

# v2 = vp.rotate(v1, angle=a, axis=vp.vector(x, y, z))
# Angle in radians, The default axis is (0, 0, 1) for a rotation in the xy plane around the z axis
# Equivalent v1.rotate(v1, angle=a, axis=vector(x, y, z))
