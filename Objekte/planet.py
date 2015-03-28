# pylint: disable=wildcard-import, unused-wildcard-import, invalid-name, import-error,  missing-docstring
__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Planet(object):

    def addPlanet(self, radius, rot, x, y, z, x2, z2, longitude, latitude):
        """
        Method adPlanet
        This Method adds a planet to an existing universe
        :param radius: size of the planet
        :param rot: roation
        :param x: translation to x
        :param y: --
        :param z: --
        :param x2: to extend the orbit
        :param z2:
        :param longitude: how many vertexes
        :param latitude:
        :return:
        """
        try:
            glLoadIdentity()
            glTranslatef(x, y, z)


            glRotatef(rot[1], 0.0, 1.0, 0.0)

            glTranslatef(x2, 0.0, z2)

            # create a planet
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, radius, longitude, latitude)
        except Exception:
            print("Please enter an integer")


    def rotation(self, rot, x, y, z):
        """
        Method rotation
        This Method rotates an existing planet
        :param rot: roation
        :param x:
        :param y:
        :param z:
        :return:
        """
        rot[1] = rot[1] + y

        return rot
