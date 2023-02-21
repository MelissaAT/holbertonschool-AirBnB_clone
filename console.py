#!/usr/bin/python3
"""Entry point of the commamd interpreter"""

import cmd
import json

from models import FileStorage, storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print('** class name missing **')
            return
        try:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)
        except Exception:
            print('** class doesn\'t exist **')

        
    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        list_arg = arg.split()
        try:
            class_name = eval(list_arg[0]).__name__
        except Exception:
             print("** class doesn't exist **")
             return
        if len(list_arg) == 1:
            print("** instance id missing **")
            return
        try:
            class_name = f"{list_arg[0]}.{list_arg[1]}"
            print(storage.all()[class_name])
        except Exception:
            print("** no instance found **")

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return
        list_arg = arg.split()
        try:
            class_name = eval(list_arg[0]).__name__
        except Exception:
             print("** class doesn't exist **")
             return
        if len(list_arg) == 1:
            print("** instance id missing **")
            return
        try:
            class_name = f"{list_arg[0]}.{list_arg[1]}"
            object = storage.all().get(class_name)
            del(object)
            storage.save()
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, arg):
        if not arg:
            print("** class name missing **")
            return
        elif arg:
            _list = []
            class_name = arg
            for i in storage.all():
                _list.append()
                for _class in _list:
                    object = storage.all().get(_class)
            print(object)
            return     

if __name__ == '__main__':
    HBNBCommand().cmdloop()