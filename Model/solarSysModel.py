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

        self.lightStatus = "On"
        self.lightOff = [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]
        self.lightOn = [1, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0.0], [0.0, 0.0, 0.0, 0.0]

        self.quadratic = None

        self.speedEarth = 5
        self.speedMoon = 10

        self.t = Texturen()
        pass