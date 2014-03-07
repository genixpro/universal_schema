Tutorial
============================================

To get started with Universal schema, first import the Model class and any number of field classes. Then define your models schema by subclassing from the Model baseclass, and defining the fields as variables within the account. This functions similar to most Python based ORM systems.::

    from universal_schema import Model
    from universal_schema.fields import DateTime, String, Binary, Integer, Email
    
    
    class Account(Model):
        email = Email(min=1, max=1024)
        first_name = String(min=1, max=128)
        last_name = String(min=1, max=128)
        password_hash = String(min=1, max=128)
        current_balance = Integer()
        image = Binary()
        last_modified = DateTime()


Directly from the class object, you can generate schemas for alternate systems::

    colander_schema = Account.schema("colander")
    # This creates an instantiated Colander.Model object, which can be used to serialize and deserialize
    # the way that colander does. By default, all variables are set as missing=colander.drop and default=None
    # unless another default is provided.
    account_json = {'email' : 'awesome@gmail.com',
                    'first_name' : "Usefuller",
                    'last_name' : "Johnson",
                    'current_balance' : 10.0,
                    'last_modified' : '2014-05-01T22:15:38'}
                    
    deserialized = colander_schema.deserialize(account_json)
    

