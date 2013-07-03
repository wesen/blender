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

# <pep8 compliant>
#
bl_info = {
    'name': 'Layer Management',
    'author': 'Alfonso Annarumma',
    'version': (0,5),
    'blender': (2, 6, 3),
    'location': 'Proprieties > Object Data > Layer Bone',
    'warning': '',
    'description': 'Display and Edit Bones Layer Name',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'UI'}

import random    
import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty, CollectionProperty, BoolVectorProperty

EDIT = ["EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"]




class LayerToggle(bpy.types.Operator):
    '''Visualize this Layer, Shift-Click to select multiple layers'''
    bl_idname = "object.layertoggle"
    bl_label = "Visualize this layer"
    
    #prop definition
    #layer number
    layerN = bpy.props.IntProperty()
    spacecheck = bpy.props.BoolProperty()
    index_group = bpy.props.IntProperty()

    @classmethod
 
    def poll(cls, context):
        
        return context.scene
        
    
    def execute(self, context):
        
        
        spacecheck = self.spacecheck
        scene = context.scene
        
        layerN = self.layerN
        
        
        
        
        
        
        if spacecheck:
            
            space = context.area.spaces.active
        else:
            space = context.scene
        
        
        if layerN==-1:
            index = self.index_group
            groups = scene.layergroups[index].layer_groups
            layergroups = scene.layergroups[index]
            
            layers = space.layers
            union= [False]*20
            
            if not layergroups.toggle:
                for i in range(0,20):
                    
                    union[i]= groups[i] or layers[i]
                    
                
                space.layers=union  
                layergroups.toggle=True
            else:
                for i in range(0,20):
                    
                    union[i]=  not groups[i]  and layers[i]
                    
                
                space.layers=union  
                layergroups.toggle=False
                        
        else:
        
            if self.shift:
                
                if space.layers[layerN]:
                    toggle = False
                else:
            
            
                    toggle= True                            
                space.layers[layerN]=toggle
            
            else:
                
              
                layer = [False]*20
                layer[layerN]=True
                space.layers=layer
    #                   
                
                if space.layers[layerN]:
                    toggle = False   
                        
                
            
        return {'FINISHED'}
    def invoke(self, context, event):
        self.shift = event.shift
        
        return self.execute(context)

    
    
class BLMergeSelected(bpy.types.Operator):
    '''Move Selected Bones in this Layer Shift-Click to select multiple layers'''
    bl_idname = "object.blmergeselected"
    bl_label = "Merge Selected bones in this layer"
    
    #prop definition
    #layer number
    layerN = bpy.props.IntProperty()


    @classmethod
 
    def poll(cls, context):
        
        return context.scene
        
    
    def execute(self, context):
        arm =context.armature
        layerN = self.layerN

        if context.mode =='EDIT_ARMATURE':
            bones= arm.edit_bones
            
        else:
            bones = arm.bones
           
        #cyecle all object in the layer 
        for bone in bones:
      
            if bone.select:
                visible = False
                for i in range (0,32):
                    if bone.layers[i] and arm.layers[i]:
                        visible =True
                        break
                if visible:
                    
                    if self.shift:
                        
                        if bone.layers[layerN]:
                            toggle = False
                        
                        else:
                            toggle= True 
                                                       
                        bone.layers[layerN]=toggle
                    
                    else:
                        
                      
                        layer = [False]*32
                        layer[layerN]=True
                        bone.layers=layer
    #                   
                        
                        if bone.layers[layerN]:
                            toggle = False   
                    
                
            
        return {'FINISHED'}
    
    def invoke(self, context, event):
        self.shift = event.shift
        
        return self.execute(context)


