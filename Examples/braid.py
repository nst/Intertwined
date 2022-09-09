# !/usr/bin/env python3
# Nicolas Seriot
# 2022-09-06

import sys
sys.path.append('..')

from Intertwined import *

def draw_1():

    cv = Canvas(7, 15, col_size=20, row_size=30)
    
    #cv.c.set_antialias(cairo.ANTIALIAS_NONE)

    cv.draw_grid()

    t1 = cv.create_thread(o = (1,0))

    t2 = cv.create_thread(o = (3,0))

    t3 = cv.create_thread(o = (5,0))

    cv.arc_rel(t1, 0, 1, 1, cp2=(0,-1))
    cv.arc_rel(t2, 0, 1, 1, cp2=(0,-1))
    cv.arc_rel(t3, 0, 1, 1, cp2=(0,-1))

    R = 2
    for i in range(R):

        cv.arc_rel(t1,   4,  2, 1, cp2=(0, -1))
        cv.arc_rel(t1,  -4,  4, 4, cp2=(0, -1))

        cv.arc_rel(t2,  -2,  2, 0, cp2=(0, -1))
        cv.arc_rel(t2,   4,  2, 3, cp2=(0, -1))

        cp2x = 4/3. if i != (R-1) else 0
        cv.arc_rel(t2,  -2,  2, 5, cp2=(cp2x, -1))

        cv.arc_rel(t3,  -4,  4, 2, cp2=(0, -1))
        cv.arc_rel(t3,   4,  2, 4, cp2=(0, -1))

    cv.arc_rel(t1, 0, 1, 1, cp2=(0, -1))
    cv.arc_rel(t2, 0, 1, 5, cp2=(0, -1))
    cv.arc_rel(t3, 0, 1, 4, cp2=(0, -1))
    
    cv.draw()
    
    cv.surface.write_to_png("braid.png")

draw_1()
