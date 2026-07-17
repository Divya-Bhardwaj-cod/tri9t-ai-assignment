from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Node:
    id: int
    number: str
    title: str
    level: int

    parent: Optional["Node"] = None

    children: list = field(default_factory=list)

    body: str = ""