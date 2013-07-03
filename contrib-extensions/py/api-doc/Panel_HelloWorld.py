class OBJECT_PT_hello(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    bl_label = "My new panel"
    
    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        type = obj.type.capitalize()
        
        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')
        col = layout.column()
        row = col.row()
        row.label(text="The currently selected object is: "+obj.name)
        row = col.row()
        row = layout.row()
        row.prop(obj, "name")
        row = col.row()
        if type == 'Mesh':
            row.label(text="It is a mesh containing "+str(len(obj.data.verts))+" vertices.")
        else:
            row.label(text="it is a "+type+".")
        row = layout.row()
        row.alignment = 'RIGHT'
        row.label(text="The end")

bpy.types.register(OBJECT_PT_hello)

print("Hello little black box")