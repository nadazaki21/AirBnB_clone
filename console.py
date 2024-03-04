#!/usr/bin/env python3

import cmd
import os

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


    def do_EOF(self, line):
        """Recieves the end of a file marker and returns True"""
        print()
        return True
    
    def precmd(self, line: str):
        if not os.isatty(0) and line.strip():
            print()
        return super().precmd(line)

    def do_quit(self, line):
        """Exits the current process"""
        return True
    
    def do_test(self, line):
        """ test """
        print("hi")
    
    def emptyline(self):
        """Returns an empty string if no command is entered"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()


