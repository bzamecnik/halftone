from setuptools import setup

import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(name='halftone',
      version='0.0.1',
      description='Image halftoning',
      url='http://github.com/bzamecnik/halftone',
      author='Bohumir Zamecnik',
      author_email='bohumir.zamecnik@gmail.com',
      license='MIT',
      packages=['halftone'],
      zip_safe=False,
      install_requires=[
         'numpy',
         'Pillow',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown',
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion',

          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3',

          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
      ],
      entry_points={
          'console_scripts': [
              'halftone = halftone.__main__:main'
          ]
      })
