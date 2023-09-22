from setuptools import setup, find_packages

with open("requirements.txt", "r") as req:
    print(req)
    get_requirements = req.readlines()

setup(
    name="my_package",
    version="1.0",
    description='Helps organize and customize daily tasks',
    author='Radu Arsith',
    author_email='rarsith@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements,
    license="MIT"

)