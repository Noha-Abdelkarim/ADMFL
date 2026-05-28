import logging
import random
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class SwarmAttack:

    def __init__(self):

        self.swarm_size = 10

    def launch_attack(self):

        logging.info("Launching coordinated swarm attack...")

        for drone in range(self.swarm_size):

            malicious_target = (
                f"UAV-{random.randint(0, 5)}"
            )

            attack_strength = random.randint(50, 500)

            logging.warning(
                f"Malicious drone-{drone} attacking "
                f"{malicious_target} "
                f"with intensity {attack_strength}"
            )

            time.sleep(0.3)

        logging.info("Swarm attack simulation completed.")


if __name__ == "__main__":

    attack = SwarmAttack()

    attack.launch_attack()