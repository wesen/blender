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
import mathutils
#import ivo_anim_tools
#from ivo_anim_tools import bone_match_rotation, snap_bone_to_position, snap_posebone_to_posebone
from mathutils import Vector, Matrix


#  In:
#    posebone: the one that should be snapped/transformed
#    target: can bei either a posebone or a matrix in armature space
def snap_posebone_to_posebone( posebone, target, loc=True, rot=True ):

    if posebone.parent != None:
        parent_inverse = posebone.parent.matrix.copy()
        parent_inverse.invert()
        parent_local_inverse = posebone.parent.bone.matrix_local.copy()
        parent_local_inverse.invert()
        matrix_local = posebone.bone.matrix_local.copy()

    else:
        parent_inverse = parent_local_inverse = matrix_local = mathutils.Matrix()
    #~ tmp3 = posebone.parent.bone.matrix_local.copy()
    #~ tmp3.invert()
    
    #~ parent_offset = tmp3 * posebone.bone.matrix_local.copy() 
    parent_offset = parent_local_inverse * posebone.bone.matrix_local.copy() 
    #~ tmp4 = parent_offset.copy()
    #~ tmp4.invert()
    parent_offset.invert()
    #~ m = tmp4 * parent_inverse #  we have the world center now ...
    m = parent_offset * parent_inverse #  we have the world center now ...
    
    #  ... and simply mul by target world matrix
    if type(target) == mathutils.Matrix:
        m *= target
    elif type(target) == bpy.types.PoseBone:
        m *= target.matrix
    
    #  output
    if loc:
        posebone.location = m.to_translation()
    if rot:
        if posebone.rotation_mode == 'QUATERNION':
            posebone.rotation_quaternion = m.to_quaternion()
        else:
            posebone.rotation_euler = m.to_euler( posebone.rotation_mode )


# unfortunately the snapping script only works reliable when having it inserting keys as it goes atm


def refresh():
    bpy.context.scene.frame_current = bpy.context.scene.frame_current


def key_rotation(posebone):
    if posebone.rotation_mode == 'QUATERNION':
        posebone.keyframe_insert('rotation_quaternion')
    else:
        posebone.keyframe_insert('rotation_euler')


def snap_rot_and_keyframe( ob, posebone, matrix ):
    
    snap_posebone_to_posebone( posebone, matrix, loc=False, rot=True )
    bpy.context.scene.update()
    key_rotation(posebone)


def snap_trans_and_keyframe( ob, posebone, vector ):

    snap_posebone_to_posebone( posebone, mathutils.Matrix.Translation(vector), True, False )
    posebone.keyframe_insert('location')
    bpy.context.scene.update()



def arm_fk_to_ik(ob, side="_L"):

    # remember wrist rotation
    wrist_mat = ob.pose.bones["bdy_wrist"+side].matrix.copy()
    uparm_mat = ob.pose.bones["bdy_uparm"+side].matrix.copy()
    loarm_mat = ob.pose.bones["bdy_loarm"+side].matrix.copy()


    ob.pose.bones["bdy_shoulder"+side]["FK_IK"] = 0
    ob.pose.bones["bdy_shoulder"+side].keyframe_insert( '["FK_IK"]' )
    refresh()
    
    # apply upper arm rotation
    snap_rot_and_keyframe( ob, ob.pose.bones["MCH-uparm_fk"+side], uparm_mat )

    # apply lower arm rotation
    snap_rot_and_keyframe( ob, ob.pose.bones["MCH-loarm_fk"+side], loarm_mat )

    # re-apply wrist rotation
    snap_rot_and_keyframe( ob, ob.pose.bones["bdy_wrist"+side], wrist_mat )


def arm_ik_to_fk(ob, side="_L"):


    scene = bpy.context.scene
    # remember wrist rotation
    wrist_mat = ob.pose.bones["bdy_wrist"+side].matrix.copy()
    wrist_pos = ob.pose.bones["bdy_wrist"+side].matrix.copy().to_translation()
    elbow_pos = ob.pose.bones["bdy_loarm"+side].matrix.copy().to_translation()
    wrist_pos = ob.pose.bones["bdy_wrist"+side].matrix.copy()
    elbow_pos = ob.pose.bones["bdy_loarm"+side].matrix.copy()


    ob.pose.bones["bdy_shoulder"+side]["FK_IK"] = 1
    ob.pose.bones["bdy_shoulder"+side].keyframe_insert( '["FK_IK"]' )
    refresh()
    
    ik = ob.pose.bones["arm_IK_upvec"+side]
    snap_posebone_to_posebone( ik, elbow_pos, loc=True, rot=False )
    ik.keyframe_insert('location')
    scene.update()

    ik = ob.pose.bones["IK_wrist"+side]    
    snap_posebone_to_posebone( ik, wrist_pos, loc=True, rot=False )
    ik.keyframe_insert('location')
    scene.update()

    # re-apply wrist rotation
    fk = ob.pose.bones["bdy_wrist"+side]
    snap_posebone_to_posebone( fk, wrist_mat, loc=True, rot=True )
    bpy.context.scene.update()
    key_rotation(fk)


