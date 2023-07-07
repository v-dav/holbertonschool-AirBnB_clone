#!/usr/bin/python3
"""Commande line interpreter for the AirBnb Console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class representing the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program with quit command
        """
        return True

    def do_EOF(self, arg):
        """End of the file, a method allowing
        to make a clean exit of the interpreter with Ctrl-D
        """
        return True

    def emptyline(self):
        """Empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
