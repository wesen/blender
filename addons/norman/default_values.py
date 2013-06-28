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

def refresh():
    bpy.context.scene.frame_current = bpy.context.scene.frame_current

def arm_default_values(side="_L"):
    ob = bpy.context.active_object

    ob.pose.bones["bdy_shoulder"+side]["FK_IK"] = 1
    ob.pose.bones["bdy_shoulder"+side]["FK_2"] = 0
    ob.pose.bones["bdy_shoulder"+side]["Stretchy"] = 0.0
    ob.pose.bones["bdy_shoulder"+side]["IK_show"] = 0
    ob.pose.bones["bdy_shoulder"+side]["FK_global"] = 0.0    
    ob.pose.bones["bdy_shoulder"+side]["Follow_chest"] = 0.0
    ob.pose.bones["bdy_shoulder"+side].keyframe_insert("Follow_chest")
    ob.pose.bones["bdy_shoulder"+side]["Follow_hip"] = 0.0
    ob.data.bones["gimbal_MCH-uparm_fk"+side].hide = True
    ob.data.bones["gimbal_bdy_wrist"+side].hide = True
    
    refresh()

def leg_default_values(side="_L"):
    ob = bpy.context.active_object

    ob.pose.bones["bdy_hip"]["FK_IK"+side] = 1
    ob.pose.bones["bdy_hip"]["FK_2"+side] = 0
    ob.pose.bones["bdy_hip"]["FK_2_show"+side] = 0
    
    ob.pose.bones["bdy_hip"]["FK_leg_global"+side] = 1.0
    ob.pose.bones["MCH-upleg_fk"+side]["volume"] = 1.0
    ob.pose.bones["MCH-loleg_fk"+side]["volume"] = 1.0
    
    ob.pose.bones["bdy_hip"]["IK_show"+side] = 0
    ob.pose.bones["ikfoot"+side]["stretchy"] = 0.0
    ob.pose.bones["ikfoot"+side]["knee_roll"+side] = 0.0
    ob.pose.bones["ikfoot"+side]["space_global"] = 0
    ob.pose.bones["ikfoot"+side]["foot_rock"] = 0.0
    
    ob.data.bones["gimbal_MCH-upleg_fk"+side].hide = True
    ob.data.bones["gimbal_bdy_foot"+side].hide = True
    
    refresh()

    
def spine_default_values():
    ob = bpy.context.active_object

    ob.pose.bones["bdy_chest"]["IK"] = 1
    ob.pose.bones["bdy_chest"]["stretch_amount"] = 1.0
    
    ob.pose.bones["bdy_chest"]["show_fk"] = 0
    ob.pose.bones["bdy_chest"]["show_ik"] = 0
    ob.data.bones["gimbal_bdy_hip"].hide = True
   
    refresh()

def head_default_values():
    ob = bpy.context.active_object
    ob.pose.bones["bdy_head"]["head_global"] = 0.0
    ob.pose.bones["bdy_head"]["neck_global"] = 0.0   
    refresh()


def hand_default_values(side="_L"):
    ob = bpy.context.active_object

    ob.pose.bones["bdy_wrist"+side]["flex"] = 0.0
    ob.pose.bones["bdy_wrist"+side]["shear"] = 0.0
    ob.pose.bones["bdy_wrist"+side]["spread"] = 0.0
    ob.pose.bones["bdy_wrist"+side]["wrist_global"] = 0.0
    ob.data.bones["gimbal_bdy_wrist"+side].hide = True

    refresh()

def mouth_default_values():
    ob = bpy.context.active_object
    ob.pose.bones["mouth_center"]["Curl_Up_Lip"] = 0.0
    ob.pose.bones["mouth_center"]["Curl_Lo_Lip"] = 0.0
    ob.pose.bones["mouth_center"]["Mouth_Clench"] = 0.0
    ob.pose.bones["mouth_center"]["Mouth_Puff"] = 0.0
    ob.pose.bones["mouth_center"]["Mouth_Pull"] = 0.0
    ob.pose.bones["mouth_center"]["UD_Up_Lip"] = 0.0
    ob.pose.bones["mouth_center"]["UD_Lo_Lip"] = 0.0
    
    refresh()

