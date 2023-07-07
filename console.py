#!/usr/bin/python3
"""Commande line interpreter for the AirBnb Console"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


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

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on its class Name and id. Usage: show BaseModel 13213216-464
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        else:
            class_name = args[0]
            if class_name != BaseModel.__name__:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            else:
                object_id = args[1]
                key = str(class_name) + "." + str(object_id)
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                    return
                else:
                    print(objects[key])
                    return

    def do_create(self, class_name=None):
        """Creates a new instance of BaseModel,
        and saves it to JSON file and prints the id.

        Args:
            class_name (str): name of the class we want to create
        """
        if not class_name:
            print("** class name missing **")
            return

        if class_name and class_name != BaseModel.__name__:
            print("** class doesn't exist **")
            return

        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_all(self, arg):
        """Prints all string representation of all instances
        """

        objects = storage.all()
        if not arg:
            for obj in objects.values():
                print(str(obj))
        else:
            class_name = arg.split()[0]
            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                instances = []
                for obj in objects.values():
                    if isinstance(obj, BaseModel):
                        instances.append(str(obj))
                print(instances)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Usage: destroy BaseModel 12345-45643-45645.

        Args:
            class_name (str): the name of the class
            id (int): the class id
        """
        arguments = arg.split()

        if not arguments:
            print("** class name missing **")
            return

        class_name = arguments[0]
        if class_name != BaseModel.__name__:
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        id = arguments[1]
        key = str(class_name) + "." + str(id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        else:
            del objects[key]
            storage.save()
            return

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        by adding or updating attribute. All changes are saved to JSON file
        Usage: update BaseModel 1234-1534-6545 email "airbnb@mail.com"
        """

        arguments = arg.split()

        if not arguments:
            print("** class name missing **")
            return
        else:
            class_name = arguments[0]
            if class_name != BaseModel.__name__:
                print("** class doesn't exist **")
                return

        if len(arguments) < 2:
            print("** instance id missing **")
            return
        else:
            id = arguments[1]
            key = str(class_name) + "." + str(id)
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return

        if len(arguments) < 3:
            print("** attribute name missing **")
            return
        else:
            attr_name = arguments[2]

        if len(arguments) < 4:
            print("** value missing **")
            return
        else:
            attr_value = arguments[3]

        setattr(objects[key], attr_name, attr_value)
        storage.save()
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
