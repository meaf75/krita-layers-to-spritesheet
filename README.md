# Spritesheet generator
Create a new document with your **selected** layers and place them next to each other, ordered by the order of your layers

<img width="775" height="353" alt="result" src="https://github.com/user-attachments/assets/2c531cae-06b2-4366-be25-8229390c8773" />

# Installation instructions
- Inside krita go to `Tools/Scripts/Import Python Plugin from Web...`

  <img width="369" height="279" alt="1" src="https://github.com/user-attachments/assets/6053532b-aa9b-4b97-a178-6dc2284b9db4" />


- Paste the link of this repository: 

        https://github.com/meaf75/krita-layers-to-spritesheet

  <img width="362" height="213" alt="2" src="https://github.com/user-attachments/assets/b23d060a-e230-4843-930d-cc8dcff52c39" />

- Hit "OK" and restart Krita
        

# Usage
- **Select** the layers you want to export into a sprite sheet (this will create a new document with the layers you selected)
- After select your layers go to (Tools > Scripts > Generate SpriteSheet from selected layers)
 

# Development

1. Extract the stubs for vscode suggestions (the script works for a linux Krita installation from flatpak)

        python3 ./extract_python_stubs.py

1. In krita use `Tools/Scripts/Scripter` and import the [sprite_sheet_generator.py](./sprite_sheet_generator/sprite_sheet_generator.py) to run and debug what you make
        
