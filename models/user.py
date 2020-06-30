#!/usr/bin/python3
""" Write a class User that inherits from BaseModel """


import models


class User(models.BaseModel):
    """ class that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
