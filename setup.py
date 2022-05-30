#!/usr/bin/env python3 
#
# ModelHamiltonian performs 1 or 2 electron intergrations corresponding
# to various models of Hamiltonians 
# 
# Copyright (C) The ModelHamiltonian Development Team
# 
# This file is part of the ModelHamiltonian package
#
# ModelHamiltonian is free software; you can redistribute it and/or
# modify it under the terms of the Lesser GNU Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# ModelHamiltonian is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the Lesser GNU Public License along
# with this program; if not, please see <https://www.gnu.org/licenses/> 
# --


from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))
long_description = open(path.join(here, 'README.md'), encoding='utf-8').read()
license_full = open(path.join(here, 'LICENSE'), encoding='utf=8').read() 

setup(
    name='moha',
    author='ModelHamiltonian Dev Team',
    version='0.0.0',
    license=license_full,
    url='moha.qcdevs.org',
    keywords='theochem openchemistry hamiltonians quantum chemistry',
    description='Computes 1 or 2 electron Hamiltonians of different models.',
    long_description=long_description,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Lesser GNU Public License v3 or later (LGPLv3)',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Science/Engineering :: Molecular Science',
        'Topic :: Science/Engineering :: Physics',
        'Topic :: Science/Engineering :: Chemistry',
    ],
    python_requires='>=3.6',
    install_requires=['numpy', 'scipy'],
    packages=['moha', 'moha.test'],
    package_dir={'moha': 'moha'},
)
