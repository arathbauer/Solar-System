# pylint: disable=wildcard-import, unused-wildcard-import, invalid-name, import-error, too-many-instance-attributes, too-few-public-methods, undefined-variable, missing-docstring
__author__ = 'floriandienesch'

from OpenGL.GL import *

class Lighting(object):
    """
    This class sets the light of the scene
    """
    def __init__(self):
        # list of our lights
        self.lights = {}

    def enableLighting(self):
        """
        Method enableLighting
        This method enables the lighting
        """
        glEnable(GL_LIGHTING)

    def disableLighting(self):
        """
        Method disableLighting
        This method disable the lighting
        """
        glDisable(GL_LIGHTING)

    def addLight(self, id):
        """
        Method addLight
        This method adds a new light in the scene
        Of course the light needs to be already set
        :param id: id of the light, it should be e.g. GL_LIGHTn
        """
        newLight = Light(id)
        self.lights[id] = newLight

    def getLight(self):
        return str(self.lights)

    def setLight(self, id, position, diffuse, specular, ambient):
        """
        Method setLight
        This method sets the light
        :param id: id of the light, it should be e.g. GL_LIGHTn
        :param position: position of the light, it should be a list with 4 sections
        """
        self.lights[id].set(position, diffuse, specular, ambient)

    def render(self):
        """
        Method render
        This method renders the light
        """
        for light in self.lights.values():
            light.render()

class Light(object):
    """
    This class represents an OpenGL light.
    """
    def __init__(self, id):
        self.id = id
        glEnable(id)
        self.position = []
        self.diffuse = []
        self.specular = []
        self.ambient = []

    def set(self, position, diffuse, specular, ambient):
        """
        Method set
        This method sets the light
        """
        self.position = position
        self.diffuse = diffuse
        self.specular = specular
        self.ambient = ambient

    def render(self):
        """
        Method render
        This method render the light
        """
        glLight(self.id, GL_POSITION, self.position)
        glLight(self.id, GL_DIFFUSE, self.diffuse)
        glLight(self.id, GL_SPECULAR, self.specular)
        glLight(self.id, GL_AMBIENT, self.ambient)
