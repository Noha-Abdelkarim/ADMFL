# usc/communication_manager.py

import logging
import random
import time


class CommunicationManager:

    def __init__(self, config):

        self.config = config

        self.protocol = config["network"][
            "wireless_protocol"
        ]

        self.bandwidth = config["network"][
            "bandwidth_mbps"
        ]

        self.latency = config["network"][
            "latency_ms"
        ]

        logging.info(
            f"Communication Manager initialized "
            f"with protocol {self.protocol}"
        )

    def establish_connection(
        self,
        source_uav,
        destination_uav
    ):

        logging.info(
            f"Establishing communication between "
            f"UAV-{source_uav} and UAV-{destination_uav}"
        )

        connection_status = True

        time.sleep(0.1)

        return connection_status

    def send_message(
        self,
        source_uav,
        destination_uav,
        message
    ):

        logging.info(
            f"UAV-{source_uav} sending message "
            f"to UAV-{destination_uav}"
        )

        transmission_delay = random.uniform(
            0.01,
            0.2
        )

        time.sleep(transmission_delay)

        logging.info(
            f"Message delivered successfully."
        )

        return {
            "source": source_uav,
            "destination": destination_uav,
            "delay": round(
                transmission_delay,
                4
            ),
            "status": "DELIVERED"
        }

    def broadcast_message(
        self,
        source_uav,
        uav_list,
        message
    ):

        logging.info(
            f"Broadcasting message from UAV-{source_uav}"
        )

        responses = []

        for destination_uav in uav_list:

            response = self.send_message(
                source_uav,
                destination_uav,
                message
            )

            responses.append(response)

        return responses

    def calculate_link_quality(
        self,
        signal_strength,
        packet_loss
    ):

        quality_score = (

            signal_strength * 0.7
            - packet_loss * 0.3

        )

        quality_score = round(
            max(0, quality_score),
            4
        )

        logging.info(
            f"Link quality score: {quality_score}"
        )

        return quality_score

    def terminate_connection(
        self,
        source_uav,
        destination_uav
    ):

        logging.info(
            f"Connection terminated between "
            f"UAV-{source_uav} and UAV-{destination_uav}"
        )