# idt/telemetry_extractor.py

import logging
import random
import time


class TelemetryExtractor:

    def __init__(self, config):

        self.config = config

        self.telemetry_interval = config[
            "network"
        ]["telemetry_interval"]

        self.telemetry_enabled = config[
            "network"
        ]["telemetry_enabled"]

        logging.info(
            "Telemetry Extractor initialized."
        )

    def collect_telemetry(self, uav_id):

        if not self.telemetry_enabled:

            logging.warning(
                "Telemetry collection disabled."
            )

            return None

        telemetry = {
            "uav_id": uav_id,
            "packet_rate": random.randint(10, 2000),
            "latency": random.randint(1, 200),
            "throughput": round(
                random.uniform(10, 100),
                2
            ),
            "packet_loss": round(
                random.uniform(0, 10),
                2
            ),
            "entropy": round(
                random.uniform(0, 1),
                4
            ),
            "trust_score": round(
                random.uniform(0, 1),
                4
            ),
            "timestamp": time.time()
        }

        logging.info(
            f"Telemetry extracted from UAV-{uav_id}"
        )

        return telemetry

    def monitor_network_telemetry(
        self,
        num_uavs
    ):

        logging.info(
            "Starting telemetry monitoring..."
        )

        telemetry_data = []

        for uav_id in range(num_uavs):

            telemetry = self.collect_telemetry(
                uav_id
            )

            telemetry_data.append(telemetry)

            time.sleep(
                self.telemetry_interval
            )

        return telemetry_data

    def export_telemetry(
        self,
        telemetry_data,
        output_file="logs/telemetry.log"
    ):

        logging.info(
            f"Exporting telemetry to {output_file}"
        )

        with open(output_file, "w") as file:

            for entry in telemetry_data:

                file.write(
                    f"{entry}\n"
                )

        logging.info(
            "Telemetry export completed."
        )