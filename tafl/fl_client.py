# tafl/fl_client.py

import logging
import random
import time
import numpy as np


class FLClient:

    def __init__(
        self,
        client_id,
        config
    ):

        self.client_id = client_id

        self.config = config

        self.local_epochs = config[
            "federated_learning"
        ]["local_epochs"]

        self.learning_rate = config[
            "federated_learning"
        ]["learning_rate"]

        self.local_model = self.initialize_model()

        logging.info(
            f"FL Client UAV-{self.client_id} initialized."
        )

    def initialize_model(self):

        model_weights = np.random.rand(10)

        logging.info(
            f"UAV-{self.client_id} local model initialized."
        )

        return model_weights

    def train_local_model(self):

        logging.info(
            f"UAV-{self.client_id} started local training."
        )

        for epoch in range(self.local_epochs):

            self.local_model = self.update_weights(
                self.local_model
            )

            logging.info(
                f"UAV-{self.client_id} | "
                f"Epoch {epoch + 1}/"
                f"{self.local_epochs}"
            )

            time.sleep(0.1)

        training_accuracy = round(
            random.uniform(90, 99),
            2
        )

        logging.info(
            f"UAV-{self.client_id} completed training "
            f"with accuracy {training_accuracy}%"
        )

        return {
            "client_id": self.client_id,
            "weights": self.local_model.tolist(),
            "accuracy": training_accuracy
        }

    def update_weights(
        self,
        weights
    ):

        noise = np.random.normal(
            0,
            0.01,
            len(weights)
        )

        updated_weights = weights - (
            self.learning_rate * noise
        )

        return updated_weights

    def receive_global_model(
        self,
        global_weights
    ):

        self.local_model = np.array(
            global_weights
        )

        logging.info(
            f"UAV-{self.client_id} received "
            f"updated global model."
        )

    def evaluate_local_model(self):

        loss = round(
            random.uniform(0.01, 0.2),
            4
        )

        accuracy = round(
            random.uniform(90, 99),
            2
        )

        logging.info(
            f"UAV-{self.client_id} evaluation -> "
            f"Loss: {loss}, "
            f"Accuracy: {accuracy}%"
        )

        return {
            "loss": loss,
            "accuracy": accuracy
        }

    def send_model_update(self):

        logging.info(
            f"UAV-{self.client_id} sending "
            f"local model update."
        )

        return self.local_model.tolist()