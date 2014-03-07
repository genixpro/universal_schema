#    This file is part of the Universal Schema.
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

from universal_schema.format import Format
from mako.template import Template
from universal_schema.fields import *
from universal_schema import data_file
from pprint import pprint

class EmberDataFormat(Format):
    """ EmberDataFormat allows you to plug in Universal Schema into the Ember.Data libary: http://emberjs.com/guides/models/"""
    def __init__(self):
        self.template = Template(filename=data_file('/templates/emberdata.mako'))
        
    
    def schema(self, model, **kwargs):
        """ Generates a Python Class object derived from Colander.Model. """
        template_code = self.template.render(name = model.__name__, format = self, fields = model.__fields__, **kwargs)
        exec(compile(template_code, "/templates/emberdata.mako", "exec"))
        return vars()[model.__name__]


    def emberdata_type(self, field):
        if isinstance(field, String):
            return "'string'"
        elif isinstance(field, Integer):
            return "'number'"
        elif isinstance(field, Float):
            return "'number'"
        elif isinstance(field, Boolean):
            return "'boolean'"
        elif isinstance(field, Binary):
            return "'string'"
        elif isinstance(field, DateTime):
            return "'date'"
    

