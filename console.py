#!/usr/bin/python3
"""A program the contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Defines a class which is the entry point command interpreter"""
    intro = "Welcome to the AirBnB clone console! Type 'help' to list commands. \n"
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
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()