#!/usr/bin/env python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Recieves the end of a file marker and returns True"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Returns an empty string if no command is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
