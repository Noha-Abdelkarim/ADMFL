import logging
import random
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class PoisoningAttack:

    def __init__(self):

        self.malicious_clients = 5

    def launch_attack(self):

        logging.info("Launching model poisoning attack...")

        for client in range(self.malicious_clients):

            malicious_accuracy = round(
                random.uniform(0.01, 0.30),
                2
            )

            logging.warning(
                f"Malicious FL update injected "
                f"from UAV-{client} "
                f"(accuracy corruption: {malicious_accuracy})"
            )

            time.sleep(0.5)

        logging.info("Poisoning attack simulation completed.")


if __name__ == "__main__":

    attack = PoisoningAttack()

    attack.launch_attack()