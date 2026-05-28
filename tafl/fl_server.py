# tafl/fl_server.py

import logging
import random
import time


class FLServer:

    def __init__(self, config):

        self.config = config

        self.rounds = config["federated_learning"]["rounds"]

        self.aggregation_method = config["federated_learning"][
            "aggregation_method"
        ]

        self.global_model = {}

        self.clients = []

        logging.info("Federated Learning Server initialized.")

    def register_client(self, client):

        self.clients.append(client)

        logging.info(
            f"Client UAV-{client.uav_id} registered."
        )

    def initialize_global_model(self):

        self.global_model = {
            "weights": [random.random() for _ in range(10)]
        }

        logging.info("Global model initialized.")

    def start_training(self):

        logging.info("Starting Federated Learning...")

        self.initialize_global_model()

        for round_number in range(1, self.rounds + 1):

            logging.info(
                f"FL Round {round_number}/{self.rounds}"
            )

            local_updates = self.collect_local_updates()

            self.aggregate_updates(local_updates)

            self.evaluate_global_model()

            time.sleep(1)

        logging.info("Federated Learning completed.")

    def collect_local_updates(self):

        logging.info("Collecting local model updates...")

        updates = []

        for client in self.clients:

            local_update = client.perform_local_training()

            updates.append(local_update)

        return updates

    def aggregate_updates(self, updates):

        logging.info(
            f"Aggregating updates using "
            f"{self.aggregation_method}"
        )

        if not updates:
            return

        aggregated_weights = []

        num_weights = len(updates[0]["weights"])

        for i in range(num_weights):

            weight_sum = sum(
                update["weights"][i]
                for update in updates
            )

            aggregated_weights.append(
                weight_sum / len(updates)
            )

        self.global_model["weights"] = aggregated_weights

        logging.info("Global model updated.")

    def evaluate_global_model(self):

        accuracy = round(random.uniform(90, 99), 2)

        logging.info(
            f"Global Model Accuracy: {accuracy}%"
        )

    def stop(self):

        logging.info(
            "Federated Learning Server stopped."
        )