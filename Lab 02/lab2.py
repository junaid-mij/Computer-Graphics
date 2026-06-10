from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()
    glOrtho(0, 600, 0, 600, -1, 1)

    # Green Square
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(50, 50)
    glVertex2f(150, 50)
    glVertex2f(150, 150)
    glVertex2f(50, 150)
    glEnd()

    # Purple Triangle
    glColor3f(0.6, 0.0, 0.8)
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 400)
    glVertex2f(550, 400)
    glVertex2f(475, 550)
    glEnd()

    # Rectangle using two triangles
    glColor3f(0, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2f(50, 400)
    glVertex2f(250, 400)
    glVertex2f(250, 550)
    glEnd()

    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(50, 400)
    glVertex2f(50, 550)
    glVertex2f(250, 550)
    glEnd()

    # Orange Pentagon
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(450, 80)
    glVertex2f(500, 120)
    glVertex2f(480, 180)
    glVertex2f(420, 180)
    glVertex2f(400, 120)
    glEnd()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(600, 600)

glutCreateWindow(b"Marajul Islam - 28")

glClearColor(0, 0, 0, 1)

glutDisplayFunc(display)
glutMainLoop()