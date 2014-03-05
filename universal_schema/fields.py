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


class Field:
    """ Field is the baseclass for all of the different kinds of fields which can exist within the Universal Schema. """
    
    def __init__(self, **attributes):
        self.attributes = attributes
    
    


class DateTime(Field):
    """Represents a regular DateTime. """
    pass
    


class String(Field):
    """Represents a regular String. """
    pass
    


class Binary(Field):
    """A binary glob."""
    pass
    

class Number(Field):
    """ Field. """
    pass


class Boolean(Number):
    """ Boolean. """
    pass

class Integer(Number):
    """ Represents an integer. """
    pass


class Float(Number):
    """ Represents an integer. """
    pass


class Email(String):
    """ Represents an email address. """
    pass
    

