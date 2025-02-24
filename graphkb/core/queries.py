import networkx as nx

from graphkb.core.graph import GraphKnowledgeBase


class Queries:
    def __init__(self, graph: "GraphKnowledgeBase"):
        self.graph = graph.graph

    def find_neighbors(self, node_id: str):
        if node_id in self.graph.nodes:
            return list(self.graph.neighbors(node_id))
        else:
            raise ValueError(f"Node {node_id} does not exist")

    def transitive_lookup(self, node_id: str):
        if node_id in self.graph.nodes:
            return list(nx.descendants(self.graph, node_id))
        else:
            raise ValueError(f"Node {node_id} does not exist")
