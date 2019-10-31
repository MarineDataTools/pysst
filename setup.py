from setuptools import setup
import os

ROOT_DIR='pysst'
with open(os.path.join(ROOT_DIR, 'VERSION')) as version_file:
    version = version_file.read().strip()

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pysst',
      version=version,
      description='Tools to handle data acquired with Sea and Sun (www.sea-sun-tech.com) profilers',
      long_description=long_description,
      long_description_content_type='text/x-rst',
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
      python_requires='>=3.5',      
      zip_safe=False)


