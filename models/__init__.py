#!/usr/bin/python3
"""Package handler"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
