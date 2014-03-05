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

import fields
import formats

class MetaModel(type):
    """ The MetaModel processes the Model class and gathers up all of the declarations which 
        are embedded into the class objects and puts them into special fields so they don't
        get in the way of the actual values on the model."""
    def __new__(mcs, name, bases, classdict):
        fields = {}
        for name,value in classdict.iteritems():
            if isinstance(value, fields.Field):
                fields[name] = value
        for name in fields.iterkeys():
            del classdict[name]
        classdict['__fields__'] = fields
    
        return type.__new__(mcs, name, bases, classdict)

class Model:
    """ Every Model in the Universal ORM is a derivative of this one. You define the model by by deriving a
        class from Model, and putting in attributes which are instiatiated objects of classes derived from 
        fields.Field"""
    __metaclass__ = MetaModel
    
    def __init__(self):
        """ Sets up the model. """
        pass
    
    @classmethod
    def schema(format):
        """ This returns the Schema for this model, converted into a supported format. For all known supported formats,
            you can use formats.get_all_formats(). """
        
