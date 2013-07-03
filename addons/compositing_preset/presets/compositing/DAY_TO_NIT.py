import bpy
bpy.types.Scene.bf_author = "Francois Tarlier"
bpy.types.Scene.bf_category = "Grading"
bpy.types.Scene.bf_description = "F. Tarlier Day to Nit apply the   effect �day to night�"
Scene = bpy.context.scene
Tree = Scene.node_tree

Node_G = bpy.data.node_groups.new("Day to Nit", type='CompositorNodeTree')

Node_1 = Node_G.nodes.new('CompositorNodeColorBalance')
Node_1.correction_method = 'LIFT_GAMMA_GAIN'
Node_1.lift = [0.418, 0.461, 0.780]
Node_1.gamma = [0.875, 1.000, 0.750]
Node_1.gain = [0.455, 0.734, 0.840]

Node_2 = Node_G.nodes.new('CompositorNodeHueSat')
Node_2.location = (500, -100)
Node_2.color_saturation = 0.920
Node_2.color_value = 0.872
Node_2.color_value = 1.016

Node_G.links.new(Node_1.outputs[0], Node_2.inputs[1])

Node_input = Node_G.nodes.new('NodeGroupInput')
Node_output = Node_G.nodes.new('NodeGroupOutput')

Node_G.inputs.new("NodeSocketColor", 'Source')
Node_G.outputs.new("NodeSocketColor", 'Result')

Node_G.links.new(Node_input.outputs[0], Node_1.inputs[1])
Node_G.links.new(Node_output.inputs[0], Node_2.outputs[0])

g = Tree.nodes.new('CompositorNodeGroup')
g.node_tree = Node_G
