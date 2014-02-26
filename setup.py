#!/usr/bin/env python
# License: MIT (http://www.opensource.org/licenses/mit-license.php)

from setuptools import setup, find_packages

setup(
	name='nhs',
	version='1.0',
	description='Class for validating NHS numbers',
	author='Matt Seymour',
	author_email='mattaseymour@gmail.com',
	url='http://mattseymour.net/projects/nhs-number-validation/',
	packages=find_packages(),
	include_package_data=True
)