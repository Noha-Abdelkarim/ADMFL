# tafl/trust_weighted_fedavg.py

import logging
import numpy as np


class TrustWeightedFedAvg:

    def __init__(self):

        logging.info(
            "Trust-Weighted FedAvg initialized."
        )

    def aggregate(
        self,
        client_updates,
        trust_scores
    ):

        if not client_updates:

            logging.warning(
                "No client updates received."
            )

            return None

        logging.info(
            "Performing trust-weighted aggregation..."
        )

        total_trust = sum(trust_scores)

        if total_trust == 0:

            logging.warning(
                "Total trust score is zero."
            )

            return None

        num_weights = len(
            client_updates[0]
        )

        aggregated_weights = []

        for weight_index in range(num_weights):

            weighted_sum = 0

            for client_index, weights in enumerate(
                client_updates
            ):

                weighted_sum += (

                    weights[weight_index]
                    * trust_scores[client_index]

                )

            aggregated_weight = (
                weighted_sum / total_trust
            )

            aggregated_weights.append(
                round(aggregated_weight, 6)
            )

        logging.info(
            "Trust-weighted aggregation completed."
        )

        return np.array(aggregated_weights)

    def normalize_trust_scores(
        self,
        trust_scores
    ):

        total = sum(trust_scores)

        if total == 0:

            return [
                1 / len(trust_scores)
                for _ in trust_scores
            ]

        normalized_scores = [

            score / total

            for score in trust_scores
        ]

        logging.info(
            "Trust scores normalized."
        )

        return normalized_scores

    def filter_malicious_clients(
        self,
        trust_scores,
        threshold=0.5
    ):

        valid_clients = []

        for index, score in enumerate(
            trust_scores
        ):

            if score >= threshold:

                valid_clients.append(index)

        logging.info(
            f"Valid clients after filtering: "
            f"{valid_clients}"
        )

        return valid_clients