#!/usr/bin/python3
""" Write a class BaseModel that defines all common attributes/methods
for other classes """


import os
import json
import models


class FileStorage():
    """ creates FileStorage class  """
    __file_path = "file.json"  # pathfilename
    __objects = {}  # dictionary to save all instances

    # returns the __objects dictionary

    def all(self):
        """ public method that returns __objects dictionary  """
        # print("from all")
        return FileStorage.__objects

    # add objs to the dictionary
    def new(self, obj):
        """ adds obj to __objects dictionary  """
        # print("Adding new obj to __objects")
        clsname = obj.__class__.__name__
        key = clsname + "." + obj.id
        FileStorage.__objects[key] = obj
        # print(FileStorage.__objects)

    def save(self):
        """ serializes __objects as a JSON fiile """
        # print("saving into file.json")
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            my_dict = {}
            for key, obj in FileStorage.__objects.items():
                # object to dictionary
                my_dict[key] = obj.to_dict()
                # save myobj to a new dictionary, adding ascii
            json.dump(my_dict, f, ensure_ascii=False)

    def reload(self):
        """ deserializes JSON file to __objects dictionary  """
        # from models.base_model import BaseModel
        # from models import User, BaseModel
        diccionario = {"BaseModel": models.BaseModel, "User": models.User,
                       "State": models.State}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                objs_dict = json.load(f)
            for key, objd in objs_dict.items():
                # print("objd ", objd)
                # FileStorage.__objects[key] = BaseModel(**objd)
                classname = objd["__class__"]
                FileStorage.__objects[key] = diccionario[classname](**objd)
            # print("reloading dictionary", FileStorage.__objects)
