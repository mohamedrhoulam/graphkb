import argparse
from graphkb.core.graph import GraphKnowledgeBase


def main():
    parser = argparse.ArgumentParser(description="GraphKB CLI")
    parser.add_argument(
        "--add-node", nargs=2, metavar=("ID", "TYPE"), help="Add a node"
    )
    args = parser.parse_args()

    gkb = GraphKnowledgeBase()
    if args.add_node:
        node_id, node_type = args.add_node
        gkb.add_node({"id": node_id, "type": node_type, "properties": {}})
        print(f"Added node {node_id}")


if __name__ == "__main__":
    main()
