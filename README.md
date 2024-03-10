# Description

This project is a pivotal component of the ALX Software Engineer program, serving as the initial step towards building a comprehensive web application, mirroring the functionality of AirBnB. This phase entails developing a bespoke command-line interface tailored for data management, along with base classes for data storage. Through the console commands, users can seamlessly create, update, and delete objects, in addition to managing file storage. The system ensures persistent storage across sessions through JSON serialization/deserialization mechanisms.

# Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

     COMMAND                        EXAMPLE      

Run the console                 ./console.py

Quit the console                 (hbnb) quit

Display the help                 (hbnb) help <command>
for a command

Create an object                 (hbnb) create <class>
(prints its id)

Show an object                   (hbnb) show <class> <id> or (hbnb) <class>.show(<id>)


Destroy an object                (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)

Show all objects,                (hbnb) all or (hbnb) all <class>
or all instances
of a class

Update an attribute             (hbnb) update <class> <id> <attribute name> "<attribute value>" or 
of an object                    (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")


# Models

The folder /models contains all the classes used in this project.

              FILE                                             DESCRIPTION                                             ATTRIBUTES

base_model.py                                BaseModel class for all the other classes                       id, created_at, updated_at

user.py                                      User class for future user information	                 email, password, first_name, last_name

amenity.py                                   Amenity class for future amenity information	                          name

city.py	                                     City class for future location information	                         state_id, name

state.py	                                 State class for future location information	                           name

place.py	                                 Place class for future accomodation information	                city_id, user_id, name, 
                                                                                                                description,number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids

review.py	                                 Review class for future user/host review information	             place_id, user_id, text


# File storage

The folder engine manages the serialization and deserialization of all the data, following a JSON format.

A FileStorage class is defined in file_storage.py with methods to follow this flow: <object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>

The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.


# Tests
All the code is tested with the unittest module. The test for the classes are in the test_models folder.


# Authors
Hamza Semalali ~ semlalihamzauniv@gmail.com