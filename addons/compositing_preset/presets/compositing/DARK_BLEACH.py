import bpy
bpy.types.Scene.bf_author = "Gillan"
bpy.types.Scene.bf_category = "Grading"
bpy.types.Scene.bf_description = "Bleach bypass, the result is a black and white image over a color image. The images usually would have reduced saturation and exposure latitude, along with increased contrast and graininess. It usually is used to maximal effect in conjunction with a one-stop underexposure."
Scene = bpy.context.scene
Tree = Scene.node_tree

Node_G = bpy.data.node_groups.new("Dark Bleach", type='CompositorNodeTree')

Node_1 = Node_G.nodes.new('CompositorNodeBrightContrast')

Node_2 = Node_G.nodes.new('CompositorNodeHueSat')
Node_2.location = (200, -100)
Node_2.color_saturation = 0.0

Node_3 = Node_G.nodes.new('CompositorNodeMixRGB')
Node_3.blend_type = 'MULTIPLY'
Node_3.inputs['Fac'].default_value = 1
Node_3.location = (400, 100)

Node_G.links.new(Node_1.outputs[0], Node_2.inputs[1])
Node_G.links.new(Node_1.outputs[0], Node_3.inputs[1])
Node_G.links.new(Node_2.outputs[0], Node_3.inputs[2])

Node_input = Node_G.nodes.new('NodeGroupInput')
Node_output = Node_G.nodes.new('NodeGroupOutput')

Node_G.inputs.new("NodeSocketColor", 'Source')
Node_G.outputs.new("NodeSocketColor", 'Result')

Node_G.links.new(Node_input.outputs[0], Node_1.inputs[0])
Node_G.links.new(Node_output.inputs[0], Node_3.outputs[0])

g = Tree.nodes.new('CompositorNodeGroup')
g.node_tree = Node_G
