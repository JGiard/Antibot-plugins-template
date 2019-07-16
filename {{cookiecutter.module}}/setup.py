import re

from setuptools import setup, find_packages

with open('src/{{cookiecutter.module}}/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    assert version is not None

setup(name='{{cookiecutter.name}}',
      version=version,
      author='{{cookiecutter.author}}',
      license='LGPL',
      classifier=[
          'Programming Language :: Python :: 3'
      ],
      entry_points={
          'antibot': ['{{cookiecutter.module}}={{cookiecutter.module}}.plugin:{{cookiecutter.name}}']
      },
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=[
          'antibot', 'pynject'
      ],
      )
