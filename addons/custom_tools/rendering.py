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

# Author : Vincent Gires
# www.vincentgires.com


import bpy



## PANEL ##
###########


class VIEW3D_custom_panel_render(bpy.types.Panel):
    bl_label = "Rendering"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Custom"
    
    
    def draw(self, context):
        layout = self.layout
        
        layout.operator("set_object_id.btn")
        layout.operator("set_material_id.btn")



## OPERATOR ##
##############


class custom_tools_set_object_id(bpy.types.Operator):
    bl_idname = "set_object_id.btn"
    bl_label = "Set object ID"
    bl_description = "Set incremental object ID on all mesh objects in the scene"
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'OBJECT')
    
    def execute(self, context):
        cpt = 1
        for obj in context.scene.objects:
            if obj.type == "MESH":
                obj.pass_index = cpt
                cpt = cpt + 1
        
        return{'FINISHED'}

class custom_tools_set_material_id(bpy.types.Operator):
    bl_idname = "set_material_id.btn"
    bl_label = "Set material ID"
    bl_description = "Set incremental material ID on all materials of the file"
    
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'OBJECT')
    
    def execute(self, context):
        cpt = 1
        for mat in bpy.data.materials:
            mat.pass_index = cpt
            cpt = cpt + 1
        
        return{'FINISHED'}



## REGISTRATION ##
##################




def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
