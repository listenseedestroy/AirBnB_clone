#!/usr/bin/python3
""" This is a command interpreter we can use to manipulate the objects of our web application. """
import cmd
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Defines a class which is the entry point of our command interpreter."""

    prompt = "(hbnb) "
    missing_class = "** class name missing **"
    missing_id = "** instance id missing **"
    missing_attr = "** attribute name missing **"
    missing_val = "** value missing **"
    unknown_class = "** class doesn't exist **"
    unknown_id = "** no instance found **"

    def emptyline(self):
        """ Overides default emptyline execution """
        pass

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ Exits the program with EOF command like cntrl+D """
        print()
        return True

    def do_create(self, args):
        """ Create new class instance, save and display its id """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            class_name = args.split(" ")[0]
            if class_name in storage.class_map():
                new_instance = storage.class_map()[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print(self.unknown_class)

    def do_show(self, args):
        """ Get and print instance str representation by id and class name """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            arg_list = args.split(" ")
            class_name = arg_list[0]
            if len(arg_list) < 2:
                print(self.missing_id)
            elif class_name not in storage.class_map():
                print(self.unknown_class)
            else:
                instance_id = arg_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(self.unknown_id)

    def do_destroy(self, args):
        """ Removes a saved instance based on class name and id """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            arg_list = args.split(" ")
            class_name = arg_list[0]
            if len(arg_list) < 2:
                print(self.missing_id)
            elif class_name not in storage.class_map():
                print(self.unknown_class)
            else:
                instance_id = arg_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print(self.unknown_id)

    def do_all(self, args):
        """ Prints all stored args otherwise prints passed class name """
        if args == "":
            my_list = []
            for key, value in storage.all().items():
                my_list.append(str(value))
            print(my_list)
        else:
            class_name = args.split(" ")[0]
            if class_name not in storage.class_map():
                print(self.unknown_class)
            else:
                my_list = []
                for key, value in storage.all().items():
                    if type(value).__name__ == class_name:
                        my_list.append(str(value))
                print(my_list)

    def do_update(self, args):
        """ Updates an instance based on class name and id by adding or updating attribute """
        if args == "" or args is None:
            print(self.missing_class)
        else:
            arg_list = args.split(" ")
            class_name = arg_list[0]
            if len(arg_list) < 2:
                print(self.missing_id)
            elif class_name not in storage.class_map():
                print(self.unknown_class)
            else:
                instance_id = arg_list[1]
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    instance = storage.all()[key]
                    if len(arg_list) < 3:
                        print(self.missing_attr)
                    elif len(arg_list) < 4:
                        print(self.missing_val)
                    else:
                        setattr(instance, arg_list[2], arg_list[3])
                        instance.save()
                else:
                    print(self.unknown_id)

    def do_count(self, args):
        """ Prints the number of instances of a class """
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in storage.class_map():
            print("** class doesn't exist **")
            return
        count = storage.class_map()[class_name].count()
        print("Number of instances of {}: {}".format(class_name, count))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
