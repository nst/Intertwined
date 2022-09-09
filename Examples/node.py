# !/usr/bin/env python3
# Nicolas Seriot
# 2022-09-06

# https://ucsdnews.ucsd.edu/archive/newsrel/science/12-07NYTTopScienceStories2007.html
# https://ucsdnews.ucsd.edu/archive/graphics/images/2007/10-07PNAS4BIG.jpg

import sys
sys.path.append('..')

from Intertwined import *

def draw():

    cv = Canvas(16, 19)

    #cv.draw_grid()
    
    t = cv.create_thread(o = (1,1), draw_ends = False)
    
    cv.arc_to(t, 9, 4, 1, cp1=(2,-3), cp2=(-3,-3))
    cv.arc_to(t, 13, 12, 0, cp2=(1, -3))
    cv.arc_to(t, 7, 15, 1, cp2=(3, 0))
    cv.arc_to(t, 1, 12, 0, cp2=(1, 3))
    cv.arc_to(t, 5, 4, 1, cp2=(-3, 3))
    cv.arc_to(t, 13, 1, 0, cp2=(-2, -3))
    cv.arc_to(t, 9, 8, 1, cp2=(3,-3))
    cv.arc_to(t, 5, 12, 0, cp2=(3, -3))
    cv.arc_to(t, 7, 18, 1, cp2=(-3, 0))
    cv.arc_to(t, 9, 12, 0, cp2=(3, 3))
    cv.arc_to(t, 5, 8, 1, cp2=(3, 3))
    cv.arc_to(t, 1, 1, 0, cp2=(-2, 3))
    
    # col 1 | 5 | 7 | 9 | 13
    
    # row 1 | 4 | 8 | 12 | 15 | 18
    
    cv.draw(draw_cp=True, draw_depth=True)
    
    cv.surface.write_to_png("node.png")

draw()
