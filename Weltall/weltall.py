__author__ = 'floriandienesch'

from Objekte import planet
from Model.solarSysModel import *
from Objekte.lighting import *
from PyQt5 import QtCore, QtWidgets, QtWidgets, QtGui
import sys, time

# Die "view"-Klasse
# Number of the glut window.
window = 0

class Weltall(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Weltall, self).__init__(parent)
        self.model = SolarSunModel()
        self.lighting = Lighting()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

        # Lighting
        self.lighting.enableLighting()
        self.lighting.addLight(GL_LIGHT0)
        self.lighting.setLight(GL_LIGHT0, self.model.lightOn[0], self.model.lightOn[1],
                               self.model.lightOn[2], self.model.lightOn[3])

        glEnable(GL_COLOR_MATERIAL)
        glClearColor(0.0, 0.0, 0.0, 0.0)


    # The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
    def ReSizeGLScene(self, Width, Height):
        if Height == 0:                  # Prevent A Divide By Zero If The Window Is Too Small
            Height = 1

        glViewport(0, 0, Width, Height)      # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # ACHTUNG!!!
        # 3. Parameter war auf 0.1!!!
        # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)


    def DrawGLScene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   # Clear The Screen And The Depth Buffer
        glLoadIdentity()                    # Reset The Weltall

        self.lighting.render()

        # solarSunControl.addPlanet(radius, rotation, quadratic, licht, x, y, z, longitude, latitude)

        self.quadratic = self.model.t.texturePlanet("sun")
        # Sonne
        planet.addPlanet(1, self.model.rot_sonne, self.quadratic, -4, 0, -12, 20, 20)

        self.quadratic = self.model.t.texturePlanet("earth")
        # Rotation Erde
        planet.rotation(self.model.rot_erde, 0, self.model.speedEarth, 0)
        # Erde erstellen
        planet.addPlanet(1, self.model.rot_erde, self.quadratic, 0, 0, -15, 20, 20)

        self.quadratic = self.model.t.texturePlanet("moon")
        # Rotation Mond
        planet.rotation(self.model.rot_mond, 0, self.model.speedMoon, 0)
        # Mond erstellen
        planet.addPlanet(0.3, self.model.rot_mond, self.quadratic, 0, 0, -12, 20, 20)

        #  since this is double buffered, swap the buffers to display what just got drawn.
        glutSwapBuffers()


    def keyPressed(self, key, x, y):
        # If escape is pressed, kill everything.
        if key == b'l':
            if self.model.lightStatus == "On":
                self.lighting.enableLighting()
                self.lighting.setLight(GL_LIGHT0, self.model.lightOff[0], self.model.lightOff[1],
                    self.model.lightOff[2], self.model.lightOff[3])
                self.model.lightStatus = "Off"

            elif self.model.lightStatus == "Off":
                self.lighting.setLight(GL_LIGHT0, self.model.lightOn[0], self.model.lightOn[1],
                    self.model.lightOn[2], self.model.lightOn[3])
                self.model.lightStatus = "Off2"

            elif self.model.lightStatus == "Off2":
                self.lighting.disableLighting()
                self.model.lightStatus = "On"

        if key == b'd':
            self.model.speedEarth += 1
            self.model.speedMoon += 1

        if key == b'a':
            self.model.speedEarth -= 1
            self.model.speedMoon -= 1

        if key == b's':
            self.model.speedEarth = 0
            self.model.speedMoon = 0

        if key == b'f':
            if self.model.fullscreen == False:
                glutFullScreen()
                self.model.fullscreen = True
            else:
                self.model.fullscreen = False
                glutPositionWindow(0,0)
                glutReshapeWindow(640, 480)

        if key == b't':
            if self.model.textures == True:
                glEnable(GL_TEXTURE_2D)
                self.model.textures = False
            else:
                glDisable(GL_TEXTURE_2D)
                self.model.textures = True

        if key == b'\x1b':
            quit()


    def main(self):
        # Select type of Display mode:
        #  Double buffer
        #  RGBA color
        # Alpha components supported
        # Depth buffer
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

        # get a 640 x 480 window
        glutInitWindowSize(640, 480)

        # the window starts at the upper left corner of the screen
        glutInitWindowPosition(0, 0)

        # Okay, like the C version we retain the window id to use when closing, but for those of you new
        # to Python (like myself), remember this assignment would make the variable local and not global
        # if it weren't for the global declaration at the start of main.
        glutCreateWindow("Solarsystem v0.5")

        # Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
        # set the function pointer and invoke a function to actually register the callback, otherwise it
        # would be very much like the C version of the code.
        glutDisplayFunc(self.DrawGLScene)

        # When we are doing nothing, redraw the scene.
        glutIdleFunc(self.DrawGLScene)

        # Register the function called when our window is resized.
        glutReshapeFunc(self.ReSizeGLScene)

        # Register the function called when the keyboard is pressed.
        glutKeyboardFunc(self.keyPressed)

        # Initialize our window.
        self.InitGL()

        # Start Event Processing Engine
        glutMainLoop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(glutInit(sys.argv))

    splash_pix = QtGui.QPixmap('../Splashscreen2.jpg')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    time.sleep(3)

    start = Weltall()
    splash.finish(start)
    app.exit()
    start.main()