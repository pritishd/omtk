from omtk.libs import libPython
from omtk import classModule
from maya import cmds

def create(cls_name, *args, **kwargs):
    cls = libPython.get_class_def(cls_name, classModule.Module)
    if cls is None:
        raise Exception("Can't find any module named {0}".format(cls_name))
    cls(*args, **kwargs)
    return cls