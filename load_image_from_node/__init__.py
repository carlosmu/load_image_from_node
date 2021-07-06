# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Load Image From Node",
    "author" : "carlosmu <carlos.damian.munoz@gmail.com>",    
    "blender" : (2, 83, 0),
    "version" : (0, 1, 0),
    "category" : "Interface",
    "location" : "Image Editor Header",
    "description" : "Load image from selected node.",
    "warning" : "",
    "doc_url" : "",
    "tracker_url" : "",
}

import bpy

from . import draw_button
from . import op_load_image_from_node


####################################
# REGISTER/UNREGISTER
####################################
def register():
    draw_button.register()
    op_load_image_from_node.register() 
        
def unregister():
    draw_button.unregister()
    op_load_image_from_node.unregister() 