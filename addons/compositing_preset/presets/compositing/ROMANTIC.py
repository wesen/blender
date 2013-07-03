import bpy
bpy.types.Scene.bf_author = "Gillan"
bpy.types.Scene.bf_category = "Grading"
bpy.types.Scene.bf_description = "Romantic, with this filter is a must use a very soft and clear glow."
Scene = bpy.context.scene
Tree = Scene.node_tree

Node_G = bpy.data.node_groups.new("Romantic", type='CompositorNodeTree')

Node_1 = Node_G.nodes.new('CompositorNodeColorBalance')
Node_1.correction_method = 'LIFT_GAMMA_GAIN'
Node_1.lift = [1.120, 1.022, 1.026]
Node_1.gamma = [1.320, 1.082, 1.128]
Node_1.gain = [0.993, 0.929, 0.889]

Node_2 = Node_G.nodes.new('CompositorNodeHueSat')
Node_2.location = (500, 0)
Node_2.color_saturation = 0
Node_2.color_value = 1

Node_G.links.new(Node_1.outputs[0], Node_2.inputs[1])

Node_input = Node_G.nodes.new('NodeGroupInput')
Node_output = Node_G.nodes.new('NodeGroupOutput')

Node_G.inputs.new("NodeSocketColor", 'Source')
Node_G.outputs.new("NodeSocketColor", 'Result')

Node_G.links.new(Node_input.outputs[0], Node_1.inputs[1])
Node_G.links.new(Node_output.inputs[0], Node_2.outputs[0])

g = Tree.nodes.new('CompositorNodeGroup')
g.node_tree = Node_G
