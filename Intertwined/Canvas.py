# !/usr/bin/env python3
# Nicolas Seriot
# 2022-08-30

import cairo

from .Thread import *

def hexcolor(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i+2], 16) / 255. for i in (0, 2, 4))

class Canvas:
    
    MARGIN = 50

    DEFAULT_PALETTE = [(170/255., 170/255., 249/255.),
                       (243/255., 174/255., 234/255.),
                       (251/255., 231/255., 142/255.)]

    def clear_context(self):
        self.c = cairo.Context(self.surface)
        self.c.translate(self.MARGIN, self.MARGIN)
        self.threads = []

    def __init__(self, NB_COLS, NB_ROWS, background_color=(1,1,1), col_size=20, row_size=20, palette=DEFAULT_PALETTE):
        
        self.palette = palette
        self.threads = []
        
        self.RS = row_size
        self.CS = col_size
        
        self.NB_ROWS = NB_ROWS
        self.NB_COLS = NB_COLS
        
        W = self.NB_COLS * self.CS + self.MARGIN*2
        H = self.NB_ROWS * self.RS + self.MARGIN*2
        
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
        self.c = cairo.Context(self.surface)
        
        self.c.set_source_rgb(*background_color)
        self.c.paint()
        
        self.c.translate(self.MARGIN, self.MARGIN)

    def draw(self, draw_grid=False, draw_points=False, draw_cp=False, draw_depth=False):

        if draw_grid:
            self.draw_grid()

        for t in self.threads:
            t.compute_cps()
        
        Z=Thread.MAX_DEPTH-1 # limit drawing to some depth
        for z in range(Z+1):
            for t in self.threads:
                t.draw_segments_of_depth(z)
        
        for t in self.threads:
            for z in range(Z+1):
                for s in t.segments_for_depth[z]:
                    if draw_points:
                        s.debug_draw_point(self.c, s.o, (1,1,1))    
                        s.debug_draw_point(self.c, s.p, (1,1,1))
                    if draw_cp:
                        s.debug_draw_lines(self.c)
                        s.debug_draw_point(self.c, s.o, (1,1,1))    
                        s.debug_draw_point(self.c, s.p, (1,1,1))
                        s.debug_draw_point(self.c, s.cp1, (1,0,0)) 
                        s.debug_draw_point(self.c, s.cp2, (0,1,0))
            for s in t.segments:
                if draw_depth and z <= Z:
                    s.debug_write_point(self.c, s.o, "%d" % s.z) 
    
    def draw_grid(self, color=(0,0,0)):
    
        self.c.save()
    
        self.c.set_line_width(1)

        self.c.set_source_rgb(*color)
    
        for i in range(self.NB_ROWS+1):
            self.c.move_to(0, i*self.RS)
            self.c.rel_line_to(self.NB_COLS * self.CS, 0)

        for i in range(self.NB_COLS+1):
            self.c.move_to(i*self.CS, 0)
            self.c.rel_line_to(0, self.NB_ROWS * self.RS)

        self.c.stroke()
        
        self.c.restore()

    def canvas_to_surface(self, p, add_half_offset=False):
        if not p:
            return None
        
        x = p[0] * self.CS + (self.CS/2. if add_half_offset else 0)
        y = p[1] * self.RS + (self.RS/2. if add_half_offset else 0)
        return (x, y)

    def create_thread(self, o, ext_color=(0,0,0), int_color=None, ext_width=24, int_width=18, draw_ends=True):

        if not ext_color:
            ext_color = (0,0,0)
        
        if not int_color:
            int_color = self.palette[len(self.threads) % len(self.palette)]

        t = Thread(self.c,
            self.canvas_to_surface(o, add_half_offset=True),
            ext_color, int_color, ext_width, int_width,
            draw_ends)

        self.threads.append(t)
        return t
    
    def arc_to(self, t, col, row, z, cp1=None, cp2=None):
        p_s = self.canvas_to_surface((col, row), add_half_offset=True)
        cp2_s = self.canvas_to_surface(cp2)
        cp1_s = self.canvas_to_surface(cp1)
        t.arc_to(p_s[0], p_s[1], z, cp1_s, cp2_s)

    def arc_rel(self, t, col, row, z, cp1=None, cp2=None):
        p_s = self.canvas_to_surface((col, row))
        cp2_s = self.canvas_to_surface(cp2)
        cp1_s = self.canvas_to_surface(cp1)
        t.arc_rel(p_s, z, cp1_s, cp2_s)
