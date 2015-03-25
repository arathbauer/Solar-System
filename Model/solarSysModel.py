__author__ = 'floriandienesch'

from Objekte.texturen import *

class SolarSunModel:

    def __init__(self):
        #Sonne
        self.rot_erde = [0, 0, 0]
        # Erde
        self.rot_sonne = [0, 0, 0]
        # Mond
        self.rot_mond = [0, 0, 0]
        # Jupiter
        self.rot_jupiter = [0, 0, 0]

        self.lightStatus = "On"
        self.lightOff = [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]
        self.lightOn = [0, 0, -1.3, 0.1], [255, 255, 255, 255], [0, 0, 0, 0.0], [0.0, 0.0, 0.0, 0.0]

        self.quadratic = None

        self.speedEarth = 5
        self.speedMoon = 5
        self.speedSun = 0.1
        self.speedJupiter = 2

        self.fullscreen = False
        self.textures = False

        self.zoom = 45

        self.width = 640
        self.height = 480

        self.t = Texturen()
        pass