#!/usr/bin/python3

""" Write a class BaseModel that defines all common attributes/methods
for other classes """


import os
import json
import models

class FileStorage():
    __file_path = "file.json"  # pathfilename
    __objects = {}  # dictionary to save all instances

    # returns the __objects dictionary

    def all(self):
        # print("from all")
        return FileStorage.__objects

    # add objs to the dictionary
    def new(self, obj):
        # print("Adding new obj to __objects")
        clsname = obj.__class__.__name__
        key = clsname + "." + obj.id
        FileStorage.__objects[key] = obj
        # print(FileStorage.__objects)

    def save(self):
        # print("saving into file.json")
        with open(FileStorage.__file_path, "w") as f:
            my_dict = {}
            for key, obj in FileStorage.__objects.items():
                # object to dictionary
                my_dict[key] = obj.to_dict()
                # save myobj to a new dictionary
            json.dump(my_dict, f)

    def reload(self):
        #from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                objs_dict = json.load(f)
            for key, objd in objs_dict.items():
                #print("objd ", objd)
                #FileStorage.__objects[key] = BaseModel(**objd)
                FileStorage.__objects[key] = models.BaseModel(**objd)
