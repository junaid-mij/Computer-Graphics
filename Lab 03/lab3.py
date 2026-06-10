from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18

show_bresenham = False

def DDA(x1, y1, x2, y2):
    points = []

    start = time.perf_counter_ns()

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    end = time.perf_counter_ns()

    return points, end - start

def Bresenham(x0, y0, x1, y1):
    points = []

    start = time.perf_counter_ns()

    dx = x1 - x0
    dy = y1 - y0

    y = y0
    p = 2 * dy - dx

    for x in range(x0, x1 + 1):
        points.append((x, y))

        if p >= 0:
            y += 1
            p += 2 * dy - 2 * dx
        else:
            p += 2 * dy

    end = time.perf_counter_ns()

    return points, end - start

def drawCircle(cx, cy, r):
    glBegin(GL_POINTS)

    x = 0
    y = r
    p = 3 - 2 * r

    while x <= y:

        pts = [
            (cx+x, cy+y),
            (cx-x, cy+y),
            (cx+x, cy-y),
            (cx-x, cy-y),
            (cx+y, cy+x),
            (cx-y, cy+x),
            (cx+y, cy-x),
            (cx-y, cy-x)
        ]

        for px, py in pts:
            glVertex2i(px, py)

        if p < 0:
            p = p + 4*x + 6
        else:
            p = p + 4*(x-y) + 10
            y -= 1

        x += 1

    glEnd()

def draw_text(x, y, text):
    glRasterPos2f(x, y)

    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def timer(value):
    global show_bresenham
    show_bresenham = True
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    dda_points, dda_time = DDA(100,100,300,300)

    glColor3f(1,0,0)

    glBegin(GL_POINTS)
    for x,y in dda_points:
        glVertex2i(x,y)
    glEnd()

    draw_text(20,570,f"DDA Time: {dda_time} ns")

    if show_bresenham:
        bres_points, bres_time = Bresenham(100,300,300,100)

        glColor3f(0,0,1)

        glBegin(GL_POINTS)
        for x,y in bres_points:
            glVertex2i(x,y)
        glEnd()

        draw_text(20,540,f"Bresenham Time: {bres_time} ns")

    glColor3f(0,1,0)
    drawCircle(250,250,10)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(600,600)

glutCreateWindow(b"Marajul Islam - 28")

glClearColor(1,1,1,1)

gluOrtho2D(0,600,0,600)

glutDisplayFunc(display)

glutTimerFunc(3000, timer, 0)

glutMainLoop()