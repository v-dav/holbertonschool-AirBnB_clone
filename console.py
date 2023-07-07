#!/usr/bin/python3
"""Commande interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class representing the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True
  
    def do_EOF(self, arg):
        """End of the file"""
        return True

    def emptyline(self, arg):
        """Empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
