Documentation

1. The Dog API

 The API gives data on dog breeds: names, breed groups, life spans, temperaments, and origins.

 Used the /v1/breeds endpoint.


2. SQLite Database Structure
 Database: dog_breeds.db
 Table: breeds
    * id (INTEGER PRIMARY KEY)
    * name (TEXT)
    * breed_group (TEXT)
    * life_span (TEXT)
    * temperament (TEXT)
    * origin (TEXT)


3. CRUD Functions
* Create: insert_breed(breed) - Adds a new breed.
* Read: read_breed_by_id(breed_id) - Retrieves a breed by ID.
* Update: update_breed(breed) - Updates a breed’s details.
* Delete: delete_breed(breed_id) - Deletes a breed by ID.
* Search: search_breed_by_name(name) - Finds breeds by name.


4. User Interface
 CLI Options:
    1. View all records
    2. Search by ID
    3. Search by name
    4. Update a record
    5. Delete a record
    6. Exit
