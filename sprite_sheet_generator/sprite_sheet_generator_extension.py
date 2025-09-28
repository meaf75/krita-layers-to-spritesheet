"""
spritesheet generator from selected layers
"""

from krita import (Extension, Krita)
from . import sprite_sheet_generator

class spritesheetGeneratorExtension(Extension):

    # Always initialise the superclass.
    # This is necessary to create the underlying C++ object
    def __init__(self, parent):
        super().__init__(parent)

    # this too is necessary, because "Extension.setup() is abstract
    # and must be overridden" and we inherit from Extension
    def setup(self):
        pass

    def createActions(self, window):
        generateButton = window.createAction("pykrita_sprite_sheet_generator",
                                       "Generate SpriteSheet from selected layers",
                                       "tools/scripts")

        generateButton.setToolTip("Generate spritesheet from selected layers")

        generateButton.triggered.connect(sprite_sheet_generator.start)

app = Krita.instance()
# windows and menu stuff
Scripter.addExtension(spritesheetGeneratorExtension(app))