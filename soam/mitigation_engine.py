# soam/mitigation_engine.py

import logging
import time


class MitigationEngine:

    def __init__(self, config):

        self.config = config

        self.packet_filtering = config[
            "mitigation"
        ]["packet_filtering"]

        self.isolation_enabled = config[
            "mitigation"
        ]["malicious_uav_isolation"]

        self.active_mitigations = []

        logging.info(
            "Mitigation Engine initialized."
        )

    def detect_attack_type(
        self,
        anomaly_report
    ):

        anomaly_score = anomaly_report.get(
            "anomaly_score",
            0
        )

        if anomaly_score > 0.9:

            return "DDoS"

        elif anomaly_score > 0.7:

            return "Spoofing"

        elif anomaly_score > 0.5:

            return "Poisoning"

        return "Normal"

    def apply_mitigation(
        self,
        uav_id,
        attack_type
    ):

        logging.warning(
            f"Applying mitigation for "
            f"{attack_type} attack on UAV-{uav_id}"
        )

        mitigation_action = {
            "uav_id": uav_id,
            "attack_type": attack_type,
            "actions": []
        }

        if self.packet_filtering:

            mitigation_action["actions"].append(
                "PACKET_FILTERING"
            )

        if self.isolation_enabled:

            mitigation_action["actions"].append(
                "UAV_ISOLATION"
            )

        self.active_mitigations.append(
            mitigation_action
        )

        logging.info(
            f"Mitigation actions: "
            f"{mitigation_action['actions']}"
        )

        time.sleep(0.1)

    def remove_mitigation(
        self,
        uav_id
    ):

        self.active_mitigations = [

            mitigation

            for mitigation in self.active_mitigations

            if mitigation["uav_id"] != uav_id
        ]

        logging.info(
            f"Mitigation removed for UAV-{uav_id}"
        )

    def monitor_mitigations(self):

        logging.info(
            "Monitoring active mitigations..."
        )

        for mitigation in self.active_mitigations:

            logging.info(mitigation)

            time.sleep(0.1)

    def clear_all_mitigations(self):

        self.active_mitigations.clear()

        logging.info(
            "All mitigation policies cleared."
        )