class BoneLayerGroup(bpy.types.Operator):
    '''Create a Bone Group of the bone in this layer'''
    bl_idname = "object.bonelayergroup"
    bl_label = "Hide Select of Selected"
    
    #prop definition
    #layer number
    layerN = bpy.props.IntProperty()
    
    
 
    
    @classmethod
    
    def poll(cls, context):
        
        return context.scene
        
    
    def execute(self, context):
        
        arm = context.armature
        layerN = self.layerN
        scene = context.scene
        pose = context.active_object.pose
        
        
        
        #create the empty group
        bpy.ops.pose.group_add()
        
        bonelayer = "BoneLayerName"+str(layerN+1)
        
        name = getattr(scene, bonelayer)
        
        groups = pose.bone_groups
        
        
        index = len(groups)-1
        
        groups[index].name=name
        
        
        n = random.randrange(1,20)
        
        if n<10:
            Nstr= "0"+str(n)
        
        else: 
            Nstr = str(n)

        
        groups[index].color_set='THEME'+Nstr
            
        #cyecle all bones in the layer 
        for bone in pose.bones:
            
        
            if bone.bone.layers[layerN]:
                bone.bone_group_index = index        
                
                
               


        return {'FINISHED'}

class BoneLockSelected(bpy.types.Operator):
    '''Loock All Bone on this Layer'''
    bl_idname = "object.bonelockselected"
    bl_label = "Hide Select of Selected"
    
    #prop definition
    #layer number
    layerN = bpy.props.IntProperty()
    
    #lock status
    lock = bpy.props.BoolProperty()
    
             
    
    
    @classmethod
    
    def poll(cls, context):
        
        return context.scene
        
    
    def execute(self, context):
        
        arm = context.armature
        layerN = self.layerN
        lock =self.lock  
        scene = context.scene
        
        
        #check if layer have some thing
        if arm.layers[layerN]:
            
            if context.mode =='EDIT_ARMATURE':
                bones= arm.edit_bones
            
            else:
                bones = arm.bones
                
            #cyecle all bones in the layer 
            for bone in bones:
                
            
                if bone.layers[layerN]:
                    bone.hide_select=not lock
                    bone.select=False
            
                    
                    scene.LockBoneLayer[layerN]= not lock
               
                
     
        
            
        return {'FINISHED'}

class SelectBonesLayer(bpy.types.Operator):
    '''Select All the Bones on this Layer'''
    bl_idname = "object.selectboneslayer"
    bl_label = "Select bones in Layer"
    
    
    layerN = bpy.props.IntProperty()
    
    
    @classmethod
    def poll(cls, context):
        return context.armature

    def execute(self, context):
        
        arm =context.armature
        
        
        
        layerN = self.layerN
        
        i=0
        s=0
        
        #check if layer have some thing       
        if arm.layers[layerN]:
            
            
            if context.mode =='EDIT_ARMATURE':
                bones= arm.edit_bones
            
            else:
                bones = arm.bones
            
            for bone in bones:
                
                
                if bone.layers[layerN]:
                    i = i+1
                if bone.layers[layerN] and bone.select:
                    s = s+1
            
            
            if s==i:
                select=False
            else:
                select=True
                
            for bone in bones:
                    
                if bone.layers[layerN]:
                    bone.select=select
                    print("Fatto")
                        
                        
                        
                        
                    
                 
                    

                
                
    
            
                    
            
        
        return {'FINISHED'}




            
            
        
  

class AllLayersSelect(bpy.types.Operator):
    '''Active all Layer in scene'''
    bl_idname = "scene.layersselect"
    bl_label = "Select All Layer"
    
    vis = bpy.props.BoolProperty()

    
    @classmethod
    def poll(cls, context):
        return context.scene

    def execute(self, context):
        
        scene = context.scene
        vis = self.vis
        #store the active layer
        active = scene.active_layer
        
        view_3d = context.area.spaces.active
                #check for lock camera and layer is active
        if view_3d.lock_camera_and_layers is True:
            space= scene
            
            
        else:
            space= view_3d         
            
            
        if not vis:
            for i in range (0,20):           
            
                 #keep selection of active layer
                if active == i:
                    space.layers[i]= True
                
                #deselect the other...
                else: 
                    space.layers[i]= False
        
        
        else:
            for i in range (0,20):     
                #select all layer
                space.layers[i]=True
                
            #after the cycle, deselect and select the previus active layer        
            space.layers[active]=False
            space.layers[active]=True
        return {'FINISHED'}




