#!/usr/bin/python3
"""Load storage."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
