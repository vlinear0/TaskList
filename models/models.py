from dataclasses import dataclass
from typing import List


@dataclass
class Task:
  name: str
  description: str
  full_text: str = ""
  is_important: bool = False
  status: bool = False

@dataclass
class Tasks:
  tasks: List[Task]