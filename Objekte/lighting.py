__author__ = 'floriandienesch'

from OpenGL.GL import *

class Lighting(object):
        """
        Diese Klasse leuchtet die Szene aus
        """
        
        def __init__(self):
                # Liste der Lichter
                self.lights = {}
                
        def enableLighting(self):
                """
                Aktiviert das Licht
                """
                
                glEnable(GL_LIGHTING)

        def disableLighting(self):
                """
                Deaktiviert das Licht
                """

                glDisable(GL_LIGHTING)

        def addLight(self, id):
                """
                Fuegt ein neues Licht in die Szene.
                Id sollte GL_LIGHTn sein.
                """
                
                newLight = Light(id)
                self.lights[id] = newLight
                
        def setLight(self, id, position, diffuse, specular, ambient):
                """
                Setzt ein neues Licht
                """
                
                self.lights[id].set(position, diffuse, specular, ambient)
                
        def render(self):
                """
                Rendert alle Lichter
                """
                
                for light in self.lights.values():
                        light.render()

class Light(object):
        """
        This class represents an OpenGL light.
        """
        
        def __init__(self, id):
                """
                Konstruktor
                """
                
                self.id = id
                glEnable(id)
                
                self.position = []
                self.diffuse = []
                self.specular = []
                self.ambient = []
                
        def set(self, position, diffuse, specular, ambient):
                """
                Setzt das Licht
                """
                
                self.position = position
                self.diffuse = diffuse
                self.specular = specular
                self.ambient = ambient
                
        def render(self):
                """
                Rendert das Licht
                """
                                
                glLight(self.id, GL_POSITION, self.position)
                glLight(self.id, GL_DIFFUSE, self.diffuse)
                glLight(self.id, GL_SPECULAR, self.specular)
                glLight(self.id, GL_AMBIENT, self.ambient)