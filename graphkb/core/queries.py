from graphkb.core.graph import GraphKnowledgeBase

class Queries:
    def __init__(self, graph: "GraphKnowledgeBase"):
        self.graph = graph.graph

    def find_neighbors(self, node_id: str):
        return list(self.graph.neighbors(node_id))
