#!/usr/bin/env python
# License: MIT (http://www.opensource.org/licenses/mit-license.php)

import nhs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name='nhs',
	version=nhs.__version__,
	description='function for validating NHS numbers',
	author='Matt Seymour',
	author_email='matt@mattseymour.net',
	url='https://github.com/mattseymour/NhsNumberValidation',
	packages=['nhs'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
	include_package_data=True
)