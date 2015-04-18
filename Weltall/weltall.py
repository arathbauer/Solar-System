# pylint: disable=import-error, wildcard-import, invalid-name, undefined-variable, no-member, attribute-defined-outside-init
__author__ = 'floriandienesch'

from Objekte import planet, fixstern, mond
from Model.solarSysModel import *
from Objekte.lighting import Lighting
from PyQt5 import QtCore, QtWidgets, QtGui
from Objekte.planet import Planet
from Objekte.mond import Mond
from Objekte.fixstern import Fixstern
import time

class Weltall(QtWidgets.QWidget):
    """
    This class is our universe.
    We can display here our planets, stars or our moon
    """

    def __init__(self, parent=None):
        """
        Constructor
        Initialize the variables
        """
        QtWidgets.QWidget.__init__(self)
        self.model = SolarSunModel()
        self.lighting = Lighting()
        self.planet = Planet()
        self.mond = Mond()
        self.fixstern = Fixstern()

    def InitGL(self):
        """
        Method InitGL
        This Method initializes our Solar System
        It sets the lighting and enables or rather sets the textures
        """
        # make the objects transparent
        glEnable(GL_DEPTH_TEST)
        # enable texturing
        glEnable(GL_TEXTURE_2D)

        # enable lighting
        self.lighting.enableLighting()
        # add a new light
        self.lighting.addLight(GL_LIGHT0)

        # set the position of the light to the sun
        self.lighting.setLight(GL_LIGHT0, self.model.lightOn[0], self.model.lightOn[1],
                               self.model.lightOn[2], self.model.lightOn[3])

        # set the textures when starting the program
        if self.model.fileSet == False:
            try:
                self.imageIDMoon = self.model.t.textureOrbit(self.model.file[0])
                self.imageIDEarth = self.model.t.textureOrbit(self.model.file[1])
                self.imageIDSun = self.model.t.textureOrbit(self.model.file[2])
                self.imageIDJupiter = self.model.t.textureOrbit(self.model.file[3])
            except:
                print("Can't find the textures!")
        # load the textures which are assigned by the user
        else:
            self.imageIDMoon = self.model.t.textureOrbit(self.model.file[0][0])
            self.imageIDEarth = self.model.t.textureOrbit(self.model.file[1][0])
            self.imageIDSun = self.model.t.textureOrbit(self.model.file[2][0])
            self.imageIDJupiter = self.model.t.textureOrbit(self.model.file[3][0])


        # open the help window
        self.help()

        # set color of the back of the planet not to black
        glEnable(GL_COLOR_MATERIAL)
        # set the Backgroundcolor
        glClearColor(0.0, 0.0, 0.0, 0.0)

    def reSizeGLScene(self, width, height):
        """
        Method reSizeGLScene
        This function is called automatically by pyopengl when the window is resized
        :param width: width of the window
        :param height: height of the window
        """
        # prevent A Divide By Zero If The Window Is Too Small
        try:
            if height == 0:
                height = 1

            # reset The Current Viewport And Perspective Transformation
            glViewport(0, 0, width, height)

            # save the values of the current width and height
            self.model.width = width
            self.model.height = height
        except Exception:
            print("Please enter an integer")


    def drawGLScene(self):
        """
        Method drawGLScene
        This Function is called automatically by opengl
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.model.zoom, float(self.model.width)/ float(self.model.height), 1, 110.0)

        if self.model.perspective == 1:
            gluLookAt(0, 8, 4, 0, 6, 0, 0, 1, 0)

        glMatrixMode(GL_MODELVIEW)
        # clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # reset The Weltall
        glLoadIdentity()

        # renders the light
        self.lighting.render()

        # bind the sun texture in our buffer
        glBindTexture(GL_TEXTURE_2D, self.imageIDSun[2])
        self.lighting.disableLighting()
        # rotate the sun
        self.fixstern.rotation(self.model.rot_sonne, self.model.speedSun, 0, 0)
        # add the sun to our solar system
        self.fixstern.addFixstern(1, self.model.rot_sonne, -4, 0, -12, 40, 20)
        self.lighting.enableLighting()

        # bind the earth texture in our buffer
        glBindTexture(GL_TEXTURE_2D, self.imageIDEarth[2])
        # rotate the earth
        self.planet.rotation(self.model.rot_erde, 0, self.model.speedEarth, 0)
        # add the earth to our solar system
        self.planet.addPlanet(0.8, self.model.rot_erde, 0, 0, -15, 3.0, 3.0, 20, 20)

        glBindTexture(GL_TEXTURE_2D, self.imageIDMoon[2])
        self.mond.rotation(self.model.rot_mond, 0, self.model.speedMoon, 0)
        self.mond.addMond(0.2, self.model.rot_mond, 0, 0, -12, 20, 20)

        glBindTexture(GL_TEXTURE_2D, self.imageIDJupiter[2])
        self.planet.rotation(self.model.rot_jupiter, 0, self.model.speedJupiter, 0)
        self.planet.addPlanet(1, self.model.rot_jupiter, 0, 0, -15, 6.0, 6.0, 20, 20)

        # limit our FPS to 60 FPS
        time.sleep(1 / float(60))

        # since this is double buffered, swap the buffers to display what just got drawn.
        glutSwapBuffers()

    def mousePressed(self, button, state, x, y):
        """
        Method mousePressed
        This function is called when the user clicks the left or
        right mouse button
        :param button: left or right button
        :param state: fire the event on mouse-up or mouse-down
        :param x: x-Coordinate of the mouse
        :param y: y-Coordinate of the mouse
        """
        # when the left mouse is pressed down
        if state == GLUT_DOWN and button == GLUT_LEFT_BUTTON:
            # if the light is already on, turn it off
            if self.model.lightStatus == "On":
                self.lighting.enableLighting()
                self.lighting.setLight(GL_LIGHT0, self.model.lightOff[0], self.model.lightOff[1],
                    self.model.lightOff[2], self.model.lightOff[3])
                self.model.lightStatus = "Off"

            # if the light is already off, turn it off2
            elif self.model.lightStatus == "Off":
                self.lighting.setLight(GL_LIGHT0, self.model.lightOn[0], self.model.lightOn[1],
                                       self.model.lightOn[2], self.model.lightOn[3])
                self.model.lightStatus = "Off2"

            # if the light is already off, turn it on
            elif self.model.lightStatus == "Off2":
                self.lighting.disableLighting()
                self.model.lightStatus = "On"

        # if the right button is pressed down
        if state == GLUT_DOWN and button == GLUT_RIGHT_BUTTON:
            # turn the textures on
            if self.model.textures == True:
                glEnable(GL_TEXTURE_2D)
                self.model.textures = False
            # turn the textures off
            else:
                glDisable(GL_TEXTURE_2D)
                self.model.textures = True

    def help(self):
        """
        Method help
        This displays an extern window with the description of the controls
        """
        self.setGeometry(300, 300, 300, 330)
        self.setWindowTitle('Solarsystem Help')
        self.setToolTip('This is the <i>Help</i> of the <i>controls</i> ')
        self.setMaximumSize(300, 330)
        self.move(650, 0)
        self.edit = QtWidgets.QTextEdit()
        self.edit.setEnabled(False)
        self.edit.append('<h1>Controls</h1>'
                         '<b><i>Mouse controls:</i></b>'
                         '<br>Turn light on/ off: <b>Left mouse click</b>'
                         '<br>Turn texture on/ off: <b>Right mouse click</b>'
                         '<br>'
                         '<br><b><i>Keyboard controls:</i></b>'
                         '<br>Increase speed of Planets: <b>d</b>'
                         '<br>Decrease speed of Planets: <b>a</b>'
                         '<br>Stop animation: <b>s</b>'
                         '<br>Load your own textures: <b>t</b>'
                         '<br>Switch view: <b>m</b>'
                         '<br>Zoom in: <b>x</b>'
                         '<br>Zoom out: <b>y</b>'
                         '<br>Switch to fullscreen mode: <b>f</b>'
                         '<br>Display this help: <b>h</b>'
                         '<br>Quit program: <b>ESC</b>')
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.edit)
        self.setWindowOpacity(0.9)
        self.show()

    def keyPressed(self, *args):
        """
        Method keyPressed
        This function is called when a button on the keyboard is pressed
        :param args: which button is pressed
        """
        # speed up the planets
        if args[0] == b'd':
            self.model.speedEarth += 0.2
            self.model.speedMoon += 0.2
            self.model.speedSun = 0.1
            self.model.speedJupiter += 0.2
        # speed down the planets
        if args[0] == b'a':
            self.model.speedEarth -= 0.2
            self.model.speedMoon -= 0.2
            self.model.speedSun = 0.1
            self.model.speedJupiter -= 0.2
        # stop the planets
        if args[0] == b's':
            self.model.speedEarth = 0
            self.model.speedMoon = 0
            self.model.speedSun = 0
            self.model.speedJupiter = 0
        # start/ stop the fullsreen
        if args[0] == b'f':
            if self.model.fullscreen == False:
                glutFullScreen()
                self.model.fullscreen = True
            else:
                self.model.fullscreen = False
                glutPositionWindow(0, 0)
                glutReshapeWindow(640, 480)
        # If escape is pressed, kill everything.
        if args[0] == b'\x1b':
            sys.exit()
        # zoom out
        if args[0] == b'x':
            if int(self.model.zoom) < 20:
                self.model.zoom = 20
            else:
                self.model.zoom -= 1
        # zoom out
        if args[0] == b'y':
            if int(self.model.zoom) > 100:
                self.model.zoom = 100
            else:
                self.model.zoom += 1
        # assign new textures
        if args[0] == b't':
            self.model.fileSet = True
            try:
                self.model.file[0] = QtWidgets.QFileDialog.\
                    getOpenFileName(self, 'Load texture Moon', '/home')
                self.model.file[1] = QtWidgets.QFileDialog\
                    .getOpenFileName(self, 'Load texture Earth', '/home')
                self.model.file[2] = QtWidgets.QFileDialog.\
                    getOpenFileName(self, 'Load texture Sun', '/home')
                self.model.file[3] = QtWidgets.QFileDialog.\
                    getOpenFileName(self, 'Load texture Jupiter', '/home')
            except Exception:
                if self.model.file[0] or self.model.file[1] \
                        or self.model.file[2] or self.model.file[3] == '':
                    print("empty")
                print("empty")

            self.InitGL()
        if args[0] == b'h':
            self.help()

        if args[0] == b'm':
            if self.model.perspective == 0:
                self.model.perspective = 1
            else:
                self.model.perspective = 0

    def main(self):
        """
        Method main
        This function initializes and start pyopengl
        """
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

        # Okay, like the C version we retain the window id to
        # use when closing, but for those of you new
        # to Python (like myself), remember this assignment
        # would make the variable local and not global
        # if it weren't for the global declaration at the
        # start of main.
        glutCreateWindow("Solarsystem v1.1")

        # Register the drawing function with glut, BUT in Python
        # land, at least using PyOpenGL, we need to
        # set the function pointer and invoke a function to
        # actually register the callback, otherwise it
        # would be very much like the C version of the code.
        glutDisplayFunc(self.drawGLScene)

        # When we are doing nothing, redraw the scene.
        glutIdleFunc(self.drawGLScene)

        # Register the function called when our window is resized.
        glutReshapeFunc(self.reSizeGLScene)

        # Register the function called when the keyboard is pressed.
        glutKeyboardFunc(self.keyPressed)

        # Register the function called when the mouse is clicked.
        glutMouseFunc(self.mousePressed)

        # Initialize our window.
        self.InitGL()

        # Start Event Processing Engine
        glutMainLoop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(glutInit(sys.argv))

    # load splashscreen
    splash_pix = QtGui.QPixmap('../Splashscreen2.jpg')
    # generate the splashscreen with the image
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # show the splashscreen
    splash.show()
    app.processEvents()

    time.sleep(1)

    start = Weltall()
    splash.finish(start)
    app.exit()
    start.main()
