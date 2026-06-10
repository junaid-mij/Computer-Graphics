from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_pixel(x, y):
    glVertex2i(int(x), int(y))

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):
        draw_pixel(round(x), round(y))
        x += x_inc
        y += y_inc

def Bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        draw_pixel(x1, y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_POINTS)

    DDA(100, 100, 300, 300)
    Bresenham(300, 100, 100, 300)

    glEnd()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)

glutCreateWindow(b"Marajul Islam - 28")

glClearColor(0.0, 0.0, 0.0, 1.0)

gluOrtho2D(0, 500, 0, 500)

glutDisplayFunc(display)
glutMainLoop()