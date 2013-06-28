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
from keyingsets_utils import *

class BUILTIN_KSI_norman_spine(bpy.types.KeyingSetInfo):
    bl_label = "norman_spine"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"]["IK"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"]["stretch_amount"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"]["global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["eyes_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["head_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["neck_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["fk_bdy_spine1"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["fk_bdy_spine2"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["fk_bdy_spine3"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["pelvis"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["pelvis"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["pelvis_swing"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["center1"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["center2"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].scale', 1 )
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_head_parent"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["eye_control"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_hip"].rotation_euler', 0 )
        p.use_entire_array = True



class BUILTIN_KSI_norman_arm_L(bpy.types.KeyingSetInfo):
    bl_label = "norman_arm_L"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["FK_IK"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["FK_2"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["Stretchy"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["Follow_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["Follow_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_head"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["wrist_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["space_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["space_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_L"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["arm_IK_upvec_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.elbow_offset_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["shoulder_offset_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-wrist_axis_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_L"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_L"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-uparm_fk_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-uparm_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loarm_fk_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loarm_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-uparm_fk_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_wrist_L"].lock_rotation', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["FK_global"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-wrist_axis_L"].rotation_euler', 0 )



class BUILTIN_KSI_norman_arm_R(bpy.types.KeyingSetInfo):
    bl_label = "norman_arm_R"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["FK_IK"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["FK_2"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["Stretchy"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["Follow_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["Follow_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_head"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["wrist_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["space_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["space_chest"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_R"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["arm_IK_upvec_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.elbow_offset_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["shoulder_offset_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-wrist_axis_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_R"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_R"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-uparm_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-uparm_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loarm_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loarm_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-uparm_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-uparm_fk_R"].rotation_euler', 1 )
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_wrist_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["FK_global"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-wrist_axis_R"].rotation_euler', 0 )



class BUILTIN_KSI_norman_hand_R(bpy.types.KeyingSetInfo):
    bl_label = "norman_hand_R"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["flex"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["shear"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["spread"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_pinky_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky_R"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky1_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky2_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky3_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_ring_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring_R"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring1_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring2_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring3_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_middle_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle_R"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle1_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle2_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle3_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_index_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index_R"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index1_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index2_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index3_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_thumb_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb_R"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb1_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb2_R"].rotation_euler', 0 )
        p.use_entire_array = True



class BUILTIN_KSI_norman_hand_L(bpy.types.KeyingSetInfo):
    bl_label = "norman_hand_L"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["flex"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["shear"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["spread"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_pinky_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky_L"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky1_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky2_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky3_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_ring_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring_L"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring1_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring2_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring3_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_middle_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle_L"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle1_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle2_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle3_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_index_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index_L"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index1_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index2_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index3_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_thumb_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb_L"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb1_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb2_L"].rotation_euler', 0 )
        p.use_entire_array = True



class BUILTIN_KSI_norman_leg_L(bpy.types.KeyingSetInfo):
    bl_label = "norman_leg_L"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_IK_L"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_2_L"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_leg_global_L"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["space_global_L"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["stretchy_L"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_L"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_upvector_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.knee_offset_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_L"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_L"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_offset_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-upleg_fk_L"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loleg_fk_L"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-upleg_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loleg_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_roll_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_tip_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_foot_L"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_toe_L"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_foot_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-upleg_fk_L"].lock_rotation', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["stretchy"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["knee_roll_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["space_global"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["foot_rock"]', 0 )



class BUILTIN_KSI_norman_leg_R(bpy.types.KeyingSetInfo):
    bl_label = "norman_leg_R"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_IK_R"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_2_R"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_leg_global_R"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["space_global_R"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["stretchy_R"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["stick"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["space_hip"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["space_global"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_R"]["volume"]', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_upvector_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.knee_offset_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_R"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_R"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_offset_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-upleg_fk_R"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loleg_fk_R"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-upleg_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loleg_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_roll_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_tip_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_foot_R"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_toe_R"].rotation_quaternion', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_foot_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-upleg_fk_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["stretchy"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["knee_roll_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["foot_rock"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["space_global"]', 0 )



class BUILTIN_KSI_norman_mouth(bpy.types.KeyingSetInfo):
    bl_label = "norman_mouth"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["remote_tung1"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["remote_tung2"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_jaw"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_jaw"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_jaw"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["tung1"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["tung2"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"].location', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Curl_Up_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Curl_Lo_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Mouth_Clench"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Mouth_Puff"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Mouth_Pull"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["UD_Up_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["UD_Lo_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"]["Puff"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"]["UD_Up_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"]["UD_Lo_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"]["Puff"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"]["UD_Up_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"]["UD_Lo_Lip"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"].location', 1 )



class BUILTIN_KSI_norman_eyes(bpy.types.KeyingSetInfo):
    bl_label = "norman_eyes"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["eye_control"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["eyes_global"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"].rotation_euler', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].rotation_euler', 1 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].rotation_euler', 1 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["UD_Up_Lid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["UD_Lo_Lid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_1_Inner_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_2_Mid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_3_Outer_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_1_Inner_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_2_Mid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_3_Outer_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Pupil_Scale"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["TW_Up_Lid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["TW_Lo_Lid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Follow_Up_Lid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Follow_Lo_Lid_L"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["UD_Up_Lid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["UD_Lo_Lid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Up_1_Inner_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Up_2_Mid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_1_Inner_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_2_Mid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_3_Outer_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Pupil_Scale"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["TW_Up_Lid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["TW_Lo_Lid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Follow_Up_Lid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Follow_Lo_Lid_R"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["brow_L"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["brow1_L"].location', 1 )
        p = ks.paths.add(id_block, 'pose.bones["brow2_L"].location', 1 )
        p = ks.paths.add(id_block, 'pose.bones["brow3_L"].location', 1 )
        p = ks.paths.add(id_block, 'pose.bones["brow_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["brow3_R"].location', 1 )
        p = ks.paths.add(id_block, 'pose.bones["brow2_R"].location', 1 )
        p = ks.paths.add(id_block, 'pose.bones["brow1_R"].location', 1 )



class BUILTIN_KSI_norman_head(bpy.types.KeyingSetInfo):
    bl_label = "norman_head"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].scale', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].scale', 1 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["head_global"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["neck_global"]', 0 )
        p = ks.paths.add(id_block, 'pose.bones["roll_head_parent"].rotation_euler', 2 )
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_R"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_R"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_R"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bpy_nose"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bpy_nose"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bpy_nose"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_L"].scale', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_L"].rotation_euler', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_L"].location', 0 )
        p.use_entire_array = True



class BUILTIN_KSI_norman_ALL(bpy.types.KeyingSetInfo):
    bl_label = "norman_ALL"

    # poll - test for whether Keying Set can be used at all
    def poll(ksi, context):
        ob = context.active_object
        if ob.type == 'ARMATURE':
            if ob.data.name.find('norman') != -1:
                return (context.active_object) or (context.selected_objects)
        
    # iterator - go over all relevant data, calling generate()
    def iterator(ksi, context, ks):
        for ob in context.selected_objects:
            ksi.generate(context, ks, ob)
            
    # generator - populate Keying Set with property paths to use
    def generate(ksi, context, ks, data):
        id_block = data.id_data
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"]["IK"]', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"]["stretch_amount"]', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"]["stick"]', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"]["global"]', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["eyes_global"]', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["head_global"]', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["neck_global"]', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"].scale', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_chest"].location', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["fk_bdy_spine1"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["fk_bdy_spine2"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["fk_bdy_spine3"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"].location', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["pelvis"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["pelvis"].location', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["pelvis_swing"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["center1"].location', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["center2"].location', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].scale', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].scale', 1, group_method='NAMED', group_name="norman_spine" )
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"].location', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_head_parent"].rotation_euler', 2, group_method='NAMED', group_name="norman_spine" )
        p = ks.paths.add(id_block, 'pose.bones["eye_control"].location', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_hip"].rotation_euler', 0, group_method='NAMED', group_name="norman_spine" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["FK_IK"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["FK_2"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["Stretchy"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["Follow_hip"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["Follow_chest"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_chest"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_hip"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_head"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"]["space_global"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["wrist_global"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["stick"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["space_hip"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["space_chest"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["space_global"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["stick"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["space_hip"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["space_chest"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["space_global"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_L"]["stick"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["arm_IK_upvec_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.elbow_offset_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["shoulder_offset_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"].scale', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-wrist_axis_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_L"].scale', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_L"].scale', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-uparm_fk_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-uparm_fk_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loarm_fk_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loarm_fk_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_L"].location', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-uparm_fk_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_wrist_L"].lock_rotation', 0, group_method='NAMED', group_name="norman_arm_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_L"]["FK_global"]', 0, group_method='NAMED', group_name="norman_arm_L" )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-wrist_axis_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["FK_IK"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["FK_2"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["Stretchy"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["Follow_hip"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["Follow_chest"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_chest"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_hip"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_head"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"]["space_global"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["wrist_global"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["stick"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["space_hip"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["space_chest"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["space_global"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["stick"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["space_hip"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["space_chest"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["space_global"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_R"]["stick"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["IK_wrist_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["arm_IK_upvec_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.elbow_offset_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["shoulder_offset_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"].scale', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-wrist_axis_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-wrist_axis_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_R"].scale', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-uparm_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_R"].scale', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loarm_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-uparm_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-uparm_fk_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-uparm_fk_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loarm_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loarm_fk_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loarm_fk_R"].location', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-uparm_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-uparm_fk_R"].rotation_euler', 1, group_method='NAMED', group_name="norman_arm_R" )
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_wrist_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_shoulder_R"]["FK_global"]', 0, group_method='NAMED', group_name="norman_arm_R" )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-wrist_axis_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_arm_R" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["flex"]', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["shear"]', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_R"]["spread"]', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_pinky_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky_R"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky1_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky2_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky3_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_ring_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring_R"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring1_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring2_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring3_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_middle_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle_R"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle1_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle2_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle3_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_index_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index_R"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index1_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index2_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index3_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_thumb_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb_R"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb1_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb2_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["flex"]', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["shear"]', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_wrist_L"]["spread"]', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_pinky_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky_L"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky1_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky2_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_pinky3_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_ring_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring_L"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring1_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring2_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_ring3_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_middle_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle_L"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle1_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle2_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_middle3_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_index_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index_L"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index1_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index2_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_index3_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["rot_bdy_hnd_thumb_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb_L"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb1_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hnd_thumb2_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_hand_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_IK_L"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_2_L"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_leg_global_L"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["space_global_L"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["stretchy_L"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["stick"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["space_hip"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["space_global"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["stick"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["space_hip"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["space_global"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_L"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"].location', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_upvector_L"].location', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.knee_offset_L"].location', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_L"].scale', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_L"].scale', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_offset_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-upleg_fk_L"].rotation_euler', 2, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loleg_fk_L"].rotation_euler', 2, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-upleg_fk_L"].location', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loleg_fk_L"].location', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_L"].location', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_L"].location', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_roll_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_tip_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_foot_L"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_toe_L"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_foot_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-upleg_fk_L"].lock_rotation', 0, group_method='NAMED', group_name="norman_leg_L" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["stretchy"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["knee_roll_L"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["space_global"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_L"]["foot_rock"]', 0, group_method='NAMED', group_name="norman_leg_L" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_IK_R"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_2_R"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_hip"]["FK_leg_global_R"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["space_global_R"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["stretchy_R"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["stick"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["space_hip"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["space_global"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["stick"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["space_hip"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["space_global"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_R"]["volume"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"].location', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_upvector_R"].location', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-self.knee_offset_R"].location', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_R"].scale', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-upleg_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_R"].scale', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["MCH-loleg_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_offset_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-upleg_fk_R"].rotation_euler', 2, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["roll_MCH-loleg_fk_R"].rotation_euler', 2, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-upleg_fk_R"].location', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["roll_end_MCH-loleg_fk_R"].location', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-upleg_fk_R"].location', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["dir_MCH-loleg_fk_R"].location', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_roll_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["leg_ik_tip_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_foot_R"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_toe_R"].rotation_quaternion', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_bdy_foot_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["gimbal_MCH-upleg_fk_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_leg_R" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["stretchy"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["knee_roll_R"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["foot_rock"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["ikfoot_R"]["space_global"]', 0, group_method='NAMED', group_name="norman_leg_R" )
        p = ks.paths.add(id_block, 'pose.bones["remote_tung1"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["remote_tung2"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_jaw"].scale', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_jaw"].rotation_euler', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_jaw"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["tung1"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["tung2"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"].rotation_euler', 2, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"].location', 0, group_method='NAMED', group_name="norman_mouth" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Curl_Up_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Curl_Lo_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Mouth_Clench"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Mouth_Puff"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["Mouth_Pull"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["UD_Up_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"]["UD_Lo_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"]["Puff"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"]["UD_Up_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_L"]["UD_Lo_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"]["Puff"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"]["UD_Up_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["lip_corner_R"]["UD_Lo_Lip"]', 0, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["mouth_center"].location', 1, group_method='NAMED', group_name="norman_mouth" )
        p = ks.paths.add(id_block, 'pose.bones["eye_control"].location', 0, group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["eyes_global"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"].rotation_euler', 2, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"].rotation_euler', 2, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].location', 0, group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].scale', 0, group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].rotation_euler', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].location', 0, group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].scale', 0, group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].rotation_euler', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["UD_Up_Lid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["UD_Lo_Lid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_1_Inner_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_2_Mid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_3_Outer_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_1_Inner_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_2_Mid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_3_Outer_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Pupil_Scale"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["TW_Up_Lid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["TW_Lo_Lid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Follow_Up_Lid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Follow_Lo_Lid_L"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["UD_Up_Lid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["UD_Lo_Lid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Up_1_Inner_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Up_2_Mid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_1_Inner_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_2_Mid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_3_Outer_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Pupil_Scale"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["TW_Up_Lid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["TW_Lo_Lid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Follow_Up_Lid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Follow_Lo_Lid_R"]', 0, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow_L"].location', 0, group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["brow1_L"].location', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow2_L"].location', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow3_L"].location', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow_R"].location', 0, group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["brow3_R"].location', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow2_R"].location', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow1_R"].location', 1, group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].rotation_euler', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].rotation_euler', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"].scale', 0, group_method='NAMED', group_name="norman_head" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_neck"].scale', 1, group_method='NAMED', group_name="norman_head" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["head_global"]', 0, group_method='NAMED', group_name="norman_head" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["neck_global"]', 0, group_method='NAMED', group_name="norman_head" )
        p = ks.paths.add(id_block, 'pose.bones["roll_head_parent"].rotation_euler', 2, group_method='NAMED', group_name="norman_head" )
        p = ks.paths.add(id_block, 'pose.bones["dir_head_parent"].location', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_R"].scale', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_R"].rotation_euler', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_R"].location', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bpy_nose"].scale', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bpy_nose"].rotation_euler', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bpy_nose"].location', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_L"].scale', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_L"].rotation_euler', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_ear_L"].location', 0, group_method='NAMED', group_name="norman_head" )
        p.use_entire_array = True





        p = ks.paths.add(id_block, 'pose.bones["eye_control"].location', 0 )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_head"]["eyes_global"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"].rotation_euler', 2 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"].rotation_euler', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"].rotation_euler', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"].rotation_euler', 2 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].location', 0 , group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].scale', 0 , group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_L"].rotation_euler', 1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].location', 0 , group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].scale', 0 , group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_flesh_R"].rotation_euler', 1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["UD_Up_Lid_L"]', -1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["UD_Lo_Lid_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_1_Inner_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_2_Mid_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Up_3_Outer_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_1_Inner_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_2_Mid_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Lid_Lo_3_Outer_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Pupil_Scale"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["TW_Up_Lid_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["TW_Lo_Lid_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Follow_Up_Lid_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_L"]["Follow_Lo_Lid_L"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["UD_Up_Lid_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["UD_Lo_Lid_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Up_1_Inner_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Up_2_Mid_R"]', 0 , group_method='NAMED', group_name="norman_eyes2" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_1_Inner_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_2_Mid_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Lid_Lo_3_Outer_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Pupil_Scale"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["TW_Up_Lid_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["TW_Lo_Lid_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Follow_Up_Lid_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["bdy_eye_R"]["Follow_Lo_Lid_R"]', 0 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow_L"].location', 0 , group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["brow1_L"].location', 1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow2_L"].location', 1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow3_L"].location', 1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow_R"].location', 0 , group_method='NAMED', group_name="norman_eyes" )
        p.use_entire_array = True
        p = ks.paths.add(id_block, 'pose.bones["brow3_R"].location', 1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow2_R"].location', 1 , group_method='NAMED', group_name="norman_eyes" )
        p = ks.paths.add(id_block, 'pose.bones["brow1_R"].location', 1 , group_method='NAMED', group_name="norman_eyes" )



def register():
    bpy.types.register(BUILTIN_KSI_norman_head)
    bpy.types.register(BUILTIN_KSI_norman_eyes)
    bpy.types.register(BUILTIN_KSI_norman_mouth)
    bpy.types.register(BUILTIN_KSI_norman_leg_R)
    bpy.types.register(BUILTIN_KSI_norman_leg_L)
    bpy.types.register(BUILTIN_KSI_norman_hand_L)
    bpy.types.register(BUILTIN_KSI_norman_hand_R)
    bpy.types.register(BUILTIN_KSI_norman_arm_R)
    bpy.types.register(BUILTIN_KSI_norman_arm_L)
    bpy.types.register(BUILTIN_KSI_norman_spine)
    bpy.types.register(BUILTIN_KSI_norman_ALL)

def unregister():
    bpy.types.unregister(BUILTIN_KSI_norman_head)
    bpy.types.unregister(BUILTIN_KSI_norman_eyes)
    bpy.types.unregister(BUILTIN_KSI_norman_mouth)
    bpy.types.unregister(BUILTIN_KSI_norman_leg_R)
    bpy.types.unregister(BUILTIN_KSI_norman_leg_L)
    bpy.types.unregister(BUILTIN_KSI_norman_hand_L)
    bpy.types.unregister(BUILTIN_KSI_norman_hand_R)
    bpy.types.unregister(BUILTIN_KSI_norman_arm_R)
    bpy.types.unregister(BUILTIN_KSI_norman_arm_L)
    bpy.types.unregister(BUILTIN_KSI_norman_spine)
    bpy.types.unregister(BUILTIN_KSI_norman_ALL)

if __name__ == "__main__":
    register()
