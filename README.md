![AirBnB Clone Holberton Taieb](https://github.com/v-dav/holbertonschool-AirBnB_clone/assets/115344057/c3200352-a0fa-4f20-a04e-e2c80c34bfa3)

# AirBNB Clone Project

A first full Web Application group project at Holberton School. The goal of the project is to deploy on our server a simple copy of the AirBnB website.

## Description :scroll:
The learning aims of this project is to consolidate our knowledge and skills in Python and OOP, to learn HTML/CSS, database storage, API, front-end integration and networking basics.

This project doesn' implement all the AirBNB features, only some of them to cover all fundamental concepts of the higher level programming track.

## Detailed Learning Objectives :mortar_board:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Web Application Components :gear:
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging). Allows to:
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

A website (the front-end) that shows the final product to everybody: static and dynamic
- Static:
	- learn HTML/CSS
	- create the HTML of our application
	- create template of each object
- Dynamic:
	- learn JQuery
	- load objects from the client side by using your own RESTful API

A database (MySQL) or files that store data (data = objects)
An API (RESTful API) that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Technologies & Tools :computer:
- Python
- HTML
- CSS

## Requirements :exclamation:
- Python 3.5+
- PEP 8 - Style Python Code

## Installation
Ensure you have Python 3 installed. Then, simply clone the repository.
  ```
  https://github.com/v-dav/holbertonschool-AirBnB_clone
  ```
## Files Structure

```
.
├── AUTHORS
├── README.md
├── console.py
├── file.json
├── models
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

## Final Product

## Testing
Tests for this project are contained in the tests directory, and are run using the Python unittest module.
To run all tests for the BaseModel class, use:
```
python3 -m unittest
```

## Authors
- Vladimir Davidov
- Djamaldine Mohamed
