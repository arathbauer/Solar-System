__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Mond(object):

    def addMond(self, radius, rot, x, y, z, longitude, latitude):
        """
        Method addMond
        This Method adds a mond to an existing universe
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

            glRotatef(rot[1], 0.0, 1.0, 0.0)

            glTranslatef(3.0, 0.0, 3.0)

            # create a mond
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, radius, longitude, latitude)
        except Exception:
            print("Please enter an integer")


    def rotation(self, rot, x, y, z):
        """
        Method rotation
        This Method rotates an existing mond
        :param rot: roation
        :param x:
        :param y:
        :param z:
        :return:
        """
        rot[1] = rot[1] + y

        return rot
