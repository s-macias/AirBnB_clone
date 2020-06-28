#!/usr/bin/python3
""" program called console.py that contains the entry point
of the command interpreter """


import cmd


class HBNBCommand(cmd.Cmd):
    """ creates HBNBCommand class that handles commands """
    prompt = '(hbnb) '      

    def do_quit(self, line):
        """ class method to quit program """ 
        return True
   
    def do_EOF(self, line):
        """ class method to quit program """
        print ('')
        return True
    
    def emptyline(self):
        """ method that does nothing when enter is pressed """
        pass
    
    def help_quit(self):
        """ prints help on quit command """
        print ('class method to quit program\n')

if __name__ == "__main__":
    HBNBCommand().cmdloop()
