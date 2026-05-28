# tests/test_fl_server.py

import unittest

from tafl.fl_server import FLServer


class TestFLServer(unittest.TestCase):

    def setUp(self):

        self.config = {
            "federated_learning": {
                "rounds": 5,
                "aggregation_method": "FedAvg"
            }
        }

        self.server = FLServer(self.config)

    def test_initialize_global_model(self):

        self.server.initialize_global_model()

        self.assertTrue(
            "weights" in self.server.global_model
        )

    def test_register_client(self):

        class MockClient:

            uav_id = 1

        client = MockClient()

        self.server.register_client(client)

        self.assertEqual(
            len(self.server.clients),
            1
        )


if __name__ == "__main__":

    unittest.main()