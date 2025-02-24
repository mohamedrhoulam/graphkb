import json
import networkx as nx


class JSONStore:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, graph: nx.DiGraph):
        data = nx.node_link_data(graph)
        try:
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving graph to {self.filepath}: {e}")

    def load(self) -> nx.DiGraph:
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
                return nx.node_link_graph(data)
        except FileNotFoundError:
            print(f"File {self.filepath} not found. Returning an empty graph.")
            return nx.DiGraph()
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {self.filepath}: {e}")
            return nx.DiGraph()
        except IOError as e:
            print(f"Error loading graph from {self.filepath}: {e}")
            return nx.DiGraph()
