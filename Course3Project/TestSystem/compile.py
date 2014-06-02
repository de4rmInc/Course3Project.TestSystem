from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
				Extension('TestModuleLib', ['TestModuleLib.py']),
				Extension('task1.task1_test', ['task1/task1_test.py']),
				Extension('task2.task2_test', ['task2/task2_test.py'])
				]

setup(
      name = 'Test Module Library',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules
)