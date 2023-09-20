from setuptools import setup, find_packages

with open("requirements.txt", "r") as req:
    print(req)
    get_requirements = req.readlines()

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=get_requirements

)