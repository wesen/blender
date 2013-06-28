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

import bpy
from . import norman_snapping

#
#  Written by Ivo Grigull
#  http://ivogrigull.com
#  http://character-rigger.com
#

#  Global variables
head = ["bdy_head", "bdy_neck", "roll_head_parent", "dir_head_parent"]
arm_l = ["IK_wrist_L", "bdy_shoulder_L", "MCH-self.elbow_offset_L", "arm_IK_upvec_L", "shoulder_offset_L", "MCH-uparm_fk_L", "MCH-loarm_fk_L", "roll_MCH-uparm_fk_L", "roll_MCH-loarm_fk_L", "gimbal_MCH-uparm_fk_L"]
arm_r = ["IK_wrist_R", "bdy_shoulder_R", "MCH-self.elbow_offset_R", "arm_IK_upvec_R", "shoulder_offset_R", "MCH-uparm_fk_R", "MCH-loarm_fk_R", "roll_MCH-uparm_fk_R", "roll_MCH-loarm_fk_R", "gimbal_MCH-uparm_fk_R"]
spine = ["bdy_hip", "pelvis", "center1", "center2", "bdy_chest", "pelvis_swing", "fk_bdy_spine1", "fk_bdy_spine2", "fk_bdy_spine3"]
leg_l = ["ikfoot_L", "leg_offset_L", "MCH-upleg_fk_L", "MCH-loleg_fk_L", "dir_MCH-upleg_fk_L", "MCH-self.knee_offset_L", "roll_MCH-upleg_fk_L", "dir_MCH-loleg_fk_L", "roll_MCH-loleg_fk_L", "bdy_foot_L", "bdy_toe_L", "leg_ik_tip_L", "leg_ik_roll_L", "leg_upvector_L", "gimbal_MCH-upleg_fk_L", "gimbal_bdy_foot_L"]
leg_r = ["ikfoot_R", "leg_offset_R", "MCH-upleg_fk_R", "MCH-loleg_fk_R", "dir_MCH-upleg_fk_R", "MCH-self.knee_offset_R", "roll_MCH-upleg_fk_R", "dir_MCH-loleg_fk_R", "roll_MCH-loleg_fk_R", "bdy_foot_R", "bdy_toe_R", "leg_ik_tip_R", "leg_ik_roll_R", "leg_upvector_R", "gimbal_MCH-upleg_fk_R", "gimbal_bdy_foot_R"]
wrist_l = ["bdy_wrist_L", "dir_MCH-wrist_axis_L", "bdy_hnd_thumb_L", "bdy_hnd_thumb1_L", "bdy_hnd_thumb2_L", "rot_bdy_hnd_thumb_L", "roll_MCH-wrist_axis_L", "bdy_hnd_index_L", "bdy_hnd_index1_L", "bdy_hnd_index2_L", "bdy_hnd_index3_L", "bdy_hnd_middle_L", "bdy_hnd_middle1_L", "bdy_hnd_middle2_L", "bdy_hnd_middle3_L", "bdy_hnd_ring_L", "bdy_hnd_ring1_L", "bdy_hnd_ring2_L", "bdy_hnd_ring3_L", "bdy_hnd_pinky_L", "bdy_hnd_pinky1_L", "bdy_hnd_pinky2_L", "bdy_hnd_pinky3_L", "rot_bdy_hnd_pinky_L", "rot_bdy_hnd_ring_L", "rot_bdy_hnd_middle_L", "rot_bdy_hnd_index_L", "gimbal_bdy_wrist_L"]
wrist_r = ["bdy_wrist_R", "dir_MCH-wrist_axis_R", "bdy_hnd_thumb_R", "bdy_hnd_thumb1_R", "bdy_hnd_thumb2_R", "rot_bdy_hnd_thumb_R", "roll_MCH-wrist_axis_R", "bdy_hnd_index_R", "bdy_hnd_index1_R", "bdy_hnd_index2_R", "bdy_hnd_index3_R", "bdy_hnd_middle_R", "bdy_hnd_middle1_R", "bdy_hnd_middle2_R", "bdy_hnd_middle3_R", "bdy_hnd_ring_R", "bdy_hnd_ring1_R", "bdy_hnd_ring2_R", "bdy_hnd_ring3_R", "bdy_hnd_pinky_R", "bdy_hnd_pinky1_R", "bdy_hnd_pinky2_R", "bdy_hnd_pinky3_R", "rot_bdy_hnd_pinky_R", "rot_bdy_hnd_ring_R", "rot_bdy_hnd_middle_R", "rot_bdy_hnd_index_R", "gimbal_bdy_wrist_R"]
mouth_c = ["mouth_center",  "bdy_jaw"]
mouth_l = [ "lip_corner_L" ]
mouth_r = [ "lip_corner_R" ]
eye_l = [ "bdy_eye_L", "eye_control", "bdy_eye_flesh_L" ]
eye_r = [ "bdy_eye_R", "eye_control", "bdy_eye_flesh_R" ]
#brow_l = [ "brow_L", "brow1_L", "brow2_L", "brow3_L" ]
#brow_l = [ "brow_R", "brow1_R", "brow2_R", "brow3_R" ]


