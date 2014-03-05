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

from ../formats import Format
from mako.template import Template
from ../fields import *

class ColanderFormat(Format):
    """ ColanderFormat allows you to plug in Universal ORM into the Colander libary: http://colander.readthedocs.org/en/latest/."""
    def __init__(self):
        self.template = Template(filename='/templates/colander.mako')
        
    
    def schema(self, model):
        """ Generates a Python Class object derived from Colander.Model. """
        template_code = self.template.render(name = model.__name__, format = self, fields = model.__fields__)
        eval(template_code)
        return vars()[model.__name__]

    def colander_class_name(self, field):
        if isinstance(field, String):
            return "String"
        elif isinstance(field, Integer):
            return "Integer"
    
    def colander_validator(self, field):
        if isinstance(field, String):
            if hasattr(field, "min") and hasattr(field, "max"):
                return "colander.Length(min=%d, max=%d)" % (field.min, field.max)
            elif hasattr(field, "min"):
                return "colander.Length(min=%d)" % (field.min)
            elif hasattr(field, "max"):
                return "colander.Length(max=%d)" % (field.max)
        elif isinstance(field, Integer):
            return "None"
        return "None"

