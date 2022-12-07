#!/usr/bin/env python

from os import path

from setuptools import find_packages, setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tic-set-screen",
    version="0.1",
    description="Command-line tool for replacing the cover image of a TIC-80 .tic cartridge file",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Matt Westcott",
    author_email="matt@west.co.tt",
    url="https://github.com/gasman/tic-set-screen",
    scripts=['tic-set-screen'],
    include_package_data=True,
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Emulators",
    ],
    python_requires=">=3.7",
    install_requires=[
        "ticfile>=0.1",
        "Pillow>=9.0",
    ],
    zip_safe=True,
)
