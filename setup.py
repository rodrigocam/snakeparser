# -*- coding: utf-8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
import codecs
from setuptools import setup, find_packages

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'src', 'snakeparser', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = 'Rodrigo Oliveira'
''' % version
with open(path, 'w') as F:
    F.write(meta)

setup(
    # Basic info
    name='snakeparser',
    version=version,
    author='Rodrigo Oliveira',
    author_email='rodrigo.redcode@gmail.com',
    url='',
    description='A short description for your project.',
    long_description=codecs.open('README.md', 'rb', 'utf8').read(),

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and dependencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'astroid~=2.0.4',
        'pyaml~=19.4.1',
    ],
    extras_require={
        'dev': [
            'python-boilerplate[dev]',
        ],
    },
    entry_points={
        'console_scripts': [
            'snakeparser=snakeparser.__main__:main',
        ],
    },


    # Other configurations
    zip_safe=False,
    platforms='any',
)