#  Sets a property value and inserts a key if an fcurve exists
def set_property_value( posebone, property, value ):

    ob = posebone.id_data    
    path = posebone.path_from_id('["' + property + '"]')
    posebone[property] = value
    
    #  insert key if possible
    if ob.animation_data != None:
        if ob.animation_data.action != None:
            
            for n in ob.animation_data.action.fcurves:
                if n.data_path == path:
                    ob.keyframe_insert(path)
                    found = True
                    break
        

#  Default values

def refresh():
    bpy.context.scene.frame_current = bpy.context.scene.frame_current

def arm_default_values(side="_L"):
            
    ob = bpy.context.active_object

    set_property_value(ob.pose.bones["bdy_shoulder"+side], 'FK_IK', 1 )
    set_property_value(ob.pose.bones["bdy_shoulder"+side], 'FK_2', 0 )
    set_property_value(ob.pose.bones["bdy_shoulder"+side], 'Stretchy', 0.0 )
    #set_property_value(ob.pose.bones["bdy_shoulder"+side], 'IK_show', 0.0 )
    set_property_value(ob.pose.bones["bdy_shoulder"+side], 'FK_global', 0.0 )
    set_property_value(ob.pose.bones["bdy_shoulder"+side], 'Follow_chest', 0.0 )
    set_property_value(ob.pose.bones["bdy_shoulder"+side], 'Follow_hip', 0.0 )
        
    #~ ob.data.bones["gimbal_MCH-uparm_fk"+side].hide = True
    #~ ob.data.bones["gimbal_bdy_wrist"+side].hide = True
    
    refresh()


def leg_default_values(side="_L"):
    ob = bpy.context.active_object
        

    set_property_value(ob.pose.bones["bdy_hip"], 'FK_IK'+side, 1 )
    set_property_value(ob.pose.bones["bdy_hip"], 'FK_2'+side, 0 )
    #set_property_value(ob.pose.bones["bdy_hip"], 'FK_2_show'+side, 0 )

    set_property_value(ob.pose.bones["bdy_hip"], 'FK_leg_global'+side, 1.0 )
    set_property_value(ob.pose.bones["MCH-upleg_fk"+side], 'volume', 1.0 )
    set_property_value(ob.pose.bones["MCH-loleg_fk"+side], 'volume', 1.0 )

    #set_property_value(ob.pose.bones["bdy_hip"], 'IK_show'+side, 0 )
    set_property_value(ob.pose.bones["ikfoot"+side], 'stretchy', 0.0 )
    set_property_value(ob.pose.bones["ikfoot"+side], 'knee_roll'+side, 0.0 )
    set_property_value(ob.pose.bones["ikfoot"+side], 'space_global', 1.0 )
    set_property_value(ob.pose.bones["ikfoot"+side], 'foot_rock', 0.0 )
        
    #~ ob.data.bones["gimbal_MCH-upleg_fk"+side].hide = True
    #~ ob.data.bones["gimbal_bdy_foot"+side].hide = True
    
    refresh()

    
