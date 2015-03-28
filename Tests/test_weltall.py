from unittest import TestCase
from Weltall.weltall import Weltall
from Model.solarSysModel import SolarSunModel
from Objekte.planet import Planet
from OpenGL.GLUT import *

__author__ = 'floriandienesch'


class TestWeltall(TestCase):

    def setUp(self):
        glutInit(sys.argv)
        glutCreateWindow("Solarsystem v0.9")

        self.weltall = Weltall
        self.planet = Planet()
        self.model = SolarSunModel()

    def tearDown(self):
        self.weltall = None
        self.planet = None
        self.model = None

    def test_reSizeGLScene(self):
        self.assertEqual(self.weltall.reSizeGLScene("d", 200, 200), None)