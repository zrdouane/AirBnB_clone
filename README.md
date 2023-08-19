# AirBnB clone
![ Airbnb_Logo.png]( Airbnb_Logo.png)

The Airbnb Console is a command-line interface (CLI) tool that simplifies the testing of various CRUD (Create, Read, Update, Delete) functionalities. With intuitive commands, you can efficiently interact with your data models and perform essential operations.

## How To start the console
To start the console, run the follow these steps:
**To start up the interpreter, clone this repository, and run the console file on linux as follows:**
- Clone this repository: ```git clone "https://github.com/elfadili-ae/AirBnB_clone"```
- Access AirBnb directory: ```cd AirBnB_clone```
- Run hbnb(interactively): ```./console``` and then press enter command
- Run hbnb(non-interactively): ```echo "<command>" | ./console.py```
```
./console.py
```
## How to use the console
Below is a detailed breakdown of each command and its usage:

### **all**: View All Instances

Description: Prints the string representation of all instances of a given class or all classes.

Usage: ``` all or all <class_name>```

### **count**: Count Instances

Description: Count the number of instances for a specified class.

Usage: ```<class_name>.count()```

### **create**: Create a New Instance

Description: Creates a new instance of the BaseModel class and saves it to the JSON file.

Usage: ```create <class_name>```

### **destroy**: Delete an Instance

Description: Deletes an instance based on the class name and ID, saving the change to the JSON file.

Usage: ```destroy <class_name> <id>```

### **help**: Get Command Help

Description: List available commands or display detailed help for a specific command.

Usage: ```help <command_name>```

### **quit**: Exit the Console

Description: Quit and exit the Airbnb Console.

Usage: ```quit```

### **show**: Show Instance Details

Description: Prints the string representation of an instance based on the class name and ID.

Usage: ```show <class_name> <id>```

### **update**: Update Instance Attributes

Description: Update an instance's attributes by adding or modifying specific attributes.

Usage: ```update <class_name> <id> <attribute_name> '<attribute_value>'```

## examples
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

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
```

Here is an example of cerating an a BaseModel instance and deleting it

```
(hbnb) create BaseModel
ff251868-a146-4269-a651-12951a524b59
(hbnb)
(hbnb) destroy BaseModel ff251868-a146-4269-a651-12951a524b59
(hbnb)
```

# Authors
### Zakaria rdouane.
### Abdessamad EL FADILI.