def spine_default_values():
    ob = bpy.context.active_object

    
    set_property_value(ob.pose.bones["bdy_chest"], 'IK', 1 )
    set_property_value(ob.pose.bones["bdy_chest"], 'stretch_amount', 1.0 )

    set_property_value(ob.pose.bones["bdy_chest"], 'show_fk', 0.0 )

    ob.pose.bones["bdy_chest"]["show_fk"] = 0
    ob.pose.bones["bdy_chest"]["show_ik"] = 0
    #~ ob.data.bones["gimbal_bdy_hip"].hide = True
   
    refresh()

def head_default_values():
    ob = bpy.context.active_object
    set_property_value(ob.pose.bones["bdy_head"], 'head_global', 0.0 )
    set_property_value(ob.pose.bones["bdy_head"], 'neck_global', 0.0 )
    refresh()


def hand_default_values(side="_L"):
    ob = bpy.context.active_object

    set_property_value(ob.pose.bones["bdy_wrist"+side], 'flex', 0.0 )
    set_property_value(ob.pose.bones["bdy_wrist"+side], 'shear', 0.0 )
    set_property_value(ob.pose.bones["bdy_wrist"+side], 'spread', 0.0 )
    set_property_value(ob.pose.bones["bdy_wrist"+side], 'wrist_global', 0.0 )

    #ob.pose.bones["bdy_wrist"+side]["flex"] = 0.0
    #ob.pose.bones["bdy_wrist"+side]["shear"] = 0.0
    #ob.pose.bones["bdy_wrist"+side]["spread"] = 0.0
    #ob.pose.bones["bdy_wrist"+side]["wrist_global"] = 0.0
    #~ ob.data.bones["gimbal_bdy_wrist"+side].hide = True

    refresh()

def mouth_default_values():
    ob = bpy.context.active_object
    
    set_property_value(ob.pose.bones["mouth_center"], 'Curl_Up_Lip', 0.0 )
    set_property_value(ob.pose.bones["mouth_center"], 'Curl_Lo_Lip', 0.0 )
    set_property_value(ob.pose.bones["mouth_center"], 'Mouth_Clench', 0.0 )
    set_property_value(ob.pose.bones["mouth_center"], 'Mouth_Puff', 0.0 )
    set_property_value(ob.pose.bones["mouth_center"], 'Mouth_Pull', 0.0 )
    set_property_value(ob.pose.bones["mouth_center"], 'UD_Up_Lip', 0.0 )
    set_property_value(ob.pose.bones["mouth_center"], 'UD_Lo_Lip', 0.0 )
    
    refresh()

def mouth_corner_default_values(side="_L"):
    ob = bpy.context.active_object
    
    set_property_value(ob.pose.bones["lip_corner"+side], 'Puff', 0.0 )
    set_property_value(ob.pose.bones["lip_corner"+side], 'UD_Up_Lip', 0.0 )
    set_property_value(ob.pose.bones["lip_corner"+side], 'UD_Lo_Lip', 0.0 )

    refresh()

