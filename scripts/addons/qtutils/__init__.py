import bpy
from qtutils.core import QtWindowEventLoop

bl_info = {
    'name': 'qtutils',
    'author': 'Vincent Girès',
    'description': 'Qt Integration',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'category': 'Qt'}


def register():
    bpy.utils.register_class(QtWindowEventLoop)
    from qtutils import example
    bpy.utils.register_class(example.CustomWindowOperator)
    bpy.utils.register_class(example.QtPanelExample)


def unregister():
    bpy.utils.unregister_class(QtWindowEventLoop)
    bpy.utils.unregister_class(example.CustomWindowOperator)
    bpy.utils.unregister_class(example.QtPanelExample)
