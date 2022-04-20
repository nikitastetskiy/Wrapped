""" This module contains wrapped entity """

from dataclasses import dataclass
from typing import Optional
from enum import Enum

@dataclass
class Wrapped:
    """ Represents a wrapped trend that you could be informed on the platform """
    title: str
    summary: str
    image: Optional[str] = None
    popularity: Optional[int] = None