class BoneLayerName(bpy.types.Panel):
    
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    
   
    bl_label = "Bone Layer Management"
    bl_idname = "_PT_rig_layers"
    bl_options = {'DEFAULT_CLOSED'}
    
    # layer name prop definition
    bpy.types.Scene.BoneLayerName1 = bpy.props.StringProperty(name="Layer Name", default='layer1')
    bpy.types.Scene.BoneLayerName2 = bpy.props.StringProperty(name="Layer Name", default='layer2')
    bpy.types.Scene.BoneLayerName3 = bpy.props.StringProperty(name="Layer Name", default='layer3')
    bpy.types.Scene.BoneLayerName4 = bpy.props.StringProperty(name="Layer Name", default='layer4')
    bpy.types.Scene.BoneLayerName5 = bpy.props.StringProperty(name="Layer Name", default='layer5')
    bpy.types.Scene.BoneLayerName6 = bpy.props.StringProperty(name="Layer Name", default='layer6')
    bpy.types.Scene.BoneLayerName7 = bpy.props.StringProperty(name="Layer Name", default='layer7')
    bpy.types.Scene.BoneLayerName8 = bpy.props.StringProperty(name="Layer Name", default='layer8')
    bpy.types.Scene.BoneLayerName9 = bpy.props.StringProperty(name="Layer Name", default='layer9')
    bpy.types.Scene.BoneLayerName10 = bpy.props.StringProperty(name="Layer Name", default='layer10')
    bpy.types.Scene.BoneLayerName11 = bpy.props.StringProperty(name="Layer Name", default='layer11')
    bpy.types.Scene.BoneLayerName12 = bpy.props.StringProperty(name="Layer Name", default='layer12')
    bpy.types.Scene.BoneLayerName13 = bpy.props.StringProperty(name="Layer Name", default='layer13')
    bpy.types.Scene.BoneLayerName14 = bpy.props.StringProperty(name="Layer Name", default='layer14')
    bpy.types.Scene.BoneLayerName15 = bpy.props.StringProperty(name="Layer Name", default='layer15')
    bpy.types.Scene.BoneLayerName16 = bpy.props.StringProperty(name="Layer Name", default='layer16')
    bpy.types.Scene.BoneLayerName17 = bpy.props.StringProperty(name="Layer Name", default='layer17')
    bpy.types.Scene.BoneLayerName18 = bpy.props.StringProperty(name="Layer Name", default='layer18')
    bpy.types.Scene.BoneLayerName19 = bpy.props.StringProperty(name="Layer Name", default='layer19')
    bpy.types.Scene.BoneLayerName20 = bpy.props.StringProperty(name="Layer Name", default='layer20')
    bpy.types.Scene.BoneLayerName21 = bpy.props.StringProperty(name="Layer Name", default='layer21')
    bpy.types.Scene.BoneLayerName22 = bpy.props.StringProperty(name="Layer Name", default='layer22')
    bpy.types.Scene.BoneLayerName23 = bpy.props.StringProperty(name="Layer Name", default='layer23')
    bpy.types.Scene.BoneLayerName24 = bpy.props.StringProperty(name="Layer Name", default='layer24')
    bpy.types.Scene.BoneLayerName25 = bpy.props.StringProperty(name="Layer Name", default='layer25')
    bpy.types.Scene.BoneLayerName26 = bpy.props.StringProperty(name="Layer Name", default='layer26')
    bpy.types.Scene.BoneLayerName27 = bpy.props.StringProperty(name="Layer Name", default='layer27')
    bpy.types.Scene.BoneLayerName28 = bpy.props.StringProperty(name="Layer Name", default='layer28')
    bpy.types.Scene.BoneLayerName29 = bpy.props.StringProperty(name="Layer Name", default='layer29')
    bpy.types.Scene.BoneLayerName30 = bpy.props.StringProperty(name="Layer Name", default='layer30')
    bpy.types.Scene.BoneLayerName31 = bpy.props.StringProperty(name="Layer Name", default='layer31')
    bpy.types.Scene.BoneLayerName32 = bpy.props.StringProperty(name="Layer Name", default='layer32')
    
    
    
    
    
    
    
    #prop for hide empty
    bpy.types.Scene.BoneLayerVisibility = bpy.props.BoolProperty(name="Hide empty Bone Layer", default=False)
    
    #prop for extra option
    bpy.types.Scene.BLExtraOptions = bpy.props.BoolProperty(name="Show extra options", default=True)
    
    #lock layer status
    bpy.types.Scene.LockBoneLayer = bpy.props.BoolVectorProperty(name="Lock Layer", default = ([False]*32), size=32)
    
     
    #prop for show index
    bpy.types.Scene.BoneLayerIndex = bpy.props.BoolProperty(name="Show Index", default=False)
   
    #prop for show classic
    bpy.types.Scene.BLClassic = bpy.props.BoolProperty(name="Classic", default=False,description="Use a classic layer selection visibility")
    #Select object Status
    bpy.types.Scene.BLObjectSelect = bpy.props.BoolVectorProperty(name="Object Select", default = ([True]*32), size=32)
      
    #toggle for merge
    #bpy.types.Scene.MergeToggle = bpy.props.BoolVectorProperty(name="Merge Toggle", default = (False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False), size=20)

    
    @classmethod
    def poll(cls, context):
        return context.armature

   
        
    def draw(self, context):
        
        arm = context.armature
        scene = context.scene   
        layout = self.layout
        column = layout.column()
        row = column.row()
        
        
        
