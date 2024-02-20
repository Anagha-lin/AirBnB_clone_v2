#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_create(self, args):
        """Create an object of any class"""
        try:
            if not args:
                raise SyntaxError("** class name missing **")
            
            arg_list = args.split()
            class_name = arg_list[0]

            if class_name not in self.classes:
                raise NameError("** class doesn't exist **")
            
            kwargs = {}
            for arg in arg_list[1:]:
                key, value = arg.split("=")
                value = value.strip('"').replace('_', ' ')

                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('\\"', '"')
                elif '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                
                kwargs[key] = value
            
            new_instance = self.classes[class_name](**kwargs)
            new_instance.save()
            print(new_instance.id)

        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    def help_create(self):
        """Help information for the create method"""
        print("Creates a class of any type")
        print("[Usage]: create <className> <param1=value1> <param2=value2> ...\n")

    def do_quit(self, arg):
        """Exit the HBNB console"""
        return True

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        return True

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

