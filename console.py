#!/usr/bin/python3
""" program called console.py that contains the entry point
of the command interpreter """
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """ creates HBNBCommand class that handles commands """
    prompt = '(hbnb) '
    classes_dic = {"BaseModel": models.BaseModel, "User": models.User,
                   "State": models.State, "City": models.City,
                   "Amenity": models.Amenity, "Place": models.Place,
                   "Review": models.Review}

    def do_quit(self, line):
        """ class method to quit program """
        return True

    def do_EOF(self, line):
        """ class method to quit program """
        print('')
        return True

    def emptyline(self):
        """ method that does nothing when enter is pressed """
        pass

    def help_quit(self):
        """ prints help on quit command """
        print('class method to quit program\n')

    def do_create(self, line):
        """Create a new instance

        Args:
            line (str): command line
        """
        arg = line.split()
        if arg:
            if arg[0] in HBNBCommand.classes_dic:
                # creating new instance
                b1 = HBNBCommand.classes_dic[arg[0]]()
                print(b1)
                b1.save()
                print(b1.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        # ret = cmd.Cmd.parseline(self, line)

    def do_show(self, line):
        """Shows  a specific instance saved in the file.json

        Args:
            line (str): command line
        """
        arg = line.split()
        # print(arg)
        if arg:
            if arg[0] in HBNBCommand.classes_dic:
                lg = len(arg)
                if lg != 1:
                    idfind = arg[1]
                    classname = arg[0]
                    keyfind = classname + "." + idfind
                    objs = models.storage.all()
                    if keyfind in objs:
                        print(objs[keyfind])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Destroy an instance specified with class and id

        Args:
            line (str): command line
        """
        arg = line.split()
        if arg:
            if arg[0] in HBNBCommand.classes_dic:
                lg = len(arg)
                if lg != 1:
                    idfind = arg[1]
                    classname = arg[0]
                    keyfind = classname + "." + idfind
                    objs = models.storage.all()
                    if keyfind in objs:
                        del objs[keyfind]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """ Shows all instances in the file by default.
        If the class is specified, finds all instances that belong to it
        Args:
            line (str): command line
        """
        arg = line.split()
        lg = len(arg)
        list_strings = []
        objs = models.storage.all()
        if lg == 0:
            # all
            for key in objs.keys():
                obj_string = objs[key].__str__()
                list_strings.append(obj_string)
            print(list_strings)
        elif lg >= 1:
            # all class
            class_find = arg[0]
            if class_find in HBNBCommand.classes_dic:
                for key in objs.keys():
                    class_filter = key.split(".")
                    if class_find == class_filter[0]:
                        obj_string = objs[key].__str__()
                        list_strings.append(obj_string)
                print(list_strings)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an attribute of a specific instance

        Args:
            line (str): command line
        """
        arg = shlex.split(line)
        if arg:
            if arg[0] in HBNBCommand.classes_dic:
                lg = len(arg)
                if lg != 1:
                    if lg < 3:
                        print("** attribute name missing **")
                        return
                    elif lg < 4:
                        print("** value missing **")
                        return
                    idfind = arg[1]
                    class_name = arg[0]
                    key_find = class_name + "." + idfind
                    objs = models.storage.all()
                    if key_find in objs:
                        # attribute name
                        attr_name = arg[2]
                        # attribute value
                        attr_val = arg[3]
                        obj_update = objs[key_find]
                        # validating if exist in class __dict__
                        if attr_name in obj_update.__class__.__dict__:
                            type_attr = obj_update.__class__.__dict__[
                                attr_name]
                            attr_val = type(type_attr)(attr_val)
                            # print("casting", type(attr_val))
                        setattr(obj_update, attr_name, attr_val)
                        obj_update.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_count(self, line):
        """ Counts instances of a given class """
        instance_n = 0
        arg = line.split()
        class_find = arg[0]
        objs = models.storage.all()
        for key in objs.keys():
            class_filter = key.split(".")
            if class_find == class_filter[0]:
                instance_n += 1
        print(instance_n)

    def onecmd(self, line):
        """ Retrieves all instances of a given class """
        if "." in line:
            arg = line.split(".")
            cmd_list = ["show", "destroy", "update"]
            if cmd_list[0] in arg[1]:
                cmd_unquote = arg[1]
                class_name = arg[0]
                if class_name == "":
                    print("** class name missing **")
                    return
                cmd_id = cmd_unquote.split('(')[1].split(')')[0]
                cmd_id = cmd_id.strip('"')
                tosend = cmd_list[0] + " " + class_name + " " + cmd_id
            else:
                tosend = arg[1].strip("()") + " " + arg[0]
            return cmd.Cmd.onecmd(self, tosend)
        else:
            return cmd.Cmd.onecmd(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
