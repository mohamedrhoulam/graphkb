import networkx as nx
from graphkb.core.models import Node, Edge


class GraphKnowledgeBase:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node: Node):
        self.graph.add_node(node.id, type=node.type, properties=node.properties)

    def add_edge(self, edge: Edge):
        self.graph.add_edge(
            edge.source, edge.target, label=edge.label, attributes=edge.attributes
        )
