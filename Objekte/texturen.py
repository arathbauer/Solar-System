__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from PIL.Image import *

class Texturen():

    def texturePlanet(self, textur):
        image = open("./out.png")

        if textur == "sun":
            # Laden der Sonnentextur
            image = open("./texture_sun.jpg")
        elif textur == "earth":
            # Laden der Erdtextur
            image = open("./earth.jpg")
        elif textur == "moon":
            # Laden der Mondtextur
            image = open("./texture_moon.png")

        ix = image.size[0]
        iy = image.size[1]
        image = image.convert("RGBA").tostring("raw", "RGBA")

        textures = glGenTextures(2)
        glBindTexture(GL_TEXTURE_2D, int(textures[0]))  # 2d texture (x and y size)

        glBindTexture(GL_TEXTURE_2D, int(textures[0]))
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)

        planet = gluNewQuadric()
        gluQuadricNormals(planet, GLU_SMOOTH)  # Create Smooth Normals (NEW)
        gluQuadricTexture(planet, GL_TRUE)  # Create Texture Coords (NEW)

        return planet