# pylint: disable=wildcard-import, invalid-name, import-error, too-many-instance-attributes, too-few-public-methods, undefined-variable, missing-docstring
__author__ = 'floriandienesch'
"""
This class saves various values of variables
"""

from Objekte.texturen import *

class SolarSunModel(object):
    """
    Class SolarSunModel
    This class saves various values of variables
    """

    def __init__(self):
        """
        Constructor
        """
        # rotation of the earth
        self.rot_erde = [0, 0, 0]
        # rotation of the sun
        self.rot_sonne = [0, 0, 0]
        # rotation of the moon
        self.rot_mond = [0, 0, 0]
        # rotation of the jupiter
        self.rot_jupiter = [0, 0, 0]

        # light status
        self.lightStatus = "On"
        self.lightOff = [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], \
                        [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]
        self.lightOn = [0, 0, -1.3, 0.1], [255, 255, 255, 255], \
                       [0, 0, 0, 0.0], [0.0, 0.0, 0.0, 0.0]

        # speed of the planets
        self.speedEarth = 2
        self.speedMoon = 2
        self.speedSun = 0.2
        self.speedJupiter = 0.5

        self.fullscreen = False
        self.textures = False

        # zoom level
        self.zoom = 45

        # width and height of the window
        self.width = 640
        self.height = 480

        # texture files
        self.file = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.file[0] = "./texture_moon.png"
        self.file[1] = "./texture_earth_2.jpg"
        self.file[2] = "./texture_sun.jpg"
        self.file[3] = "./texture_jupiter.jpg"
        self.fileSet = False

        # camera perspective
        self.perspective = 0

        self.t = Texturen()
