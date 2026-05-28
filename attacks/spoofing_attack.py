import logging
import random
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class SpoofingAttack:

    def __init__(self):

        self.fake_identities = 10

    def launch_attack(self):

        logging.info("Launching spoofing attack simulation...")

        for index in range(self.fake_identities):

            fake_mac = (
                f"AA:BB:CC:"
                f"{random.randint(10,99)}:"
                f"{random.randint(10,99)}:"
                f"{random.randint(10,99)}"
            )

            logging.warning(
                f"Spoofed identity detected: {fake_mac}"
            )

            time.sleep(0.3)

        logging.info("Spoofing attack simulation completed.")


if __name__ == "__main__":

    attack = SpoofingAttack()

    attack.launch_attack()