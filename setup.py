#    This file is part of the Universal ORM.
# 
#    The Universal ORM is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    The Universal ORM is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
LICENSE = open(os.path.join(here, 'LICENSE.txt')).read()

requires = [
        'mako',
    ]

setup(name='universal_orm',
      version='0.0',
      description='universal_orm',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Database",
        ],
      author='Bradley Arsenault',
      author_email='bradley.allen.arsenault@gmail.com',
      url='',
      keywords='orm universal database validation format conversion',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="universal_orm",
      entry_points="""\
      [console_scripts]
      """,
      )

