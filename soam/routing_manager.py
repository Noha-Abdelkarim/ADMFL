# soam/routing_manager.py

import logging
import random
import time


class RoutingManager:

    def __init__(self, config):

        self.config = config

        self.routing_table = {}

        self.routing_update_interval = config[
            "mitigation"
        ]["routing_update_interval"]

        logging.info(
            "Routing Manager initialized."
        )

    def add_route(
        self,
        source,
        destination,
        next_hop
    ):

        route_key = f"{source}->{destination}"

        self.routing_table[route_key] = next_hop

        logging.info(
            f"Route added: "
            f"{route_key} via {next_hop}"
        )

    def remove_route(
        self,
        source,
        destination
    ):

        route_key = f"{source}->{destination}"

        if route_key in self.routing_table:

            del self.routing_table[route_key]

            logging.info(
                f"Route removed: {route_key}"
            )

    def get_next_hop(
        self,
        source,
        destination
    ):

        route_key = f"{source}->{destination}"

        next_hop = self.routing_table.get(
            route_key,
            None
        )

        logging.info(
            f"Next hop for {route_key}: "
            f"{next_hop}"
        )

        return next_hop

    def compute_optimal_route(
        self,
        source,
        destination
    ):

        possible_hops = [
            "EDGE-1",
            "EDGE-2",
            "S1",
            "S2"
        ]

        optimal_hop = random.choice(
            possible_hops
        )

        logging.info(
            f"Optimal route computed: "
            f"{source} -> {destination} "
            f"via {optimal_hop}"
        )

        return optimal_hop

    def reroute_traffic(
        self,
        source,
        destination
    ):

        new_hop = self.compute_optimal_route(
            source,
            destination
        )

        self.add_route(
            source,
            destination,
            new_hop
        )

        logging.info(
            f"Traffic rerouted for "
            f"{source}->{destination}"
        )

    def monitor_routes(self):

        logging.info(
            "Monitoring routing table..."
        )

        for route, next_hop in self.routing_table.items():

            logging.info(
                f"{route} -> {next_hop}"
            )

            time.sleep(0.1)

    def clear_routes(self):

        self.routing_table.clear()

        logging.info(
            "All routing entries cleared."
        )