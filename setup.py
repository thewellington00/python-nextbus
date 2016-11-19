#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'nextbus',
]

requires = ['requests>=2.0.1', 'lxml>=3.2.4']

readme =''
history =''

setup(
    name='python-nextbus',
    version='0.1b',
    description='python client for nextbus api',
    long_description=readme + '\n\n' + history,
    author='Sam Bolgert',
    author_email='sbolgert@gmail.com',
    url='https://github.com/linuxlewis/python-nextbus',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'nextbus': 'nextbus'},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5'
    ),
)
