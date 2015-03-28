__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def addFixstern(radius, rot, x, y, z, longitude, latitude):
    glLoadIdentity()
    glTranslatef(x, y, z)

    glRotatef(rot[0], 1.0, 0.0, 0.0)

    glTranslatef(4.0, 0.0, 0.0)

    # Planet erstellen
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, longitude, latitude)


def rotation(rot, x, y, z):
    rot[0] = rot[0] + x

    return rot