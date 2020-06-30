#!/usr/bin/python3
"""Write a class Review that inherits from BaseModel"""
import models


class Review(models.BaseModel):
    """ Review class that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
