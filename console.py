#!/usr/bin/python3
"""a program the contains the entry point of the command interpreter"""
import cmd
import sys

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines a class which is the entry point command interpreter"""
    intro = 'Welcome to the AirBnB console! Typehelp to list commands. \n'
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the interpreter"""
        return True

    def help_quit(self):
        """help message for quit"""
        print("Quit command to exit the program\n")
        return

    def do_EOF(self, line):
        """Cleanly exits the"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON)
        and prints the id."""
        args = line.split()
        if not args:
            print("** class doesn't exist **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class name missing **")
            return
        elif class_name in storage.classes():
            object = storage.classes()[class_name]()
            object.save()
            print(object.id)
            return

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234."""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) == 2:
            id = args[1]
            cls_na = args[0]
            key = str(cls_na + '.' + id)

            if key in storage.all():
                print(storage.all()[key].__str__())
                return
            else:
                print("** no instance found **")
                return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (and saves changes to JSON file)"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) == 2:
            id = args[1]
            cls_na = args[0]
            key = str(cls_na + '.' + id)

            if key in storage.all():
                storage.all().pop(key)
                storage.save()
                return
            else:
                print("** no instance found **")
                return

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all"""

        if line != "":
            words = line.split()
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                str_obj = [str(obj) for key, obj in storage.all().items()
                           if type(obj).__name__ == words[0]]
                print(str_obj)
        else:
            str_obj = [str(obj) for key, obj in storage.all.items()]
            print(str_obj)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex:
        $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) in range(2, 4):
            id = args[1]
            cls_na = args[0]
            key = str(cls_na + '.' + id)

            if key not in storage.all():
                print("** no instance found **")
                return

            if len(args) == 2:
                print("** attribute name missing **")
                return

            if len(args) == 3:
                print("** value missing **")
                return

        if len(args) == 4:
            cls_na = args[0]
            id = args[1]
            atr_na = args[2]
            atr_va = args[3]
            val_key = str(cls_na + '.' + id)
            dict_inst = storage.all()

            for key in dict_inst.keys():
                if key == val_key:
                    setattr(dict_inst[key], atr_na, atr_va)
                    dict_inst[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
