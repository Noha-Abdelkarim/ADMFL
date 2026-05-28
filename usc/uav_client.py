# usc/uav_client.py

import logging
import random
import time


class UAVClient:

    def __init__(self, uav_id, config):

        self.uav_id = uav_id
        self.config = config

        self.trust_score = 1.0

        self.position = self.generate_initial_position()

        self.status = "ACTIVE"

        logging.info(f"UAV-{self.uav_id} initialized.")

    def generate_initial_position(self):

        return {
            "x": random.randint(0, 100),
            "y": random.randint(0, 100),
            "z": random.randint(10, 50)
        }

    def start(self):

        logging.info(f"Starting UAV-{self.uav_id}...")

        self.send_telemetry()

        self.perform_local_training()

    def send_telemetry(self):

        telemetry = {
            "uav_id": self.uav_id,
            "position": self.position,
            "trust_score": self.trust_score,
            "status": self.status
        }

        logging.info(f"Telemetry from UAV-{self.uav_id}: {telemetry}")

    def perform_local_training(self):

        logging.info(f"UAV-{self.uav_id} performing local training...")

        time.sleep(1)

        logging.info(f"UAV-{self.uav_id} completed local training.")

    def update_trust_score(self, new_score):

        self.trust_score = new_score

        logging.info(
            f"UAV-{self.uav_id} trust score updated to {self.trust_score}"
        )

    def move(self):

        self.position["x"] += random.randint(-5, 5)
        self.position["y"] += random.randint(-5, 5)

        logging.info(
            f"UAV-{self.uav_id} moved to {self.position}"
        )

    def stop(self):

        self.status = "INACTIVE"

        logging.info(f"UAV-{self.uav_id} stopped.")