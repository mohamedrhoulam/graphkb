from graphkb.persistence.json_store import JSONStore
from graphkb.core.graph import GraphKnowledgeBase
import networkx as nx


def test_save_load():
    gkb = GraphKnowledgeBase()
    store = JSONStore("data/test.json")

    data = nx.node_link_data(gkb.graph, edges="links")
    store.save(data)

    loaded_data = store.load()
    loaded_gkb = nx.node_link_graph(loaded_data, edges="links")

    assert isinstance(loaded_gkb, GraphKnowledgeBase)
