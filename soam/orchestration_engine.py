# soam/orchestration_engine.py

import logging
import time


class OrchestrationEngine:

    def __init__(self, config):

        self.config = config

        self.active_policies = []

        self.isolation_enabled = config[
            "mitigation"
        ]["malicious_uav_isolation"]

        self.traffic_rerouting = config[
            "mitigation"
        ]["traffic_rerouting"]

        logging.info(
            "Orchestration Engine initialized."
        )

    def analyze_network_state(
        self,
        telemetry_data
    ):

        logging.info(
            "Analyzing network state..."
        )

        suspicious_uavs = []

        for telemetry in telemetry_data:

            trust_score = telemetry.get(
                "trust_score",
                1.0
            )

            packet_loss = telemetry.get(
                "packet_loss",
                0
            )

            if trust_score < 0.5 or packet_loss > 5:

                suspicious_uavs.append(
                    telemetry["uav_id"]
                )

        logging.info(
            f"Suspicious UAVs: {suspicious_uavs}"
        )

        return suspicious_uavs

    def apply_orchestration_policy(
        self,
        suspicious_uavs
    ):

        for uav_id in suspicious_uavs:

            if self.isolation_enabled:

                self.isolate_uav(uav_id)

            if self.traffic_rerouting:

                self.reroute_traffic(uav_id)

    def isolate_uav(self, uav_id):

        policy = {
            "uav_id": uav_id,
            "action": "ISOLATE"
        }

        self.active_policies.append(policy)

        logging.warning(
            f"UAV-{uav_id} isolated from network."
        )

    def reroute_traffic(self, uav_id):

        policy = {
            "uav_id": uav_id,
            "action": "REROUTE"
        }

        self.active_policies.append(policy)

        logging.info(
            f"Traffic rerouted for UAV-{uav_id}"
        )

    def monitor_policies(self):

        logging.info(
            "Monitoring orchestration policies..."
        )

        for policy in self.active_policies:

            logging.info(policy)

            time.sleep(0.1)

    def clear_policies(self):

        self.active_policies.clear()

        logging.info(
            "All orchestration policies cleared."
        )