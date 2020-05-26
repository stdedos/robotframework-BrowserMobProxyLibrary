#!/usr/bin/env python

import sys
from os.path import join, dirname
from setuptools import setup

sys.path.append(join(dirname(__file__), 'src'))

# Is it really not possible with ... ?
# from BrowserMobProxyLibrary import VERSION
VERSION_SOURCE = join(dirname(__file__), 'src', 'BrowserMobProxyLibrary', 'version.py')
if sys.version_info.major >= 3:
    with open(VERSION_SOURCE, "rb") as source_file:
        exec(compile(source_file.read(), VERSION_SOURCE, 'exec'))
else:
    execfile(VERSION_SOURCE)

DESCRIPTION = """
BrowserMobProxyLibrary is a Robot Framework library ro interface with BrowserMob Proxy.
BrowserMob Proxy is a simple utility to capture performance data for web apps (via the HAR format),
as well as manipulate browser behavior and traffic, such as whitelisting and blacklisting content,
simulating network traffic and latency, and rewriting HTTP requests and responses.
"""

setup(name         = 'robotframework-browsermobproxylibrary',
      version      = VERSION,
      description  = 'BrowserMob Proxy library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Marcin Mierzejewski',
      author_email = '<mmierz@gmail.com>',
      url          = 'https://github.com/s4int/robotframework-BrowserMobProxyLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing selenium selenium2 webdriver web browsermob proxy',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
      ],
      install_requires = [
          'browsermob-proxy >= 0.7.1',
      ],
      package_dir = {'': 'src'},
      packages    = ['BrowserMobProxyLibrary'],
      )
