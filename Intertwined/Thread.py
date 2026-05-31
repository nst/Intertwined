# !/usr/bin/env python3
# Nicolas Seriot
# 2022-07-03

import cairo
import math

from .Segment import *

class Thread:

    # knows only context (pixels) coordinates, not canvas ones

    EXT_C = (0,0,0)
    INT_C = (1,1,1)

    EXT_W = 16
    INT_W = 12

    VISUAL_DEBUG = True

    draw_ends = True

    def __init__(self, c, o, ext_color, int_color, ext_width, int_width, draw_ends):

        self.EXT_C = ext_color
        self.INT_C = int_color

        self.EXT_W = ext_width
        self.INT_W = int_width

        self.c = c
        self.segments = []
        self.draw_ends = draw_ends

        self.pos = o

    def arc_rel(self, p, z, cp1=None, cp2=None, cp1_length=None):
        self.arc_to(self.pos[0] + p[0], self.pos[1] + p[1], z, cp1, cp2)

    def arc_to(self, x, y, z, cp1=None, cp2=None):
        o = self.pos
        p = (x, y)

        # resolve cp1 to absolute
        if cp1 is not None:
            cp1_abs = (o[0] + cp1[0], o[1] + cp1[1])
        elif self.segments:
            # symmetric to previous segment's cp2 around o
            pcp2 = self.segments[-1].cp2
            cp1_abs = (2*o[0] - pcp2[0], 2*o[1] - pcp2[1])
        else:
            cp1_abs = o # 1st segment with no cp1: default_cp2 handles the degeneracy

        # resolve cp2 to absolute (uses the now-final cp1)
        if cp2 is not None:
            cp2_abs = (p[0] + cp2[0], p[1] + cp2[1])
        else:
            cp2_abs = default_cp2(o, p, cp1_abs)

        self.segments.append(Segment(o, p, z, cp1_abs, cp2_abs))
        self.pos = p

    def draw_segment_end(self, p):

        self.c.save()

        line_width = (self.EXT_W - self.INT_W) / 2.

        if self.c.get_antialias() == cairo.ANTIALIAS_DEFAULT:
            line_width = line_width - 0.5

        self.c.set_line_width(line_width)

        self.c.set_source_rgb(*self.INT_C)
        self.c.arc(p[0], p[1], self.EXT_W / 2. - 2, 0, 2*math.pi)
        self.c.fill_preserve()
        self.c.set_source_rgb(*self.EXT_C)
        self.c.stroke()

        self.c.restore()

    def draw_segments_of_depth(self, z):

        if not self.segments:
            return

        s0 = self.segments[0]
        sn = self.segments[-1]

        if self.draw_ends:
            if s0.z == z:
                self.draw_segment_end(s0.o)
            if sn.z == z:
                self.draw_segment_end(sn.p)

        # hack: draw several times to soften external antialiasing on segment ends
        aa = self.c.get_antialias() == cairo.ANTIALIAS_DEFAULT
        ext_repeat = 2 if aa else 1
        int_repeat = 16 if aa else 1

        for s in self.segments:
            if s.z != z:
                continue
            for _ in range(ext_repeat):
                s.draw(self.c, self.EXT_W, self.EXT_C, cairo.LINE_CAP_BUTT)
            for _ in range(int_repeat):
                s.draw(self.c, self.INT_W, self.INT_C, cairo.LINE_CAP_BUTT)
