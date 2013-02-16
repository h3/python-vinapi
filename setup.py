from setuptools import setup, find_packages
import sys, os

VERSION = '0.0.1'

setup(name='vinapi',
    version=VERSION,
    description="Python client for the Vin Api web service",
    classifiers=[],
    keywords='vin vinapi',
    author='Maxime Haineault',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/python-vinapi',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    tests_require=['nose'],
    install_requires=[],
)
