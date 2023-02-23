# AirBnB Clone
# Project Description
This repository contains an implementation of a simplified version of the Airbnb website, including a command-line interface and data models for users, places, cities, amenities, reviews, and states.


# Files and Directories
   
- models directory will contain all classes used for the entire project. 
-tests directory will contain all unit tests.
- console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
- attributes: id, created_at and updated_at
- methods: save()
- models/engine directory will contain all storage classes (using the same prototype). For the moment I will have only one: file_storage.py.

# How to Start the Command Interpreter
To start the command interpreter, clone the repository from GitHub and navigate to the project directory in your terminal. Run the following command to start the interpreter:
    
    ./console.py

This will open the command prompt, and you can start typing commands.

# How to Use the Command Interpreter
The command interpreter provides a set of commands to manage and interact with the data models. The basic syntax for a command is as follows:

**command_name model_name [arguments]**

Here are some examples:

To create a new User:

**create User**

To update an existin User:

**update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"**
