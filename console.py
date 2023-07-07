#!/usr/bin/python3
"""Command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    clases = ["BaseModel"]

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

    def do_create(self, args):
        try:
            obj = getattr(sys.modules[__name__], args)()
            print(obj.id)
            obj.save()
        except:
            if not args:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        input = args.split()
        if len(input) < 1:
            print("** class name missing **")
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        else:
            key = input[0] + "." + input[1]
            dict = models.storage.all()
            if key in dict:
                print(dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        input = args.split()
        if len(input) < 1:
            print("** class name missing **")
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        else:
            key = input[0] + "." + input[1]
            dict = models.storage.all()
            if key in dict:
                del dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        input = args.split()
        if len(input) < 1:
            print("** class name missing **")
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        else:
            dict = models.storage.all()
            new_list = []
            for key, value in dict.items():
                if key.split(".")[0] == input[0]:
                    new_list.append(str(value))
            print(new_list)

    def do_update(self, args):
        input = args.split()
        if len(input) < 1:
            print("** class name missing **")
        elif input[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        elif input[0] + "." + input[1] not in models.storage.all():
            print("** no instance found **")
        elif len(input) < 3:
            print("** attribute name missing **")
        elif len(input) < 4:
            print("** value missing **")
        else:
            dict = models.storage.all()
            key = input[0] + "." + input[1]
            obj = dict[key]
            if input[2] in obj.__dict__:
                obj.__dict__[input[2]] = eval(input[3])
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
