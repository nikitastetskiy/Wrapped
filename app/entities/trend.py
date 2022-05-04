""" This module contains trend entity """
from dataclasses import dataclass
from typing import List
from wrapped import Wrapped


@dataclass
class Trend:
    """ Represents a array of wrapped trends """
    name: str
    my_array: List[Wrapped]
