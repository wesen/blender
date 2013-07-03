import bpy
bpy.types.Scene.bf_author = "Gillan"
bpy.types.Scene.bf_category = "Grading"
bpy.types.Scene.bf_description = "This kind of atmosphere, is typical of historical movies"
Scene = bpy.context.scene
Tree = Scene.node_tree

Node_G = bpy.data.node_groups.new("Medieval", type='CompositorNodeTree')

Node_1 = Node_G.nodes.new('CompositorNodeHueSat')
Node_1.color_saturation = 0.816
Node_1.color_value = 1.560

Node_2 = Node_G.nodes.new('CompositorNodeColorBalance')
Node_2.location = (200, 50)
Node_2.correction_method = 'LIFT_GAMMA_GAIN'
Node_2.lift = [0.426, 0.0, 0.9]
Node_2.gamma = [1.081, 1.098, 1.064]
Node_2.gain = [0.54, 0.427, 0.353]

Node_3 = Node_G.nodes.new('CompositorNodeCurveRGB')
Node_3.location = (650, 100)
Rcurve, Gcurve, Bcurve, Ccurve = Node_3.mapping.curves[0:4]
Ccurve.points.new(0.03889, 0.0)
Ccurve.points.new(0.40556, 0.84444)
Node_3.mapping.update()

Node_4 = Node_G.nodes.new('CompositorNodeHueSat')
Node_4.location = (900, 0)
Node_4.color_hue = 0.524
Node_4.color_saturation = 0.728
Node_4.color_value = 1.512

Node_G.links.new(Node_1.outputs[0], Node_2.inputs[1])
Node_G.links.new(Node_2.outputs[0], Node_3.inputs[1])
Node_G.links.new(Node_3.outputs[0], Node_4.inputs[1])

Node_input = Node_G.nodes.new('NodeGroupInput')
Node_output = Node_G.nodes.new('NodeGroupOutput')

Node_G.inputs.new("NodeSocketColor", 'Source')
Node_G.outputs.new("NodeSocketColor", 'Result')

Node_G.links.new(Node_input.outputs[0], Node_1.inputs[1])
Node_G.links.new(Node_output.inputs[0], Node_4.outputs[0])

g = Tree.nodes.new('CompositorNodeGroup')
g.node_tree = Node_G
