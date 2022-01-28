# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['simplegistyc']
setup_kwargs = {
    'name': 'simplegistyc',
    'version': '0.1.0',
    'description': 'simplegistyc allows you to create a gist without a file',
    'long_description': None,
    'author': 'FORT',
    'author_email': 'vovarod023@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
