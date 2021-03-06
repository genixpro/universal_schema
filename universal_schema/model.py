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

from universal_schema.fields import Field
from universal_schema.format import Format
import universal_schema.format
from UserDict import UserDict

class MetaModel(type):
    """ The MetaModel processes the Model class and gathers up all of the declarations which 
        are embedded into the class objects and puts them into special fields so they don't
        get in the way of the actual values on the model."""
    def __new__(mcs, name, bases, classdict):
        fields = {}
        for fieldname,value in classdict.iteritems():
            if isinstance(value, Field):
                fields[fieldname] = value
                fields[fieldname].name = fieldname
        for fieldname in fields.iterkeys():
            del classdict[fieldname]
        classdict['__fields__'] = fields
        
        return type.__new__(mcs, name, bases, classdict)

class Model(object, UserDict):
    """ Every Model in the Universal Schema is a derivative of this one. You define the model by by deriving a
        class from Model, and putting in attributes which are instiatiated objects of classes derived from 
        fields.Field"""
    __metaclass__ = MetaModel
    
    def __init__(self, data = {}):
        """ Sets up the model from the given pieces of data. """
        self.data = dict(data)
    
    @classmethod
    def schema(cls, format):
        """ This returns the Schema for this model, converted into a supported format. For all known supported formats,
            you can use formats.get_all_formats(). """
        return universal_schema.format.formats[format].schema(cls)

    @classmethod
    def create_from(cls, format, data):
        """ This creates a new Model object from the given data, assuming that the data comes from the given format."""
        return cls(universal_schema.format.formats[format].decode(cls, data))
    
    def update_from(self, format, data):
        self.data.update(universal_schema.format.formats[format].decode(self.__class__, data))
        
    
    def to(self, format):
        """ This encodes the data in this Model object into the given format."""
        return universal_schema.format.formats[format].encode(self.__class__, self.data)
    
    
    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
    
    def __setattr__(self, name, value):
        if name in self.__fields__:
            self.data[name] = value
        self.__dict__[name] = value
        
    
