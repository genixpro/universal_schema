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

import colander

class ${name}(colander.MappingSchema):
    % for field in fields:
        ${field.name} = colander.SchemaNode(${format.colander_class_name(field)}, validator=${format.colander_validator(field)});
    % endfors



class AccountSchema(colander.MappingSchema):
    id = colander.SchemaNode(colander.String(), validator=colander.Length(min=24, max=24), missing = colander.drop)
    email = colander.SchemaNode(colander.String(), validator=colander.Email(), missing = colander.drop)
    password = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=1024), default = "", missing = colander.drop)
    first_name = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=128), default = "", missing = colander.drop)
    last_name = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=128), default = "", missing = colander.drop)
    company = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=128), default = "", missing = colander.drop)
    city = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=128), default = "", missing = colander.drop)
    region = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=128), default = "", missing = colander.drop)
    address = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=128), default = "", missing = colander.drop)
    postal_code = colander.SchemaNode(colander.String(), validator=colander.Length(min=1, max=128), default = "", missing = colander.drop)
    ticket_collection_counter = colander.SchemaNode(colander.Integer(), default = 0, missing = colander.drop)

