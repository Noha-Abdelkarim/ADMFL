# idt/anomaly_detector.py

import logging
import random
import time


class AnomalyDetector:

    def __init__(self, config):

        self.config = config

        self.model_name = config["detection"][
            "anomaly_detection_model"
        ]

        self.packet_entropy_threshold = config[
            "detection"
        ]["packet_entropy_threshold"]

        logging.info(
            f"Anomaly Detector initialized "
            f"with model: {self.model_name}"
        )

    def extract_features(self, telemetry):

        features = {
            "packet_rate": telemetry.get(
                "packet_rate",
                0
            ),

            "latency": telemetry.get(
                "latency",
                0
            ),

            "entropy": telemetry.get(
                "entropy",
                0
            ),

            "trust_score": telemetry.get(
                "trust_score",
                1.0
            )
        }

        logging.info(
            f"Extracted features: {features}"
        )

        return features

    def detect_anomaly(self, telemetry):

        features = self.extract_features(
            telemetry
        )

        anomaly_score = self.compute_anomaly_score(
            features
        )

        is_anomaly = (
            anomaly_score >
            self.packet_entropy_threshold
        )

        if is_anomaly:

            logging.warning(
                f"Anomaly detected with score "
                f"{anomaly_score}"
            )

        else:

            logging.info(
                "Normal network behavior detected."
            )

        return {
            "anomaly_score": anomaly_score,
            "is_anomaly": is_anomaly
        }

    def compute_anomaly_score(self, features):

        entropy_factor = features["entropy"]

        packet_rate_factor = (
            features["packet_rate"] / 1000
        )

        latency_factor = (
            features["latency"] / 100
        )

        trust_factor = (
            1 - features["trust_score"]
        )

        anomaly_score = (
            entropy_factor * 0.4
            + packet_rate_factor * 0.3
            + latency_factor * 0.2
            + trust_factor * 0.1
        )

        anomaly_score = round(
            min(anomaly_score, 1.0),
            4
        )

        time.sleep(0.1)

        return anomaly_score

    def monitor_traffic(self):

        logging.info(
            "Monitoring network telemetry..."
        )

    def generate_sample_telemetry(self):

        telemetry = {
            "packet_rate": random.randint(10, 2000),
            "latency": random.randint(1, 200),
            "entropy": round(
                random.uniform(0, 1),
                4
            ),
            "trust_score": round(
                random.uniform(0, 1),
                4
            )
        }

        return telemetry