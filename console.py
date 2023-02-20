#!/usr/bin/python3
"""Entry point of the commamd interpreter"""

import cmd
import json
import models


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

    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
