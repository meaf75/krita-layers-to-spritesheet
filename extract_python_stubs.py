import subprocess
import re
from pathlib import Path

def copy_krita_stub():
    # Ruta donde se ejecuta este script
    script_dir = Path(__file__).resolve().parent
    dest_dir = script_dir / "stubs" / "krita"
    dest_file = dest_dir / "__init__.pyi"

    # Buscar el krita.pyi dentro del Flatpak
    find_cmd = [
        "flatpak", "run", "--command=sh", "org.kde.krita",
        "-c", "find /app -iname krita.pyi"
    ]

    try:
        result = subprocess.run(find_cmd, capture_output=True, text=True, check=True)
        stub_path = result.stdout.strip()

        if not stub_path:
            print("❌ No se encontró krita.pyi dentro del Flatpak.")
            return

        # Leer el archivo dentro del Flatpak con cat
        cat_cmd = [
            "flatpak", "run", "--command=cat", "org.kde.krita", stub_path
        ]
        result = subprocess.run(cat_cmd, capture_output=True, text=True, check=True)

        # Guardar en el host
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file.write_text(result.stdout, encoding="utf-8")

        print(f"✅ krita.pyi copiado a {dest_file}")

    except subprocess.CalledProcessError as e:
        print("❌ Error al buscar o copiar krita.pyi:", e)


# Add None to the above parameter of each method with Node type
def patch_stub():
    script_dir = Path(__file__).resolve().parent
    dest_dir = script_dir / "stubs" / "krita"
    stub_file = dest_dir / "__init__.pyi"
    text = stub_file.read_text(encoding="utf-8")

    text = "from typing import Optional\n" + text

    text = re.sub(r": 'Node'", r": Optional[Node]", text)
    text = re.sub(r"->\s*Node\b", r"-> Optional[Node]", text)

    # patch PYQT5 imports
    text = re.sub(r"import PyQt5.sip", r"import PyQt5.sip # type: ignore", text)
    text = re.sub(r"from PyQt5 import QtWidgets", r"from PyQt5 import QtWidgets # type: ignore", text)
    text = re.sub(r"from PyQt5 import QtXml", r"from PyQt5 import QtXml # type: ignore", text)
    text = re.sub(r"from PyQt5 import QtGui", r"from PyQt5 import QtGui # type: ignore", text)
    text = re.sub(r"from PyQt5 import QtCore", r"from PyQt5 import QtCore # type: ignore", text)

    stub_file.write_text(text, encoding="utf-8")
    print(f"✅ krita.pyi patched")


if __name__ == "__main__":
    copy_krita_stub()
    patch_stub()
