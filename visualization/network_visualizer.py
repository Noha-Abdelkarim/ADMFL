# visualization/network_visualizer.py

import logging
import matplotlib.pyplot as plt
import networkx as nx


class NetworkVisualizer:

    def __init__(self):

        logging.info(
            "Network Visualizer initialized."
        )

    def create_network_graph(
        self,
        nodes,
        links
    ):

        graph = nx.Graph()

        for node in nodes:

            graph.add_node(node)

        for link in links:

            graph.add_edge(
                link["source"],
                link["target"]
            )

        return graph

    def visualize_network(
        self,
        nodes,
        links
    ):

        graph = self.create_network_graph(
            nodes,
            links
        )

        plt.figure(figsize=(10, 8))

        nx.draw(
            graph,
            with_labels=True
        )

        plt.title(
            "ADMFL Network Topology"
        )

        plt.show()

        logging.info(
            "Network topology visualized."
        )

    def save_visualization(
        self,
        filename="results/network_topology.png"
    ):

        plt.savefig(filename)

        logging.info(
            f"Visualization saved to {filename}"
        )