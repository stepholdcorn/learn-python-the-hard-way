try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'My project',
  'author': 'Steph',
  'url': 'URL to get it at',
  'download_url': 'Where to download it',
  'author_email': 'steph@test.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['example'],
  'scripts': [],
  'name': 'test'
}

setup(**config)