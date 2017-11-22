#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session='hack')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='ReceitaMais',
      version='1.0',
      description='A simple Django project about doctor''s prescription.',
      long_description='This project is from a college subject.A simple Django project about doctor''s prescription.',
      author='Ronyell Henrique & Thiago Nogueira',
      install_requires=reqs,
      license='MIT License',
      platforms='Web',
      author_email='ronyellhenrique@gmail.com, thiagonf10@gmail.com',
      url='https://preskribe.herokuapp.com/',
      packages=find_packages(),
      )
