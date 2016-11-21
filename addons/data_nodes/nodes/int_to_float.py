# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy
from bpy.types import NodeTree, Node, NodeSocket
from data_nodes.functions import send_value


class IntToFloat(Node):
    
    '''Float To String node'''
    bl_idname = 'IntToFloatNodeType'
    bl_label = 'Int To Float'
    
    
    
    
    def init(self, context):
        self.inputs.new('NodeSocketInt', "Int")
        self.outputs.new('NodeSocketFloat', "Float")
    
    
    def update(self):
        
        input_value = self.inputs["Int"].default_value
        input_value = float(input_value)
        
        # send data value to connected nodes
        send_value(self.outputs, input_value)
                    
        
    
                 
    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        pass
    
    # Detail buttons in the sidebar.
    """def draw_buttons_ext(self, context, layout):
        pass"""

    
    def draw_label(self):
        return "Int To Float"








def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
    
print ("---")