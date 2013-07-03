
__author__ = "Joshua Leung"
__email__ = "aligorith@gmail.com"
__version__ = "1.0"
__bpydoc__ = """\
This script is a demonstration of how F-Curves in a given action can be 
automatically fixed (i.e. when their paths are invalid)
"""

import bpy;
from bpy.props import *

# Define the operator
class ANIM_OT_fcurve_path_fixer(bpy.types.Operator):
	'''
	Tweak the RNA-Paths used by F-Curves in a given Action
	so that they work again. 
	
	This currently doesn't use any fancy Regular-Expressions
	magic, but rather just uses simple text-replacement clobbering.
	
	The default patterns given are for fixing RNA Paths for Bone
	animation that were made in earlier versions of 2.5 
	(i.e. for files saved prior to revision 24637), and are meant
	to given an example of how these could be done.
	'''
	bl_idname = "anim.fcurve_path_fixer"
	bl_label = "Fix FCurve Paths"
	bl_register = True
	bl_undo = True
	
	# List of operator properties.
	action = StringProperty(name="Action", description="Name of Action containing the F-Curves to modify", maxlen=63, default="Action")
	string_find = StringProperty(name="Search For", description="String in paths to replace", maxlen=256, default="pose.pose_channels")
	string_replace = StringProperty(name="Replace With", description="String to replace 'Old Pattern' with in the paths", maxlen=256, default="pose.bones")
	
	def execute(self, context):
		# get the requested action
		try:
			act= bpy.data.actions[self.action];
		except KeyError:
			act= None;
		
		if act:
			# loop over the F-Curves, checking if the paths need fixing
			for fcurve in act.fcurves:
				# perform simple text replacement
				# TODO: maybe this should only happen when the paths aren't working?
				if self.string_find in fcurve.rna_path:
					fcurve.rna_path= fcurve.rna_path.replace(self.string_find, self.string_replace);
		else:
			# action not valid... 
			# 	but don't cancel yet otherwise invoke panel doesn't work
			#return('CANCELLED', );
			pass;
		
		# done
		return('FINISHED', );
	
	def invoke(self, context, event):
		wm = context.window_manager
		wm.invoke_props_popup(self, event) 
		return('RUNNING_MODAL', );
	

# Register this operator
bpy.ops.add(ANIM_OT_fcurve_path_fixer);