def leg_fk_to_ik(ob, side="_L"):


    # remember foot rotation
    foot_mat = ob.pose.bones["bdy_foot"+side].matrix.copy()
    upleg_mat = ob.pose.bones["bdy_upleg"+side].matrix.copy()
    loleg_mat = ob.pose.bones["bdy_loleg"+side].matrix.copy()


    ob.pose.bones["bdy_hip"]['FK_IK' + side ] = 0
    ob.pose.bones["bdy_hip"].keyframe_insert( '["FK_IK' + side + '"]' )
    refresh()
    
    # apply upper leg rotation
    snap_rot_and_keyframe( ob, ob.pose.bones["MCH-upleg_fk"+side], upleg_mat )

    # apply lower leg rotation
    snap_rot_and_keyframe( ob, ob.pose.bones["MCH-loleg_fk"+side], loleg_mat )

    # re-apply foot rotation
    snap_rot_and_keyframe( ob, ob.pose.bones["bdy_foot"+side], foot_mat )


def leg_ik_to_fk(ob, side="_L"):

    scene = bpy.context.scene
    
    # remember wrist rotation
    foot_mat = ob.pose.bones["bdy_foot"+side].matrix.copy()
    upleg_pos = ob.pose.bones["bdy_upleg"+side].matrix.copy().to_translation()
    knee_pos = ob.pose.bones["bdy_loleg"+side].matrix.copy().to_translation()
    ankle_pos = ob.pose.bones["bdy_foot"+side].matrix.copy().to_translation()
    upvec_mat = ob.pose.bones["bdy_loleg"+side].matrix.copy() * mathutils.Matrix.Translation( Vector([0,0,0]) )

    rot_dir = upleg_pos.copy() - ankle_pos.copy()
    rot_dir.normalize()
    
    rot_up = upleg_pos.copy() - knee_pos.copy()
    
    rot_z = rot_dir.copy().cross( rot_up.copy() )
    rot_z.normalize()
    
    rot_up = rot_z.copy().cross( rot_dir.copy())
    rot_up.normalize()

    rot_z = rot_dir.copy().cross( rot_up.copy() )
    rot_z.normalize()
    
    rot_mat = mathutils.Matrix( (rot_dir, rot_up, rot_z) )
    rot_mat.resize4x4()
    rot_mat[3] = ankle_pos.copy().resize4D()
    #bpy.data.objects['Empty'].matrix_world = mathutils.Matrix.Translation(Vector([0.1,0,0])) * rot_mat.copy()


    ob.pose.bones["bdy_hip"]['FK_IK' + side ] = 1
    ob.pose.bones["bdy_hip"].keyframe_insert( '["FK_IK' + side + '"]' )
    refresh()


    ik_foot_offset_mat = (mathutils.Matrix((
        [-0.9999991059303284, -0.001253195689059794, 0.0002014651836361736, 0.0],
        [0.0008448574226349592, -0.7756551504135132, -0.6311563849449158, 0.0],
        [0.0009471820667386055, -0.6311556100845337, 0.7756554484367371, 0.0],
        [-0.0015875680837780237, 4.8762798542156816e-05, 7.268171611940488e-05, 1.0]) ))    
        
    if side == "_L":
        
        upvec_mat = rot_mat.copy() * mathutils.Matrix.Translation(Vector([0,0,-0.5]))

    else:
        upvec_mat = rot_mat.copy() * mathutils.Matrix.Translation(Vector([0,0,0.5]))
        
    
    snap_trans_and_keyframe( ob, ob.pose.bones["ikfoot"+side], ankle_pos )
    snap_rot_and_keyframe( ob, ob.pose.bones["ikfoot"+side], foot_mat.copy() * ik_foot_offset_mat )
        
    snap_trans_and_keyframe( ob, ob.pose.bones["leg_upvector"+side], upvec_mat.to_translation()  )


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
            if ob.pose.bones["bdy_shoulder_L"]["FK_IK"] == 1:
                arm_fk_to_ik(ob, side="_L")
            elif ob.pose.bones["bdy_shoulder_L"]["FK_IK"] == 0:
                arm_ik_to_fk(ob, side="_L")
            
        elif posebone.name in arm_r:
            if ob.pose.bones["bdy_shoulder_R"]["FK_IK"] == 1:
                arm_fk_to_ik(ob, side="_R")
            elif ob.pose.bones["bdy_shoulder_R"]["FK_IK"] == 0:
                arm_ik_to_fk(ob, side="_R")

        elif posebone.name in leg_l:
            if ob.pose.bones["bdy_hip"]['FK_IK_L' ] == 1:
                leg_fk_to_ik(ob, side="_L")
            elif ob.pose.bones["bdy_hip"]['FK_IK_L' ] == 0:
                leg_ik_to_fk(ob, side="_L")

        elif posebone.name in leg_r:
            if ob.pose.bones["bdy_hip"]['FK_IK_R' ] == 1:
                leg_fk_to_ik(ob, side="_R")
            elif ob.pose.bones["bdy_hip"]['FK_IK_R' ] == 0:
                leg_ik_to_fk(ob, side="_R")
            
        
        return {'FINISHED'}


    
#ob = bpy.context.active_object
#arm_fk_to_ik(ob, "_L")
#arm_ik_to_fk(ob, "_L")
#leg_fk_to_ik(ob)
#leg_ik_to_fk(ob, "_R")


def register():
    pass

def unregister():
    pass

if __name__ == "__main__":
    register()
#    bpy.ops.pose.norman_snap_fk_ik()