#        col2= row.column()
#           
#        #lock camera and layers button 
#           
#        col2.prop(view_3d, "lock_camera_and_layers", text="")
#        
#        #select all
#        
#        allView = col2.operator("scene.layersselect", emboss=False, icon=allIcon, text="")
#        allView.vis=vis
#        
        col= row.column()  
#        col.alignment='RIGHT'
#        #classic
#        col.prop(scene, "Classic", text="Classic")
#        
#        #show extra option checkbox
#       
        
        if context.mode=='POSE':
            onlypose=True
        else:
            onlypose=False
                 
        col.active = onlypose
        col.alignment='RIGHT'
        
        col.prop(scene, "BLExtraOptions", text="Options")
        
        
        column = layout.column(align=True) #ADDED BY KENT TRAMMELL
        col1= row.column()  
#        
#        
#        #show index        
        col1.prop(scene, "BoneLayerIndex", text="Index")
#        
#        # hide empty
#        
#        
      
        col1.alignment='RIGHT'
        col1.prop(scene, "BoneLayerVisibility", toggle=False, text="Hide Empty")        
        
        
        ##########
        
        
        
        
        
        
        
        
               
        
        

        
        
  
        

            
            
            
            
        
        
        #list the layer
        for i in range(0,32): 
            
            
            
            if context.mode =='EDIT_ARMATURE':
                bones= arm.edit_bones
            
            else:
                bones = arm.bones
            

            #inizializing the icon 
            #lockIcon='UNLOCKED'            
            iconUsed= 'RADIOBUT_OFF'
            iconAc='NONE'
            iconLayer='NONE'
            #selectIcon ='RESTRICT_SELECT_OFF'
            #inizializing the bool value
            noitem = False
            
            active=False
            
            layer=32
            scene = context.scene
            
            extra = scene.BLExtraOptions
            
            
            #check the hide empty value
            if scene.BoneLayerVisibility:
               
                #find the empty layer                  
                
                for bone in bones:
                    
                    if bone.layers[i]:
                        
                        layer = i
                
               
                
                    
            else:
                layer=i
                #the layer number
                            
            #set icon for lock layer
            lock = scene.LockBoneLayer[i]
                     
            if lock:
                lockIcon= 'LOCKED'
            else:
                lockIcon= 'UNLOCKED'
           
            
            
            
            
            #check if there are Selected obj in the layer
            
            
            
            
            
            
                
            
           
            
            
            
            
            #check if layer have some thing       
            for bone in bones:
                
            
                if bone.layers[i]:
                   
                    iconUsed= 'LAYER_USED'
                    
                    
                   
                    if bone.select:
                            
                        active = True     
        
            
            else:
                scene.BLObjectSelect[i]= True
                
                
                        
                        

                                     
                
                
            if layer ==i:
            
               

                
           
                #set icon for layer view        
                if arm.layers[layer]:
                    viewIcon = 'RESTRICT_VIEW_OFF'
                    noitem = True
                else:
                    viewIcon = 'RESTRICT_VIEW_ON'
                    noitem = False
                if active:
                    iconUsed = 'LAYER_ACTIVE'
                
                
                #set icon for layer protected view        
                if arm.layers_protected[layer]:
                    iconLayerProtected = 'LINK'
                    noitem = True
                else:
                    iconLayerProtected = 'NONE'
                    noitem = False
                
                
                
                row2=column.row(align=True)
