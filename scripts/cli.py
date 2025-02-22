import sys
import os
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graphkb.core.graph import GraphKnowledgeBase
from graphkb.core.models import Node


def main():
    parser = argparse.ArgumentParser(description="GraphKB CLI")
    parser.add_argument(
        "--add-node",
        nargs=3,
        metavar=("ID", "TYPE", "PROPERTIES"),
        help="Add a node with ID, TYPE, and PROPERTIES (JSON string, e.g., '{\"age\": 30}')",
    )
    args = parser.parse_args()

    gkb = GraphKnowledgeBase(filepath="data/knowledge_base.json")

    if args.add_node:
        node_id, node_type, properties_json = args.add_node
        import json

        properties = json.loads(properties_json) if properties_json else {}
        node = Node(id=node_id, type=node_type, properties=properties)
        gkb.add_node(node)
        print(f"Added node {node_id} with type {node_type} and properties {properties}")


if __name__ == "__main__":
    main()
