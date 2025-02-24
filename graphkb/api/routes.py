from fastapi import APIRouter, HTTPException
from graphkb.core.graph import GraphKnowledgeBase
from graphkb.core.models import Node, Edge
from graphkb.core.queries import Queries

router = APIRouter()
gkb = GraphKnowledgeBase()  
queries = Queries(gkb)


@router.post("/nodes")
def add_node(node: Node):
    gkb.add_node(node)
    return {"message": f"Node {node.id} added"}


@router.post("/edges")
def add_edge(edge: Edge):
    gkb.add_edge(edge)
    return {"message": f"Edge from {edge.source} to {edge.target} added"}


@router.put("/nodes/{node_id}")
def update_node(node_id: str, new_properties: dict):
    try:
        gkb.update_node(node_id, new_properties)
        return {"message": f"Node {node_id} updated"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/edges/{source}/{target}")
def update_edge(source: str, target: str, new_attributes: dict):
    try:
        gkb.update_edge(source, target, new_attributes)
        return {"message": f"Edge from {source} to {target} updated"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/nodes/{node_id}")
def get_node(node_id: str):
    try:
        node = gkb.get_node(node_id)
        return node.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/edges/{source}/{target}")
def get_edge(source: str, target: str):
    try:
        edge = gkb.get_edge(source, target)
        return edge.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/nodes/{node_id}/neighbors")
def find_neighbors(node_id: str):
    try:
        neighbors = queries.find_neighbors(node_id)
        return {"neighbors": neighbors}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/nodes/{node_id}/transitive")
def transitive_lookup(node_id: str):
    try:
        descendants = queries.transitive_lookup(node_id)
        return {"descendants": descendants}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
