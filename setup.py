import setuptools
from distutils.core import setup, Extension
import numpy as np

module1 = Extension('_dpcore_py',
                    sources = ['dpcore_py.c'])

setup (name = '_dpcore_py',
       version = '0.0',
       description = 'Dynamic programming core routine',
       include_dirs=[np.get_include()],
       ext_modules = [module1])
