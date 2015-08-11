"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['barion.py']
DATA_FILES = []
PKGS = ['PyQt5', 'fortranformat']

OPTIONS = {'argv_emulation': True,
           'includes': ['sip'],
           'iconfile': 'icon.icns',
           'packages': PKGS}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)