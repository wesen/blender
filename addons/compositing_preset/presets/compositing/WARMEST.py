import bpy
bpy.types.Scene.bf_author = "Gillan"
bpy.types.Scene.bf_category = "Grading"
bpy.types.Scene.bf_description = "Warmest ignite your image."
Scene = bpy.context.scene
Tree = Scene.node_tree

Node_G = bpy.data.node_groups.new("Warmest", type='CompositorNodeTree')

Node_1 = Node_G.nodes.new('CompositorNodeColorBalance')
Node_1.correction_method = 'LIFT_GAMMA_GAIN'
Node_1.inputs['Fac'].default_value = 0.5
Node_1.lift = [1.160, 0.842, 0.807]
Node_1.gamma = [1.165, 0.932, 0.879]
Node_1.gain = [1.160, 1.075, 0.934]

Node_input = Node_G.nodes.new('NodeGroupInput')
Node_output = Node_G.nodes.new('NodeGroupOutput')

Node_G.inputs.new("NodeSocketColor", 'Source')
Node_G.outputs.new("NodeSocketColor", 'Result')

Node_G.links.new(Node_input.outputs[0], Node_1.inputs[1])
Node_G.links.new(Node_output.inputs[0], Node_1.outputs[0])

g = Tree.nodes.new('CompositorNodeGroup')
g.node_tree = Node_G
