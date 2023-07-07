#!/usr/bin/python3
"""Commande line interpreter for the AirBnb Console"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class representing the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program. Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """End of the file, a method allowing
        to make a clean exit of the interpreter with Ctrl-D
        """
        return True

    def emptyline(self):
        """Does nothing if no command were given
        and pressed ENTER
        """
        pass

    def do_create(self, class_name=None):
        """Creates a new instance of BaseModel,
        and saves it to JSON file and prints the id.
        """
        if not class_name:
            print("** class name  missing **")
            return

        if class_name and class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        obj = BaseModel()
        obj.save()
        print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
