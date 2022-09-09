# !/usr/bin/env python3
# Nicolas Seriot
# 2022-09-06

# https://www.hardybarn.co.uk/adobe-illustrator-how-to-knitting-illustrations/
# https://math.hws.edu/eck/cs424/notes2013/canvas/bezier.html

import sys
sys.path.append('..')

from Intertwined import *

cv = Canvas(47, 25)
        
v_offset = 6

for row in range(3):

    t = cv.create_thread(o = (1, 10 + (v_offset*row)))
    
    for col in range(3):

        cv.arc_rel(t,  8,  0, 1, cp1=(2, 2), cp2=(-2, 2))
        cv.arc_rel(t, -2, -8, 1, cp2=(-2, 2))
        cv.arc_rel(t,  8,  0, 0, cp2=(-2,-2))
        cv.arc_rel(t, -2,  8, 1, cp2=(-2,-2))
    
    cv.arc_rel(t,  8,  0, 1, cp2=(-2, 2))

cv.draw()

cv.surface.write_to_png("crochet.png")
