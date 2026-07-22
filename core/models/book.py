from dataclasses import dataclass, field
from typing import List

from .page import Page


@dataclass
class Book:

    title: str

    pages: List[Page] = field(default_factory=list)
