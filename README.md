universal_schema
=============

When building server systems, I have often found the need to express the same basic data model to multiple different libraries that do serialization in some form and sometimes in several different programming languages, such as in javascript pages with a Python backend. Similar validation routines must exist on both client and server side, and similar data models expressed for serialization and storage in backend services like task processors and databases. The Universal ORM allows you to express your data model once and get its schema represented in many different forms, and to subsequently convert between those representations seamlessly.


