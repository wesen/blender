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

import bpy
from bpy.props import *
import os


def get_path(paths):
    return paths[ len(paths)-1 ]

def scene_copy_keying_sets( source, target):
    
    for n in source.keying_sets:
    
        bpy.ops.anim.keying_set_add()
        ks = target.keying_sets[ len(target.keying_sets)-1]
        ks.name = n.name
        for i in n.paths:
            if( i.id == None):
                break
            ob = target.objects[i.id.name]
            if ob == None:
                print("Error")
                break
            ks.paths.add( ob, i.data_path, i.array_index )
            path = get_path(ks.paths)
            path.use_entire_array = i.use_entire_array
            path.bl_options = i.bl_options
            path.group_method = i.group_method
            
    

class characters_norman(bpy.types.Operator):
    '''Cop'''
    bl_idname = "characters.norman"
    bl_label = "Norman"

    rig_name = StringProperty( name="rig_name", description="rig_name", maxlen = 200, default = "")

    def execute(self, context):

        #tail = '/addons/norman/norman.blend'
        tail = '/addons/norman/' + self.rig_name +'.blend'

        path = None
        for n in bpy.utils.script_paths():
            if os.path.exists( n+tail ):
                path = n+tail
                break

        if path == None:
            print("Invalid path")
            return {'FAILED'}


        
        print("Loading %s ..." % self.rig_name)
        
        #  Center cursor first
        try:
            bpy.ops.view3d.snap_cursor_to_center()
        except:
            pass

        try:                

            #  Load group as linked
            bpy.ops.wm.link_append(filepath="", directory=path+"/Group/", filename=self.rig_name+'_rig')
    
            try:
                bpy.ops.wm.link_append(filepath="", directory=path+"/Action/", filename="walk", link=False)
                bpy.ops.wm.link_append(filepath="", directory=path+"/Action/", filename="jump", link=False)
            except:
                print("No actions loaded")
                
            #  Adjust empty draw size, so it is not like 2 meters wide
            ob = bpy.context.active_object
            ob.empty_draw_size = 0.1
            
            #  Make proxy
            bpy.ops.object.proxy_make(object="", type='rig')
            
            #  Set pose mode
            bpy.ops.object.mode_set(mode='POSE')
            
        except:
            print('oops - error while loading rig')
                        
        return {'FINISHED'}

class INFO_MT_norman_add(bpy.types.Menu):
    bl_idname = "INFO_MT_norman_add"
    bl_label = "Characters"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        #layout.operator("object.armature_add", text="Single Bone", icon='BONE_DATA')
        layout.operator("characters_cop", text="Cop", icon='BONE_DATA')


class INFO_MT_norman_character_add(bpy.types.Menu):
    bl_idname = "INFO_MT_norman_character_add"
    bl_label = "Rigs"

    def draw(self, context):
        import rigify

        #tail = '/addons/norman/norman.blend'
        tail = '/addons/norman/'

        path = None
        for n in bpy.utils.script_paths():
            if os.path.exists( n+tail ):
                path = n+tail
                break

        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        files = os.listdir(path)
        for n in files:
            split = os.path.splitext(n)
            if split[1] == '.blend':
                print(split[0])
                
                text = split[0]
                layout.operator("characters.norman", text=text, icon='OUTLINER_OB_ARMATURE').rig_name = split[0]
                
        
        #~ text = "Norman"
        #~ layout.operator("characters.norman", text=text, icon='OUTLINER_OB_ARMATURE')

def menu_func(self, context):
    self.layout.menu("INFO_MT_norman_character_add", icon='OUTLINER_OB_ARMATURE')

#~ menu_func = (lambda self, context: self.layout.menu("INFO_MT_norman_character_add", icon='OUTLINER_OB_ARMATURE'))
#~ import space_info  # ensure the menu is loaded first


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_add.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_armature_add.remove(menu_func)

if __name__ == "__main__":
    register()
