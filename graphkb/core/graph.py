import networkx as nx
from graphkb.core.models import Node, Edge
from graphkb.persistence.json_store import JSONStore


class GraphKnowledgeBase:
    def __init__(self, filepath: str = "data/knowledge_base.json"):
        self.graph = nx.DiGraph()
        self.store = JSONStore(filepath)
        try:
            self.graph = self.store.load()
        except FileNotFoundError:
            pass

    def add_node(self, node: Node):
        self.graph.add_node(node.id, type=node.type, properties=node.properties)
        self.store.save(self.graph)

    def add_edge(self, edge: Edge):
        self.graph.add_edge(
            edge.source, edge.target, label=edge.label, attributes=edge.attributes
        )
        self.store.save(self.graph)

    def update_node(self, node_id: str, new_properties: dict):
        if node_id in self.graph.nodes:
            self.graph.nodes[node_id].update(new_properties)
            self.store.save(self.graph)
        else:
            raise ValueError(f"Node {node_id} does not exist")

    def update_edge(self, source: str, target: str, new_attributes: dict):
        if self.graph.has_edge(source, target):
            self.graph.edges[source, target].update(new_attributes)
            self.store.save(self.graph)
        else:
            raise ValueError(f"Edge from {source} to {target} does not exist")

    def get_node(self, node_id: str) -> Node:
        if node_id in self.graph.nodes:
            data = self.graph.nodes[node_id]
            return Node(id=node_id, type=data["type"], properties=data["properties"])
        else:
            raise ValueError(f"Node {node_id} does not exist")

    def get_edge(self, source: str, target: str) -> Edge:
        if self.graph.has_edge(source, target):
            data = self.graph.edges[source, target]
            return Edge(
                source=source,
                target=target,
                label=data["label"],
                attributes=data.get("attributes"),
            )
        else:
            raise ValueError(f"Edge from {source} to {target} does not exist")


