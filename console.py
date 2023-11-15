#!/usr/bin/python3
"""
    This module contains code that implements a console
"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Command prompt class
    """
    prompt = "(hbnb) "
    clss = {"BaseModel": BaseModel}
    clss["Amenity"] = Amenity
    clss["City"] = City
    clss["Place"] = Place
    clss["Review"] = Review
    clss["State"] = State
    clss["User"] = User

    def emptyline(self):
        """
            Handles empty lines
        """
        pass

    def do_quit(self, line):
        """
            Quit command to exit the program
        """
        exit()

    def help_quit(self):
        """
           A personalized message to appear when typed 'help quit'
        """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
            Handles end of the file condition
        """
        exit()

    def help_EOF(file):
        """
            A personalized message to appear when typed 'help EOF'
        """
        print("Sends a signal to quit the program")

    def do_create(self, arguments):
        """
            Implements the create command
        """
        if not arguments:
            print("** class name missing **")
            return
        tokens = shlex.split(arguments)
        if tokens[0] not in HBNBCommand.clss.keys():
            print("** class doesn't exist **")
        else:
            b1 = HBNBCommand.clss[tokens[0]]()
            b1.save()
            print(b1.id)

    def help_create(self):
        """
            A personalized message to appear when type 'help create'
        """
        print("Used to create a new instance of a class")

    def do_show(self, arguments):
        """"
            Implements the show command
        """
        if not arguments:
            print("** class name missing **")
            return
        tokens = shlex.split(arguments)
        if tokens[0] not in HBNBCommand.clss.keys():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            key_to_find = tokens[0] + "." + tokens[1]
            for key in objects:
                if key_to_find == key:
                    print(str(objects[key_to_find]))
                    return
            print("** no instance found **")

    def help_show(self):
        """
            Show an instance of the received class that contains
            given id
        """
        print("Used to find an instance of a class based on its id")

    def do_destroy(self, arguments):
        """
            Implements the destroy command
        """
        if not arguments:
            print("** class name missing **")
            return
        tokens = shlex.split(arguments)
        if tokens[0] not in HBNBCommand.clss.keys():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            key_to_find = tokens[0] + "." + tokens[1]
            for key in objects:
                if key_to_find == key:
                    del objects[key_to_find]
                    storage.save()
                    return
            print("** no instance found **")

    def help_destroy(self):
        """ Function Description """
        print("Used to delete an instance of a class based on its id")

    def do_all(self, arguments):
        """
            all command implementation
        """
        list_to_print = list()
        storage.reload()
        objects = storage.all()
        if arguments:
            tokens = shlex.split(arguments)
            if tokens[0] not in HBNBCommand.clss.keys():
                print("** class doesn't exist **")
                return
            for key in objects.keys():
                if tokens[0] in key:
                    list_to_print.append(str(objects[key]))
            print(json.dumps(list_to_print))
        else:
            for key in objects.keys():
                list_to_print.append(str(objects[key]))
            print(json.dumps(list_to_print))

    def help_all(self):
        """ Function Description """
        print("Uses to list all the instances in the file storage")

    def do_update(self, arguments):
        """
            Implements the update command
        """
        if not arguments:
            print("** class name missing **")
            return
        data = shlex.split(arguments)
        storage.reload()
        objects = storage.all()
        if data[0] not in HBNBCommand.clss.keys():
            print("** class doesn't exist **")
            return
        if len(data) == 1:
            print("** instance id missing **")
            return
        if len(data) == 2:
            print("** attribute name missing **")
            return
        if len(data) == 3:
            print("** value missing **")
            return
        try:
            key = data[0] + "." + data[1]
            objects[key]
        except Exception as e:
            print("** no instance found **")
            return
        instance = objects[key]
        if hasattr(instance, data[2]):
            data_type = type(getattr(instance, data[2]))
            setattr(instance, data[2], data_type(data[3]))
        else:
            setattr(instance, data[2], data[3])
        storage.save()

    def help_update(self):
        """ Function Declaration """
        print("Updates instance's attributes")

    def do_count(self, argument):
        """
            Counts the number of instance of a class
        """
        num = 0
        objects = storage.all()
        for key in objects.keys():
            if argument in key:
                num += 1
        print(num)

    def default(self, argument):
        """
            For when a command that doesn't match the previous
            is inserted
        """
        methods = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy
        }
        argument = argument.strip()
        data = argument.split(".")
        if len(data) != 2:
            cmd.Cmd.default(self, argument)
            return
        class_name = data[0]
        method = data[1].split("(")[0]
        if method in ["all", "count"]:
            methods[method](class_name.strip())
            return
        ids_number = data[1].split("(")
        id_number = ids_number[1].split(")")[0]
        line = class_name + " " + id_number
        methods[method](line.strip())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
