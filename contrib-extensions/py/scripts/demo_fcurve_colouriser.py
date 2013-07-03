
__author__ = "Joshua Leung"
__email__ = "aligorith@gmail.com"
__version__ = "1.0"
__bpydoc__ = """\
This script is a demonstration of how F-Curves can be made to have certain colours
other than the automatically assigned ones. 

To use this script, add it in the appropriate directories so that Blender can find
and register it on startup. Then, simply run it as a normal operator, and use the
repeat-operator (F6) properties to tweak its behaviour (i.e. make it operate on
another action, or perform the operation on other F-Curves)
"""

import bpy;

# Ways to map colors to axis indices
indices2RGB = [
	(1,0,0),	# red for x
	(0,1,0),	# green for y
	(0,0,1)		# blue for z
]

# Define the operator
class ANIM_OT_fcurve_colouriser(bpy.types.Operator):
	'''
	Make the F-Curves for a given setting in a given Action,
	use RGB colours derived from the axis the F-Curve affects.
	'''
	__idname__ = "anim.fcurve_colouriser"
	__label__ = "RGB-ify F-Curve Colours"
	
	# List of operator properties, the attributes will be assigned
	# to the class instance from the operator settings before calling.
	__props__ = [
		bpy.props.StringProperty(attr="action", name="Action", description="Name of Action containing the F-Curves to modify", maxlen=63, default="Action"),
		bpy.props.StringProperty(attr="prop_identifier", name="Property identifier", description="Identifier for property that F-Curve should affect (i.e. 'location', 'rotation', 'scale')", default= "rotation"),
	]
	
	def execute(self, context):
		# get the requested action
		act= bpy.data.actions[self.action];
		
		# if the action is not valid, we should throw an error about this...
		if act == None:
			# TODO: how do we throw errors?
			return('CANCELLED' );
			
		# loop over the F-Curves, and for each one with a path which is acceptable,
		# the colour of the F-Curve will now be determined by the array index
		for fcurve in act.fcurves:
			if self.prop_identifier in fcurve.rna_path:
				# make sure that Blender knows that we want a specific colour for the F-Curve
				fcurve.color_mode= 'CUSTOM';
				
				# set the colour 
				#	- '%' takes the 'modulo' (i.e. makes sure we get triplets of colours)
				fcurve.color= indices2RGB[fcurve.array_index % 3];
		
		# done
		return('FINISHED', );

# Register this operator
bpy.ops.add(ANIM_OT_fcurve_colouriser);
