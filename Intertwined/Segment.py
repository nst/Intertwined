import cairo
import math

class Segment:

    def __init__(self, o, p, z, cp1=None, cp2=None):

        if cp2 == None:
            pass

        self.o = o # origin
        self.p = p # point
        self.z = z # z-depth
        self.cp1 = (o[0] + cp1[0], o[1] + cp1[1]) if cp1 else None
        self.cp2 = (p[0] + cp2[0], p[1] + cp2[1]) if cp2 else None
        
    def norm(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def compute_cp2(self):
    
        # from p towards cp1, same length as o_cp1

        v = ((self.cp1[0] - self.p[0]), (self.cp1[1] - self.p[1])) # from cp1 to p
        #v = ((self.o[0] - self.p[0]), (self.o[1] - self.p[1])) # another way to compute cp2

        length = self.norm(self.o, self.cp1)

        if length < 0.0001: # eg. for 1st segment, when cp1 is not set
            length = self.norm(self.o, self.p) / 2. # pure heuristic..

        v_norm = math.sqrt(v[0]**2 + v[1]**2)
        
        ratio = v_norm / length
        
        (dx, dy) = (v[0]/ratio, v[1]/ratio)
        
        return (self.p[0] + dx, self.p[1] + dy)

    def compute_cp1(self, pcp2):

        # symetric to previous segement cp2, aka pcp2, around segment origin

        if pcp2:
            dx = (self.o[0] - pcp2[0])
            dy = (self.o[1] - pcp2[1])
        else:
            dx = 0
            dy = 0

        return (self.o[0] + dx, self.o[1] + dy)

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

        #print("----- o cp1 cp2 p", self.o, self.cp1, self.cp2, self.p)

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
