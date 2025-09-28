# Spritesheet generator
Create a new document with your **selected** layers and place them next to each other, ordered by the order of your layers

# Installation instructions
- Inside krita go to `Tools/Scripts/Import Python Plugin from Web...`

- Paste the link of this repository: 

        https://github.com/meaf75/krita-layers-to-spritesheet

- Hit "OK" and restart Krita


# Usage
- **Select** the layers you want to export into a sprite sheet (this will create a new document with the layers you selected)
- After select your layers go to (Tools > Scripts > Generate SpriteSheet from selected layers)

# Development

1. Extract the stubs for vscode suggestions (the script works for a linux Krita installation from flatpak)

        python3 ./extract_python_stubs.py

1. In krita use `Tools/Scripts/Scripter` and import the [sprite_sheet_generator.py](./sprite_sheet_generator/sprite_sheet_generator.py) to run and debug what you make
        