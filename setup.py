from setuptools import setup
import os

ROOT_DIR='pysst'
with open(os.path.join(ROOT_DIR, 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(name='pysst',
      version=version,
      description='Tools to handle data acquired with Sea and Sun (sst) profilers',
      url='https://github.com/MarineDataTools/pysst',
      author='Peter Holtermann',
      author_email='peter.holtermann@io-warnemuende.de',
      license='GPLv03',
      packages=['pysst'],
      scripts = [],
      entry_points={},
      package_data = {'':['VERSION','rules/standard_names.yaml']},
      zip_safe=False)


