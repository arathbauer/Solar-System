from unittest import TestCase
from Objekte.planet import Planet
from Model.solarSysModel import SolarSunModel
from OpenGL.GLUT import *

__author__ = 'floriandienesch'


class TestPlanet(TestCase):

    def setUp(self):
        glutInit(sys.argv)
        glutCreateWindow("Solarsystem v0.9")

        self.planet = Planet()
        self.model = SolarSunModel()

    def tearDown(self):
        self.planet = None
        self.model = None

    def test_addPlanet(self):
        self.assertEqual(self.planet.addPlanet("dd", self.model.rot_mond, 0, 0, 0, 4, 4, 20, 20), None)

    def test_rotation(self):
        self.assertEqual(self.planet.rotation(self.model.rot_mond,3,3,3), [0, 3, 0])