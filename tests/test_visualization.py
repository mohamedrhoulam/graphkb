from graphkb.visualization.renderer import visualize
from graphkb.core.graph import GraphKnowledgeBase
import os


def test_visualize():
    gkb = GraphKnowledgeBase()
    visualize(gkb, "test_graph.png")
    assert os.path.exists("test_graph.png")
    os.remove("test_graph.png")
