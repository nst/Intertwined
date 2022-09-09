# !/usr/bin/env python3
# Nicolas Seriot
# 2022-07-03

import cairo

from .Segment import *

class Thread:

    # knows only context (pixels) coordinates, not canvas ones
    
    EXT_C = (0,0,0)
    INT_C = (1,1,1)
    
    EXT_W = 16
    INT_W = 12
    
    MAX_DEPTH = 100
    VISUAL_DEBUG = True

    draw_ends = True
            
    def __init__(self, c, o, ext_color, int_color, ext_width, int_width, draw_ends):

        self.EXT_C = ext_color
        self.INT_C = int_color

        self.EXT_W = ext_width
        self.INT_W = int_width

        self.c = c
        self.segments = []
        self.segments_for_depth = []
        self.draw_ends = draw_ends
        
        for i in range(Thread.MAX_DEPTH):
            self.segments_for_depth.append([])

        self.pos = o

    def arc_rel(self, p, z, cp1=None, cp2=None, cp1_length=None):
        assert(z < Thread.MAX_DEPTH)
        self.arc_to(self.pos[0] + p[0], self.pos[1] + p[1], z, cp1, cp2)
        
    def arc_to(self, x, y, z, cp1=None, cp2=None):
        s = Segment(self.pos, (x,y), z, cp1, cp2)
        self.segments.append(s)
        self.segments_for_depth[z].append(s)
        self.pos = (x, y)

    def compute_cps(self):
        
        pcp2 = None # previous segment cp2

        for s in self.segments:
            if not s.cp1:
                s.cp1 = s.compute_cp1(pcp2)
            if not s.cp2:
                s.cp2 = s.compute_cp2()
            pcp2 = s.cp2

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

        if len(self.segments) == 0:
            print("-- %s has no segments to draw for depth %d" % (self, z))
            return

        s0 = self.segments[0]
        sn = self.segments[-1]
        
        if self.draw_ends:
            if s0.z == z:
                self.draw_segment_end(s0.o)

            if sn.z == z:
                self.draw_segment_end(sn.p)
                                    
        for s in self.segments_for_depth[z]:

            # hack: draw several times to soften external antialiasing on segment ends             
            aa =self.c.get_antialias() == cairo.ANTIALIAS_DEFAULT
            ext_repeat = 2 if aa else 1
            int_repeat = 16 if aa else 1

            for i in range(ext_repeat):
                s.draw(self.c, self.EXT_W, self.EXT_C, cairo.LINE_CAP_BUTT)
            
            for i in range(int_repeat):                       
                s.draw(self.c, self.INT_W, self.INT_C, cairo.LINE_CAP_BUTT)
