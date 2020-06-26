#!/usr/bin/python3
""" Write a class BaseModel that defines all common attributes/methods
for other classes """


from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ BaseModel class """
    def __init__(self):
        """Initializes the BaseModel class
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        dic = self.__dict__.copy()
        # print(self.__dict__)
        # adding instance class name to the dictionary
        dic['__class__'] = self.__class__.__name__
        # converting datetime object to str
        dic['created_at'] = dic['created_at'].isoformat()
        # converting datetime object to str
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__> """
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
