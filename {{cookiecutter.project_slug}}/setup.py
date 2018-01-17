#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import find_packages
from setuptools import setup
import io
import re
import sys

import versioneer

# See https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/
setup(name='{{cookiecutter.project_slug}}',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='{{cookiecutter.project_short_description}}',
      keywords='',
      author='{{cookiecutter.full_name}}',
      author_email='{{cookiecutter.email}}',
      {%- if cookiecutter.project_url %}
      url='{{cookiecutter.project_url }}',
      {% endif -%}
      license='{{cookiecutter.license}}',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['openpyxl'],
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
      # Install data listed in `MANIFEST.in`
      include_package_data=True)
