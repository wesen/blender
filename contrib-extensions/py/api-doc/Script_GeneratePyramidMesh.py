# The following code was originally posted at http://www.pasteall.org/11056/python

# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
coords = [ -1.0,-1.0,-1.0, 1.0,-1.0,-1.0, 1.0,1.0,-1.0, -1.0,1.0,-1.0, 0.0,0.0,1.0 ]

# Define the faces by index numbers. Each faces is defined by 4 consecutive integers.
# For triangles you need to repeat the first vertex also in the fourth position.
faces = [ 2,1,0,3, 0,1,4,0, 1,2,4,1, 2,3,4,2, 3,0,4,3 ]

# Create a new mesh
me = bpy.data.meshes.new("Pyramid")         
me.add_geometry(5, 0, 5)                    # add 5 vertices, 0 edges and 5 faces
me.verts.foreach_set('co', coords)          # set the coordinates of the vertices
me.faces.foreach_set('verts_raw', faces)    # define the faces (automatically creates edges)
me.update()                                 # update the mesh with the new data

# Create a new object
ob = bpy.data.objects.new("Pyramid",'MESH') 
ob.data = me                                # link the mesh data to the object

scene = bpy.context.scene                   # get the current scene
scene.objects.link(ob)                      # link the object into the scene

ob.location = scene.cursor_location         # position object at 3d-cursor

