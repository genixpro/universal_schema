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

formats = {}

def get_all_formats():
    """ This function is used to get a list of all formats currently loaded by the system. """
    global formats
    return formats.keys()
    
def get_format(name):
    """ This function is used to return the form with a given name. Note that the names are case-insensitive
        and that you do not need to include the word format if your Format-derived class has it in its name. E.g.
        if you have a format class called JSONFormat, get_format("name") will work fine. """
    global formats
    return formats[name.lower().replace("format", "")]


class MetaFormat(type):
    """ The MetaFormat metaclass allows Formats to be automatically registered in a global format registry.
        """
    def __new__(mcs, name, bases, classdict):
        newclass = type.__new__(mcs, name, bases, classdict)
        formats[name.lower().replace("format", "")] = newclass
        return newclass


class Format:
    """ This is the base class representing a format which a universal orm can be represented in. """
    __metaclass__ = MetaFormat
    
    def schema(self, model):
        """ This generates the schema for this format for the given model. model must be a class-object derived
            from the model.Model class."""
        raise NotImplementedError("This format does not generate a schema.") # Unimplemented. 









