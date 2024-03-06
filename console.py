#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from shlex import split


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

    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if argv == ("",):
            self.stdout.write("** class name missing **\n")
        elif argv[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            self.stdout.write("** class doesn't exist **\n")
        else:
            new_obj = eval(argv[0] + "()")
            storage.new(new_obj)
            storage.save()
            self.stdout.write(f"{argv[0]}.{new_obj.id}\n")

    def do_show(self, argv):
        """Prints the string representation of an instance based on the class name and id"""
        all_class_objs = storage.all()
        if argv == ("",):
            self.stdout.write("** class name missing **\n")
        else:
            arguments = argv[0].split()

            if arguments[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                self.stdout.write("** class doesn't exist **\n")
            elif arguments[0] in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"] and len(arguments) < 2:
                self.stdout.write("** instance id missing **\n")
            elif f"{arguments[0]}.{arguments[1]}" not in all_class_objs.keys():
                self.stdout.write("** no instance found **\n")
            else:
                # storage.reload() #not needed as reload already ahppens in init.
                
                for key, value in all_class_objs.items():
                    if f"{arguments[0]}.{arguments[1]}" == key:
                        print(value)

    def do_all(self, class_name):
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all."""
        obj_list = []
        all_class_objs = storage.all()
        if class_name == ("",):
            for key, value in all_class_objs.items():
                obj_list.append(str(value))
        elif class_name[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            self.stdout.write("** class doesn't exist **\n")
        else:  # a name of a class that exists is given
            for key, value in all_class_objs.items():
                class_name_with_id = key.split(".")
                if class_name_with_id[0] == class_name[0]:
                    obj_list.append(str(value))
        print(obj_list)

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id"""
        arguments = split(argv[0])
        all_class_objs = storage.all()

        if len(arguments) < 1:
            self.stdout.write("** class name missing **\n")
        elif arguments[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            self.stdout.write("** class doesn't exist **\n")
        elif len(arguments) < 2:
            self.stdout.write("** instance id missing **\n")
        elif f"{arguments[0]}.{arguments[1]}" not in all_class_objs.keys():
            self.stdout.write("** no instance found **\n")
        else:
            del all_class_objs[f"{arguments[0]}.{arguments[1]}"]
            storage.save()

    def do_update(self, argv):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        only one sttaribute can be chanes at a time
        """

        arguments = split(argv[0])  # shlex function to take care of "" when taking argv
        argv_num = len(arguments)
        all_objs = storage.all()

        if argv_num < 1:
            self.stdout.write("** class name missing **\n")
        elif arguments[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            self.stdout.write("** class doesn't exist **\n")
        elif argv_num < 2:
            self.stdout.write("** instance id missing **\n")
        elif f"{arguments[0]}.{arguments[1]}" not in all_objs.keys():
            self.stdout.write("** no instance found **\n")
        elif argv_num < 3:
            self.stdout.write("** attribute name missing **\n")
        elif argv_num < 4:
            self.stdout.write("** value missing **\n")
        else:
            setattr(
                all_objs[f"{arguments[0]}.{arguments[1]}"], arguments[2], arguments[3]
            )
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()




