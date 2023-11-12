#!/usr/bin/python3
"""
    This module contains code that implements a console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Command prompt class
    """
    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