#                if space==scene:
#                    
#                    colb1= row2.column()
#                    #layer visibility operator   
#                    tog = colb1.operator("view3d.layers", text="",icon=viewIcon, emboss=False)
#                    tog.nr=layer+1
#                    tog.toggle=True
#                    viewemboss = True
                
                iconLayer=viewIcon
                
                
                # layer index
                if scene.BoneLayerIndex:
                    
                    col6 = row2.column()
                    
                    col6.scale_x=0.14
                    
                    
                    col6.label(text=str(i+1)+".")
                
                # visualization 
#                classic = scene.BLClassic
#                if not classic:
                    
                colb2= row2.column()
                colb2.prop(arm, "layers", index=layer, emboss=True, icon=iconLayer, toggle=True, text="")
#                else:    
#                    colb6 = row2.column() 
#                    used = colb6.operator("object.layertoggle", text="", icon= iconLayer, emboss=True)
#                    used.layerN=i
#                    used.spacecheck=spacecheck
                
                #protect layer
                colb9= row2.column()
                colb9.prop(arm, "layers_protected", index=layer, emboss=True, icon=iconLayerProtected, toggle=True, text="")
#                 
                
                #text prop
                s = "BoneLayerName"+str(i+1)
                colb3= row2.column()
                colb3.prop(scene,s,text="",icon=iconAc)
                
                
                
                
                
                if (context.mode == 'EDIT_ARMATURE' or context.mode == 'POSE') and extra:
                    
                
                
                
                    
                        
                        
                    
                    
                         
                    #Select by type operator
                    colb4 = row2.column()
                    select = colb4.operator("object.selectboneslayer", icon='RESTRICT_SELECT_OFF',text="", emboss=True ) 
                    select.layerN = i 
                    
                    #select.select_obj= selobj
                        
                    
                    
                    #lock operator 
                    colb5 = row2.column()   
                    lk = colb5.operator("object.bonelockselected", text="", emboss=True, icon= lockIcon)
                    
                    lk.layerN = i
                    lk.lock=lock
                    
                    
    #                #occuped layer
                    
    #                colb6.label(text="", icon=iconUsed)
                    
                    
                    #merge layer
                    colb7 = row2.column()
                    merge = colb7.operator("object.blmergeselected", text="", emboss=True, icon= iconUsed)
                    merge.layerN=i
                    
                if context.mode == 'POSE':
                        
                    #bone group creator
                    colb8 = row2.column()
                    groupB = colb8.operator("object.bonelayergroup", text="", emboss=True, icon= 'GROUP_BONE')
                    groupB.layerN=i
               
                
                
                if not scene.BoneLayerVisibility:
                    if i==7 or i==15 or i==23 or i==31:
                        row3 = column.row()
                        
                        
                        row3.separator()


                
                    
                    
def register():
    

#    bpy.utils.register_class(AllLayersSelect)
#    bpy.utils.register_class(LayerToggle)
    bpy.utils.register_class(BLMergeSelected)
    bpy.utils.register_class(BoneLayerName)
    bpy.utils.register_class(BoneLockSelected)
    bpy.utils.register_class(SelectBonesLayer)
    bpy.utils.register_class(BoneLayerGroup)
    
def unregister():

    bpy.utils.unregister_class(BoneLayerName)
#    bpy.utils.uregister_class(AllLayersSelect)
#    bpy.utils.unregister_class(LayerToggle)
    bpy.utils.uregister_class(BLMergeSelected)
    bpy.utils.unregister_class(BoneLockSelected)
    bpy.utils.unregister_class(SelectBonesLayer)
    bpy.utils.unregister_class(BoneLayerGroup)
    
if __name__ == "__main__":
    register()
