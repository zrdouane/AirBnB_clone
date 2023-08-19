#!/usr/bin/python3
"""BaseModel's Module."""
import json
import uuid
import models
from datetime import datetime


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize the model.

        Args:
            *args: not used
            **kwargs: attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    # setattr(self, key, value)
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Representation of the model.

        Returns:
            representation
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Keys/values of __dict__.

        Returns:
            Keys/valeus dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
