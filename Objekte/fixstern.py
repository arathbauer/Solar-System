__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def addFixstern(radius, rot, x, y, z, longitude, latitude):
    """
    Method addFixstern
    This Method adds a fixstern to an existing universe
    :param radius: size of the planet
    :param rot: roation
    :param x: translation to x
    :param y: --
    :param z: --
    :param longitude: how many vertexes
    :param latitude:
    :return:
    """
    glLoadIdentity()
    glTranslatef(x, y, z)

    glRotatef(rot[0], 1.0, 0.0, 0.0)

    glTranslatef(4.0, 0.0, 0.0)

    # create a fixstern
    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, longitude, latitude)


def rotation(rot, x, y, z):
    """
    Method rotation
    This Method rotates an existing fixstern
    :param rot: roation
    :param x:
    :param y:
    :param z:
    :return:
    """
    rot[0] = rot[0] + x

    return rot