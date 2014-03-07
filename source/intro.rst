Introduction to Universal Schema
============================================

Universal Schema is a tool which allows you to express your data model once and get its schema represented in many different forms, and to subsequently convert between instances of those representations seamlessly. Its like an ORM designed to easily plug into other ORMS.

The problem is that we often need to express the same basic data model to multiple different libraries that do serialization in some form and sometimes in several different programming languages, such as in javascript pages with a Python backend. Similar validation routines must exist on both client and server side, and similar data models expressed for serialization and storage in backend services like task processors and databases.

Universal Schema currently supports the following libraries:

Colander - schemas, data
pymongo - data
Ember.js-Data - schemas

Please feel free to contribute to the project and expand the number of supported libaries. Just fork on github and make a pull request when you are ready.