def mouth_corner_default_values(side="_L"):
    ob = bpy.context.active_object
    ob.pose.bones["lip_corner"+side]["Puff"] = 0.0
    ob.pose.bones["lip_corner"+side]["UD_Up_Lip"] = 0.0
    ob.pose.bones["lip_corner"+side]["UD_Lo_Lip"] = 0.0    
    refresh()

def eye_default_values(side="_L"):
    ob = bpy.context.active_object
    ob.pose.bones["bdy_eye"+side]["UD_Up_Lid"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["UD_Lo_Lid"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["Lid_Up_1_Inner"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["Lid_Up_2_Mid"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["Lid_Up_3_Outer"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["Lid_Lo_1_Inner"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["Lid_Lo_2_Mid"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["Lid_Lo_3_Outer"+side] = 0.0
    
    ob.pose.bones["bdy_head"]["eyes_global"] = 0.0
    ob.pose.bones["bdy_eye"+side]["Pupil_Scale"] = 0.0
    ob.pose.bones["bdy_eye"+side]["TW_Up_Lid"+side] = 0.0
    ob.pose.bones["bdy_eye"+side]["TW_Lo_Lid"+side] = 0.0
    
    ob.pose.bones["bdy_eye"+side]["Follow_Up_Lid"+side] = 1.0
    ob.pose.bones["bdy_eye"+side]["Follow_Lo_Lid"+side] = 0.3
    
    refresh()

    

class norman_snap_fk_ik(bpy.types.Operator):
    ''''''
    bl_idname = "object.norman_snap_fk_ik"
    bl_label = "Snap fk/ik"

    @classmethod
    def poll(cls, context):
        return context.active_object != None

    def execute(self, context):

        arm_l = ["IK_wrist_L", "bdy_shoulder_L", "MCH-self.elbow_offset_L", "arm_IK_upvec_L", "shoulder_offset_L", "MCH-uparm_fk_L", "MCH-loarm_fk_L", "roll_MCH-uparm_fk_L", "roll_MCH-loarm_fk_L", "gimbal_MCH-uparm_fk_L"]
        arm_r = ["IK_wrist_R", "bdy_shoulder_R", "MCH-self.elbow_offset_R", "arm_IK_upvec_R", "shoulder_offset_R", "MCH-uparm_fk_R", "MCH-loarm_fk_R", "roll_MCH-uparm_fk_R", "roll_MCH-loarm_fk_R", "gimbal_MCH-uparm_fk_R"]
        leg_l = ["ikfoot_L", "leg_offset_L", "MCH-upleg_fk_L", "MCH-loleg_fk_L", "dir_MCH-upleg_fk_L", "MCH-self.knee_offset_L", "roll_MCH-upleg_fk_L", "dir_MCH-loleg_fk_L", "roll_MCH-loleg_fk_L", "bdy_foot_L", "bdy_toe_L", "leg_ik_tip_L", "leg_ik_roll_L", "leg_upvector_L", "gimbal_MCH-upleg_fk_L", "gimbal_bdy_foot_L"]
        leg_r = ["ikfoot_R", "leg_offset_R", "MCH-upleg_fk_R", "MCH-loleg_fk_R", "dir_MCH-upleg_fk_R", "MCH-self.knee_offset_R", "roll_MCH-upleg_fk_R", "dir_MCH-loleg_fk_R", "roll_MCH-loleg_fk_R", "bdy_foot_R", "bdy_toe_R", "leg_ik_tip_R", "leg_ik_roll_R", "leg_upvector_R", "gimbal_MCH-upleg_fk_R", "gimbal_bdy_foot_R"]
        
                
        posebone = context.active_pose_bone
        ob = context.active_object
                
        if posebone.name in arm_l:
            pass            
        
        elif posebone.name in arm_r:
            pass            

        elif posebone.name in leg_l:
            pass            

        elif posebone.name in leg_r:
            pass            
            
        
        return {'FINISHED'}


def register():
    pass

def unregister():
    pass

if __name__ == "__main__":
    register()
