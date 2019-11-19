# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:40:25 2019

@author: clara
"""

import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Module",
    version="1.0",
    author="Albane Keravec, Pierre-Antoine Michel, Clara Minel, Théo Roudil-Valentin,
    author_email='albane.keravec@ensae.fr, pierre-antoine.michel@ensae.fr, clara.minel@ensae.fr, theo.roudil-valentin@ensae.fr',
    description="Module Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albanek/crispy-goggles/tree/Module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)