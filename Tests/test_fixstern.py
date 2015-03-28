from unittest import TestCase
from Objekte.fixstern import Fixstern
from Model.solarSysModel import SolarSunModel
from OpenGL.GLUT import *

__author__ = 'floriandienesch'


class TestFixstern(TestCase):

    def setUp(self):
        glutInit(sys.argv)
        glutCreateWindow("test")

        self.fixstern = Fixstern()
        self.model = SolarSunModel()

    def tearDown(self):
        self.fixstern = None
        self.model = None

    def test_addFixstern(self):
        self.assertEqual(self.fixstern.addFixstern("dd", self.model.rot_mond, 0, 0, 0, 20, 20), None)

    def test_rotation(self):
        self.assertEqual(self.fixstern.rotation(self.model.rot_mond,3,3,3), [3, 0, 0])