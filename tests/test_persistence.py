from graphkb.persistence.json_store import JSONStore
from graphkb.core.graph import GraphKnowledgeBase


def test_save_load():
    gkb = GraphKnowledgeBase()
    store = JSONStore("data/test.json")
    store.save(gkb)
    loaded_gkb = store.load()
    assert isinstance(loaded_gkb, GraphKnowledgeBase)
