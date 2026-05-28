import logging
import random
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class DDoSAttack:

    def __init__(self):

        self.target = "SDN Controller"

        self.packet_count = 20

    def launch_attack(self):

        logging.info("Launching DDoS attack simulation...")

        for packet in range(self.packet_count):

            fake_ip = f"192.168.1.{random.randint(1, 254)}"

            logging.warning(
                f"DDoS packet {packet + 1} "
                f"sent from {fake_ip} to {self.target}"
            )

            time.sleep(0.2)

        logging.info("DDoS attack simulation completed.")


if __name__ == "__main__":

    attack = DDoSAttack()

    attack.launch_attack()