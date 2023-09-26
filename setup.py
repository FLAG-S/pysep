#!/usr/bin/env python

from distutils.core import setup

setup(name='pysep',
      version='0.1',
      description='Python Source Extraction and Photometry',
      author='Stephen Wilkins',
      author_email='s.wilkins@sussex.ac.uk',
      url='https://github.com/FLAG-S/pysep',
      packages=['pysep'],
      install_requires=[
        "numpy",
        "scipy",
        "h5py",
        "astropy"
        ],
        )