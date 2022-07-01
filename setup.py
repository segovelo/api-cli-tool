# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 19:40:25 2022

@author: sebas
"""

from setuptools import setup
setup(
      name='api-tool',
      version='0.0.1',
      entry_points={
              'console_scripts': [
                      'api=api:preview'
              ]
      }
  )