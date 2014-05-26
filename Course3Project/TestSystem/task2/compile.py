from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('task2_test_pyd', ['task2_test.py'])]

setup(
      name = 'Test Module Library',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules
)