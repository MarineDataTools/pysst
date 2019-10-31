from setuptools import setup
import os

ROOT_DIR='pysst'
with open(os.path.join(ROOT_DIR, 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(name='pysst',
      version=version,
      description='Tools to handle data acquired with Sea and Sun (www.sea-sun-tech.com) profilers',
      url='https://github.com/MarineDataTools/pysst',
      author='Peter Holtermann',
      author_email='peter.holtermann@io-warnemuende.de',
      license='GPLv03',
      packages=['pysst'],
      scripts = [],
      entry_points={},
      package_data = {'':['VERSION','rules/standard_names.yaml']},
      install_requires=[ 'gsw', 'pyproj','pytz','pyaml' ],      
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering',          
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
      ],
      python_requires='>=3.4',      
      zip_safe=False)


