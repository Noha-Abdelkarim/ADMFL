# usc/local_training.py

import logging
import random
import time
import numpy as np


class LocalTraining:

    def __init__(self, config):

        self.config = config

        self.local_epochs = config[
            "federated_learning"
        ]["local_epochs"]

        self.learning_rate = config[
            "federated_learning"
        ]["learning_rate"]

        self.batch_size = config[
            "federated_learning"
        ]["batch_size"]

        logging.info(
            "Local Training module initialized."
        )

    def initialize_local_model(self):

        local_model = np.random.rand(10)

        logging.info(
            "Local model initialized."
        )

        return local_model

    def train(
        self,
        uav_id,
        dataset=None
    ):

        logging.info(
            f"UAV-{uav_id} started local training."
        )

        model_weights = self.initialize_local_model()

        for epoch in range(self.local_epochs):

            model_weights = self.update_weights(
                model_weights
            )

            logging.info(
                f"UAV-{uav_id} | "
                f"Epoch {epoch + 1}/"
                f"{self.local_epochs}"
            )

            time.sleep(0.1)

        local_accuracy = round(
            random.uniform(90, 99),
            2
        )

        logging.info(
            f"UAV-{uav_id} training completed "
            f"with accuracy {local_accuracy}%"
        )

        return {
            "uav_id": uav_id,
            "weights": model_weights.tolist(),
            "accuracy": local_accuracy
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

    def evaluate_local_model(
        self,
        weights
    ):

        loss = round(
            random.uniform(0.01, 0.2),
            4
        )

        accuracy = round(
            random.uniform(90, 99),
            2
        )

        logging.info(
            f"Local evaluation -> "
            f"Loss: {loss}, "
            f"Accuracy: {accuracy}%"
        )

        return {
            "loss": loss,
            "accuracy": accuracy
        }