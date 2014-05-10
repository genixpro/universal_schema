#    This file is part of the Universal ORM.
# 
#    The Universal Schema is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    The Universal Schema is distributed in the hope that it will be useful,
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

requires = [
        'mako',
    ]

setup(name='universal_schema',
      version='0.1.5',
      description='universal_schema',
      long_description=""" """,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Database",
        ],
      author='Bradley Arsenault',
      author_email='bradley.allen.arsenault@gmail.com',
      url='http://universal-schema.readthedocs.org/en/latest/',
      keywords='universal schema orm database validation format conversion',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="universal_schema",
      entry_points="""\
      [console_scripts]
      """,
      )

