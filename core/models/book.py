from dataclasses import dataclass, field
from typing import List

from .page import Page

@dataclass
class Book:
    title: str
    stage: int
    term: int
    pages: List[Page] = field(default_factory=list)
