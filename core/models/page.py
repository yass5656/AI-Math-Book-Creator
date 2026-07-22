from dataclasses import dataclass, field
from typing import List

from .exercise import Exercise


@dataclass
class Page:

    title: str

    exercises: List[Exercise] = field(default_factory=list)
