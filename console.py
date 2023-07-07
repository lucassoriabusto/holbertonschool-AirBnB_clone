#!/usr/bin/python3
"""Command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exits the program with EOF"""
        return True

    def help_help(self):
        """Show help message"""

    def emptyline(self):
        """No action on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
