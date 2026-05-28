# idt/trust_engine.py

import logging
import time


class TrustEngine:

    def __init__(self, config):

        self.config = config

        self.trust_threshold = config["trust_management"]["trust_threshold"]

        self.trust_memory_factor = config["trust_management"][
            "trust_memory_factor"
        ]

        self.trust_scores = {}

        logging.info("Trust Engine initialized.")

    def initialize_uav(self, uav_id):

        self.trust_scores[uav_id] = 1.0

        logging.info(f"Trust initialized for UAV-{uav_id}")

    def compute_trust(self, uav_id, anomaly_score):

        if uav_id not in self.trust_scores:
            self.initialize_uav(uav_id)

        previous_trust = self.trust_scores[uav_id]

        updated_trust = (
            self.trust_memory_factor * previous_trust
            + (1 - self.trust_memory_factor) * (1 - anomaly_score)
        )

        updated_trust = round(updated_trust, 4)

        self.trust_scores[uav_id] = updated_trust

        logging.info(
            f"UAV-{uav_id} trust updated: {updated_trust}"
        )

        return updated_trust

    def is_malicious(self, uav_id):

        trust_score = self.trust_scores.get(uav_id, 1.0)

        if trust_score < self.trust_threshold:

            logging.warning(
                f"UAV-{uav_id} detected as malicious."
            )

            return True

        return False

    def get_trust_score(self, uav_id):

        return self.trust_scores.get(uav_id, 1.0)

    def monitor_trust(self):

        logging.info("Monitoring UAV trust scores...")

        for uav_id, score in self.trust_scores.items():

            logging.info(
                f"UAV-{uav_id} Trust Score: {score}"
            )

            time.sleep(0.1)

    def reset_trust(self, uav_id):

        self.trust_scores[uav_id] = 1.0

        logging.info(
            f"Trust score reset for UAV-{uav_id}"
        )