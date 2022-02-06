import bpy
from bpy.types import Panel, Operator
from math import radians
from bpy.types import Operator
from bpy.props import (
        EnumProperty,
        FloatProperty,
        IntProperty,
        )
from math import (
        sin, cos,
        radians,
        sqrt,
        )
 
 
 
 
 
class Mainpanel(Panel):
    bl_label = "Custom Lighting"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "New Tab"
 
    def draw(self, context):
        layout = self.layout
        row=layout.row()
        row.label(text="This button adds custom lighting to the selected object")
        layout.operator("addonname.myop_operator")
        
 
 
 
 
 
##Add trilight panel## 
class Addtrilight(Operator):
    bl_label = "Add trilighting"
    bl_idname = "addonname.myop_operator"
    
    
    
    def execute(self, context):
      
            selected= bpy.context.active_object
            bpy.ops.object.light_add(type='AREA')
            so= bpy.context.active_object
            sops=bpy.ops.object
            so.location=selected.location
            x=0
            y=5
            height=5
            bpy.context.object.data.energy = 50
            so.location[0]+=x
            so.location[1]+=y
            so.location[2]+=y
            so.rotation_euler[0]+= radians(-45)

            def dupli(x,angle_x,angle_y,angle_z,loc_x,loc_y,loc_z):
              a=1
              while a<x:
               bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False,   "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-0-loc_x, -5-loc_y, -0-loc_z), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 1, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, True, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
               bpy.context.object.data.energy = 100
               bpy.context.active_object.rotation_euler[0]+= radians(angle_x)
               bpy.context.active_object.rotation_euler[1]+= radians(angle_y)
               bpy.context.active_object.rotation_euler[2]+= radians(angle_z)


               a=a+1

            dupli(2,90,0,0,0,y,0)
            dupli(2,20,0,90,-10,0,0)
                    
            return {'FINISHED'}
 ##Scaling panel##       
class Scale(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "Scale_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Scale"
    bl_parent_id="ADDONNAME_PT_main_panel"
 
    def draw(self, context):
        layout = self.layout
        row=layout.row()
        row.label(text="Change thes size of the light through here")
        
        col=layout.column()
        col.prop(context.object, "scale")


##Placing all the classes in one Array to register all at once##     
 
classes = [Mainpanel,Addtrilight,Scale]
 
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
   
        
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
   
    
 
 
 
if __name__ == "__main__":
    register()
    
    
    
    


