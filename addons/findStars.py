#!BPY

bl_info = {
   "name": "Select star poles",
   "author": "Manuel Odendahl <wesen@ruinwesen.com>",
   "description": "Select star poles in the active mesh",
   "version": (0, 1),
   "blender": (2, 6, 7),
   "category": "Mesh",
   "location": "Mesh > Vertices > Select start loops",
   "wiki_url": "",
   "warning": "",
   "tracker_url": ""
}

import bpy
import logging

def searchStars(mesh):
    vertexEdgeCount = {}

    def incEdgeCount(v):
        if vertexEdgeCount.get(v) == None:
            vertexEdgeCount[v] = 1
        else:
            vertexEdgeCount[v] += 1

    for edge in mesh.edges:
        (v1, v2) = edge.vertices
        incEdgeCount(v1)
        incEdgeCount(v2)
        
    res = []
    for k in vertexEdgeCount.keys():
        if vertexEdgeCount[k] >= 6:
            res += [k]
    
    return res

class MESH_OT_select_stars(bpy.types.Operator):
    '''Searches for star poles (6 or more edges) in the mesh.'''
    bl_idname = 'mesh.select_stars'
    bl_label = 'Select star poles'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        ob_act = bpy.context.active_object
        if not ob_act or ob_act.type != 'MESH':
            self.report({'ERROR'}, "No mesh selected!")
            return {'CANCELLED'}
        curMode = ob_act.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.tool_settings.mesh_select_mode[0] = True
        bpy.context.tool_settings.mesh_select_mode[1] = False
        bpy.context.tool_settings.mesh_select_mode[2] = False
        stars = searchStars(ob_act.data)
        for star in stars:
            ob_act.data.vertices[star].select = True
        bpy.ops.object.mode_set(mode=curMode)
        return {'FINISHED'}
    
def selectstarpoles_menu_func(self, context):
    self.layout.operator(MESH_OT_select_stars.bl_idname, text="Select star poles", icon="PLUGIN")
    
def register():
    bpy.utils.register_class(MESH_OT_select_stars)
    bpy.types.VIEW3D_MT_edit_mesh_vertices.append(selectstarpoles_menu_func)
    
def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(selectstarpoles_menu_func)

if __name__ == "__main__":
    register()
