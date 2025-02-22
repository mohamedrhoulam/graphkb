import json
import networkx as nx


class JSONStore:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, graph: nx.DiGraph):
        data = nx.node_link_data(graph)
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def load(self) -> nx.DiGraph:
        with open(self.filepath, "r") as f:
            data = json.load(f)
            return nx.node_link_graph(data)
