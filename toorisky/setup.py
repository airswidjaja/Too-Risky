from setuptools import setup, find_packages
from codecs import open
from os import path

# Credit to the guys at PyPA on GitHub for helping me make this. Their setup.py example is available here: https://github.com/pypa/sampleproject/blob/master/setup.py

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Too Risky',
    version='0.1',
    description='oo Risky is a story-based, educational computer game that runs in command line interfaces. It is about taking risks at the beach.',
    long_description=long_description,
    url='https://github.com/airswidjaja/TooRisky.py',
    author='Adrian Widjaja',
    author_email='adrian.marcus.widjaja@gmail.com',
    license='GNU GPL',
    classifiers=[
        'Development Status :: My PDHPE Class haha',
        'Topic :: Computer Games :: Text-based games',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python 2',
        'Programming Language :: Python 2.7',
        ],
    keywords='games text risks',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires['termcolor'},
    },
)
