from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Task:
    id: int
    title: str
    type: str
    schedule: Dict
    last_run: Optional[str]
    active: bool = True
