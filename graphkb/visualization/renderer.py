import matplotlib.pyplot as plt
import networkx as nx

from graphkb.core.graph import GraphKnowledgeBase


def visualize(graph: "GraphKnowledgeBase", output_file: str):
    nx.draw(graph.graph, with_labels=True)
    plt.savefig(output_file)
    plt.close()
