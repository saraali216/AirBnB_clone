#!/usr/bin/python3
""" Console Module """
import sys
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # the prompt for interactive or not interactive models
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
        """Prints if isatty is false or not"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """cmd syntax
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        # initiate line elements
        _cmds = _cls = _id = _args = ''

        # scanning for general format - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line
        try:
            xline = line[:]
            # isolate class name
            _cls = xline[:xline.find('.')]
            # isolate and validate command
            _cmds = xline[xline.find('.') + 1:xline.find('(')]
            if _cmds not in HBNBCommand.dot_cmds:
                raise Exception

            xline = xline[xline.find('(') + 1:xline.find(')')]

            if xline:
                # xline converts to tuple
                xline = xline.partition(', ')

                # stripping quotes and isolate _id
                _id = xline[0].replace('\"', '')

                xline = xline[2].strip()
                if xline:
                    if xline[0] == '{' and xline[-1] == '}'\
                            and type(eval(xline)) == dict:
                        _args = xline
                    else:
                        _args = xline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false or not"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ this is a method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ The quitting help documentation"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit prog"""
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptylines in the method of cmd """
        pass

    def do_create(self, args):
        """ Creates an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        show_name = new[0]
        show_id = new[2]

        if show_id and ' ' in show_id:
            show_id = show_id.partition(' ')[0]

        if not show_name:
            print("** class name  missing **")
            return

        if show_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not show_id:
            print("** instance id  missing **")
            return

        key = show_name + "." + show_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help for the show cmd"""
        print("Shows an individual instance of the class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroying a specified object """
        new = args.partition(" ")
        destroy_name = new[0]
        destroy_id = new[2]
        if destroy_id and ' ' in destroy_id:
            destroy_id = destroy_id.partition(' ')[0]

        if not destroy_name:
            print("** class name missing **")
            return

        if destroy_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not destroy_id:
            print("** instance id missing **")
            return

        key = destroy_name + "." + destroy_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help for the destroy cmd """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of the class"""
        print_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for i, j in storage._FileStorage__objects.items():
                if i.split('.')[0] == args:
                    print_list.append(str(j))
        else:
            for i, j in storage._FileStorage__objects.items():
                print_list.append(str(v))
        print(print_list)

    def help_all(self):
        """Help for the all cmd"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def help_count(self):
        """ prints usage number (counter) """
        print("Usage: count <class_name>")

    def do_count(self, args):
        """Count current number of instances class"""
        compt = 0
        for i, j in storage._FileStorage__objects.items():
            if args == i.split('.')[0]:
                compt += 1
            print(compt)

    def do_update(self, args):
        """ Updates a certain object """
        class_name = class_id = attrb_name = attrb_val = kwargs = ''

        # isolates cls from id or args,e.g:(<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            class_name = args[0]
        else:
            print("** class name missing **")
            return

        # if class name is invalid
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # isolating the id from args
        args = args[2].partition(" ")
        if args[0]:
            class_id = args[0]
        else:
            print("** instance id missing **")
            return

        # generating a key from : id and the class
        key = class_name + "." + class_id

        # determine if the key is there or not
        if key not in storage.all():
            print("** no instance key found **")
            return

        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) == dict:
            kwargs = eval(args[2])
            args = []
            for i, j in kwargs.items():
                args.append(i)
                args.append(j)
        else:
            args = args[2]
            # checks the quoted arg
            if args and args[0] == '\"':
                scnd_quote = args.find('\"', 1)
                attrb_name = args[1:scnd_quote]
                args = args[scnd_quote + 1:]
            args = args.partition(' ')
            if not attrb_name and args[0] != ' ':
                attrb_name = args[0]
            if args[2] and args[2][0] == '\"':
                attrb_val = args[2][1:args[2].find('\"', 1)]

            if not attrb_val and args[2]:
                attrb_val = args[2].partition(' ')[0]
            args = [attrb_name, attrb_val]
        new_dict = storage.all()[key]

        for i, attrb_name in enumerate(args):
            if (i % 2 == 0):
                attrb_val = args[i + 1]
                if not attrb_name:
                    print("** attribute name missing **")
                    return
                if not attrb_val:
                    print("** value missing **")
                    return
                if attrb_name in HBNBCommand.types:
                    attrb_val = HBNBCommand.types[attrb_name](attrb_val)

                new_dict.__dict__.update({attrb_name: attrb_val})
        # saves updates
        new_dict.save()

    def help_update(self):
        """Help for update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    if __name__ == "__main__":
        HBNBCommand().cmdloop()
