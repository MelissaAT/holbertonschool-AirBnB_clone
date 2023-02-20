#!/usr/bin/env python3
"""Entry point of the commamd interpreter"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
