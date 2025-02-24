from fastapi import APIRouter, HTTPException, Query
from graphkb.core.graph import GraphKnowledgeBase
from graphkb.core.models import Node, Edge
from graphkb.core.queries import Queries

router = APIRouter()


def get_graph_knowledge_base(graph_name: str):
    return GraphKnowledgeBase(graph_name=graph_name)


@router.post("/graphs")
def create_graph(graph_name: str = Query("knowledge_base")):
    gkb = GraphKnowledgeBase()
    gkb.create_graph(graph_name)
    return {"message": f"Graph {graph_name} created"}


@router.post("/nodes")
def add_node(node: Node, graph_name: str = Query("knowledge_base")):
    gkb = get_graph_knowledge_base(graph_name)
    gkb.add_node(node)
    return {"message": f"Node {node.id} added to {graph_name}"}


@router.post("/edges")
def add_edge(edge: Edge, graph_name: str = Query("knowledge_base")):
    gkb = get_graph_knowledge_base(graph_name)
    gkb.add_edge(edge)
    return {
        "message": f"Edge from {edge.source} to {edge.target} added to {graph_name}"
    }


@router.put("/nodes/{node_id}")
def update_node(
    node_id: str, new_properties: dict, graph_name: str = Query("knowledge_base")
):
    gkb = get_graph_knowledge_base(graph_name)
    try:
        gkb.update_node(node_id, new_properties)
        return {"message": f"Node {node_id} updated in {graph_name}"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/edges/{source}/{target}")
def update_edge(
    source: str,
    target: str,
    new_attributes: dict,
    graph_name: str = Query("knowledge_base"),
):
    gkb = get_graph_knowledge_base(graph_name)
    try:
        gkb.update_edge(source, target, new_attributes)
        return {"message": f"Edge from {source} to {target} updated in {graph_name}"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/nodes/{node_id}")
def get_node(node_id: str, graph_name: str = Query("knowledge_base")):
    gkb = get_graph_knowledge_base(graph_name)
    try:
        node = gkb.get_node(node_id)
        return node.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/edges/{source}/{target}")
def get_edge(source: str, target: str, graph_name: str = Query("knowledge_base")):
    gkb = get_graph_knowledge_base(graph_name)
    try:
        edge = gkb.get_edge(source, target)
        return edge.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/nodes/{node_id}/neighbors")
def find_neighbors(node_id: str, graph_name: str = Query("knowledge_base")):
    gkb = get_graph_knowledge_base(graph_name)
    queries = Queries(gkb)
    try:
        neighbors = queries.find_neighbors(node_id)
        return {"neighbors": neighbors}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/nodes/{node_id}/transitive")
def transitive_lookup(node_id: str, graph_name: str = Query("knowledge_base")):
    gkb = get_graph_knowledge_base(graph_name)
    queries = Queries(gkb)
    try:
        descendants = queries.transitive_lookup(node_id)
        return {"descendants": descendants}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
