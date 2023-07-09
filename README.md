# AirBnB Clone

![65f4a1dd9c51265f49d0](https://github.com/Diego-Bonora/holbertonschool-AirBnB_clone/assets/44532670/47a59566-4a53-435a-9469-55a7b7e7f537)

## Description
The purpose of this project is to create a clone of the AirBnB website. In this first part we will create a command interpreter to manipulate data without a visual interface.

## What is a command interpreter?
It is a user interface in which text commands can be entered and executed. It provides an interactive way to interact with an operating system or computer environment.

Acting as a communication layer between the user and the operating system. It allows the user to enter text commands, which are then interpreted and executed by the operating system. The result of the command execution is displayed on the screen, allowing the user to see the output and respond accordingly.

Similar to a Shell or Terminal, our Interpreter can recognize a series of commands.


## Our interpreter consists of:

**base_model.py:** It contains BaseModel is a base class that defines common attributes and methods for other classes. It serves as a template that other classes can inherit to obtain common functionality.


**file_storage.py**: It is in charge of managing the serialization and deserialization of objects using a JSON file. It serves as a storage mechanism to store and retrieve objects constantly.

**console.py:** Implements a command interpreter that provides an interface to interact with the classes and objects of the program, allowing the user to create, display, update or delete objects using the provided commands.

### Subclasses
Update, State, City, Amenity, Place and Review.

## How to start the command interpreter?

Download our interpreter: ``git clone https://github.com/Diego-Bonora/holbertonschool-AirBnB_clone.git``

To run the console you must use the command ``./console.py``.
Showing a prompt ``(hbnb)`` donde ingresar los comandos.

### Interactive mode

<pre>
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</pre>

### Non-interactive mode

<pre>
  $ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
</pre>


## How to use?

### Commands

| Name | Function |
| --- | --- |
| **quit** | Exit the program or end the execution of the command interpreter. |
| **help** | Displays a help message that provides information on how to use the shell and the available commands. |
| **create** | Creates a new instance of a specified class and saves it. |
| **show** | Displays the details of a specified instance using the class name and its id. | | **destroy** | Elsewhere, the class name and id are displayed.
| **destroy** | Deletes a specified instance using the class name and id. | |
| **all** | Displays all instances of a specific class or all instances of all classes, as specified. |
| **update** | Updates the attributes of a specific instance. |


### How to use

| Commands | Use |
| --- | --- |
| **quit** | quit \<none> |
| **help** | help \<none> or \<command-name> |
| **create** | create \<class-name> |
| **show** | show \<class-name> \<id> |
| **destroy**| destroy \<class-name> \<id> |
| **all**| all \<none> or \<class-name> |
| **update**| update \<class-name> \<id> \<attribute-name> \<attribute-value> |



## Ejemplos

### Create
<pre>
(hbnb) create User
e5bc51b6-e31d-4304-b4e2-046e9a337fad
</pre>

### Show
<pre>
(hbnb) show User e5bc51b6-e31d-4304-b4e2-046e9a337fad
[User] (e5bc51b6-e31d-4304-b4e2-046e9a337fad) {'id': 'e5bc51b6-e31d-4304-b4e2-046e9a337fad', 'created_at': datetime.datetime(2023, 7, 9, 13, 19, 36, 291509), 'updated_at': datetime.datetime(2023, 7, 9, 13, 19, 36, 291560)}
</pre>

### Destroy
<pre>
(hbnb) destroy User e5bc51b6-e31d-4304-b4e2-046e9a337fad
</pre>

### All
<pre>
(hbnb) all User
["[User] (e5bc51b6-e31d-4304-b4e2-046e9a337fad) {'id': 'e5bc51b6-e31d-4304-b4e2-046e9a337fad', 'created_at': datetime.datetime(2023, 7, 9, 13, 19, 36, 291509), 'updated_at': datetime.datetime(2023, 7, 9, 13, 19, 36, 291560)}"]
</pre>

### Update
<pre>
(hbnb) update User e5bc51b6-e31d-4304-b4e2-046e9a337fad Name "Pepe"
</pre>

### Testing

All the files, classes and functions are tested with unitests

### Interactive mode

<pre>
$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 40 tests in 0.070s

OK
guillaume@ubuntu:~/AirBnB$
</pre>

### Non-interactive mode

<pre>
$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 40 tests in 0.070s

OK
guillaume@ubuntu:~/AirBnB$
</pre>

# Authors
Diego Bonora / Lucas Soria