def eye_default_values(side="_L"):
    
    ob = bpy.context.active_object
    
    set_property_value(ob.pose.bones["bdy_eye"+side], 'UD_Up_Lid'+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], 'UD_Lo_Lid'+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], 'Lid_Up_1_Inner'+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], 'Lid_Up_2_Mid'+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], 'Lid_Up_3_Outer'+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], 'Lid_Lo_1_Inner'+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], 'Lid_Lo_2_Mid'+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], 'Lid_Lo_3_Outer'+side, 0.0 )

    set_property_value(ob.pose.bones["bdy_head"], 'eyes_global', 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], "Pupil_Scale",  0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], "TW_Up_Lid"+side, 0.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], "TW_Lo_Lid"+side, 0.0 )
    
    set_property_value(ob.pose.bones["bdy_eye"+side], "Follow_Up_Lid"+side, 1.0 )
    set_property_value(ob.pose.bones["bdy_eye"+side], "Follow_Lo_Lid"+side, 0.3 )

    
    refresh()

    


class norman_default_values(bpy.types.Operator):
    ''''''
    bl_idname = "object.norman_default_values"
    bl_label = "Reset values"

    @classmethod
    def poll(cls, context):
        return context.active_object != None

    def execute(self, context):

        global arm_l, arm_r, leg_l, leg_r        
                
        posebone = context.active_pose_bone
        ob = context.active_object
                
        if posebone.name in arm_l:
            arm_default_values(side="_L")
            
        elif posebone.name in arm_r:
            arm_default_values(side="_R")

        elif posebone.name in leg_l:
            leg_default_values(side="_L")

        elif posebone.name in leg_r:
            leg_default_values(side="_R")

        elif posebone.name in spine:
            spine_default_values()
            
        elif posebone.name in head:
            head_default_values()

        elif posebone.name in eye_l:
            eye_default_values(side="_L")

        elif posebone.name in eye_r:
            eye_default_values(side="_L")

        elif posebone.name in mouth_c:
            mouth_default_values()
            
        elif posebone.name in mouth_l:
            mouth_corner_default_values(side="_L")
            
        elif posebone.name in mouth_r:
            mouth_corner_default_values(side="_R")
            
        elif posebone.name in wrist_l:
            hand_default_values(side="_L")

        elif posebone.name in wrist_r:
            hand_default_values(side="_R")
            
        
        return {'FINISHED'}



