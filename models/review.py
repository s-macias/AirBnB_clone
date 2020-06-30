#!/usr/bin/python3
"""Write a class State that inherits from BaseModel"""
import models


class Review(models.BaseModel):
    """State class that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
