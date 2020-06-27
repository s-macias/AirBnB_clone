#!/usr/bin/python3
import models.engine.file_storage
from models.engine.file_storage import FileStorage

#print("hello from __init__.py")
storage = FileStorage()
storage.reload()
