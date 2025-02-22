from pydantic import BaseModel
from typing import Dict, Optional


class Node(BaseModel):
    id: str
    type: str
    properties: Optional[Dict[str, object]] = None


class Edge(BaseModel):
    source: str
    target: str
    label: str
    attributes: Optional[Dict[str, object]] = None
