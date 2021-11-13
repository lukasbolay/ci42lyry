#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from distutils.core import setup
from setuptools import find_packages
setup(name='ci42lyry',
      version='0.1',
      author='Lukas Bolay',
      author_email='lukas.bolay@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])

