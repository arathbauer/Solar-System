# pylint: disable=wildcard-import, unused-wildcard-import, invalid-name, import-error,  missing-docstring, too-few-public-methods, redefined-builtin
__author__ = 'floriandienesch'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *

class Texturen(object):
    """
    Class Texturen
    This class loads a texture
    """

    def textureOrbit(self, imageName):
        """
        Method texturePlanet
        Load an image from a file using PIL, produces 3 textures of filter types.
        Converts the paletted image to RGB format.
        """
        # load the image
        im = open(imageName)
        try:
            # Note the conversion to RGB the crate bitmap is paletted!
            im = im.convert('RGB')
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)
        assert ix*iy*4 == len(image), """Image size != expected array size"""
        IDs = []
        # a Nearest-filtered texture...
        ID = glGenTextures(1)
        IDs.append(ID)
        glBindTexture(GL_TEXTURE_2D, ID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        # linear-filtered
        ID = glGenTextures(1)
        IDs.append(ID)
        glBindTexture(GL_TEXTURE_2D, ID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        # linear + mip-mapping
        ID = glGenTextures(1)
        IDs.append(ID)
        glBindTexture(GL_TEXTURE_2D, ID)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)
        return IDs
