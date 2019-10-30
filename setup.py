#!/usr/bin/env python

from distutils.core import setup
import numpy as np

setup(name='pyvlmc',
      version='0.1',
      description='Variable length markov chains',
      author='Mohsen Hadianpour',
      author_email='mohsenhadianpour@gmail.com',
      install_requires=['numpy', 'scipy', 'pandas'],
      include_dirs=[np.get_include(), ],
      packages=['pyvlmc', 'pyvlmc.internals', 'pyvlmc.smoothing']
      )
