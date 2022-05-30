#!/usr/bin/env python3 
#
# ModelHamiltonian performs 1 or 2 electron intergrations corresponding
# to various models of Hamiltonians 
# 
# Copyright (C) The ModelHamiltonian Development Team
# 

from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))
long_description = open(path.join(here, 'README.md'), encoding='utf-8').read()


setup(
    name='moha',
    author='ModelHamiltonian Dev Team',
    version='0.0.0',
    license='LGPLV3',
    url='moha.qcdevs.org',
    keywords='chemtools hamiltonians quantum chemistry',
    description='Computes 1 or 2 electron Hamiltonians of different models.',
    long_description=long_description,
    classifiers=[
        'Environment :: Console',
        'License :: LGPLV3',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
        'Topic :: Science/Engineering :: Molecular Science',
        'Topic :: Science/Engineering :: Physics',
        'Topic :: Science/Engineering :: Chemistry',
    ],
    python_requires='>=3.6',
    install_requires=['numpy', 'scipy'],
    packages=['moha', 'moha.test'],
    package_dir={'moha': 'moha'},
)
