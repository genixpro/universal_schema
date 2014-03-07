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
import bson

class PymongoFormat(Format):
    """ This module works as an adapter that plugs into pymongo. Although pymongo does not use schemas, it does use
        a variety of special classes when inserting and retrieving data. """
    
    def encode(self, modelcls, data):
        moddata = dict(data)
        if 'id' in moddata:
            moddata['_id'] = bson.objectid.ObjectId(moddata['id'])
            del moddata['id']
        
        # Add in the default values
        for name,variable in modelcls.__fields__.iteritems():
            if hasattr(variable, 'default') and name not in moddata:
                moddata[name] = variable.default
        
        return moddata
        
        
        
    def decode(self, modelcls, data):
        moddata = dict(data)
        if '_id' in moddata:
            moddata['id'] = str(moddata['_id'])
            del moddata['_id']
        
        # Add in the default values
        for name,variable in modelcls.__fields__.iteritems():
            if hasattr(variable, 'default') and name not in moddata:
                moddata[name] = variable.default
        return moddata
