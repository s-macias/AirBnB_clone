#!/usr/bin/python3
""" program called console.py that contains the entry point
of the command interpreter """


import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """ creates HBNBCommand class that handles commands """
    prompt = '(hbnb) '
    classes_dic = {"BaseModel": models.BaseModel, "User": models.User}
    

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
        # miniparse
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
        arg = line.split()
        # print(arg)
        if arg:
            if arg[0] in HBNBCommand.classes_dic:
                lg = len(arg)
                if lg != 1:
                    idfind = arg[1]
                    objs = models.storage.all()
                    # print ("print)
                    for key in objs.keys():
                        obj_id = objs[key].id
                        if idfind == obj_id:
                            # prints the object
                            print(objs[key])
                            break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        arg = line.split()
        # print(arg)
        if arg:
            if arg[0] in HBNBCommand.classes_dic:
                lg = len(arg)
                if lg != 1:
                    idfind = arg[1]
                    objs = models.storage.all()
                    for key in objs.keys():
                        obj_id = objs[key].id
                        if idfind == obj_id:
                            # prints the object
                            del objs[key]
                            models.storage.save()
                            break
                    else:
                        print("** no instance found **")

                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        arg = line.split()
        # print("self", self)
        # print("line", arg)
        lg = len(arg)
        list_strings = []
        objs = models.storage.all()
        if lg == 0:
            for key in objs.keys():
                obj_string = objs[key].__str__()
                list_strings.append(obj_string)
            print(list_strings)
        elif lg >= 1:
            classn = arg[0]
            if classn in HBNBCommand.classes_dic:
                for key in objs.keys():
                    obj_string = objs[key].__str__()
                    list_strings.append(obj_string)
                print(list_strings)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        arg = shlex.split(line)
        # print(arg)
        if arg:
            if arg[0] in HBNBCommand.classes_dic:
                lg = len(arg)
                if lg != 1:
                    idfind = arg[1]
                    objs = models.storage.all()
                    for key in objs.keys():
                        obj_id = objs[key].id
                        # finding the id
                        if idfind == obj_id:
                            if lg > 2:
                                if lg > 3:
                                    obn = objs[key]
                                    attr_name = arg[2]
                                    attr_val = arg[3]
                                    print(type(attr_val))
                                    setattr(
                                        obn, attr_name, attr_val)
                                    obn.save()
                                    break
                                else:
                                    print("** value missing **")
                                    break
                            else:
                                print(
                                    "** attribute name missing **")
                                break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
