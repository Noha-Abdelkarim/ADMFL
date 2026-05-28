# idt/security_enforcer.py

import logging
import time


class SecurityEnforcer:

    def __init__(self, config):

        self.config = config

        self.blocked_uavs = []

        self.active_rules = []

        logging.info(
            "Security Enforcer initialized."
        )

    def block_uav(
        self,
        uav_id
    ):

        if uav_id not in self.blocked_uavs:

            self.blocked_uavs.append(uav_id)

            logging.warning(
                f"UAV-{uav_id} blocked."
            )

    def unblock_uav(
        self,
        uav_id
    ):

        if uav_id in self.blocked_uavs:

            self.blocked_uavs.remove(uav_id)

            logging.info(
                f"UAV-{uav_id} unblocked."
            )

    def apply_firewall_rule(
        self,
        source,
        destination,
        action="DENY"
    ):

        rule = {
            "source": source,
            "destination": destination,
            "action": action
        }

        self.active_rules.append(rule)

        logging.info(
            f"Firewall rule applied: "
            f"{rule}"
        )

    def remove_firewall_rule(
        self,
        source,
        destination
    ):

        self.active_rules = [

            rule

            for rule in self.active_rules

            if not (
                rule["source"] == source
                and rule["destination"] == destination
            )
        ]

        logging.info(
            f"Firewall rule removed for "
            f"{source}->{destination}"
        )

    def isolate_malicious_uav(
        self,
        uav_id
    ):

        logging.warning(
            f"Isolating malicious UAV-{uav_id}"
        )

        self.block_uav(uav_id)

        self.apply_firewall_rule(
            source=f"UAV-{uav_id}",
            destination="ALL",
            action="DENY"
        )

    def monitor_security_status(self):

        logging.info(
            "Monitoring security enforcement status..."
        )

        logging.info(
            f"Blocked UAVs: {self.blocked_uavs}"
        )

        logging.info(
            f"Active Rules: {len(self.active_rules)}"
        )

        time.sleep(0.1)

    def clear_security_rules(self):

        self.active_rules.clear()

        self.blocked_uavs.clear()

        logging.info(
            "All security rules cleared."
        )