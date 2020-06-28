#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
# #!/usr/bin/python3
# import models.engine.file_storage
# from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

#print("hello from __init__.py")
# storage = FileStorage()
# storage.reload()
