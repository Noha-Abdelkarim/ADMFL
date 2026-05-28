import argparse
import logging
import os
import time
import yaml

from topology.network_topology import NetworkTopology
from usc.uav_client import UAVClient
from tafl.fl_server import FLServer
from idt.trust_engine import TrustEngine
from soam.ryu_controller import RyuController


def create_directories():
    """
    Create required runtime directories.
    """

    directories = [
        "logs",
        "results"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def initialize_logging():
    """
    Configure logging system.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/admfl.log"),
            logging.StreamHandler()
        ]
    )

    logging.info("Logging system initialized.")


def load_config(config_path="config.yaml"):
    """
    Load YAML configuration file.
    """

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    logging.info("Configuration loaded successfully.")

    return config


def initialize_topology(config):
    """
    Initialize network topology.
    """

    logging.info("Initializing network topology...")

    topology = NetworkTopology(config)

    topology.build()

    return topology


def initialize_uavs(config):
    """
    Initialize UAV clients.
    """

    logging.info("Initializing UAV clients...")

    num_uavs = config["network"]["num_uavs"]

    uavs = []

    for uav_id in range(num_uavs):

        client = UAVClient(
            uav_id=uav_id,
            config=config
        )

        uavs.append(client)

        logging.info(f"UAV-{uav_id} initialized.")

    return uavs


def initialize_fl_server(config):
    """
    Initialize Federated Learning server.
    """

    logging.info("Starting Federated Learning server...")

    return FLServer(config)


def initialize_trust_engine(config):
    """
    Initialize Trust Engine.
    """

    logging.info("Initializing Trust Engine...")

    return TrustEngine(config)


def initialize_controller(config):
    """
    Initialize SDN controller.
    """

    logging.info("Starting SD-IoT Controller...")

    return RyuController(config)


def start_simulation(uavs):
    """
    Start UAV simulation.
    """

    logging.info("Starting UAV simulation...")

    for uav in uavs:
        uav.start()

    logging.info("All UAV clients started.")


def shutdown_framework(topology):
    """
    Gracefully shutdown framework.
    """

    logging.info("Shutting down ADMFL Framework...")

    topology.stop()

    logging.info("ADMFL shutdown complete.")


def main():

    parser = argparse.ArgumentParser(
        description="ADMFL Framework"
    )

    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to configuration file"
    )

    args = parser.parse_args()

    create_directories()

    initialize_logging()

    logging.info("Starting ADMFL Framework...")

    config = load_config(args.config)

    topology = initialize_topology(config)

    controller = initialize_controller(config)

    trust_engine = initialize_trust_engine(config)

    fl_server = initialize_fl_server(config)

    uavs = initialize_uavs(config)

    start_simulation(uavs)

    logging.info("ADMFL Framework is running successfully.")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        shutdown_framework(topology)


if __name__ == "__main__":
    main()