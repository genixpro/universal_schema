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
import colander

class ColanderBinary(object):
    def serialize(self, node, appstruct):
        if appstruct is colander.null:
            return colander.null
        if appstruct is None:
            return None
        if not isinstance(appstruct, str):
            raise colander.Invalid(node, '%r is not a string' % appstruct)
        return appstruct
    
    def deserialize(self, node, cstruct):
        if cstruct is colander.null:
            return colander.null
        if cstruct is None:
            return None
        if not isinstance(cstruct, basestring):
            raise colander.Invalid(node, '%r is not a string' % cstruct)
        return cstruct
    
    def cstruct_children(self, node, cstruct):
        return []

class ColanderFormat(Format):
    """ ColanderFormat allows you to plug in Universal Schema into the Colander libary: http://colander.readthedocs.org/en/latest/."""
    def __init__(self):
        self.template = Template(filename=data_file('/templates/colander.mako'))
        
    
    def schema(self, modelcls):
        """ Generates a Python Class object derived from Colander.Model. """
        template_code = self.template.render(name = modelcls.__name__, format = self, fields = modelcls.__fields__)
        exec(compile(template_code, "/templates/colander.mako", "exec"))
        return vars()[modelcls.__name__]()

    def encode(self, modelcls, data):
        schema = self.schema(modelcls)
        return schema.serialize(data)
    
    def decode(self, modelcls, data):
        schema = self.schema(modelcls)
        return schema.deserialize(data)

    def colander_class_name(self, field):
        if isinstance(field, String):
            return "colander.String"
        elif isinstance(field, Integer):
            return "colander.Integer"
        elif isinstance(field, Float):
            return "colander.Float"
        elif isinstance(field, Boolean):
            return "colander.Boolean"
        elif isinstance(field, Binary):
            return "ColanderBinary"
        elif isinstance(field, DateTime):
            return "colander.DateTime"
        else:
            raise TypeError(field.__class__.__name__ + " not supported.")
    
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
        elif isinstance(field, Float):
            return "None"
        elif isinstance(field, Boolean):
            return "None"
        elif isinstance(field, Binary):
            return "None"
        elif isinstance(field, DateTime):
            return "None"
        return "None"

    def colander_default(self, field):
        if isinstance(field, String):
            if hasattr(field, "default"):
                return "\"%s\"" % field.default    
            return "\"\""
        elif isinstance(field, Integer):
            if hasattr(field, "default"):
                return "%d" % field.default    
            return "0"
        elif isinstance(field, Float):
            if hasattr(field, "default"):
                return "%f" % field.default    
            return "0"
        elif isinstance(field, Boolean):
            if hasattr(field, "default"):
                return "%s" % ("true" if field.default else "false")    
            return "None"
        elif isinstance(field, Binary):
            if hasattr(field, "default"):
                return "\"%s\"" % field.default
            return "None"
        elif isinstance(field, DateTime):
            return "None"
        return "None"

