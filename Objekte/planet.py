__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def addPlanet(radius, rot, x, y, z, x2, z2, longitude, latitude):
    glLoadIdentity()
    glTranslatef(x, y, z)

    glRotatef(rot[1], 0.0, 1.0, 0.0)

    glTranslatef(x2, 0.0, z2)

    # Planet erstellen
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, longitude, latitude)


def rotation(rot, x, y, z):
    rot[1] = rot[1] + y

    return rot