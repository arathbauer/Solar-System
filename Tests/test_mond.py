from unittest import TestCase
from Objekte.mond import Mond
from Model.solarSysModel import SolarSunModel
from OpenGL.GLUT import *

__author__ = 'floriandienesch'


class TestMond(TestCase):

    def setUp(self):
        glutInit(sys.argv)
        glutCreateWindow("Solarsystem v0.9")

        self.mond = Mond()
        self.model = SolarSunModel()

    def test_addMond(self):
        self.assertEqual(self.mond.addMond("dd", self.model.rot_mond, 0, 0, 0, 20, 20), None)

    def test_rotation(self):
        self.assertEqual(self.mond.rotation(self.model.rot_mond,3,3,3), [0, 3, 0])