class NormanRigProperties(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Character Properties"
    
    @classmethod
    def poll(self, context):    
        try:
            ob = context.active_object  
            mode = context.mode
            return (ob.type == 'ARMATURE' and ob.data.name == "norman" and mode == "POSE")
        except AttributeError:
            return 0

    def draw(self, context):
        
        active_object = context.active_object
        ob = active_object
        layout = self.layout        
        col = layout.column(align=True)
            
        def is_selected(context, names):
            try:
                for name in names:
                    if context.active_pose_bone.name == name:
                        return True
                for bone in context.selected_pose_bones:
                    for name in names:
                        if bone.name == name:
                            return True
            except AttributeError:
                pass
            return False
        
        global head, arm_l, arm_r, spine, leg_l, leg_r, wrist_l, wrist_r, mouth_c, mouth_l, mouth_r, eye_l, eye_r
                        
        pose_bones = context.active_object.pose.bones

        layout = self.layout        
        col = layout.column()

        if is_selected(context, arm_l):
            col.label("Left Arm")
            
            col = layout.column()
            col.label("FK/IK")
            col = layout.column()
            col.prop(pose_bones["bdy_shoulder_L"], '["FK_IK"]', text="IK")
            col.prop(pose_bones["bdy_shoulder_L"], '["FK_2"]', text="FK2")
            col = layout.column()
            col.label("Stretchy")
            col.prop(pose_bones["bdy_shoulder_L"], '["Stretchy"]', text="Stretchy", slider=True)
            col = layout.column()
            col.label("Misc")
            col.prop(pose_bones["bdy_shoulder_L"], '["IK_show"]', text="Show IK and FK")
            col.prop(pose_bones["bdy_shoulder_L"], '["FK_global"]', text="FK Glboal")
            col = layout.column()
            col.label("IK wrist Spaces")
            col.prop(pose_bones["bdy_shoulder_L"], '["Follow_chest"]', text="Follow chest")
            col.prop(pose_bones["bdy_shoulder_L"], '["Follow_hip"]', text="Follow hip")
            #col.prop(pose_bones["bdy_shoulder_L"], '["FK2_show"]')
            #layout.prop(context.active_pose_bone, "honk", expand=True)
            col.label("Snapping")
            col.operator("object.norman_snap_fk_ik", text="Snap fk/ik" )
                        
            #~ col.label("Gimbal controls")
            #~ col.prop( ob.data.bones["gimbal_MCH-uparm_fk_L"], 'hide', text="hide gimbal uparm" )
            #~ col.prop( ob.data.bones["gimbal_bdy_wrist_L"], 'hide', text="hide gimbal wrist" )

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            
            
        if is_selected(context, arm_r):
            col.label("Right Arm")
            
            col = layout.column()
            col.label("FK/IK")
            col = layout.column()
            col.prop(pose_bones["bdy_shoulder_R"], '["FK_IK"]', text="IK")
            col.prop(pose_bones["bdy_shoulder_R"], '["FK_2"]', text="FK2")
            col = layout.column()
            col.label("Stretchy")
            col.prop(pose_bones["bdy_shoulder_R"], '["Stretchy"]', text="Stretchy", slider=True)
            col = layout.column()
            col.label("Misc")
            col.prop(pose_bones["bdy_shoulder_R"], '["IK_show"]', text="Show IK and FK")
            col.prop(pose_bones["bdy_shoulder_R"], '["FK_global"]', text="FK Glboal")
            col = layout.column()
            col.label("IK Spaces")
            col.prop(pose_bones["bdy_shoulder_R"], '["Follow_chest"]', text="Follow chest")
            col.prop(pose_bones["bdy_shoulder_R"], '["Follow_hip"]', text="Follow hip")
            #col.prop(pose_bones["bdy_shoulder_R"], '["FK2_show"]')
            #layout.prop(context.active_pose_bone, "honk", expand=True)
            col.label("Snapping")
            col.operator("object.norman_snap_fk_ik", text="Snap fk/ik" )
            
            #~ col.label("Gimbal controls")
            #~ col.prop( ob.data.bones["gimbal_MCH-uparm_fk_R"], 'hide', text="hide gimbal uparm" )
            #~ col.prop( ob.data.bones["gimbal_bdy_wrist_R"], 'hide', text="hide gimbal wrist" )

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            
        # Spine
        if is_selected(context, spine):
            col.label("Spine")
            
            col.label("FK/IK")
            col = layout.column()
            col.prop(pose_bones["bdy_chest"], '["IK"]', text="IK")
            col.prop(pose_bones["bdy_chest"], '["stretch_amount"]', text="Stretch amount")
            col.label("Visibility")
            col = layout.column()
            col.prop(pose_bones["bdy_chest"], '["show_fk"]', text="Show FK")
            col.prop(pose_bones["bdy_chest"], '["show_ik"]', text="Show IK")
            
            #~ col.label("Gimbal controls")
            #~ col.prop( ob.data.bones["gimbal_bdy_hip"], 'hide', text="hide gimbal hip" )

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            

        # Left leg
        if is_selected(context, leg_l):
            col.label("Left Leg")
            
            col.label("FK/IK")
            col = layout.column()
            col.prop(pose_bones["bdy_hip"], '["FK_IK_L"]', text="FK/IK")
            col.prop(pose_bones["bdy_hip"], '["FK_2_L"]', text="FK2")
            col.prop(pose_bones["bdy_hip"], '["FK_2_show_L"]', text="Show FK2")
            
            col.label("FK")
            col = layout.column()
            col.prop(pose_bones["bdy_hip"], '["FK_leg_global_L"]', text="FK global")
            col.prop(pose_bones["MCH-upleg_fk_L"], '["volume"]', text="Upleg_scale_squash")
            col.prop(pose_bones["MCH-loleg_fk_L"], '["volume"]', text="Loleg_scale_squash")
            
            col.label("IK")
            col = layout.column()
            col.prop(pose_bones["bdy_hip"], '["IK_show_L"]', text="Show IK and FK")
            col.prop(pose_bones["ikfoot_L"], '["stretchy"]', text="Stretchy")
            col.prop(pose_bones["ikfoot_L"], '["knee_roll_L"]', text="Knee roll")
            col.prop(pose_bones["ikfoot_L"], '["space_global"]', text="Global")
            col.prop(pose_bones["ikfoot_L"], '["foot_rock"]', text="Foot rock")

            col.label("Snapping")
            col.operator("object.norman_snap_fk_ik", text="Snap fk/ik" )

            #~ col.label("Gimbal controls")
            #~ col.prop( ob.data.bones["gimbal_MCH-upleg_fk_L"], 'hide', text="hide gimbal upleg" )
            #~ col.prop( ob.data.bones["gimbal_bdy_foot_L"], 'hide', text="hide gimbal foot" )

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            
            
        # Right leg
        if is_selected(context, leg_r):
            col.label("Right Leg")
            
            col.label("FK/IK")            
            col = layout.column()
            col.prop(pose_bones["bdy_hip"], '["FK_IK_R"]', text="FK/IK")
            col.prop(pose_bones["bdy_hip"], '["FK_2_R"]', text="FK2")
            col.prop(pose_bones["bdy_hip"], '["FK_2_show_R"]', text="Show FK2")
            
            col.label("FK")
            col = layout.column()
            col.prop(pose_bones["bdy_hip"], '["FK_leg_global_R"]', text="FK global")
            col.prop(pose_bones["MCH-upleg_fk_R"], '["volume"]', text="Upleg_scale_squash")
            col.prop(pose_bones["MCH-loleg_fk_R"], '["volume"]', text="Loleg_scale_squash")
            
            col.label("IK")
            col = layout.column()
            col.prop(pose_bones["bdy_hip"], '["IK_show_R"]', text="Show IK and FK")
            col.prop(pose_bones["ikfoot_R"], '["stretchy"]', text="Stretchy")
            col.prop(pose_bones["ikfoot_R"], '["knee_roll_R"]', text="Knee roll")
            col.prop(pose_bones["ikfoot_R"], '["space_global"]', text="Global")
            col.prop(pose_bones["ikfoot_R"], '["foot_rock"]', text="Foot rock")

            col.label("Snapping")
            col.operator("object.norman_snap_fk_ik", text="Snap fk/ik" )
            
            #~ col.label("Gimbal controls")
            #~ col.prop( ob.data.bones["gimbal_MCH-upleg_fk_R"], 'hide', text="hide gimbal upleg" )
            #~ col.prop( ob.data.bones["gimbal_bdy_foot_R"], 'hide', text="hide gimbal foot" )

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            
            
        # Head
        if is_selected(context, head):
            col.label("Head")
            
            col = layout.column()
            col.prop(pose_bones["bdy_head"], '["head_global"]', text="Head global")
            col.prop(pose_bones["bdy_head"], '["neck_global"]', text="Neck global")

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            

        # Wrist_L
        if is_selected(context, wrist_l):
            col.label("Left Wrist")
            col = layout.column()
            col.prop(pose_bones["bdy_wrist_L"], '["flex"]', text="Spread")
            col.prop(pose_bones["bdy_wrist_L"], '["shear"]', text="Shear")
            col.prop(pose_bones["bdy_wrist_L"], '["spread"]', text="Flex")
            col.prop(pose_bones["bdy_wrist_L"], '["wrist_global"]', text="Wrist Global")
            #~ col.prop( ob.data.bones["gimbal_bdy_wrist_L"], 'hide', text="hide gimbal wrist" )

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            

        # Wrist_R       
        if is_selected(context, wrist_r):
            col.label("Right Wrist")
            col = layout.column()
            col.prop(pose_bones["bdy_wrist_R"], '["flex"]', text="Spread")
            col.prop(pose_bones["bdy_wrist_R"], '["shear"]', text="Shear")
            col.prop(pose_bones["bdy_wrist_R"], '["spread"]', text="Flex")
            col.prop(pose_bones["bdy_wrist_R"], '["wrist_global"]', text="Wrist Global")
            #~ col.prop( ob.data.bones["gimbal_bdy_wrist_R"], 'hide', text="hide gimbal wrist" )

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            

        # Mouth Center
        if is_selected(context, mouth_c):
            col.label("Mouth Center")
            col = layout.column()
            col.prop(pose_bones["mouth_center"], '["Curl_Up_Lip"]', text="Curl Up Lip")
            col.prop(pose_bones["mouth_center"], '["Curl_Lo_Lip"]', text="Curl Lo Lip")
            col.prop(pose_bones["mouth_center"], '["Mouth_Clench"]', text="Mouth Clench")
            col.prop(pose_bones["mouth_center"], '["Mouth_Puff"]', text="Puff")
            col.prop(pose_bones["mouth_center"], '["Mouth_Pull"]', text="Pull")
            col.prop(pose_bones["mouth_center"], '["UD_Up_Lip"]', text="Up/Dwn Up Lip")
            col.prop(pose_bones["mouth_center"], '["UD_Lo_Lip"]', text="Up/Dwn Lo Lip")
            
            col.label("Reset Values")
            col.operator("object.norman_default_values")
            

        # Lips Lef Corner
        if is_selected(context, mouth_l):
            col.label("* Lips Left Corner *")
            col = layout.column()
            col.prop(pose_bones["lip_corner_L"], '["Puff"]', text="Puff")
            col.prop(pose_bones["lip_corner_L"], '["UD_Up_Lip"]', text="Up/Dwn Up Lip")
            col.prop(pose_bones["lip_corner_L"], '["UD_Lo_Lip"]', text="Up/Dwn Lo Lip")

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            

        # Lips Lef Corner
        if is_selected(context, mouth_r):
            col.label("* Lips Right Corner *")
            col = layout.column()
            col.prop(pose_bones["lip_corner_R"], '["Puff"]', text="Puff")
            col.prop(pose_bones["lip_corner_R"], '["UD_Up_Lip"]', text="Up/Dwn Up Lip")
            col.prop(pose_bones["lip_corner_R"], '["UD_Lo_Lip"]', text="Up/Dwn Lo Lip")

            col.label("Reset Values")
            col.operator("object.norman_default_values")
            

        # Eye Left
        if is_selected(context, eye_l):
            col.label("* Eye Left *")
            col = layout.column()
            
            col.label("Lids")            
            col.prop(pose_bones["bdy_eye_L"], '["UD_Up_Lid_L"]', text="Up/Dwn up Lid")
            col.prop(pose_bones["bdy_eye_L"], '["UD_Lo_Lid_L"]', text="Up/Dwn Lo Lid")

            col.label("Lids Micro")            
            col = layout.column()
            col.prop(pose_bones["bdy_eye_L"], '["Lid_Up_1_Inner_L"]', text="Up Lid Inner")
            col.prop(pose_bones["bdy_eye_L"], '["Lid_Up_2_Mid_L"]', text="Up Lid Mid")
            col.prop(pose_bones["bdy_eye_L"], '["Lid_Up_3_Outer_L"]', text="Up Lid Outer")
            
            col = layout.column()
            col.prop(pose_bones["bdy_eye_L"], '["Lid_Lo_1_Inner_L"]', text="Lo Lid Inner")
            col.prop(pose_bones["bdy_eye_L"], '["Lid_Lo_2_Mid_L"]', text="Lo Lid Mid")
            col.prop(pose_bones["bdy_eye_L"], '["Lid_Lo_3_Outer_L"]', text="Lo Lid Outer")

            col.label("Settings")                        
            col = layout.column()
            col.prop(pose_bones["bdy_head"], '["eyes_global"]', text="Eye aim global")
            col.prop(pose_bones["bdy_eye_L"], '["Pupil_Scale"]', text="Pupil Scale")
            col.prop(pose_bones["bdy_eye_L"], '["TW_Up_Lid_L"]', text="Twist Up Lid")
            col.prop(pose_bones["bdy_eye_L"], '["TW_Lo_Lid_L"]', text="Twist Lo Lid")
            
            col.label("Auto Lids")
            col = layout.column()
            col.prop(pose_bones["bdy_eye_L"], '["Follow_Up_Lid_L"]', text="Auto Lid Up")
            col.prop(pose_bones["bdy_eye_L"], '["Follow_Lo_Lid_L"]', text="Auto Lid Lo")
            
            col.label("Reset Values")
            col.operator("object.norman_default_values")
            
            
        # Eye Right
        if is_selected(context, eye_r):
            col.label("* Eye Right *")
            col = layout.column()
            
            col.label("Lids")            
            col.prop(pose_bones["bdy_eye_R"], '["UD_Up_Lid_R"]', text="Up/Dwn up Lid")
            col.prop(pose_bones["bdy_eye_R"], '["UD_Lo_Lid_R"]', text="Up/Dwn Lo Lid")

            col.label("Lids Micro")            
            col = layout.column()
            col.prop(pose_bones["bdy_eye_R"], '["Lid_Up_1_Inner_R"]', text="Up Lid Inner")
            col.prop(pose_bones["bdy_eye_R"], '["Lid_Up_2_Mid_R"]', text="Up Lid Mid")
            col.prop(pose_bones["bdy_eye_R"], '["Lid_Up_3_Outer_R"]', text="Up Lid Outer")
            
            col = layout.column()
            col.prop(pose_bones["bdy_eye_R"], '["Lid_Lo_1_Inner_R"]', text="Lo Lid Inner")
            col.prop(pose_bones["bdy_eye_R"], '["Lid_Lo_2_Mid_R"]', text="Lo Lid Mid")
            col.prop(pose_bones["bdy_eye_R"], '["Lid_Lo_3_Outer_R"]', text="Lo Lid Outer")

            col.label("Settings")                        
            col = layout.column()
            col.prop(pose_bones["bdy_head"], '["eyes_global"]', text="Eye aim global")
            col.prop(pose_bones["bdy_eye_R"], '["Pupil_Scale"]', text="Pupil Scale")
            col.prop(pose_bones["bdy_eye_R"], '["TW_Up_Lid_R"]', text="Twist Up Lid")
            col.prop(pose_bones["bdy_eye_R"], '["TW_Lo_Lid_R"]', text="Twist Lo Lid")
            
            col.label("Auto Lids")
            col = layout.column()
            col.prop(pose_bones["bdy_eye_R"], '["Follow_Up_Lid_R"]', text="Auto Lid Up")
            col.prop(pose_bones["bdy_eye_R"], '["Follow_Lo_Lid_R"]', text="Auto Lid Lo")
            
            col.label("Reset Values")
            col.operator("object.norman_default_values")
            


        if is_selected(context, ["visibility_settings"] ):
            col.prop(pose_bones["visibility_settings"], '["show_head"]')
            col.prop(pose_bones["visibility_settings"], '["show_torso"]')
            col.prop(pose_bones["visibility_settings"], '["show_L_Arm"]')
            col.prop(pose_bones["visibility_settings"], '["show_R_Arm"]')
            col.prop(pose_bones["visibility_settings"], '["show_L_Leg"]')
            col.prop(pose_bones["visibility_settings"], '["show_R_Leg"]')
            


def register():
    pass

def unregister():
    pass

if __name__ == "__main__":
    register()
