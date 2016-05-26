import os
from setuptools import setup, find_packages
import shutil

# get documentation from the README
try:
    here = os.path.dirname(os.path.abspath(__file__))
    description = file(os.path.join(here, 'README.md')).read()
except (OSError, IOError):
    description = ''

# version number
version = {}
execfile('version.py', version)

# dependencies
with open('requirements.txt') as f:
    deps = f.read().splitlines()

setup(name='qtest',
      version=version['__version__'],
      description="pytest demo",
      long_description=description,
      author='eric.chang',
      author_email='cateyeatlas@gmail.com',
      install_requires=deps)
