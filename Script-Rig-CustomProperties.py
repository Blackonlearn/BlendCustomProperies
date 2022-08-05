import bpy


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Rig Properties"
    bl_idname = "Rig_Properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        for bone in obj.pose.bones:
            for prop in bone.keys():
                if not prop.startswith('constraint_'):
                    if not prop.startswith('rigify_p'):
                        if not prop.startswith('_RNA'):
                            row = layout.row()
                            row.prop(bone, '["{}"]'.format(prop), slider=True)


def register():
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
