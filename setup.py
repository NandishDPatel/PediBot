#Getting the local package, Whenver there is __init__.py it is consider as a local page
from setuptools import find_packages, setup

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Satya Shah',
    author_email='satyashah2610@gmail.com',
    packages=find_packages(), #This will find the init file from src and we can import anywhere as a package by writing from src.helper.(function_name) 
    install_requires=[]
)
###