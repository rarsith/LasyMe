import sys
import shutil
import subprocess
import win32com.client
from cx_Freeze import setup, Executable

# from setuptools import setup, find_packages

with open("start_lasy.bat", "w") as bat_file:
    bat_file.write("@echo on\n")
    bat_file.write('rem ----LASY_DATA_ROOT -- Add the path where you want the databases to be saved on your storage\n')
    bat_file.write('set "LASY_DATA_ROOT=---insert_path_to_databases_location"\n')
    bat_file.write('rem ----LASY_ROOT -- Add the path where Lasy Me app exists on your storage\n')
    bat_file.write('set "LASY_ROOT=--add_path_to_where_App_is_located"\n')
    bat_file.write('"%LASY_ROOT%\\lasy_me.exe"\n')

executables = [
    Executable(
        script="main.py"
    )
]

buildOptions = dict(include_files=[
    ("lasy_external/", "lib/lasy_external/"),
    ("lasy_icons/", "lib/lasy_icons/"),
    ("start_lasy.bat", "start_lasy.bat")
]
)




with open("requirements.txt", "r") as req:
    print(req)
    get_requirements = req.readlines()

setup(
    name="Lasy Me",
    version="1.0",
    description='Helps organize and customize daily tasks',
    author='Radu Arsith',
    author_email='rarsith@gmail.com',
    executables=executables,
    license="MIT",
    options=dict(build_exe=buildOptions)

)