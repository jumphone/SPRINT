"""

SPRINT

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sprint',
    version='0.1.7',
    description='A toolkit for accurately identifying RNA editing sites without the need to filter SNPs',
    long_description=long_description,
    url='http://sprint.tianlab.cn',
    author='Feng Zhang',
    author_email='15110700005@fudan.edu.cn',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for,

        
        'License :: OSI Approved :: MIT License',


        
        'Programming Language :: Python :: 2.7',
       
    ],

    
    keywords='RNA editing',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    
    


    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={
        'sprint': ['package_data.dat'],
    },

    #data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'sprint=sprint:main',
        ],
    },
)
