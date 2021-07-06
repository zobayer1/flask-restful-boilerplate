# -*- coding: utf-8 -*-
from enum import Enum

__all__ = ["Errors"]


class Errors(tuple, Enum):
    """Enums for error subtypes"""

    SERVER_ERROR = (500001, "Something Went Wrong")
