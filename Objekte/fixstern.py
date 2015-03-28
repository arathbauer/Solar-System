__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Fixstern(object):

    def addFixstern(self, radius, rot, x, y, z, longitude, latitude):
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
        try:
            glLoadIdentity()
            glTranslatef(x, y, z)

            glRotatef(rot[0], 1.0, 0.0, 0.0)

            glTranslatef(4.0, 0.0, 0.0)

            # create a fixstern
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            return gluSphere(quadric, radius, longitude, latitude)
        except Exception:
            print("Input should be a integer")


    def rotation(self, rot, x, y, z):
        """
        Method rotation
        This Method rotates an existing fixstern
        :param rot: roation
        :param x:
        :param y:
        :param z:
        :return:
        """
        try:
            rot[0] = rot[0] + x
        except Exception:
            print("Please enter an integer")

        return rot