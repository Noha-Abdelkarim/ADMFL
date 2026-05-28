# tafl/aggregation.py

import logging
import numpy as np


class AggregationManager:

    def __init__(self, method="FedAvg"):

        self.method = method

        logging.info(
            f"Aggregation Manager initialized "
            f"with method: {self.method}"
        )

    def aggregate(
        self,
        client_updates
    ):

        if not client_updates:

            logging.warning(
                "No updates available for aggregation."
            )

            return None

        logging.info(
            "Starting aggregation process..."
        )

        num_clients = len(client_updates)

        num_weights = len(client_updates[0])

        aggregated_weights = []

        for weight_index in range(num_weights):

            weight_sum = 0

            for client_weights in client_updates:

                weight_sum += (
                    client_weights[weight_index]
                )

            average_weight = (
                weight_sum / num_clients
            )

            aggregated_weights.append(
                round(average_weight, 6)
            )

        logging.info(
            "Aggregation completed successfully."
        )

        return np.array(aggregated_weights)

    def weighted_aggregate(
        self,
        client_updates,
        client_weights
    ):

        logging.info(
            "Starting weighted aggregation..."
        )

        total_weight = sum(client_weights)

        aggregated_weights = []

        num_weights = len(client_updates[0])

        for weight_index in range(num_weights):

            weighted_sum = 0

            for index, update in enumerate(
                client_updates
            ):

                weighted_sum += (

                    update[weight_index]
                    * client_weights[index]

                )

            aggregated_value = (
                weighted_sum / total_weight
            )

            aggregated_weights.append(
                round(aggregated_value, 6)
            )

        logging.info(
            "Weighted aggregation completed."
        )

        return np.array(aggregated_weights)

    def validate_updates(
        self,
        client_updates
    ):

        logging.info(
            "Validating client updates..."
        )

        valid_updates = []

        for update in client_updates:

            if isinstance(update, list):

                valid_updates.append(update)

        logging.info(
            f"Valid updates: {len(valid_updates)}"
        )

        return valid_updates