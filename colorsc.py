# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.33
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _colorsc
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


sgn = _colorsc.sgn
sqr = _colorsc.sqr
clamp = _colorsc.clamp
to_rad = _colorsc.to_rad
to_deg = _colorsc.to_deg
fixed_scale = _colorsc.fixed_scale
endian_swap = _colorsc.endian_swap
class Pos(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Pos, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Pos, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _colorsc.Pos_x_set
    __swig_getmethods__["x"] = _colorsc.Pos_x_get
    if _newclass:x = _swig_property(_colorsc.Pos_x_get, _colorsc.Pos_x_set)
    __swig_setmethods__["y"] = _colorsc.Pos_y_set
    __swig_getmethods__["y"] = _colorsc.Pos_y_get
    if _newclass:y = _swig_property(_colorsc.Pos_y_get, _colorsc.Pos_y_set)
    def __init__(self, *args): 
        this = _colorsc.new_Pos(*args)
        try: self.this.append(this)
        except: self.this = this
    def __add__(*args): return _colorsc.Pos___add__(*args)
    def __sub__(*args): return _colorsc.Pos___sub__(*args)
    def __mul__(*args): return _colorsc.Pos___mul__(*args)
    def __div__(*args): return _colorsc.Pos___div__(*args)
    __swig_getmethods__["create_from_min"] = lambda x: _colorsc.Pos_create_from_min
    if _newclass:create_from_min = staticmethod(_colorsc.Pos_create_from_min)
    __swig_getmethods__["create_from_max"] = lambda x: _colorsc.Pos_create_from_max
    if _newclass:create_from_max = staticmethod(_colorsc.Pos_create_from_max)
    __swig_getmethods__["create_from_angle"] = lambda x: _colorsc.Pos_create_from_angle
    if _newclass:create_from_angle = staticmethod(_colorsc.Pos_create_from_angle)
    __swig_getmethods__["create_from_rotation"] = lambda x: _colorsc.Pos_create_from_rotation
    if _newclass:create_from_rotation = staticmethod(_colorsc.Pos_create_from_rotation)
    __swig_destroy__ = _colorsc.delete_Pos
    __del__ = lambda self : None;
Pos_swigregister = _colorsc.Pos_swigregister
Pos_swigregister(Pos)
cvar = _colorsc.cvar
PI = cvar.PI
map_range = _colorsc.map_range
Pos_create_from_min = _colorsc.Pos_create_from_min
Pos_create_from_max = _colorsc.Pos_create_from_max
Pos_create_from_angle = _colorsc.Pos_create_from_angle
Pos_create_from_rotation = _colorsc.Pos_create_from_rotation

class Color(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Color, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Color, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _colorsc.Color_r_set
    __swig_getmethods__["r"] = _colorsc.Color_r_get
    if _newclass:r = _swig_property(_colorsc.Color_r_get, _colorsc.Color_r_set)
    __swig_setmethods__["g"] = _colorsc.Color_g_set
    __swig_getmethods__["g"] = _colorsc.Color_g_get
    if _newclass:g = _swig_property(_colorsc.Color_g_get, _colorsc.Color_g_set)
    __swig_setmethods__["b"] = _colorsc.Color_b_set
    __swig_getmethods__["b"] = _colorsc.Color_b_get
    if _newclass:b = _swig_property(_colorsc.Color_b_get, _colorsc.Color_b_set)
    __swig_setmethods__["a"] = _colorsc.Color_a_set
    __swig_getmethods__["a"] = _colorsc.Color_a_get
    if _newclass:a = _swig_property(_colorsc.Color_a_get, _colorsc.Color_a_set)
    def __init__(self, *args): 
        this = _colorsc.new_Color(*args)
        try: self.this.append(this)
        except: self.this = this
    def get_a8r8g8b8(*args): return _colorsc.Color_get_a8r8g8b8(*args)
    __swig_getmethods__["create_from_a8r8g8b8"] = lambda x: _colorsc.Color_create_from_a8r8g8b8
    if _newclass:create_from_a8r8g8b8 = staticmethod(_colorsc.Color_create_from_a8r8g8b8)
    def get_a8b8g8r8(*args): return _colorsc.Color_get_a8b8g8r8(*args)
    __swig_getmethods__["create_from_a8b8g8r8"] = lambda x: _colorsc.Color_create_from_a8b8g8r8
    if _newclass:create_from_a8b8g8r8 = staticmethod(_colorsc.Color_create_from_a8b8g8r8)
    def get_r5g6b5(*args): return _colorsc.Color_get_r5g6b5(*args)
    __swig_getmethods__["create_from_r5g6b5"] = lambda x: _colorsc.Color_create_from_r5g6b5
    if _newclass:create_from_r5g6b5 = staticmethod(_colorsc.Color_create_from_r5g6b5)
    def get_b5g6r5(*args): return _colorsc.Color_get_b5g6r5(*args)
    __swig_getmethods__["create_from_float"] = lambda x: _colorsc.Color_create_from_float
    if _newclass:create_from_float = staticmethod(_colorsc.Color_create_from_float)
    __swig_getmethods__["create_from_blend"] = lambda x: _colorsc.Color_create_from_blend
    if _newclass:create_from_blend = staticmethod(_colorsc.Color_create_from_blend)
    __swig_getmethods__["create_from_lerp"] = lambda x: _colorsc.Color_create_from_lerp
    if _newclass:create_from_lerp = staticmethod(_colorsc.Color_create_from_lerp)
    __swig_getmethods__["create_from_yuv"] = lambda x: _colorsc.Color_create_from_yuv
    if _newclass:create_from_yuv = staticmethod(_colorsc.Color_create_from_yuv)
    __swig_getmethods__["yuv_to_hsv"] = lambda x: _colorsc.Color_yuv_to_hsv
    if _newclass:yuv_to_hsv = staticmethod(_colorsc.Color_yuv_to_hsv)
    __swig_destroy__ = _colorsc.delete_Color
    __del__ = lambda self : None;
Color_swigregister = _colorsc.Color_swigregister
Color_swigregister(Color)
Color_create_from_a8r8g8b8 = _colorsc.Color_create_from_a8r8g8b8
Color_create_from_a8b8g8r8 = _colorsc.Color_create_from_a8b8g8r8
Color_create_from_r5g6b5 = _colorsc.Color_create_from_r5g6b5
Color_create_from_float = _colorsc.Color_create_from_float
Color_create_from_blend = _colorsc.Color_create_from_blend
Color_create_from_lerp = _colorsc.Color_create_from_lerp
Color_create_from_yuv = _colorsc.Color_create_from_yuv
Color_yuv_to_hsv = _colorsc.Color_yuv_to_hsv

class ByteBuffer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ByteBuffer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ByteBuffer, name)
    __repr__ = _swig_repr
    __swig_setmethods__["size"] = _colorsc.ByteBuffer_size_set
    __swig_getmethods__["size"] = _colorsc.ByteBuffer_size_get
    if _newclass:size = _swig_property(_colorsc.ByteBuffer_size_get, _colorsc.ByteBuffer_size_set)
    __swig_setmethods__["data"] = _colorsc.ByteBuffer_data_set
    __swig_getmethods__["data"] = _colorsc.ByteBuffer_data_get
    if _newclass:data = _swig_property(_colorsc.ByteBuffer_data_get, _colorsc.ByteBuffer_data_set)
    def __init__(self, *args): 
        this = _colorsc.new_ByteBuffer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _colorsc.delete_ByteBuffer
    __del__ = lambda self : None;
ByteBuffer_swigregister = _colorsc.ByteBuffer_swigregister
ByteBuffer_swigregister(ByteBuffer)

class SurfaceA8R8G8B8(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SurfaceA8R8G8B8, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SurfaceA8R8G8B8, name)
    __repr__ = _swig_repr
    __swig_setmethods__["width"] = _colorsc.SurfaceA8R8G8B8_width_set
    __swig_getmethods__["width"] = _colorsc.SurfaceA8R8G8B8_width_get
    if _newclass:width = _swig_property(_colorsc.SurfaceA8R8G8B8_width_get, _colorsc.SurfaceA8R8G8B8_width_set)
    __swig_setmethods__["height"] = _colorsc.SurfaceA8R8G8B8_height_set
    __swig_getmethods__["height"] = _colorsc.SurfaceA8R8G8B8_height_get
    if _newclass:height = _swig_property(_colorsc.SurfaceA8R8G8B8_height_get, _colorsc.SurfaceA8R8G8B8_height_set)
    __swig_setmethods__["stride"] = _colorsc.SurfaceA8R8G8B8_stride_set
    __swig_getmethods__["stride"] = _colorsc.SurfaceA8R8G8B8_stride_get
    if _newclass:stride = _swig_property(_colorsc.SurfaceA8R8G8B8_stride_get, _colorsc.SurfaceA8R8G8B8_stride_set)
    __swig_setmethods__["pixels"] = _colorsc.SurfaceA8R8G8B8_pixels_set
    __swig_getmethods__["pixels"] = _colorsc.SurfaceA8R8G8B8_pixels_get
    if _newclass:pixels = _swig_property(_colorsc.SurfaceA8R8G8B8_pixels_get, _colorsc.SurfaceA8R8G8B8_pixels_set)
    def __init__(self, *args): 
        this = _colorsc.new_SurfaceA8R8G8B8(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _colorsc.delete_SurfaceA8R8G8B8
    __del__ = lambda self : None;
SurfaceA8R8G8B8_swigregister = _colorsc.SurfaceA8R8G8B8_swigregister
SurfaceA8R8G8B8_swigregister(SurfaceA8R8G8B8)

class DrawCommandBuffer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DrawCommandBuffer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DrawCommandBuffer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _colorsc.new_DrawCommandBuffer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _colorsc.delete_DrawCommandBuffer
    __del__ = lambda self : None;
    def append(*args): return _colorsc.DrawCommandBuffer_append(*args)
    def clear(*args): return _colorsc.DrawCommandBuffer_clear(*args)
    def get_bytes(*args): return _colorsc.DrawCommandBuffer_get_bytes(*args)
    __swig_setmethods__["cmds"] = _colorsc.DrawCommandBuffer_cmds_set
    __swig_getmethods__["cmds"] = _colorsc.DrawCommandBuffer_cmds_get
    if _newclass:cmds = _swig_property(_colorsc.DrawCommandBuffer_cmds_get, _colorsc.DrawCommandBuffer_cmds_set)
    __swig_setmethods__["ncommands"] = _colorsc.DrawCommandBuffer_ncommands_set
    __swig_getmethods__["ncommands"] = _colorsc.DrawCommandBuffer_ncommands_get
    if _newclass:ncommands = _swig_property(_colorsc.DrawCommandBuffer_ncommands_get, _colorsc.DrawCommandBuffer_ncommands_set)
    __swig_getmethods__["create_from_string"] = lambda x: _colorsc.DrawCommandBuffer_create_from_string
    if _newclass:create_from_string = staticmethod(_colorsc.DrawCommandBuffer_create_from_string)
DrawCommandBuffer_swigregister = _colorsc.DrawCommandBuffer_swigregister
DrawCommandBuffer_swigregister(DrawCommandBuffer)
DrawCommandBuffer_create_from_string = _colorsc.DrawCommandBuffer_create_from_string

class DrawCommand(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DrawCommand, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DrawCommand, name)
    __repr__ = _swig_repr
    TYPE_DRAW = _colorsc.DrawCommand_TYPE_DRAW
    TYPE_DRAWEND = _colorsc.DrawCommand_TYPE_DRAWEND
    TYPE_COLORCHANGE = _colorsc.DrawCommand_TYPE_COLORCHANGE
    TYPE_SIZECHANGE = _colorsc.DrawCommand_TYPE_SIZECHANGE
    __swig_setmethods__["type"] = _colorsc.DrawCommand_type_set
    __swig_getmethods__["type"] = _colorsc.DrawCommand_type_get
    if _newclass:type = _swig_property(_colorsc.DrawCommand_type_get, _colorsc.DrawCommand_type_set)
    __swig_setmethods__["pos"] = _colorsc.DrawCommand_pos_set
    __swig_getmethods__["pos"] = _colorsc.DrawCommand_pos_get
    if _newclass:pos = _swig_property(_colorsc.DrawCommand_pos_get, _colorsc.DrawCommand_pos_set)
    __swig_setmethods__["color"] = _colorsc.DrawCommand_color_set
    __swig_getmethods__["color"] = _colorsc.DrawCommand_color_get
    if _newclass:color = _swig_property(_colorsc.DrawCommand_color_get, _colorsc.DrawCommand_color_set)
    __swig_setmethods__["pressure"] = _colorsc.DrawCommand_pressure_set
    __swig_getmethods__["pressure"] = _colorsc.DrawCommand_pressure_get
    if _newclass:pressure = _swig_property(_colorsc.DrawCommand_pressure_get, _colorsc.DrawCommand_pressure_set)
    __swig_setmethods__["flipx"] = _colorsc.DrawCommand_flipx_set
    __swig_getmethods__["flipx"] = _colorsc.DrawCommand_flipx_get
    if _newclass:flipx = _swig_property(_colorsc.DrawCommand_flipx_get, _colorsc.DrawCommand_flipx_set)
    __swig_setmethods__["flipy"] = _colorsc.DrawCommand_flipy_set
    __swig_getmethods__["flipy"] = _colorsc.DrawCommand_flipy_get
    if _newclass:flipy = _swig_property(_colorsc.DrawCommand_flipy_get, _colorsc.DrawCommand_flipy_set)
    __swig_setmethods__["is_text"] = _colorsc.DrawCommand_is_text_set
    __swig_getmethods__["is_text"] = _colorsc.DrawCommand_is_text_get
    if _newclass:is_text = _swig_property(_colorsc.DrawCommand_is_text_get, _colorsc.DrawCommand_is_text_set)
    __swig_setmethods__["text"] = _colorsc.DrawCommand_text_set
    __swig_getmethods__["text"] = _colorsc.DrawCommand_text_get
    if _newclass:text = _swig_property(_colorsc.DrawCommand_text_get, _colorsc.DrawCommand_text_set)
    __swig_setmethods__["brush_control"] = _colorsc.DrawCommand_brush_control_set
    __swig_getmethods__["brush_control"] = _colorsc.DrawCommand_brush_control_get
    if _newclass:brush_control = _swig_property(_colorsc.DrawCommand_brush_control_get, _colorsc.DrawCommand_brush_control_set)
    __swig_setmethods__["brush_type"] = _colorsc.DrawCommand_brush_type_set
    __swig_getmethods__["brush_type"] = _colorsc.DrawCommand_brush_type_get
    if _newclass:brush_type = _swig_property(_colorsc.DrawCommand_brush_type_get, _colorsc.DrawCommand_brush_type_set)
    __swig_setmethods__["size"] = _colorsc.DrawCommand_size_set
    __swig_getmethods__["size"] = _colorsc.DrawCommand_size_get
    if _newclass:size = _swig_property(_colorsc.DrawCommand_size_get, _colorsc.DrawCommand_size_set)
    __swig_setmethods__["opacity"] = _colorsc.DrawCommand_opacity_set
    __swig_getmethods__["opacity"] = _colorsc.DrawCommand_opacity_get
    if _newclass:opacity = _swig_property(_colorsc.DrawCommand_opacity_get, _colorsc.DrawCommand_opacity_set)
    def __init__(self, *args): 
        this = _colorsc.new_DrawCommand(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_getmethods__["create_color_change"] = lambda x: _colorsc.DrawCommand_create_color_change
    if _newclass:create_color_change = staticmethod(_colorsc.DrawCommand_create_color_change)
    __swig_getmethods__["create_draw"] = lambda x: _colorsc.DrawCommand_create_draw
    if _newclass:create_draw = staticmethod(_colorsc.DrawCommand_create_draw)
    __swig_getmethods__["create_end_draw"] = lambda x: _colorsc.DrawCommand_create_end_draw
    if _newclass:create_end_draw = staticmethod(_colorsc.DrawCommand_create_end_draw)
    __swig_getmethods__["create_size_change"] = lambda x: _colorsc.DrawCommand_create_size_change
    if _newclass:create_size_change = staticmethod(_colorsc.DrawCommand_create_size_change)
    __swig_getmethods__["create_flip"] = lambda x: _colorsc.DrawCommand_create_flip
    if _newclass:create_flip = staticmethod(_colorsc.DrawCommand_create_flip)
    __swig_destroy__ = _colorsc.delete_DrawCommand
    __del__ = lambda self : None;
DrawCommand_swigregister = _colorsc.DrawCommand_swigregister
DrawCommand_swigregister(DrawCommand)
DrawCommand_create_color_change = _colorsc.DrawCommand_create_color_change
DrawCommand_create_draw = _colorsc.DrawCommand_create_draw
DrawCommand_create_end_draw = _colorsc.DrawCommand_create_end_draw
DrawCommand_create_size_change = _colorsc.DrawCommand_create_size_change
DrawCommand_create_flip = _colorsc.DrawCommand_create_flip

class BrushType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BrushType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BrushType, name)
    __repr__ = _swig_repr
    BRUSHTYPE_HARD = _colorsc.BrushType_BRUSHTYPE_HARD
    BRUSHTYPE_SOFT = _colorsc.BrushType_BRUSHTYPE_SOFT
    BRUSHTYPE_CURSOR = _colorsc.BrushType_BRUSHTYPE_CURSOR
    NUM_BRUSHES = _colorsc.BrushType_NUM_BRUSHES
    DIST_TABLE_WIDTH = _colorsc.BrushType_DIST_TABLE_WIDTH
    DIST_TABLE_CENTER = _colorsc.BrushType_DIST_TABLE_CENTER
    BRUSH_TABLE_WIDTH = _colorsc.BrushType_BRUSH_TABLE_WIDTH
    BRUSH_TABLE_HEIGHT = _colorsc.BrushType_BRUSH_TABLE_HEIGHT
    EXTRA_BRUSH_SCALE = _colorsc.BrushType_EXTRA_BRUSH_SCALE
    __swig_setmethods__["distance_tbl"] = _colorsc.BrushType_distance_tbl_set
    __swig_getmethods__["distance_tbl"] = _colorsc.BrushType_distance_tbl_get
    if _newclass:distance_tbl = _swig_property(_colorsc.BrushType_distance_tbl_get, _colorsc.BrushType_distance_tbl_set)
    __swig_setmethods__["intensity_tbl"] = _colorsc.BrushType_intensity_tbl_set
    __swig_getmethods__["intensity_tbl"] = _colorsc.BrushType_intensity_tbl_get
    if _newclass:intensity_tbl = _swig_property(_colorsc.BrushType_intensity_tbl_get, _colorsc.BrushType_intensity_tbl_set)
    __swig_getmethods__["create_distance_table"] = lambda x: _colorsc.BrushType_create_distance_table
    if _newclass:create_distance_table = staticmethod(_colorsc.BrushType_create_distance_table)
    def smooth_step(*args): return _colorsc.BrushType_smooth_step(*args)
    def create_brush(*args): return _colorsc.BrushType_create_brush(*args)
    def create_hard_brush(*args): return _colorsc.BrushType_create_hard_brush(*args)
    def create_soft_brush(*args): return _colorsc.BrushType_create_soft_brush(*args)
    def create_cursor(*args): return _colorsc.BrushType_create_cursor(*args)
    def __init__(self, *args): 
        this = _colorsc.new_BrushType(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _colorsc.delete_BrushType
    __del__ = lambda self : None;
BrushType_swigregister = _colorsc.BrushType_swigregister
BrushType_swigregister(BrushType)
BrushType_create_distance_table = _colorsc.BrushType_create_distance_table

class Brush(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Brush, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Brush, name)
    __repr__ = _swig_repr
    BRUSHCONTROL_VARIABLEOPACITY = _colorsc.Brush_BRUSHCONTROL_VARIABLEOPACITY
    BRUSHCONTROL_VARIABLESIZE = _colorsc.Brush_BRUSHCONTROL_VARIABLESIZE
    __swig_setmethods__["brush_type"] = _colorsc.Brush_brush_type_set
    __swig_getmethods__["brush_type"] = _colorsc.Brush_brush_type_get
    if _newclass:brush_type = _swig_property(_colorsc.Brush_brush_type_get, _colorsc.Brush_brush_type_set)
    __swig_setmethods__["color"] = _colorsc.Brush_color_set
    __swig_getmethods__["color"] = _colorsc.Brush_color_get
    if _newclass:color = _swig_property(_colorsc.Brush_color_get, _colorsc.Brush_color_set)
    __swig_setmethods__["type"] = _colorsc.Brush_type_set
    __swig_getmethods__["type"] = _colorsc.Brush_type_get
    if _newclass:type = _swig_property(_colorsc.Brush_type_get, _colorsc.Brush_type_set)
    __swig_setmethods__["size"] = _colorsc.Brush_size_set
    __swig_getmethods__["size"] = _colorsc.Brush_size_get
    if _newclass:size = _swig_property(_colorsc.Brush_size_get, _colorsc.Brush_size_set)
    __swig_setmethods__["control"] = _colorsc.Brush_control_set
    __swig_getmethods__["control"] = _colorsc.Brush_control_get
    if _newclass:control = _swig_property(_colorsc.Brush_control_get, _colorsc.Brush_control_set)
    __swig_setmethods__["opacity"] = _colorsc.Brush_opacity_set
    __swig_getmethods__["opacity"] = _colorsc.Brush_opacity_get
    if _newclass:opacity = _swig_property(_colorsc.Brush_opacity_get, _colorsc.Brush_opacity_set)
    def __init__(self, *args): 
        this = _colorsc.new_Brush(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _colorsc.delete_Brush
    __del__ = lambda self : None;
Brush_swigregister = _colorsc.Brush_swigregister
Brush_swigregister(Brush)

class Canvas(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Canvas, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Canvas, name)
    __repr__ = _swig_repr
    REFERENCE_WIDTH = _colorsc.Canvas_REFERENCE_WIDTH
    REFERENCE_HEIGHT = _colorsc.Canvas_REFERENCE_HEIGHT
    VIDEO_WIDTH = _colorsc.Canvas_VIDEO_WIDTH
    VIDEO_HEIGHT = _colorsc.Canvas_VIDEO_HEIGHT
    DRAWBRUSH_TYPE_NORMAL = _colorsc.Canvas_DRAWBRUSH_TYPE_NORMAL
    DRAWBRUSH_TYPE_OLDCURSOR = _colorsc.Canvas_DRAWBRUSH_TYPE_OLDCURSOR
    DRAWBRUSH_TYPE_DIRECT = _colorsc.Canvas_DRAWBRUSH_TYPE_DIRECT
    DRAWBRUSH_TYPE_GETCOLOR = _colorsc.Canvas_DRAWBRUSH_TYPE_GETCOLOR
    DRAWBRUSH_TYPE_CURSOR = _colorsc.Canvas_DRAWBRUSH_TYPE_CURSOR
    __swig_setmethods__["commands"] = _colorsc.Canvas_commands_set
    __swig_getmethods__["commands"] = _colorsc.Canvas_commands_get
    if _newclass:commands = _swig_property(_colorsc.Canvas_commands_get, _colorsc.Canvas_commands_set)
    __swig_setmethods__["width"] = _colorsc.Canvas_width_set
    __swig_getmethods__["width"] = _colorsc.Canvas_width_get
    if _newclass:width = _swig_property(_colorsc.Canvas_width_get, _colorsc.Canvas_width_set)
    __swig_setmethods__["height"] = _colorsc.Canvas_height_set
    __swig_getmethods__["height"] = _colorsc.Canvas_height_get
    if _newclass:height = _swig_property(_colorsc.Canvas_height_get, _colorsc.Canvas_height_set)
    __swig_setmethods__["image"] = _colorsc.Canvas_image_set
    __swig_getmethods__["image"] = _colorsc.Canvas_image_get
    if _newclass:image = _swig_property(_colorsc.Canvas_image_get, _colorsc.Canvas_image_set)
    __swig_setmethods__["image_backup"] = _colorsc.Canvas_image_backup_set
    __swig_getmethods__["image_backup"] = _colorsc.Canvas_image_backup_get
    if _newclass:image_backup = _swig_property(_colorsc.Canvas_image_backup_get, _colorsc.Canvas_image_backup_set)
    __swig_setmethods__["alpha"] = _colorsc.Canvas_alpha_set
    __swig_getmethods__["alpha"] = _colorsc.Canvas_alpha_get
    if _newclass:alpha = _swig_property(_colorsc.Canvas_alpha_get, _colorsc.Canvas_alpha_set)
    __swig_setmethods__["image_shared"] = _colorsc.Canvas_image_shared_set
    __swig_getmethods__["image_shared"] = _colorsc.Canvas_image_shared_get
    if _newclass:image_shared = _swig_property(_colorsc.Canvas_image_shared_get, _colorsc.Canvas_image_shared_set)
    __swig_setmethods__["image_reference"] = _colorsc.Canvas_image_reference_set
    __swig_getmethods__["image_reference"] = _colorsc.Canvas_image_reference_get
    if _newclass:image_reference = _swig_property(_colorsc.Canvas_image_reference_get, _colorsc.Canvas_image_reference_set)
    __swig_setmethods__["image_video"] = _colorsc.Canvas_image_video_set
    __swig_getmethods__["image_video"] = _colorsc.Canvas_image_video_get
    if _newclass:image_video = _swig_property(_colorsc.Canvas_image_video_get, _colorsc.Canvas_image_video_set)
    __swig_setmethods__["video_idx"] = _colorsc.Canvas_video_idx_set
    __swig_getmethods__["video_idx"] = _colorsc.Canvas_video_idx_get
    if _newclass:video_idx = _swig_property(_colorsc.Canvas_video_idx_get, _colorsc.Canvas_video_idx_set)
    __swig_setmethods__["videopaint_pos"] = _colorsc.Canvas_videopaint_pos_set
    __swig_getmethods__["videopaint_pos"] = _colorsc.Canvas_videopaint_pos_get
    if _newclass:videopaint_pos = _swig_property(_colorsc.Canvas_videopaint_pos_get, _colorsc.Canvas_videopaint_pos_set)
    __swig_setmethods__["videopaint_pressure"] = _colorsc.Canvas_videopaint_pressure_set
    __swig_getmethods__["videopaint_pressure"] = _colorsc.Canvas_videopaint_pressure_get
    if _newclass:videopaint_pressure = _swig_property(_colorsc.Canvas_videopaint_pressure_get, _colorsc.Canvas_videopaint_pressure_set)
    __swig_setmethods__["brush"] = _colorsc.Canvas_brush_set
    __swig_getmethods__["brush"] = _colorsc.Canvas_brush_get
    if _newclass:brush = _swig_property(_colorsc.Canvas_brush_get, _colorsc.Canvas_brush_set)
    __swig_setmethods__["lastpos"] = _colorsc.Canvas_lastpos_set
    __swig_getmethods__["lastpos"] = _colorsc.Canvas_lastpos_get
    if _newclass:lastpos = _swig_property(_colorsc.Canvas_lastpos_get, _colorsc.Canvas_lastpos_set)
    __swig_setmethods__["lastorgpos"] = _colorsc.Canvas_lastorgpos_set
    __swig_getmethods__["lastorgpos"] = _colorsc.Canvas_lastorgpos_get
    if _newclass:lastorgpos = _swig_property(_colorsc.Canvas_lastorgpos_get, _colorsc.Canvas_lastorgpos_set)
    __swig_setmethods__["lastpressure"] = _colorsc.Canvas_lastpressure_set
    __swig_getmethods__["lastpressure"] = _colorsc.Canvas_lastpressure_get
    if _newclass:lastpressure = _swig_property(_colorsc.Canvas_lastpressure_get, _colorsc.Canvas_lastpressure_set)
    __swig_setmethods__["dirtymin"] = _colorsc.Canvas_dirtymin_set
    __swig_getmethods__["dirtymin"] = _colorsc.Canvas_dirtymin_get
    if _newclass:dirtymin = _swig_property(_colorsc.Canvas_dirtymin_get, _colorsc.Canvas_dirtymin_set)
    __swig_setmethods__["dirtymax"] = _colorsc.Canvas_dirtymax_set
    __swig_getmethods__["dirtymax"] = _colorsc.Canvas_dirtymax_get
    if _newclass:dirtymax = _swig_property(_colorsc.Canvas_dirtymax_get, _colorsc.Canvas_dirtymax_set)
    __swig_setmethods__["strokemin"] = _colorsc.Canvas_strokemin_set
    __swig_getmethods__["strokemin"] = _colorsc.Canvas_strokemin_get
    if _newclass:strokemin = _swig_property(_colorsc.Canvas_strokemin_get, _colorsc.Canvas_strokemin_set)
    __swig_setmethods__["strokemax"] = _colorsc.Canvas_strokemax_set
    __swig_getmethods__["strokemax"] = _colorsc.Canvas_strokemax_get
    if _newclass:strokemax = _swig_property(_colorsc.Canvas_strokemax_get, _colorsc.Canvas_strokemax_set)
    __swig_setmethods__["stroke"] = _colorsc.Canvas_stroke_set
    __swig_getmethods__["stroke"] = _colorsc.Canvas_stroke_get
    if _newclass:stroke = _swig_property(_colorsc.Canvas_stroke_get, _colorsc.Canvas_stroke_set)
    __swig_setmethods__["idle_while_drawing"] = _colorsc.Canvas_idle_while_drawing_set
    __swig_getmethods__["idle_while_drawing"] = _colorsc.Canvas_idle_while_drawing_get
    if _newclass:idle_while_drawing = _swig_property(_colorsc.Canvas_idle_while_drawing_get, _colorsc.Canvas_idle_while_drawing_set)
    __swig_setmethods__["drawtype"] = _colorsc.Canvas_drawtype_set
    __swig_getmethods__["drawtype"] = _colorsc.Canvas_drawtype_get
    if _newclass:drawtype = _swig_property(_colorsc.Canvas_drawtype_get, _colorsc.Canvas_drawtype_set)
    __swig_setmethods__["playing"] = _colorsc.Canvas_playing_set
    __swig_getmethods__["playing"] = _colorsc.Canvas_playing_get
    if _newclass:playing = _swig_property(_colorsc.Canvas_playing_get, _colorsc.Canvas_playing_set)
    __swig_setmethods__["playback"] = _colorsc.Canvas_playback_set
    __swig_getmethods__["playback"] = _colorsc.Canvas_playback_get
    if _newclass:playback = _swig_property(_colorsc.Canvas_playback_get, _colorsc.Canvas_playback_set)
    __swig_setmethods__["playback_speed"] = _colorsc.Canvas_playback_speed_set
    __swig_getmethods__["playback_speed"] = _colorsc.Canvas_playback_speed_get
    if _newclass:playback_speed = _swig_property(_colorsc.Canvas_playback_speed_get, _colorsc.Canvas_playback_speed_set)
    __swig_setmethods__["modified"] = _colorsc.Canvas_modified_set
    __swig_getmethods__["modified"] = _colorsc.Canvas_modified_get
    if _newclass:modified = _swig_property(_colorsc.Canvas_modified_get, _colorsc.Canvas_modified_set)
    def __init__(self, *args): 
        this = _colorsc.new_Canvas(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _colorsc.delete_Canvas
    __del__ = lambda self : None;
    def clear(*args): return _colorsc.Canvas_clear(*args)
    def resize(*args): return _colorsc.Canvas_resize(*args)
    def reset_brush(*args): return _colorsc.Canvas_reset_brush(*args)
    def save_shared_image(*args): return _colorsc.Canvas_save_shared_image(*args)
    def restore_shared_image(*args): return _colorsc.Canvas_restore_shared_image(*args)
    def clear_image(*args): return _colorsc.Canvas_clear_image(*args)
    def get_variable_brush_size(*args): return _colorsc.Canvas_get_variable_brush_size(*args)
    def command_draw(*args): return _colorsc.Canvas_command_draw(*args)
    def command_enddraw(*args): return _colorsc.Canvas_command_enddraw(*args)
    def reset_dirty_rect(*args): return _colorsc.Canvas_reset_dirty_rect(*args)
    def draw_brush(*args): return _colorsc.Canvas_draw_brush(*args)
    def add_command(*args): return _colorsc.Canvas_add_command(*args)
    def play_command(*args): return _colorsc.Canvas_play_command(*args)
    def playback_done(*args): return _colorsc.Canvas_playback_done(*args)
    def playback_length(*args): return _colorsc.Canvas_playback_length(*args)
    def playback_pos(*args): return _colorsc.Canvas_playback_pos(*args)
    def start_playback(*args): return _colorsc.Canvas_start_playback(*args)
    def pause_playback(*args): return _colorsc.Canvas_pause_playback(*args)
    def resume_playback(*args): return _colorsc.Canvas_resume_playback(*args)
    def stop_playback(*args): return _colorsc.Canvas_stop_playback(*args)
    def finish_playback(*args): return _colorsc.Canvas_finish_playback(*args)
    def playback_finish_stroke(*args): return _colorsc.Canvas_playback_finish_stroke(*args)
    def playback_to(*args): return _colorsc.Canvas_playback_to(*args)
    def playback_step_to(*args): return _colorsc.Canvas_playback_step_to(*args)
    def playback_to_timed(*args): return _colorsc.Canvas_playback_to_timed(*args)
    def set_playback_speed(*args): return _colorsc.Canvas_set_playback_speed(*args)
    def truncate_at_playback(*args): return _colorsc.Canvas_truncate_at_playback(*args)
    def update_playback(*args): return _colorsc.Canvas_update_playback(*args)
    def get_num_commands(*args): return _colorsc.Canvas_get_num_commands(*args)
    def play_range(*args): return _colorsc.Canvas_play_range(*args)
    def blit_2x(*args): return _colorsc.Canvas_blit_2x(*args)
    def blit_4x(*args): return _colorsc.Canvas_blit_4x(*args)
    def downsize_video(*args): return _colorsc.Canvas_downsize_video(*args)
    def videopaint_motion(*args): return _colorsc.Canvas_videopaint_motion(*args)
    def blit_videopaint(*args): return _colorsc.Canvas_blit_videopaint(*args)
    def set_reference_buffer(*args): return _colorsc.Canvas_set_reference_buffer(*args)
    def render_reference_overlay(*args): return _colorsc.Canvas_render_reference_overlay(*args)
    def render_overlay(*args): return _colorsc.Canvas_render_overlay(*args)
    def clear_overlay(*args): return _colorsc.Canvas_clear_overlay(*args)
    def upgrade_drw_header(*args): return _colorsc.Canvas_upgrade_drw_header(*args)
    def load(*args): return _colorsc.Canvas_load(*args)
    def save(*args): return _colorsc.Canvas_save(*args)
    def convert_from_drw(*args): return _colorsc.Canvas_convert_from_drw(*args)
    def convert_to_drw(*args): return _colorsc.Canvas_convert_to_drw(*args)
    def send_drw_commands(*args): return _colorsc.Canvas_send_drw_commands(*args)
    def receive_drw_commands(*args): return _colorsc.Canvas_receive_drw_commands(*args)
Canvas_swigregister = _colorsc.Canvas_swigregister
Canvas_swigregister(Canvas)

class Palette(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Palette, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Palette, name)
    __repr__ = _swig_repr
    WHEEL_WIDTH = _colorsc.Palette_WHEEL_WIDTH
    __swig_setmethods__["size"] = _colorsc.Palette_size_set
    __swig_getmethods__["size"] = _colorsc.Palette_size_get
    if _newclass:size = _swig_property(_colorsc.Palette_size_get, _colorsc.Palette_size_set)
    __swig_setmethods__["palette_h"] = _colorsc.Palette_palette_h_set
    __swig_getmethods__["palette_h"] = _colorsc.Palette_palette_h_get
    if _newclass:palette_h = _swig_property(_colorsc.Palette_palette_h_get, _colorsc.Palette_palette_h_set)
    __swig_setmethods__["palette_s"] = _colorsc.Palette_palette_s_set
    __swig_getmethods__["palette_s"] = _colorsc.Palette_palette_s_get
    if _newclass:palette_s = _swig_property(_colorsc.Palette_palette_s_get, _colorsc.Palette_palette_s_set)
    __swig_setmethods__["palette_v"] = _colorsc.Palette_palette_v_set
    __swig_getmethods__["palette_v"] = _colorsc.Palette_palette_v_get
    if _newclass:palette_v = _swig_property(_colorsc.Palette_palette_v_get, _colorsc.Palette_palette_v_set)
    __swig_setmethods__["triangle_cursor"] = _colorsc.Palette_triangle_cursor_set
    __swig_getmethods__["triangle_cursor"] = _colorsc.Palette_triangle_cursor_get
    if _newclass:triangle_cursor = _swig_property(_colorsc.Palette_triangle_cursor_get, _colorsc.Palette_triangle_cursor_set)
    __swig_setmethods__["triangle_capture"] = _colorsc.Palette_triangle_capture_set
    __swig_getmethods__["triangle_capture"] = _colorsc.Palette_triangle_capture_get
    if _newclass:triangle_capture = _swig_property(_colorsc.Palette_triangle_capture_get, _colorsc.Palette_triangle_capture_set)
    __swig_setmethods__["wheel_capture"] = _colorsc.Palette_wheel_capture_set
    __swig_getmethods__["wheel_capture"] = _colorsc.Palette_wheel_capture_get
    if _newclass:wheel_capture = _swig_property(_colorsc.Palette_wheel_capture_get, _colorsc.Palette_wheel_capture_set)
    def __init__(self, *args): 
        this = _colorsc.new_Palette(*args)
        try: self.this.append(this)
        except: self.this = this
    def get_wheel_radius(*args): return _colorsc.Palette_get_wheel_radius(*args)
    def rgb_to_hsv(*args): return _colorsc.Palette_rgb_to_hsv(*args)
    def hsv_to_rgb(*args): return _colorsc.Palette_hsv_to_rgb(*args)
    def set_color(*args): return _colorsc.Palette_set_color(*args)
    def get_color(*args): return _colorsc.Palette_get_color(*args)
    def sqr(*args): return _colorsc.Palette_sqr(*args)
    def dot(*args): return _colorsc.Palette_dot(*args)
    def length(*args): return _colorsc.Palette_length(*args)
    def length_sqr(*args): return _colorsc.Palette_length_sqr(*args)
    def distance(*args): return _colorsc.Palette_distance(*args)
    def distance_sqr(*args): return _colorsc.Palette_distance_sqr(*args)
    def normalize(*args): return _colorsc.Palette_normalize(*args)
    def get_triangle_points(*args): return _colorsc.Palette_get_triangle_points(*args)
    def render_wheel(*args): return _colorsc.Palette_render_wheel(*args)
    def render_triangle(*args): return _colorsc.Palette_render_triangle(*args)
    def get_wheel_pos(*args): return _colorsc.Palette_get_wheel_pos(*args)
    def get_triangle_pos(*args): return _colorsc.Palette_get_triangle_pos(*args)
    def process_mouse(*args): return _colorsc.Palette_process_mouse(*args)
    def process_mouse_release(*args): return _colorsc.Palette_process_mouse_release(*args)
    __swig_destroy__ = _colorsc.delete_Palette
    __del__ = lambda self : None;
Palette_swigregister = _colorsc.Palette_swigregister
Palette_swigregister(Palette)

class BrushPreview(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BrushPreview, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BrushPreview, name)
    __repr__ = _swig_repr
    __swig_setmethods__["size"] = _colorsc.BrushPreview_size_set
    __swig_getmethods__["size"] = _colorsc.BrushPreview_size_get
    if _newclass:size = _swig_property(_colorsc.BrushPreview_size_get, _colorsc.BrushPreview_size_set)
    __swig_setmethods__["brush"] = _colorsc.BrushPreview_brush_set
    __swig_getmethods__["brush"] = _colorsc.BrushPreview_brush_get
    if _newclass:brush = _swig_property(_colorsc.BrushPreview_brush_get, _colorsc.BrushPreview_brush_set)
    def __init__(self, *args): 
        this = _colorsc.new_BrushPreview(*args)
        try: self.this.append(this)
        except: self.this = this
    def render(*args): return _colorsc.BrushPreview_render(*args)
    __swig_destroy__ = _colorsc.delete_BrushPreview
    __del__ = lambda self : None;
BrushPreview_swigregister = _colorsc.BrushPreview_swigregister
BrushPreview_swigregister(BrushPreview)



