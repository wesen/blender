from bpy import context
from math import sin, cos, radians

# Get a reference to the operator for adding a primitive cube 

add_cube = bpy.ops.mesh.primitive_cube_add

# A object can exist in 32 layers (20 in global view and 12 in local view), 
# so the following code determines on which layers you want it to be

# Create a list of 32 elements, the value of element being False
layers = [False]*32

# Set the first element in the list created above to True
layers[0] = True

# Get the cursor's location
cursor = context.scene.cursor_location

# Radius of the circle
radius = 5

# Space the cubes around the circle. Default is 36 degrees apart
# Get a list of angles converted to radians
 
anglesInRadians = [radians(degree) for degree in range(0, 360, 36)]

# Loop through the angles, determine x,y using polar coordinates 
# and create object
for theta in anglesInRadians:
    x = cursor.x + radius * cos(theta)
    y = cursor.y + radius * sin(theta)
    z = cursor.z
    add_cube(location=(x, y, z), layer=layers)

