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


class Field:
    """ Field is the baseclass for all of the different kinds of fields which can exist within the Universal ORM. """
    
    def __init__(self, **attributes):
        self.attributes = attributes
    
    


class String(Field):
    """Represents a regular String. """
    pass
    

class Integer(Field):
    """ Represents an integer. """
    pass



class Integer(Field):
    """ Represents an integer. """
    pass


