import cairo
import math


def default_cp2(o, p, cp1):
    # from p toward cp1, with length |o-cp1| (falls back to half |o-p| when |o-cp1|~0)

    v = (cp1[0] - p[0], cp1[1] - p[1]) # from p to cp1
    length = math.hypot(o[0]-cp1[0], o[1]-cp1[1])

    if length < 0.0001: # eg. 1st segment when cp1 falls back to o
        length = math.hypot(o[0]-p[0], o[1]-p[1]) / 2.

    v_norm = math.hypot(v[0], v[1])

    if v_norm < 0.0001 or length < 0.0001:
        return p

    ratio = length / v_norm
    return (p[0] + v[0]*ratio, p[1] + v[1]*ratio)


class Segment:

    def __init__(self, o, p, z, cp1, cp2):
        self.o = o     # origin (absolute pixel coords)
        self.p = p     # endpoint (absolute pixel coords)
        self.z = z     # z-depth
        self.cp1 = cp1 # absolute pixel coords
        self.cp2 = cp2 # absolute pixel coords

    def draw(self, ctx, width, color, line_cap):

        ctx.save()

        ctx.set_line_cap(line_cap)
        ctx.set_line_width(width)
        ctx.set_source_rgb(*color)

        ctx.move_to(*self.o)
        ctx.curve_to(self.cp1[0], self.cp1[1], self.cp2[0], self.cp2[1], *self.p)
        ctx.stroke()

        ctx.restore()

    def debug_draw_lines(self, ctx):

        ctx.save()

        ctx.set_antialias(cairo.ANTIALIAS_DEFAULT)
        ctx.set_line_width(1)
        ctx.set_source_rgb(0,0,0)

        ctx.move_to(*self.o)
        ctx.line_to(*self.cp1)

        ctx.move_to(*self.cp2)
        ctx.line_to(*self.p)

        ctx.stroke()

        ctx.restore()

    def debug_write_point(self, ctx, p, s):

        ctx.save()

        ctx.set_antialias(cairo.ANTIALIAS_NONE)

        ctx.set_line_width(1)
        ctx.set_source_rgb(1,1,1)
        ctx.rectangle(p[0]-8, p[1]-8, 16, 16)
        ctx.fill_preserve()
        ctx.set_source_rgb(0,0,0)
        ctx.stroke()

        ctx.select_font_face("Courier New")
        ctx.set_font_size(14)

        fo = cairo.FontOptions()
        fo.set_antialias(cairo.ANTIALIAS_NONE)
        ctx.set_font_options(fo)

        ctx.move_to(p[0]-5, p[1]+4)
        ctx.show_text(s)

        ctx.restore()

    def debug_draw_point(self, ctx, p, color):

        ctx.save()

        ctx.set_source_rgb(*color)
        ctx.arc(p[0], p[1], 5, 0, 2*math.pi)
        ctx.fill()
        ctx.arc(p[0], p[1], 5, 0, 2*math.pi)
        ctx.set_source_rgb(0,0,0)
        ctx.stroke()

        ctx.restore()
