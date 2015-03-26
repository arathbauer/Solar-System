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

        self.speedEarth = 3
        self.speedMoon = 3
        self.speedSun = 0.2
        self.speedJupiter = 1

        self.fullscreen = False
        self.textures = False

        self.zoom = 45

        self.width = 640
        self.height = 480

        self.file = [0,1,2,3,4,5,6,7,8,9,10]
        self.file[0] = "./texture_moon.png"
        self.file[1] = "./texutre_earth.jpg"
        self.file[2] = "./texture_sun.jpg"
        self.file[3] = "./texture_jupiter.jpg"
        self.fileSet = False

        self.t = Texturen()
        pass