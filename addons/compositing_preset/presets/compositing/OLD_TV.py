import bpy
bpy.types.Scene.bf_author = "Gillan"
bpy.types.Scene.bf_category = "Grading"
bpy.types.Scene.bf_description = ""
Scene = bpy.context.scene
Tree = Scene.node_tree

Node_G = bpy.data.node_groups.new("Old TV", type='CompositorNodeTree')

Node_1 = Node_G.nodes.new('CompositorNodeRGBToBW')

Node_2 = Node_G.nodes.new('CompositorNodeCurveRGB')
Node_2.location = (150, 150)
Rcurve, Gcurve, Bcurve, Ccurve = Node_2.mapping.curves[0:4]
Ccurve.points.new(0.133, 0.0)
Ccurve.points.new(0.4166, 0.877)
Ccurve.points.new(0.627, 0.95)
Rcurve.points.new(0.2, 0.188)
Bcurve.points.new(0.75, 0.8)
Node_2.mapping.update()

Node_G.links.new(Node_1.outputs[0], Node_2.inputs[1])

Node_input = Node_G.nodes.new('NodeGroupInput')
Node_output = Node_G.nodes.new('NodeGroupOutput')

Node_G.inputs.new("NodeSocketColor", 'Source')
Node_G.outputs.new("NodeSocketColor", 'Result')

Node_G.links.new(Node_input.outputs[0], Node_1.inputs[0])
Node_G.links.new(Node_output.inputs[0], Node_2.outputs[0])

g = Tree.nodes.new('CompositorNodeGroup')
g.node_tree = Node_G

