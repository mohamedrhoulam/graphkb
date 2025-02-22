import networkx as nx
from .models import Node, Edge
from ..persistence.json_store import JSONStore


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
