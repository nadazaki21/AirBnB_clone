#!/usr/bin/env python3

import cmd
from models import storage
from models.base_model import BaseModel


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
    
    def do_create(self, *args):
        """  Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id """
        if args == ('',):
            self.stdout.write("** class name missing **\n")
        elif args[0] not in ["BaseModel"]:
            #print(args)
            self.stdout.write("** class doesn't exist **\n")
        else:
            new_obj = eval(args[0]+"()")
            storage.new(new_obj)
            storage.save()
            self.stdout.write(f"{args[0]}.{new_obj.id}\n")
    
    def do_show(self, *args):
        """  Prints the string representation of an instance based on the class name and id """
        if args == ('',):
            self.stdout.write("** class name missing **\n")
        else:
            arguments = args[0].split()

            if arguments[0] not in ["BaseModel"]:
                self.stdout.write("** class doesn't exist **\n")         
            elif arguments[0] in ["BaseModel"] and len(arguments) < 2:
                self.stdout.write("** instance id missing **\n")
            else:
                #storage.reload() #not needed as reload already ahppens in init.
                all_class_objs = storage.all()
                for key, value in all_class_objs.items():
                    if f"{arguments[0]}.{arguments[1]}" == key:
                        print(value)
    
    def do_all(self, *class_name):
        """ Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all. """
        all_class_objs = storage.all()
        if class_name == ('',):
            for key, value in all_class_objs.items():
                print(value)
        elif class_name[0] not in ["BaseModel"]:
            print(class_name)
            self.stdout.write("** class doesn't exist **\n")
        else: # a name of a class that exists is given
            for key, value in all_class_objs.items():
                class_name_with_id = key.split('.')
                if class_name_with_id[0] == class_name[0]:
                    print(value)
            
            
            
            
        


if __name__ == "__main__":
    HBNBCommand().cmdloop()
