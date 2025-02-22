from graphkb.core.graph import GraphKnowledgeBase
from graphkb.core.models import Node


def test_add_node():
    gkb = GraphKnowledgeBase()
    node = Node(id="alice", type="person", properties={"age": 30})
    gkb.add_node(node)
    assert "alice" in gkb.graph.nodes
    assert gkb.graph.nodes["alice"]["type"] == "person"
    assert gkb.graph.nodes["alice"]["properties"] == {"age": 30}
    