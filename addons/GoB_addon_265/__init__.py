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

bl_info = {
    "name": "GoB",
    "description": "An unofficial GOZ-like for Blender",
    "author": "ODe",
    "version": (2, 6, 5),
    "blender": (2, 6, 5),
    "api": 45743,
    "location": "At the top info header",
    "warning": "",
    "wiki_url": '',
    "tracker_url": '',
    "category": "Import-Export"}

if "bpy" in locals():
    import imp
    if "ext_GoB" in locals():
        imp.reload(ext_GoB)

import bpy,os,time
from . import ext_GoB

pathGoZ = "/Users/Shared/Pixologic" #<- for Macintosh

ficPathZB = None
pathZBrush = None
try:
    ficPathZB = open(pathGoZ+"/GoZBrush/GoZ_Config.txt",'rt')
except:
    print("Unable to find ZBrush")
if ficPathZB is not None:
    lines = ficPathZB.readlines()
    for line in lines:
        if line.find('PATH') == 0:
            pathZBrush = '"'+line.split('"')[1].replace('\\','/')+'"'
            break
    ficPathZB.close()

varTime = 0

class GoB_import(bpy.types.Operator):
    bl_idname = "scene.gob_import"
    bl_label = "Import from Zbrush"

    def execute(self,context):
        global varTime
        try:
            ficTime = os.path.getmtime(
                    "{0}/GoZBrush/GoZ_ObjectList.txt".format(pathGoZ))
        except:
            print("{0}/GoZBrush/GoZ_ObjectList.txt illisible".format(pathGoZ))
            return{'CANCELLED'}
        print("\n\t------")
        objectList = []
        if ficTime > varTime:
            fic = open("{0}/GoZBrush/GoZ_ObjectList.txt".format(pathGoZ),'rt')
            line = fic.readline()
            while line:
                objectList.append(line.strip() + '.GoZ')
                line = fic.readline()
            fic.close()
            varTime = ficTime
        else:
            self.report({'INFO'},"Nothing to update")
            print("Nothing to update")
            return{'CANCELLED'}
        if len(objectList) == 0:
            print("No update")
            return{'CANCELLED'}
        for objPath in objectList:
            ext_GoB.GoZit(objPath)
        self.report({'INFO'},"Done")
        return{'FINISHED'}
    def invoke(self, context, event):
        if event.shift:
            bpy.ops.paint.vertex_color_dirt()
            return{'FINISHED'}
        else:
            return self.execute(context)
class GoB_export(bpy.types.Operator):
    bl_idname = "scene.gob_export"
    bl_label = "Export to Zbrush"
    def execute(self,context):
        global varTime
        scn = bpy.context.scene
        fic = open("{0}/GoZBrush/GoZ_ObjectList.txt".format(pathGoZ),'wt')
        for obj in scn.objects:
            if obj.type == 'MESH' and obj.select:
                obj.name = obj.name.replace('.','_')
                obj.name = obj.name.replace(' ','_')
                bpy.ops.object.mode_set(mode='OBJECT')
                ext_GoB.exportGoZ(
                        pathGoZ,
                        scn,
                        obj,
                        '{0}/GoZProjects/Default'.format(pathGoZ))
                ztn = open(
                    "{0}/GoZProjects/Default/{1}.ztn".format(pathGoZ,obj.name),'wt')
                ztn.write('{0}/GoZProjects/Default/{1}'.format(pathGoZ, obj.name))
                ztn.close()
                fic.write(
                    '{0}/GoZProjects/Default/{1}\n'.format(pathGoZ, obj.name))
        fic.close()
        varTime = os.path.getmtime(
                        "{0}/GoZBrush/GoZ_ObjectList.txt".format(pathGoZ))
        os.system("{0}/GoZBrush/GoZBrushFromApp.app/Contents/MacOS/GoZBrushFromApp".format(pathGoZ))
        return{'FINISHED'}
    def invoke(self, context, event):
        if event.shift:
            if pathZBrush is not None:
                os.system('"{0} {1}/GoZApps/Photoshop/GoZ_LoadTextures.zsc"'.format(pathZBrush,pathGoZ))
                return{'FINISHED'}
        else:
            return self.execute(context)
class INFO_HT_header(bpy.types.Header):
    bl_space_type = 'INFO'

    def draw(self, context):
        layout = self.layout

        window = context.window
        scene = context.scene
        rd = scene.render

        row = layout.row(align=True)
        row.template_header()

        if context.area.show_menus:
            sub = row.row(align=True)
            sub.menu("INFO_MT_file")
            sub.menu("INFO_MT_add")
            if rd.use_game_engine:
                sub.menu("INFO_MT_game")
            else:
                sub.menu("INFO_MT_render")
            sub.menu("INFO_MT_window")
            sub.menu("INFO_MT_help")

        if window.screen.show_fullscreen:
            layout.operator(
                    operator="screen.back_to_previous",
                    icon='SCREEN_BACK',
                    text="Back to Previous")
            layout.separator()
        else:
            layout.template_ID(
                    data=context.window,
                    property="screen",
                    new="screen.new",
                    unlink="screen.delete")
            layout.template_ID(
                    data=context.screen,
                    property="scene",
                    new="scene.new",
                    unlink="scene.delete")

        layout.separator()

        if rd.has_multiple_engines:
            layout.prop(rd, "engine", text="")

        layout.separator()

        layout.template_running_jobs()

        layout.template_reports_banner()

        row = layout.row(align=True)
        row.operator(
                operator="scene.gob_export",
                text="",
                icon='BRUSH_PINCH',
                emboss=False)
        row.operator(
                operator="scene.gob_import",
                text="",
                icon='BLENDER',
                emboss=False)
        row.label(text=scene.statistics())

        # XXX: this should be right-aligned to the RHS of the region
        layout.operator(
                operator="wm.window_fullscreen_toggle",
                icon='FULLSCREEN_ENTER',
                text="")

        # XXX: BEFORE RELEASE, MOVE FILE MENU OUT OF INFO!!!
        """
        sinfo = context.space_data
        row = layout.row(align=True)
        row.prop(sinfo, "show_report_debug", text="Debug")
        row.prop(sinfo, "show_report_info", text="Info")
        row.prop(sinfo, "show_report_operator", text="Operators")
        row.prop(sinfo, "show_report_warning", text="Warnings")
        row.prop(sinfo, "show_report_error", text="Errors")

        row = layout.row()
        row.enabled = sinfo.show_report_operator
        row.operator("info.report_replay")

        row.menu("INFO_MT_report")
        """

def register():
    bpy.utils.register_class(GoB_export)
    bpy.utils.register_class(GoB_import)
    bpy.utils.register_class(INFO_HT_header)

def unregister():
    import bl_ui
    bpy.utils.unregister_class(GoB_export)
    bpy.utils.unregister_class(GoB_import)
    bpy.utils.unregister_class(INFO_HT_header)
    bpy.utils.register_class(bl_ui.space_info.INFO_HT_header)
if __name__ == "__main__":
    register()
