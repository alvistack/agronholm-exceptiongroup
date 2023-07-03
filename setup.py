#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['exceptiongroup']

package_data = \
{'': ['*']}

package_dir = \
{'': 'src'}

extras_require = \
{'test': ['pytest >= 6']}

setup(name='exceptiongroup',
      version='1.1.0',
      description='Backport of PEP 654 (exception groups)',
      author=None,
      author_email='Alex Grönholm <alex.gronholm@nextday.fi>',
      url=None,
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      extras_require=extras_require,
      python_requires='>=3.7',
     )
