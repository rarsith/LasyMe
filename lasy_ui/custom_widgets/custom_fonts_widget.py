import os
from PySide2.QtGui import QFont, QFontDatabase
from PySide2.QtGui import QFontDatabase
from lasy_ops.connection import LasyMeRoot
from pathlib import Path


external = ["lasy_external", "fonts", "roboto"]
target_font = "RobotoCondensed-Regular.ttf"
full_path = os.path.join(LasyMeRoot, *external, target_font)

def define_font():
    font_id = QFontDatabase.addApplicationFont(full_path)
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(font_family, 10)
        return custom_font
    else:
        custom_font = QFont()
        return custom_font

if __name__ =="__main__":
    ubuntu_font = define_font()
    print(ubuntu_font)