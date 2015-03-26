__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Number of the glut window.
window = 0

def addPlanet(radius, rot, x, y, z, longitude, latitude):
    glLoadIdentity()
    glTranslatef(x, y, z)

    glRotatef(rot[1], 0.0, 1.0, 0.0)

    glTranslatef(4.0, 0.0, 0.0)

    # Planet erstellen
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, longitude, latitude)


def rotation(rot, x, y, z):
    rot[0] = rot[0] + x
    rot[1] = rot[1] + y
    rot[2] = rot[2] + z

    return rot