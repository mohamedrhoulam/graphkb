from fastapi import APIRouter
from ..core.graph import GraphKnowledgeBase
from ..core.models import Node

router = APIRouter()
gkb = GraphKnowledgeBase()  # this uses in-memory storage for now


@router.post("/nodes")
def add_node(node: Node):
    gkb.add_node(node)
    return {"message": f"Node {node.id} added"}
