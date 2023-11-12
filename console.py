#!/usr/bin/python3
"""
    This module contains code that implements a console
"""
import cmd
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

    def destroy(self, arguments):
        
            
            
if __name__ == "__main__":
    HBNBCommand().cmdloop()
