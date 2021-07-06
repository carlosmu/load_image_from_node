import bpy

##############################################
## DRAW MENU BUTTON
##############################################
def load_image_from_node_button(self, context):
    layout = self.layout     
    if bpy.context.active_object.active_material.node_tree.nodes.active.type == "TEX_IMAGE": 
        layout.operator("lifn.load_image_from_node", icon='NODE_TEXTURE', text = "Load")   
        layout.separator()   


##############################################
## REGISTER/UNREGISTER
##############################################
def register():
    bpy.types.IMAGE_MT_editor_menus.prepend(load_image_from_node_button) 
    bpy.types.NODE_MT_context_menu.prepend(load_image_from_node_button) 
        
def unregister():
    bpy.types.IMAGE_MT_editor_menus.remove(load_image_from_node_button) 
    bpy.types.NODE_MT_context_menu.remove(load_image_from_node_button) 