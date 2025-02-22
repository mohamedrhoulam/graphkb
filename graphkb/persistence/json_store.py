import json
import networkx as nx

from graphkb.core.graph import GraphKnowledgeBase


class JSONStore:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, graph: GraphKnowledgeBase):
        data = nx.node_link_data(graph.graph)
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def load(self) -> GraphKnowledgeBase:
        gkb = GraphKnowledgeBase()
        with open(self.filepath, "r") as f:
            data = json.load(f)
            gkb.graph = nx.node_link_graph(data)
        return gkb
