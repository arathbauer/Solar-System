__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def addMond(radius, rot, x, y, z, longitude, latitude):
    glLoadIdentity()
    glTranslatef(x, y, z)

    glRotatef(rot[1], 0.0, 1.0, 0.0)

    glTranslatef(3.0, 0.0, 3.0)

    # Planet erstellen
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, longitude, latitude)


def rotation(rot, x, y, z):
    rot[1] = rot[1] + y

    return rot