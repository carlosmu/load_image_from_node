import bpy

##############################################
#   MAIN OPERATOR
##############################################

class LIFN_OT_load_image_from_node(bpy.types.Operator):
    """Load image from selected node """
    bl_idname = "lifn.load_image_from_node"
    bl_label = "Load Image from Node"  
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if bpy.context.active_object.active_material.node_tree.nodes.active.type == "TEX_IMAGE":
            return True 

    ##############################################
    #   Load Image from Node
    ##############################################
    def execute(self, context):
        # Load image name
        img = bpy.context.active_object.active_material.node_tree.nodes.active.image.name
        # Set image in Editor
        for area in bpy.context.screen.areas:
            if area.type == "IMAGE_EDITOR":
                area.spaces[0].image = bpy.data.images[img]
        
        return{'FINISHED'}

##############################################
## REGISTER/UNREGISTER
##############################################
def register():
    bpy.utils.register_class(LIFN_OT_load_image_from_node)
        
def unregister():
    bpy.utils.unregister_class(LIFN_OT_load_image_from_node)