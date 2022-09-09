# !/usr/bin/env python3
# Nicolas Seriot
# 2022-09-06

# https://www.hardybarn.co.uk/adobe-illustrator-how-to-knitting-illustrations/
# https://math.hws.edu/eck/cs424/notes2013/canvas/bezier.html

import sys
sys.path.append('..')

from Intertwined import *

import math

c1 = (170/255., 170/255., 249/255.)
c2 = (243/255., 174/255., 234/255.)
c3 = (251/255., 231/255., 142/255.)

def draw_knot_1(cv):

    t1 = cv.create_thread(o = (4,0),
                         int_color = c1)

    cv.arc_rel(t1, -1, 9, 0, cp2=(1,-2), cp1=(0,2))

    cv.arc_rel(t1, -2,  6,  1, cp2=(-2, -2))
    cv.arc_rel(t1,  8,  0,  0, cp2=(-2, 2))
    cv.arc_rel(t1, -2,  -6,  1, cp2=(1, 2))
    cv.arc_rel(t1, -1, -9, 0, cp2=(0, 2))

    t2 = cv.create_thread(o = (4,20),
                         ext_color = (0,0,0),
                         int_color = c2,
                         ext_width = 24,
                         int_width = 18)

    cv.arc_rel(t2, -1, -9, 1, cp2=(1,2), cp1=(0,-2))

    cv.arc_rel(t2, -2,  -6, 0, cp2=(-2, 2))
    cv.arc_rel(t2,  8,  0,  1, cp2=(-2, -2))
    cv.arc_rel(t2, -2,  6,  0, cp2=(1, -2))
    cv.arc_rel(t2, -1, 9, 1, cp2=(0, -2))
    
def draw_knot_2(cv):
    
    t1 = cv.create_thread(o = (4,0),
                         int_color = c1)

    cv.arc_rel(t1, -1, 9, 1, cp2=(1,-2), cp1=(0,2))

    cv.arc_rel(t1, -2,  6,  1, cp2=(-2, -2))
    cv.arc_rel(t1,  8,  0,  1, cp2=(-2, 2))
    cv.arc_rel(t1, -2,  -6,  3, cp2=(1, 2))
    cv.arc_rel(t1, -1, -9, 1, cp2=(0, 2))
    
    t2 = cv.create_thread(o = (1,20),
                         ext_color = (0,0,0),
                         int_color = c2,
                         ext_width = 24,
                         int_width = 18)

    cv.arc_rel(t2, 3, -6, 0, cp2=(-1,2), cp1=(0,-2))

    cv.arc_rel(t2, 5,  -9, 2, cp2=(2, 2))
    cv.arc_rel(t2, -8,  -0, 1, cp2=(2, -2))
    cv.arc_rel(t2,  3,  7,  0, cp2=(-2, -3))
    cv.arc_rel(t2, 5,  8,  1, cp2=(0, -2))
    
    cv.draw()

def draw_knot_3(cv):

    sq = 2.2
    
    t1 = cv.create_thread(o = (4,0),
                         int_color = c3)

    cv.arc_rel(t1, 4, 4, 1, cp1=(sq,0), cp2=(0,-sq))

    cv.arc_rel(t1, -4,  4,  1, cp2=(sq, 0))
    cv.arc_rel(t1, -4, -4,  1, cp2=(0, sq))
    cv.arc_rel(t1, 4,  -4,  1, cp2=(-sq, 0))
    
    t2 = cv.create_thread(o = (0,18),
                         ext_color = (0,0,0),
                         int_color = c2,
                         ext_width = 24,
                         int_width = 18)

    cv.arc_rel(t2, 4, -3, 0, cp1=(0,-2), cp2=(-2,0))

    cv.arc_rel(t2, 4, 2, 2, cp2=(0,-2))
    cv.arc_rel(t2, -5, 0, 1, cp2=(1,2))
    cv.arc_rel(t2, 0, -6, 1, cp2=(-1,2))
    cv.arc_rel(t2, 5, 1, 0, cp2=(0,-2))
    cv.arc_rel(t2, -4, 1, 2, cp2=(2,0))
    cv.arc_rel(t2, -3, -3, 0, cp2=(0,2))
    cv.arc_rel(t2, 4, -4, 0, cp2=(-2,-2))
    cv.arc_rel(t2, 0, 14, 1, cp2=(0,-2))
    
    cv.draw()
   
def draw_knots():

    cv = Canvas(38, 21)
    
    #cv.draw_grid()
    
    draw_knot_1(cv)

    cv.draw()
    cv.clear_context()

    cv.c.translate(280, 0)

    draw_knot_2(cv)

    cv.draw()
    cv.clear_context()

    cv.c.translate(280*2, 0)

    draw_knot_3(cv)
    
    cv.surface.write_to_png("knots.png")

draw_knots()
