import bpy
bpy.types.Scene.bf_author = "Gillan"
bpy.types.Scene.bf_category = "Grading"
bpy.types.Scene.bf_description = "Terror filter that transforms a quiet photo into a nightmare, it is better if you use a control brightness and selective contrast."
Scene = bpy.context.scene
Tree = Scene.node_tree

Node_G = bpy.data.node_groups.new("Terror", type='CompositorNodeTree')

Node_1 = Node_G.nodes.new('CompositorNodeBrightContrast')
Node_1.inputs['Bright'].default_value = -1.300
Node_1.inputs['Contrast'].default_value = 29.200

Node_2 = Node_G.nodes.new('CompositorNodeColorBalance')
Node_2.location = (200, 100)
Node_2.correction_method = 'LIFT_GAMMA_GAIN'
Node_2.inputs['Fac'].default_value = 0.8
Node_2.lift = [1.214, 0.524, 1.480]
Node_2.gamma = [1.2, 1.157, 1.169]
Node_2.gain = [0.586, 0.780, 0.533]

Node_G.links.new(Node_1.outputs[0], Node_2.inputs[1])

Node_input = Node_G.nodes.new('NodeGroupInput')
Node_output = Node_G.nodes.new('NodeGroupOutput')

Node_G.inputs.new("NodeSocketColor", 'Source')
Node_G.outputs.new("NodeSocketColor", 'Result')

Node_G.links.new(Node_input.outputs[0], Node_1.inputs[0])
Node_G.links.new(Node_output.inputs[0], Node_2.outputs[0])

g = Tree.nodes.new('CompositorNodeGroup')
g.node_tree = Node_G
