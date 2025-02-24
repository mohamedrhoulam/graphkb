import networkx as nx
import redis
import json
from graphkb.core.models import Node, Edge


class GraphKnowledgeBase:
    def __init__(
        self,
        redis_host: str = "localhost",
        redis_port: int = 6379,
        graph_name: str = "knowledge_base",
    ):
        self.graph_name = graph_name
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
        self.graph = nx.DiGraph()
        self.load()

    def save(self):
        data = nx.node_link_data(self.graph)
        self.redis_client.set(self.graph_name, json.dumps(data))

    def load(self):
        data = self.redis_client.get(self.graph_name)
        if data:
            self.graph = nx.node_link_graph(json.loads(data))
        else:
            self.graph = nx.DiGraph()

    def create_graph(self, graph_name: str):
        self.graph_name = graph_name
        self.graph = nx.DiGraph()
        self.save()

    def add_node(self, node: Node):
        self.graph.add_node(node.id, type=node.type, properties=node.properties)
        self.save()

    def add_edge(self, edge: Edge):
        self.graph.add_edge(
            edge.source, edge.target, label=edge.label, attributes=edge.attributes
        )
        self.save()

    def update_node(self, node_id: str, new_properties: dict):
        if node_id in self.graph.nodes:
            self.graph.nodes[node_id].update(new_properties)
            self.save()
        else:
            raise ValueError(f"Node {node_id} does not exist")

    def update_edge(self, source: str, target: str, new_attributes: dict):
        if self.graph.has_edge(source, target):
            self.graph.edges[source, target].update(new_attributes)
            self.save()
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
