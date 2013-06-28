# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

#
#  Written by Ivo Grigull
#  http://ivogrigull.com
#  http://character-rigger.com
#

bl_info = {
    "name": "Norman Rig Addon",
    "author": "Ivo Grigull (Loolarge)",
    "version": (0,1),
    "blender": (2, 5, 7),
    "api": 34470,
    "location": "Property panel -> Norman Properties",
    "description": "Fractured Object, Bomb, Projectile, Recorder",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Animation"}



if "bpy" in locals():
    import imp
    imp.reload(load_linked)
    imp.reload(default_values)
    imp.reload(norman_snapping)
    imp.reload(norman_UI)
    imp.reload(built_in_ks)
else:
    from . import load_linked
    from . import default_values
    from . import norman_snapping
    from . import norman_UI
    from . import built_in_ks

import bpy
import bpy_types


#~ class INFO_MT_add_fracture_objects(bpy.types.Menu):
    #~ bl_idname = "INFO_MT_add_fracture_objects"
    #~ bl_label = "Fracture Helper Objects"
#~ 
    #~ def draw(self, context):
        #~ layout = self.layout
        #~ layout.operator_context = 'INVOKE_REGION_WIN'
#~ 
        #~ layout.operator("object.import_fracture_bomb",
            #~ text="Bomb")
        #~ layout.operator("object.import_fracture_projectile",
            #~ text="Projectile")
        #~ layout.operator("object.import_fracture_recorder",
            #~ text="Rigidbody Recorder")

#~ import space_info

menu_func = (lambda self, context: self.layout.menu("INFO_MT_norman_character_add", icon='OUTLINER_OB_ARMATURE'))


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_add.append(menu_func)
    
    #~ if bpy.app.build_platform.find("Windows") != -1:    
    #  Problem if placed in external user script dir
	#~ built_in_ks.register()
	#~ default_values.register()
	#~ norman_snapping.register()
	#~ norman_UI.register()
	#~ load_linked.register()
    
def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
