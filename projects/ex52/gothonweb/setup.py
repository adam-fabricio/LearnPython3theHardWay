"""This file can be use to install our project later if we want."""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'discription': 'My Project',
    'author': 'Adam',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'prjectname'
}

setup(**config)

