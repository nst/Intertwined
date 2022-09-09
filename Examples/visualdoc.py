# !/usr/bin/env python3
# Nicolas Seriot
# 2022-09-06

import sys
sys.path.append('..')

from Intertwined import *

def cp_none():
    
    cv = Canvas(10, 8, col_size=20, row_size=20)
    t = cv.create_thread(o = (1,2))
    cv.arc_rel(t, 5, -1, 1)
    cv.arc_rel(t, 2, 5, 1)
    cv.draw(draw_grid=True, draw_cp=True)
    cv.surface.write_to_png("vd_cp_none.png")

def cp_cp1():
    
    cv = Canvas(10, 8, col_size=20, row_size=20)
    t = cv.create_thread(o = (1,2))
    cv.arc_rel(t, 5, -1, 1, cp1=(1,-2))
    cv.arc_rel(t, 2, 5, 1)
    cv.draw(draw_grid=True, draw_cp=True)
    cv.surface.write_to_png("vd_cp1.png")

def cp_cp2():
    
    cv = Canvas(10, 8, col_size=20, row_size=20)
    t = cv.create_thread(o = (1,2))
    cv.arc_rel(t, 5, -1, 1, cp2=(0,-2))
    cv.arc_rel(t, 2, 5, 1)
    cv.draw(draw_grid=True, draw_cp=True)
    cv.surface.write_to_png("vd_cp2.png")

def cp_cp1_cp2():
    
    cv = Canvas(10, 8, col_size=20, row_size=20)
    t = cv.create_thread(o = (1,2))
    cv.arc_rel(t, 5, -1, 1, cp1=(1,-2), cp2=(0,-2))
    cv.arc_rel(t, 2, 5, 1)
    cv.draw(draw_grid=True, draw_cp=True)
    cv.surface.write_to_png("vd_cp1_cp2.png")

def fill_canvas(cv):
    
    t = cv.create_thread(o = (3,1))

    cv.arc_rel(t, 2, 5, 1, cp1=(-1,1), cp2=(-2,-1))
    cv.arc_rel(t, 2, -3, 1, cp2=(2,1))
    cv.arc_rel(t, -6, 2, 0, cp2=(0,-1))

    return cv

def draw_grid():

    cv = Canvas(10, 8, col_size=20, row_size=20)
    cv = fill_canvas(cv)
    cv.draw(draw_grid=True)
    cv.surface.write_to_png("vd_draw_grid.png")

def stretch_grid():

    cv = Canvas(10, 8, col_size=20, row_size=30)
    cv = fill_canvas(cv)
    cv.draw(draw_grid=True)
    cv.surface.write_to_png("vd_stretch_grid.png")

def draw_control_points():

    cv = Canvas(10, 8, col_size=20, row_size=20)
    cv = fill_canvas(cv)
    cv.draw(draw_cp=True)
    cv.surface.write_to_png("vd_draw_cp.png")

def draw_points():

    cv = Canvas(10, 8, col_size=20, row_size=20)
    cv = fill_canvas(cv)
    cv.draw(draw_points=True)
    cv.surface.write_to_png("vd_draw_points.png")

def draw_depth():

    cv = Canvas(10, 8, col_size=20, row_size=20)
    cv = fill_canvas(cv)
    cv.draw(draw_depth=True)
    cv.surface.write_to_png("vd_draw_depth.png")

def draw_all():

    cv = Canvas(10, 8, col_size=20, row_size=20)
    cv = fill_canvas(cv)
    cv.draw(draw_grid=True, draw_points=True, draw_cp=True, draw_depth=True)
    cv.surface.write_to_png("vd_draw_all.png")

if __name__ == "__main__":

    draw_grid()

    stretch_grid()

    draw_control_points()

    draw_points()

    draw_depth()

    draw_all()

    cp_none()
    cp_cp1()
    cp_cp2()
    cp_cp1_cp2()