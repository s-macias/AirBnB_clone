#!/usr/bin/python3
""" makes reference to the main package"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State


# import models.engine.file_storage
# from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

# print("hello from __init__.py")
# storage = FileStorage()
# storage.reload()
